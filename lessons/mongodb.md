# NoSQL with MongoDB

### Lesson Objectives

* Describe what MongoDB databases are & why they're useful
* Compare and contrast NoSQL with SQL
* Define what a document is in the context of MongoDB
* Explain the difference between embedded and referenced documents, and how we use each to model relationships in MongoDB
* Issue basic CRUD commands to a database from the Mongo Shell

### Topics

**How did MongoDB come about?**   
MongoDB was developed in 2007 by a company named 10gen, it was originally going to be used as a PaaS product, but they instead made it open source.

**What does MONGODB stand for?**   
Mongo, as in humungous database, was named the way it was because it was made to handle humungous amounts of data.

**What does NoSQL even mean?**  
NoSQL database provides a mechanism for storage and retrieval of data which is modeled in means other than the tabular relations used in relational databases.

**What is MongoDB and how does it differ from a relational database like Postgres?**  
MongoDB is a type of database that uses documents & collections instead of tables, rows & columns. Documents are the same structure as JSON, and a collection is just a group of these JSON documents.

- Documents
  * MongoDB stores all data in documents, which are JSON-style data structures composed of field-and-value pairs

- Embedded documents
  * Allows us to model one-to-many relationships. Since there are no joins, it's often more efficient to embed document data that is almost always accessed through a single object within that document itself. In the [MongoDB documentation](http://docs.mongodb.org/manual/tutorial/model-embedded-one-to-many-relationships-between-documents/), there is a classic example of a case when you would rather embed documents rather than start a new collection. 

- Referencing documents
  * There are cases where the data in a document might be related to another document, but is accessed frequently outside the context of that document. The data within that document might contain a lot of fields (e.g. User) so repeating that document data multiple times outside of that parent document would not be optimal

- Collections
  * A collection is a grouping of documents within MongoDB. A collection is the equivalent of RDBMS tables
  * Documents within collections are schemaless, documents within a collection can have different fields
    
* Pros of MongoDB
  - Schemaless
  - Open source and runs on Linux
  - You can choose the level of consistency you want depending on the data you're saving
    * faster performance = fire and forget inserts to MongoDB
    * slower performance = wait until insert has been replicated to multiple nodes before returning
    
* Cons of MongoDB
  - Data size is typically higher, field names are repeated for every document stored
  - Not as much structure, and this may bother some people.
  - Less flexibility w/ querying (e.g. no joins)
  - No support for transactions
  
* BSON vs JSON
  - MongoDB represents JSON documents in binary-encoded format called [BSON](http://docs.mongodb.org/manual/reference/bson-types/) behind the scenes. BSON extends the JSON model to provide additional data types (e.g. dates, binary data) and to be efficient for encoding and decoding within different languages.
  - In practice, you don't have to know much about BSON when working with MongoDB, you just need to use the native types of your language and the supplied types (e.g. ObjectId) will be mapped into the appropriate BSON type by the driver.
  
* What is modeling a database? Why do we do it
  
## Activity: Model your favorite social application's database (15 minutes)
* Facebook
* Twitter
* Reddit
* AirBnB
* Tumblr

For each collection, draw a box with that collections label (E.G. User), inside of that collection, describe the document's structure. Continue drawing collections for each part of your favorite social nework

![model](http://www.ebaytechblog.com/wp-content/uploads/2014/10/mongodb_mapping.png)

## mLab

Generally for development we would create a local MongoDB database to use, but in preparation for the upcoming group project, let's set up an account on [mLab](https://mlab.com) and use a remote cloud database since we'll be deploying our apps to either AWS or Heroku. 

* Create a new database
* Create a collection for users
* Add a document

```json
{ 
  "name": "John",
  "age": 23
}
```

* Have students do a couple more 
* Insert multiple documents
* Run through different "search" options to find by id, name, age > 50, $in, etc
* Show sorting documents 

## Class Exercise

**20 min**

1. Create a new database
2. Create a new user
3. Create 2 new collections
4. Within both collections, create 3 documents appropriate for that collection

### Bonus

Find some documents by id, try some new search operators that we didn't cover in class in the sidebar on the mLab page 
