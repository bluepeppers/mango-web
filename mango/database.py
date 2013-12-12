from mongoengine import *
import json, datetime

class Alarm(Document):
    name = StringField(required=True)
    time = DateTimeField(required=True)
    activated = BooleanField(default=True)

class MovementData(Document):
    day = DateTimeField(required=True)
    movementdata = ListField(required=True)

def returnJsonFromRaw(rawJson):
    raw_data = json.loads(rawJson)
    if not raw_data:
        print "No data was sent"
        return
    if not (raw_data['name'] and raw_data['time']):
        print "The fields either could not be parsed, or one of them is missing"
        return
    return  raw_data
    
def writeJsonToDatabase(obj):
    alarm = Alarm(name=obj['name'], time=obj['time'])
    alarm.save()

def getAlarms():
    return Alarm.objects

def getTodayAlarms():
    yesterday = Date.today() - timedelta(1)
    return Alarm.objects(time__gt=yesterday)

def activateAlarm(name):
    alarm = Alarm.objects(name__exact=name)
    alarm.activated = True
    alarm.save()
    print "Alarm " + name + " saved."
    return
    
def getTodaysMovement():
    today = Date.today()
    return MovementData.objects(day__gte=today)

def getWeeksMovement():
    weekago = Date.today() - timedelta(7)
    return MovementData.objects(day__gte=weekago)

def getAllMovement():
    return Movementdata.objects


