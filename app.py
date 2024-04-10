from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from database.models import Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '' #Replace with your details
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def home():
    return 'Home'

@app.route('/users')
def get_users():
    users = db.session.query(Users).all()
    users_data = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
    return jsonify(users=users_data)

if __name__ == '__main__':
    app.run(debug=True)