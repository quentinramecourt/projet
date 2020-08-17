from flask_sqlalchemy import flask_sqlalchemy

db = SQLAlchemy()

#je créée une classe qui permet de mettre  en forme ce qu'on recoit de la BDD via des objets


class Users(db.Model):
    __tablename___ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    done = db.Column(db.Boolean)

    def __init__(self, title, description, donr):
        self.title = title
        self.description = description
        self.done = done
        