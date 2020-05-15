# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> Item Containers -> Json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo database

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
        