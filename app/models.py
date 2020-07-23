from . import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    '''
    Users class to define a user in the database
    '''

    # Name of the table
    __tablename__ = 'users'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # name column for the user name
    name = db.Column(db.String)


    def __repr__(self):
        return f'User {self.username}'