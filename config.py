import os

class Config:
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://usuario:senha@ip:porta/nome_do_banco')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:123@localhost:5432/GG_FAP')

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    