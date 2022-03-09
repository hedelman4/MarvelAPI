import os
from flask import Flask, jsonify, request
from models import setup_db, Character, Movie, db
from flask_cors import CORS
import json
from auth import AuthError, requires_auth, get_token_auth_header

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        greeting = "Welcome to the Marvel API"
        return greeting

    @app.route('/characters', methods=['GET'])
    @requires_auth('get:characters')
    def get_characters(token):
        characters = Character.query.all()
        if len(characters) == 0:
            abort(404)
        return jsonify({
        'success': True,
        'characters': dict((character.id, character.name) for character in characters)
        })

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(token):
        movies = Movie.query.all()
        if len(movies) == 0:
            abort(404)
        return jsonify({
        'success': True,
        'movies': dict((movie.id, movie.name) for movie in movies)
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(token):
        try:
            body = request.get_json()
            new_name = body.get('name')
            new_character_id = body.get('character_id')
            new_movie = Movie(name=new_name, character_id=new_character_id)
            new_movie.insert()
            return jsonify({
            'success': True,
            'movie': new_movie.name
            })
        except:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movies(token, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        body = request.get_json()
        movie.name = body.get('name')
        movie.character_id = body.get('character_id')
        movie.update()
        if movie is None:
            abort(404)
        return jsonify({
        'success': True,
        'movie': movie.name,
        'character_id': movie.character_id
        })

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(token, movie_id):
        try:
            movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
            if movie is None:
                abort(404)
            movie.delete()
            return jsonify({
            'success': True,
            'delete': movie_id
            })
        except:
            abort(422)

    return app

app = create_app()

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

@app.errorhandler(404)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

@app.errorhandler(401)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "invalid authorization credentials"
    }), 401

if __name__ == '__main__':
    app.run(debug=True)
