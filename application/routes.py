from application import app, db
from application import routes
from application.models import FriendsCharacter
from flask import request
from flask import jsonify
from flask import render_template
from application.forms import AddCharacterForm

@app.route("/")
def hello_world():
    return "<p>Hello, there!</p>"

@app.route("/characters", methods=['POST'])

def create_character():
    form = AddCharacterForm()
    if form.validate_on_submit():
        character = FriendsCharacter(name=form.name.data, age=form.age.data, catch_phrase=form.catch_phrase.data)
        db.session.add(character)
        db.session.commit()
        data = request.json
    return render_template('characters.html', form=form)


@app.route('/characters', methods=['GET'])
def get_characters():
    characters = FriendsCharacter.query.all()
    character_list = []
    title = 'Friends'
    form = AddCharacterForm()
    for character in characters:
        character_list.append(format_character(character))
    return render_template('characters.html', title=title, characters=character_list, form=form)

def format_character(character):
    return {
        "name": character.name,
        "age": character.age,
        "catch_phrase": character.catch_phrase
    }

@app.route('/characters/<id>', methods=['GET'])
def get_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    return render_template('characters.html', character=format_character(character))

@app.route('/characters/<id>', methods=['DELETE'])
def delete_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return 'Character Deleted'

@app.route('/characters/<id>', methods=['PATCH'])
def update_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    data = request.json
    character.update(dict(name=data['name'], age=data['age'], catch_phrase=data['catch_phrase']))
    db.session.commit()
    updatedCharacter = character.one()
    return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)