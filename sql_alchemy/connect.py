import sqlalchemy
# create_engine allows us to connect to our database
from sqlalchemy import create_engine, Column, Integer, String
# declarative_base allows us to map classes to database tables.
from sqlalchemy.ext.declarative import declarative_base

print sqlalchemy.__version__

# print 'engine is %r' % (engine)
# create an instance of the base
Base = declarative_base()

"""
This is a model that will be mapped to a table in our database
A class using Declarative at a minimum needs a __tablename__ attribute,
and at least one Column which is part of a primary key [1]"""

class User(Base):
    # Our column methods give this class the ability of "instrumentation",
    # Be that the ability to communicate with our database
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(40))
    age = Column(Integer)
    password = Column(String(30))

    def __repr__(self):
        return "<User(name='%s', age='%s', password='%s')>" % (self.name, self.age, self.password)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
engine = create_engine("mysql+mysqlconnector://root:5n9ws9iwd@127.0.0.1:3306/sql_alchemy_class", echo=True)
Base.metadata.create_all(engine)
