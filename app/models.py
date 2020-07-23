from . import db
from flask_login import UserMixin

class Group(UserMixin,db.Model):
    '''
    Group class to define a group in the database
    '''

    # Name of the table
    __tablename__ = 'groups'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # name column for the group name
    name = db.Column(db.String)


    def __repr__(self):
        return f'User {self.username}'