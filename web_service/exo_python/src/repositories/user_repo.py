from flask_sqlalchemy import SQLAlchemy 
from models.user import User

def get_users():
    users = Users.query.all()
    return users

def get_users_by_id(user_id):
    return users_id

def create_user(user):
    db.session.add(User)
    db.session.commit()
    return "super! un nouveau copain"