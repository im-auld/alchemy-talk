from os import environ


SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'sqlite:////lightning_talk.db')