from flask import Flask
from models import Character, Movie, db, setup_db

app = Flask(__name__)
setup_db(app)

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

db.session.commit()
