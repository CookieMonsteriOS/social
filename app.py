from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from database.models import Users
from database.db import database
from services.users import add_user_database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '' #Replace with your details
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.init_app(app)

@app.route('/')
def home():
    return 'Home'

@app.route('/users')
def get_users():
    users = database.session.query(Users).all()
    users_data = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
    return jsonify(users=users_data)

@app.route('/addusers', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    new_user_id = add_user_database(name, email)
    return jsonify({'id': new_user_id}), 201 

if __name__ == '__main__':
    app.run(debug=True)