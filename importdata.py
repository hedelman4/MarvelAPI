from flask import Flask
from models import Character, Movie, db, setup_db

app = Flask(__name__)
setup_db(app)

#Add Characters
db.session.add(Character(name='Captain America'))
db.session.add(Character(name='Captain Marvel'))
db.session.add(Character(name='Iron Man'))
db.session.add(Character(name='The Incredible Hulk'))
db.session.add(Character(name='Thor'))
db.session.add(Character(name='Avengers'))
db.session.add(Character(name='Guardians of the Galaxy'))
db.session.add(Character(name='Ant-Man'))
db.session.add(Character(name='Black Widow'))
db.session.add(Character(name='Doctor Strange'))
db.session.add(Character(name='Black Panther'))
db.session.add(Character(name='Spider-Man'))
db.session.add(Character(name='Hawkeye'))

#Add Movies
db.session.add(Movie(name='Captain America: The First Avenger', character_id=1))
db.session.add(Movie(name='Captain Marvel', character_id=2))
db.session.add(Movie(name='Iron Man', character_id=3))
db.session.add(Movie(name='Iron Man 2', character_id=3))
db.session.add(Movie(name='The Incredible Hulk', character_id=6))
db.session.add(Movie(name='Thor', character_id=4))
db.session.add(Movie(name='The Avengers', character_id=5))
db.session.add(Movie(name='Iron Man 3', character_id=6))
db.session.add(Movie(name='Thor: The Dark World', character_id=3))
db.session.add(Movie(name='Captain America: The Winter Soldier', character_id=5))
db.session.add(Movie(name='Guardians of the Galaxy', character_id=1))
db.session.add(Movie(name='Guardians of the Galaxy vol 2', character_id=7))
db.session.add(Movie(name='Avengers: Age of Ultron', character_id=7))
db.session.add(Movie(name='Ant-Man', character_id=6))
db.session.add(Movie(name='Captain America: Civil War', character_id=8))
db.session.add(Movie(name='Black Widow', character_id=1))
db.session.add(Movie(name='Doctor Strange', character_id=9))
db.session.add(Movie(name='Black Panther', character_id=10))
db.session.add(Movie(name='Spider-Man: Homecoming', character_id=11))
db.session.add(Movie(name='Thor: Ragnarok', character_id=12))
db.session.add(Movie(name='Ant-Man and the Wasp', character_id=5))
db.session.add(Movie(name='Avengers: Infinity War', character_id=8))
db.session.add(Movie(name='Avengers: Endgame', character_id=6))

db.session.commit()
