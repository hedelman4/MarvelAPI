import os
from flask import Flask, jsonify, request
from models import setup_db, Character, Movie, db
from flask_cors import CORS
import json

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

    @app.route('/movies', methods=['POST'])
    def add_movie():
        body = request.get_json()
        new_name = body.get('name')
        new_character_id = body.get('character_id')
        new_movie = Movie(name=new_name, character_id=new_character_id)
        new_movie.insert()
        return jsonify({
        'success': True,
        'movie': new_movie.name
        })

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    def patch_movies(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        body = request.get_json()
        movie.name = body.get('name')
        movie.character_id = body.get('character_id')
        movie.update()
        return jsonify({
        'success': True,
        'movie': movie.name,
        'character_id': movie.character_id
        })

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    def delete_movies(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        movie.delete()
        return jsonify({
        'success': True,
        'delete': movie_id
        })

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
