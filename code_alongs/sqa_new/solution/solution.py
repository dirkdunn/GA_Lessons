#!/usr/bin/env python

# DOTENV Imports
import os
from os.path import join, dirname
from dotenv import load_dotenv

# CONNECTION STRING ENGINE
from sqlalchemy import create_engine;
# SESSIONS, THE SESSION MAKER
from sqlalchemy.orm import sessionmaker;
# MODELS
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# print "dirname is: %r" % (join(dirname(__file__), '.env'))
# print "File is: %r" % (dirname(__file__))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
MYSQL_KEY = os.environ.get("MYSQL_KEY")

engine = create_engine(MYSQL_KEY, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# Models must inherit from Base, and must have a __tablename__
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    favorite_number = Column(Integer)
    cohort_id = Column(Integer,nullable=False)


    def __repr__(self):
        return "<User id=%d first_name=%s last_name=%s favorite_number=%s cohort_id=%s>" % (self.id, self.first_name, self.last_name, self.favorite_number, self.cohort_id)

class Cohort(Base):
    __tablename__ = "cohorts"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100))

# Base.metadata.create_all(engine)

def addPerson():
    newPerson = User(first_name="Bobby", last_name="Flay", favorite_number=900, cohort_id=1)
    session.add(newPerson)
    session.commit()
    print 'bobby flay is back! never dies.'

def deletePerson():
    personToRemove = session.query(User).filter_by(first_name='bobby')
    session.delete(personToRemove)
    session.commit()
    print 'bobby flay was removed! about time.'

def updatePerson():
    personToUpdate = session.query(User).filter(User.first_name=='bobby').first()
    personToUpdate.first_name = 'Johnny'
    session.commit()
    print 'bobby flay is now %s!' % ('Johnny')

def getWDI(searchId):
    peopleInCohort = session.query(User).outerjoin(Cohort, User.cohort_id == Cohort.id).filter_by(id=searchId)
    print "People in WDI%d:" % (searchId)

    for person in peopleInCohort:
        print "FN: %s LN: %s CID: %d" % (person.first_name, person.last_name, person.cohort_id)

# getWDI(1)
addPerson()

# updatePerson()

"""
Reference:

Bulk Insert:
session.bulk_save_objectd([User(),User()])

Queries: You can print queries and it will show the actual SQL

Query Everything:
session.query(User).all()

Loop Queries:
for person in session.query(User):
    print person

Particular Attributes:
session.query(User.ap_name, User.ap_age).first()

Order By:
for person in session.query(User).order_by(User.ap_name):
    print person

Order By Descending:
from sqlalchemy import desc
for person in session.query(User).order_by(desc(User.ap_name)):
    print person # or using python .format()

Limiting:
query = session.query(User).order_by(User.ap_name).limit(2)
print([result.ap_name for result in query])


Database Functions:
These functions actually check what functions the DB you are working with has,
and then generates the functions for them in the SA orm

from sqlalchemy import func
inv_count = session.query(func.sum(User.ap_age)).scalar()
print inv_count
"""
