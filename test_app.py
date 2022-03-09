import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import Character, Movie, db
import config

database_path = config.database_path


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class MarvelTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        self.creator_token = os.environ['creator_token']
        self.consumer_token = os.environ['consumer_token']
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def test_characters(self):
        res = self.client().get("/characters", headers={
            "Authorization": 'bearer ' + self.creator_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_movies(self):
        res = self.client().get("/movies", headers={
            "Authorization": 'bearer ' + self.consumer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def create_movie(self):
        res = self.client().post("/movies", headers={
            "Authorization": 'bearer ' + self.creator_token}, json={"name":"New Movie","character_id":50})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def create_movie_fail(self):
        res = self.client().post("/movies", json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)

    def delete_movie(self):
        res = self.client().delete("/movies/1", headers={
            "Authorization": 'bearer ' + self.creator_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def delete_movie_fail(self):
        res = self.client().delete("/movies/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)

    def delete_movie_auth_fail(self):
        res = self.client().delete("/movies/1", headers={
            "Authorization": 'bearer ' + self.consumer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)

if __name__ == "__main__":
    unittest.main()
