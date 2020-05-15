# Web Scraping in Python 3 using Scrapy

## Configuring the app (Considering python 3 is installed and using pip3 to install other dependencies)

* Create a virtual environment `virtual env .` ***(. represents same folder, can also do `/env`)***
* Instal dependencies
  * > pip3 install Scrapy, flask

## Run the application

  `scrapy crawl quotes` (quotes is the name of the spider)

## Adding pipelines to store the containers in a database (this file is automatically created by Scrapy)

* Goto settings.py file located inside ScrapeThisWeb folder.
* Search for `pipelines`
* uncomment this following line `ITEM_PIPELINES = { 'ScrapeThisWeb.pipelines.ScrapethiswebPipeline': 300 }`
  
***note:*** 300 here represents priority and if there are other pipelines like above , then lower value represents higer priority.

## Save the scrapped data as file (json/xml/csv)

  >>>
    JSON: `scrapy crawl quotes -o quotes.json`
    XML: `scrapy crawl quotes -o quotes.xml`
    CSV: `scrapy crawl quotes -o quotes.csv`
  >>>

  here **scrapy crawl** is the command, followed by **quotes** as the name of the scrape operation and finally the filename, i.e **quotes.json(also .xml and .csv)**

## Storing scraped data in a Database

### Sqlite3

This database is provided by default and hence can be used to store the scrapped data.

#### config

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
