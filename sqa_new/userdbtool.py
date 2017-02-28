from sys import argv

import os
from os.path import join, dirname
from dotenv import load_dotenv

from sqlalchemy import String, Integer, Column
from sqlalchemy import create_engine
# This sessionmaker will be what we use in order to talk to our database
from sqlalchemy.orm import sessionmaker
# declarative_base is used to turn our classes into DB models
from sqlalchemy.ext.declarative import declarative_base

filename, cohort_id_arg = argv

# Load dotenv into our file
dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)
MYSQL_STRING = os.environ.get('MYSQL_CONNECTION_STRING')

engine = create_engine(MYSQL_STRING)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "users"
    id= Column(Integer,primary_key=True)
    first_name= Column(String(100), nullable=False)
    last_name= Column(String(100), nullable=False)
    favorite_number=Column(Integer)
    cohort_id=Column(Integer, nullable=False)

    def __repr__(self):
        return "<User id=%d first_name=%s last_name=%s favorite_number=%d cohort_id=%d>" % (self.id, self.first_name, self.last_name, self.favorite_number, self.cohort_id)

# Name NN
class Cohort(Base):
    __tablename__ = "cohorts"
    id= Column(Integer,primary_key=True)
    name= Column(String(45), nullable=False)


def addUser(argFirst, argLast, argFavorite, argCohort):
    newUser = User(first_name=argFirst, last_name=argLast, favorite_number=argFavorite, cohort_id=argCohort)
    session.add(newUser)
    session.commit()
    print "%s %s was added!" % (argFirst, argLast)

def deleteUser(argId):
    userToDelete = session.query(User).filter_by(id=argId).first()
    session.delete(userToDelete)
    session.commit()
    print "%s %s was deleted!" % (userToDelete.first_name, userToDelete.last_name)

def findCohort(cohortId):
    usersToFind = session.query(User).outerjoin(Cohort, User.cohort_id == Cohort.id).filter_by(id=cohortId)

    for person in usersToFind:
        print "First_Name: %s Last_Name: %s CID: %d" % (person.first_name, person.last_name, person.cohort_id)


findCohort(cohort_id_arg)
