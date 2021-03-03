from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields, validate
import datetime
from resources.audiofile_schema import Audiobook, Song, Podcast
from sqldb import db, app


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/flask_api'
# db.init_app(app)


def table_object(audioFileType):
    tables_dict = {table.__tablename__: table for table in db.Model.__subclasses__()}
    return tables_dict.get(audioFileType)
    
# get all audioFileTypes
@app.route('/<string:audioFileType>', methods = ['GET'])
def index(audioFileType):
    get_audioFileTypes = db.session.query(table_object(audioFileType=audioFileType)).all()
    schema_list = ModelSchema.__subclasses__()
    
    for schema in schema_list:
        if str(schema.__name__) == audioFileType:
            audioFileType_schema = schema(many=True)
    audioFileTypes = audioFileType_schema.dump(get_audioFileTypes)
    return make_response(jsonify({"audioFileType": audioFileTypes})), 200

@app.route('/<string:audioFileType>/<string:id>', methods = ['GET'])
def get(audioFileType, id):
    get_audioFileTypes = db.session.query(table_object(audioFileType=audioFileType)).filter_by(id=id).first()
    schema_list = ModelSchema.__subclasses__()
   
    for schema in schema_list:
        if get_audioFileTypes and str(schema.__name__) == audioFileType:
            audioFileType_schema = schema()
            audioFileTypes = audioFileType_schema.dump(get_audioFileTypes)
            return make_response(jsonify({"audioFileType": audioFileTypes}))
    return { 'error': 'The request is invalid' }, 400


# create audioFileType
@app.route('/<string:audioFileType>', methods = ['POST'])
def create(audioFileType):
    data = request.get_json()
    schema_list = ModelSchema.__subclasses__()
    result = ''
    for schema in schema_list:
        if str(schema.__name__) == audioFileType:
            try:
                audioFileType_schema = schema()
                audioFileType = audioFileType_schema.load(data)
                result = audioFileType_schema.dump(audioFileType.create())
                return make_response(jsonify({"audioFileType": result}),200)
            except Exception as e:
                print(e)
                return { 'error': 'internal server error' }, 500

# update audiotypefile
@app.route('/<string:audioFileType>/<string:id>', methods = ['PUT'])
def update(audioFileType,id):
    data = request.get_json()
    get_audioFileType = db.session.query(table_object(audioFileType=audioFileType)).filter_by(id=id).first()
    schema_list = ModelSchema.__subclasses__()

    for schema in schema_list:
        print(schema)
        if audioFileType == "Song" and str(schema.__name__) == "Song":
            try:
                name_of_song = request.json.get('name_of_song', '')
                duration = request.json.get('duration','')
                uploaded_time = request.json.get('uploaded_time','')
                get_audioFileType.name_of_song = name_of_song
                get_audioFileType.duration = duration
                get_audioFileType.uploaded_time = uploaded_time
                db.session.add(get_audioFileType)
                db.session.commit()
                audioFileType_schema = schema()
                audio = audioFileType_schema.dump(get_audioFileType)
                return make_response(jsonify({str(audioFileType): audio}))
            except Exception as e:
                print(e)
                return { 'error': 'internal server error' }, 500
            
        elif audioFileType == "Podcast" and str(schema.__name__) == "Podcast":
            try:
                name_of_podcast = request.json.get('name_of_podcast','')
                duration = request.json.get('duration','')
                uploaded_time = request.json.get('uploaded_time','')
                host = request.json.get('host','')
                participants = request.json.get('participants','')
                
                get_audioFileType.name_of_podcast =  name_of_podcast
                get_audioFileType.duration =  duration
                get_audioFileType.uploaded_time = uploaded_time
                get_audioFileType.host = host
                get_audioFileType.participants = participants
                db.session.add(get_audioFileType)
                db.session.commit()
                audioFileType_schema = schema()
                audio = audioFileType_schema.dump(get_audioFileType)
                return make_response(jsonify({audioFileType: audio}))
            except Exception as e:
                print(e)
                return { 'error': 'internal server error' }, 500
        elif audioFileType == "Audiobook" and str(schema.__name__) == "Audiobook":
            try:
                title_audiobook = request.json.get('title_audiobook','')
                author_of_title = request.json.get('author_of_title','')
                narrator = request.json.get('narrator','')
                duration = request.json.get('duration','')
                uploaded_time = request.json.get('uploaded_time','')
                
                get_audioFileType.title_audiobook =  title_audiobook
                get_audioFileType.author_of_title =  author_of_title
                get_audioFileType.narrator = narrator
                get_audioFileType.duration = duration
                get_audioFileType.uploaded_time = uploaded_time
                db.session.add(get_audioFileType)
                db.session.commit()
                audioFileType_schema = schema(only=['id', 'title_audiobook', 'author_of_title','narrator','duration','uploaded_time'])
                audio = audioFileType_schema.dump(get_audioFileType)
                return make_response(jsonify({audioFileType: audio}))
            except Exception as e:
                print(e)
                return { 'error': 'internal server error' }, 500
        continue
    
    return { 'error': 'The request is invalid' }, 400          

# delete audioFileType
@app.route('/<string:audioFileType>/<id>', methods = ['DELETE'])
def delete(audioFileType, id):
    get_audioFileType = db.session.query(table_object(audioFileType=audioFileType)).filter_by(id=id).first()
    if get_audioFileType:
        db.session.delete(get_audioFileType)
        db.session.commit()
        return make_response("Action is successful",200)
    return { 'error': 'The request is invalid' }, 400 

if __name__ == '__main__':
    
    app.run(debug=True)