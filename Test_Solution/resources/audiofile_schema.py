from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields, validate
import datetime
from sqldb import db

    
class Song(db.Model):
    __tablename__ = "Song"
    id = db.Column(db.Integer, primary_key=True)
    name_of_song = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    uploaded_time = db.Column(db.DateTime)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def __init__(self, name_of_song, duration, uploaded_time):
        self.name_of_song = name_of_song
        self.duration = duration
        self.uploaded_time = uploaded_time
    def __repr__(self):
        return '' % self.id
    
class Song(ModelSchema):
    class Meta:
        model = Song
        sqla_session = db.session
        
    id = fields.Number(dump_only=True, required=True)
    name_of_song = fields.String(validate=validate.Length(max=100), required=True)
    duration = fields.Number(required=True, default=0)
    uploaded_time = fields.DateTime(default=datetime.datetime.utcnow)
    
# Podcast model
class Podcast(db.Model):
    __tablename__ = "Podcast"
    id = db.Column(db.Integer, primary_key=True)
    name_of_podcast = db.Column(db.String(100))
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(db.String(100), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def __init__(self, name_of_podcast, duration, uploaded_time, host, participants):
        self.name_of_podcast = name_of_podcast
        self.duration = duration
        self.uploaded_time = uploaded_time
        self.host = host
        self.participants = participants
        
    def __repr__(self):
        return '' % self.id
    
class Podcast(ModelSchema):
    class Meta:
        model = Podcast
        sqla_session = db.session
        
    id = fields.Number(dump_only=True)
    name_of_podcast = fields.String(validate=validate.Length(max=100), required=True)
    duration = fields.Number(default= 0, required=True)
    uploaded_time = fields.DateTime(required=True, default=datetime.datetime.utcnow)
    host = fields.String(validate=validate.Length(max=100), required=True)
    participants = fields.List(fields.String(), required=False, validate=validate.Length(min=100))
    
# Audiobook model
class Audiobook(db.Model):
    __tablename__ = "Audiobook"
    id = db.Column(db.Integer, primary_key=True)
    title_audiobook = db.Column(db.String(100))
    author_of_title = db.Column(db.String(100))
    narrator = db.Column(db.String(100))
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
  
    def __init__(self, title_audiobook, author_of_title, narrator, duration, uploaded_time):
        self.title_audiobook = title_audiobook
        self.author_of_title = author_of_title
        self.narrator = narrator
        self.duration = duration
        self.uploaded_time = uploaded_time
    def __repr__(self):
        return '' % self.id
    
class Audiobook(ModelSchema):
    class Meta:
        model = Audiobook
        sqla_session = db.session
        
    id = fields.Number(dump_only=True, required=True)
    title_audiobook = fields.String(validate=validate.Length(max=100), required=True)
    author_of_title = fields.String(validate=validate.Length(max=100), required=True)
    narrator = fields.String(validate=validate.Length(max=100), required=True)
    duration = fields.Number(required=True, default= 0, allow_none=True)
    uploaded_time = fields.DateTime(required=True, default=datetime.datetime.utcnow)
    