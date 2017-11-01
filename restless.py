from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column,Integer,String
import flask_restless
import readini
app = Flask(__name__)
db_connect_string=readini.get_db_config()
engine=create_engine(db_connect_string)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
mysession = scoped_session(Session)

Base = declarative_base()
Base.metadata.bind = engine

class Account(Base):
    __tablename__='account'
    
    id=Column(Integer,primary_key=True)
    user_name=Column(String(50),nullable=False)
    pass_word=Column(String(200),nullable=False)
    title=Column(String(50))
    salary=Column(Integer)
    

Base.metadata.create_all()

manager = flask_restless.APIManager(app, session=mysession)

person_blueprint = manager.create_api(Account,methods=['GET', 'POST', 'DELETE'])

app.run()