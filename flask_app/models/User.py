from sqlalchemy import Column, Integer, String
from flask_app.database import Base, TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = 'users'
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)
