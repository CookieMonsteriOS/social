from flask_sqlalchemy import SQLAlchemy
from database.models import Users
from database.db import database

def add_user_to_database(name: str, email: str) -> int:
    try:
        new_user = Users(name=name, email=email)
        database.session.add(new_user)
        database.session.commit()
        return new_user.id
    except Exception as e:
        database.session.rollback() 
        raise e 