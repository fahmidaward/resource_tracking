#!/usr/bin/env python
#from models import Device, LoggedPoint 
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
    #p=LogEntry.select()
    #return(p)
#    db.create_tables([LogEntry])

    for p in LogEntry.select():
        h=h+1
        if h>350 and h<352:
           # print(p.name, p.created, p.text)
           # print(h)
           # items = p.text
           
           # if item['format'] == 'dynamics':
           items = p.text
           elements=(items.splitlines( ))
           for element in elements:
               print(element)
"""
def save_fleet(p):
   print("Starting havesting ++++++++++++++++++")
   
   h=0
   for n in p:
        h=h+1
        if h>350 and h<352:
           # print(p.name, p.created, p.text)
           # print(h)
           # items = p.text

           # if item['format'] == 'dynamics':
           items = n.text
           elements=(items.splitlines( ))
           for element in elements:
               print(element)
   print("End of havesting ++++++++++++++++++")
   return 0
"""
"""
     deviceid = str(prop["TrackerID"]).strip()
            try:
                device = Device.objects.get(deviceid=deviceid)
                if seen == device.seen:
                    # Already harvested.
                    ignored += 1
                    continue
                updated += 1
            except ObjectDoesNotExist:
                device = Device(deviceid=deviceid)
                created += 1

            device.callsign = prop["VehicleName"]
            device.callsign_display = prop["VehicleName"]
            device.model = prop["Model"]
            device.registration = 'DFES - ' + prop["Registration"][:32]
            device.symbol = (prop["VehicleType"]).strip()
            device.velocity = int(prop["Speed"]) * 1000
            device.heading = prop["Direction"]
            device.seen = seen
            device.point = "POINT ({} {})".format(row['geometry']['coordinates'][0], row['geometry']['coordinates'][1])
            device.source_device_type = 'dfes'
            device.save()                                                                                                                    
"""


def getEntryList():
    entries = defaultdict(list)
    for entry in LogEntry.select():
        filename = entry.name
        try:
            data = json.loads(entry.text)
            deviceid = data["vehicleID"]
        except Exception as e:
            print(e)
            continue
        entries[deviceid].append({"filename": filename, "data": data})
    return entries

def main():
    init_database()

if __name__=="__main__":
    main()


