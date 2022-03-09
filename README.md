# FSND Capstone Project
Heroku URI: https://the-marvel-api.herokuapp.com/

## Marvel API
This project is intended to provide an API containing data tables that capture the lists of characters and movies from the Marvel Cinematic Universe. Specifically, the various endpoints allow for the following activities:

1. Display character and movie lists.
2. Add new movies to the list.
3. Update movie entries.
4. Delete movies.

## Getting Started
Step 1: Install Required Software
Python 3.7 - Follow instructions to install the latest version of python for your platform in the python docs

Virtual Environment - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the python docs

Postgres - Install latest version of PostgreSQL

Step 2: Set up and Populate the Database
With Postgres running, create a marvel database:
createdb Marvel

Run the importdata.py file in the repository to populate the database

Step 3: Install Dependencies
Once your virtual environment is setup and running, install the required dependencies by running:

pip install -r requirements.txt

To deploy the tests, run the test_app.py file:
> python test_app.py

## Authorization
A creator token is provided in the setup.sh filter

### Roles/Permissions
1. Creator
    - get:characters
    - get:movies
    - post:movies
    - patch:movies
    - delete:movies
2. Consumer
    - get:characters
    - get:movies

## Endpoint Documentation

### GET '/characters'
- Fetches a dictionary of characters in which the keys are the ids and the value is the corresponding string of the character
- Request Arguments: None
'''
{
    "characters": {
        "1": "Captain America",
        "2": "Captain Marvel",
        "3": "Iron Man",
        "4": "The Incredible Hulk",
        "5": "Thor",
        "6": "Avengers",
        "7": "Guardians of the Galaxy",
        "8": "Ant-Man",
        "9": "Black Widow",
        "10": "Doctor Strange",
        "11": "Black Panther",
        "12": "Spider-Man",
        "13": "Hawkeye"
    },
    "success": true
}
'''

### GET '/movies'
- Fetches a dictionary of movies in which the keys are the ids and the value is the corresponding string of the movie
- Request Arguments: None
'''
{
    "movies": {
        "1": "Captain America: The First Avenger",
        "2": "Captain Marvel",
        "3": "Iron Man",
        "4": "Iron Man 2",
        "5": "The Incredible Hulk",
        "6": "Thor",
        "7": "The Avengers",
        "8": "Iron Man 3",
        "9": "Thor: The Dark World",
        "10": "Captain America: The Winter Soldier",
        "11": "Guardians of the Galaxy",
        "12": "Guardians of the Galaxy: Vol 2",
        "13": "Avengers: Age of Ultron",
        "14": "Ant-Man",
        "15": "Captain America: Civil War",
        "16": "Black Widow",
        "17": "Doctor Strange",
        "18": "Black Panther",
        "19": "Spider-Man: Homecoming",
        "20": "Thor: Ragnarok",
        "21": "Ant-Man and the Wasp",
        "22": "Avengers: Infinity War",
        "23": "Avengers: Endgame"
    },
    "success": true
}
'''

### POST '/movies'
- Adds a new movie to the movie lists
- Request Body Arguments: name - string; character_id - integer
'''
{
'success': True,
'movie': new_movie.name
}

### PATCH '/movies/$(id)'
- Updates existing movies
- Request Arguments: id - integer
- Request Body Arguments: name - string; character_id - integer
'''
{
'success': True,
'movie': movie.name,
'character_id': movie.character_id
}
'''

### DELETE '/movies/$(id)'
- Deletes existing movies
- Request Arguments: id - integer
'''
{
'success': True,
'delete': movie_id
}
'''
