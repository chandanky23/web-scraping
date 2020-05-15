# SQLITE 3 DATABSE

This database is provided by default and hence can be used to store the scrapped data.

## config

* create a filename database.py
* add `import sqlite3`
* create a connection `connection = sqlite3.connect('<add your db name follwed by .db extension>')`
* assign a cursor `curr = connection.cursor()`
* create a table in the db (***if needed: drop the table if already created***)
* insert data in the table
* commit the changes
* close the connection

>>>
    import sqlite3
    
    connection = sqlite3.connect('quotesData.db');
    curr = connection.cursor();
    
    curr.execute(
    """
        create table quotes_table(
          title text,
          author text,
          tags text
        )
      """
    )
    
    connection.commit()
    connection.close()
>>>
***this will create a database named `quotesData.db` in the project root folder***

Insert a row in the above created table: `quotes_table`
>>>
    curr.execute(
    """
        insert into quotes_table values(
          'Hello friends',
          'Chandan',
          'welcome'
        )
      """
    )
>>>

Drop a table if created: `quotes_table`
>>>
    curr.execute("""DROP TABLE IF EXISTS <table name>""")
>>>

***tripple `"""` is used to add multiline code***

## Code
>>>
    import sqlite3

    class ScrapethiswebPipeline:

        # this __init__ method is called automatically when ever an instance of a class is created.
        def __init__(self):
            self.create_connection()
            self.create_table()

        # Create a db connection and provide a database name
        def create_connection(self):
            self.connection = sqlite3.connect('quotesDB.db');
            self.curr = self.connection.cursor();

        def create_table(self):
            # drop the table if exists
            self.curr.execute("""DROP TABLE IF EXISTS quotes_table""")
            self.curr.execute(
                """
                    create table quotes_table(
                    title text,
                    author text,
                    tags text
                    )
                """
            )

        def process_item(self, item, spider):
            # print("pipeline --" + item['title'][0`])
            self.storeInDatabase(item);
            return item

        def storeInDatabase(self, item):
            self.curr.execute(
                """
                insert into quotes_table values(?,?,?)""",(
                    item['title'][0],
                    item['author'][0],
                    item['tags'][0]
                )
            )
            self.connection.commit();
>>>