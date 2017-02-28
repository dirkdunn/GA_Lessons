# What we use to connect
from sqlalchemy import create_engine, update
# How we communicate w/ the database, we use the sessionmaker
from sqlalchemy.orm import sessionmaker
# Import our information from our connection file
from connect import Base, User

from sys import argv

# Bind the engine to the metadata of the Base class so that the
engine = create_engine("mysql+mysqlconnector://root:5n9ws9iwd@127.0.0.1:3306/sql_alchemy_class", echo=False)

# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def addUser(argName, argAge, argPassword):
    # Insert a person in the person table
    newUser = User(name=argName, age=argAge, password=argPassword)
    session.add(newUser)
    session.commit()

def removeUser(argName):
    userToDelete = session.query(User).filter_by(name=argName).first()
    session.delete(userToDelete)
    session.commit()

def updateUser(argName,argAttribute,newAttribute):
    userToUpdate = session.query(User).filter_by(name=argName).first()
    setattr(userToUpdate,argAttribute,newAttribute)
    session.commit()

if len(argv) > 1:
    command = argv[1]
    if command == 'add':
        argName, argAge, argPassword = argv[2:]
        addUser(argName,argAge,argPassword)
    elif command == 'remove':
        removeUser(argv[2])
    elif command == 'update':
        argName, argAttribute, newAttribute = argv[2:]
        # print "%s %s %s " % (argName,argAge,newAge)
        updateUser(argName,argAttribute,newAttribute)
