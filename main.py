from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import database.database as db
from models.pet_model import Pet

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/createdb', methods =["GET"])
def create_db():
    db.create_db()
    return jsonify({'message': 'Created'}), 201

@app.route('/insertpet', methods=["POST"])
def insert_pet():
    data = request.get_json()
    name = data['name']
    age = data['age']
    pet_type = data['pettype']
    new_pet = Pet(name=name, age=age, pettype=pet_type)
    db.session.add(new_pet)
    db.session.commit()
    return jsonify({'message': 'Created'}), 201 

@app.route('/getpets', methods=["GET"])
def get_pets():
    pets = db.session.query(Pet).all()
    pets_dict = []
    for item in pets:
        pets_dict.append(item.as_dict())
    return jsonify(pets_dict)

@app.route("/getpetbyid", methods=['GET'])
def get_pets_by_id():
    qstr = request.args.to_dict()
    pet = db.session.query(Pet).filter(Pet.id == int(qstr['id'])).first()
    return pet.as_dict()


@app.route('/updatepet', methods=["POST"])
def update_pet():
    qstr = request.args.to_dict()
    pet = db.session.query(Pet).filter(Pet.id == int(qstr['id'])).first()
    data = request.get_json()

    pet.name = data['name']
    pet.age = data['age']
    pet.pet_type = data['pettype']
    
    db.session.commit()
    return jsonify({'message': 'Updated'}), 200 

@app.route("/deletepet", methods=['Delete'])
def delete_pet():
    qstr = request.args.to_dict()
    pet = db.session.query(Pet).filter(Pet.id == int(qstr['id'])).first()
    db.session.delete(pet)
    db.session.commit()
    return jsonify({'message': 'Deleted'}), 203 


if __name__ == "__main__":
    app.run(debug = True)
    