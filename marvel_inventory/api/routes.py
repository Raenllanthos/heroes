from flask import Blueprint, request,jsonify
from flask_migrate import current
from marvel_inventory.helpers import token_required
from marvel_inventory.models import db,User, Hero,hero_schema, heroes_schema

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/getdata")
def getdata():
    return {"some": "value", "foo":"bar"}

# Create Drone Endpoint -- CRUD -- Create, Read, Update, Delete
@api.route("/hero", methods = ["POST"])
@token_required
def create_hero(current_user_token):
    name = request.json["name"]
    power = request.json["power"]
    is_a_hero = request.json["is_a_hero"]
    comics_appeared_in = request.json["comics_appeared_in"]
    description = request.json["description"]
    back_story = request.json["back_story"]
    date_created = request.json["date_created"]
    user_token = current_user_token.token

    print(F"BIG TESTER: {current_user_token.token}")

    hero = Hero(name,power,is_a_hero,comics_appeared_in,description,back_story,date_created,user_token=user_token)

    db.session.add(hero)
    db.session.commit()

    response = hero_schema.dump(hero)
    return jsonify(response)

# RETRIEVE ALL DRONES
@api.route("/hero", methods=["GET"])
@token_required
def get_heroes(current_user_token):
    owner = current_user_token.token
    heroes = Hero.query.filter_by(user_token = owner).all()
    response = heroes_schema.dump(heroes)
    return jsonify(response)

# RETRIEVE ONE DRONES
@api.route("/hero/<id>", methods=["GET"])
@token_required
def get_drone(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        hero = Hero.query.get(id)
        response = hero_schema.dump(hero)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}), 401

@api.route('/hero/<id>', methods = ['POST','PUT'])
@token_required
def update_hero(current_user_token,id):
    hero = Hero.query.get(id) # GET DRONE INSTANCE

    hero.name = request.json["name"]
    hero.power = request.json["power"]
    hero.is_a_hero = request.json["is_a_hero"]
    hero.comics_appeared_in = request.json["comics_appeared_in"]
    hero.description = request.json["description"]
    hero.back_story = request.json["back_story"]
    hero.date_created = request.json["date_created"]
    hero.user_token = current_user_token.token

    db.session.commit()
    response = hero_schema.dump(hero)
    return jsonify(response)


# DELETE DRONE ENDPOINT
@api.route('/hero/<id>', methods = ['DELETE'])
@token_required
def delete_drone(current_user_token, id):
    hero = Hero.query.get(id)
    db.session.delete(hero)
    db.session.commit()
    response = hero_schema.dump(hero)
    return jsonify(response)