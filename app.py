import os
from flask import Flask, jsonify
from models import setup_db, Character, Movie, db
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        greeting = "Welcome to the Marvel API"
        return greeting

    @app.route('/characters', methods=['GET'])
    def get_characters():
        characters = Character.query.all()
        return jsonify({
        'success': True,
        'characters': dict((character.id, character.name) for character in characters)
        })

    @app.route('/movies', methods=['GET'])
    def get_movies():
        movies = Movie.query.all()
        return jsonify({
        'success': True,
        'movies': dict((movie.id, movie.name) for movie in movies)
        })

    @app.route('/test')
    def test():
        query = db.session.query(Character.name).all()
        return str(app.config['SQLALCHEMY_TRACK_MODIFICATIONS']) + str(query)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
