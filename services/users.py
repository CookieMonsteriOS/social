from flask_sqlalchemy import SQLAlchemy
from database.models import Users
from database.db import database

def add_user_database(name, email):
    new_user = Users(name=name, email=email)
    database.session.add(new_user)
    database.session.commit()
    return new_user.id