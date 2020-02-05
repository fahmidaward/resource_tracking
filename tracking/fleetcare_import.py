#!/usr/bin/env python
from lazyapi import app
import os
from peewee import PostgresqlDatabase, Model, CharField, DateTimeField, TextField
from collections import defaultdict
import json
 

#db = PostgresqlDatabase(os.environ["PGDATABASE"])
db = PostgresqlDatabase(os.environ.get("FCAREDATABASE"),user=os.environ.get("FCAREUSER"), password=os.environ.get("FCAREPASSWORD"),host=os.environ.get("FCAREHOST"), port=os.environ.get("FCAREPORT"))

class LogEntry(Model):
    name = CharField()
    created = DateTimeField()
    text = TextField()
    print('1')
    class Meta:
        indexes = (
            (('name', 'created'), True),
        )
        database = db
    print('2')

def init_database():
    h=0
    db.connect()
    print('3')

    for p in LogEntry.select():
        h=h+1
        if h>350 and h<352:
           items = p.text
           elements=(items.splitlines( ))
           for element in elements:
               print(element)


def main():
    init_database()

if __name__=="__main__":
    main()


