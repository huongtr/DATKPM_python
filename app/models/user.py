import datetime as dt
from sqlalchemy.orm import relationship
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, index=True, nullable=False)
    email = db.Column(db.String(50), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    loai = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)

    # Define one-to-one relationship with Cab
#     cab = db.relationship('Cab', uselist=False, backref='driver', lazy=True)

    def __init__(self, username, email, password, loai=0):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.loai = loai

    def __repr__(self):
        return f"<User {self.id}>"

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
