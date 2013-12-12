import re

from flask import *

from mango import database

alarm = Blueprint('alarm', __name__)

NAME_REGEX = re.compile("^(\S+)$")
EPOCH_REGEX = re.compile("^(\d+)$")

@alarm.route("/alarm/<name>/", methods=["GET"])
def display_alarm(alarm_name):
    if not NAME_REGEX.match(alarm_name):
        abort(400)

    alarms = models.Alarm.objects(name=alarm_name)
    if not len(alarms):
        abort(404)

    alarm = alarms.next()
    return alarm.to_json()

@alarm.route("/alarm/<name>/", methods=["PUT"])
def toggle_alarm(alarm_name):
    if not NAME_REGEX.match(alarm_name):
        abort(400)

    alarms = models.Alarm.objects(name=alarm_name)
    if not len(alarms):
        abort(404)

    alarm = alarms.next()
    alarm.activated = not alarm.activated
    alarm.save()
    return alarm.to_json()

@alarm.route("/alarm/<name>/", methods=["DELETE"])
def delete_alarm(alarm_name):
    if not NAME_REGEX.match(alarm_name):
        abort(400)

    alarms = models.Alarm.objects(name=alarm_name)
    if not len(alarms):
        abort(404)

    alarm = alarms.next()
    alarm.delete()

    return "OK"

@alarm.route("/alarm/", methods=["POST"])
def create_alarm():
    alarm_name = request.params.get("name", None)
    if alarm_name is None or not NAME_REGEX.match(alarm_name):
        abort(400)

    if len(models.Alarm.objects(name=alarm_name)):
        abort(400)

    alarm_epoch = request.params.get("time", None)
    if alarm_epoch is None or not EPOCH_REGEX.match(alarm_epoch):
        abort(400)

    alarm_time = datetime.fromtimestamp(int(alarm_epoch))

    alarm = models.Alarm(name=alarm_name, time=alarm_time)
    alarm.save()
    return alarm.to_json()
