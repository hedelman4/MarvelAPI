import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Primary Marvel Character
'''
class Character(db.Model):
  __tablename__ = 'character'

  id = Column(db.Integer, primary_key=True)
  name = Column(String)

  def __init__(self, name):
    self.name = name

  def format(self):
    return {
      'id': self.id,
      'name': self.name
      }

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def update(self):
    db.session.commit()
'''
Marvel Movie
'''
class Movie(db.Model):
  __tablename__ = 'movie'

  id = Column(db.Integer, primary_key=True)
  name = Column(String)
  character_id = Column(db.Integer, db.ForeignKey('character.id'))

  def __init__(self, name, character_id):
    self.name = name

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'character_id': self.character_id
      }

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def update(self):
    db.session.commit()
