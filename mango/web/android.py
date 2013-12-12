from flask import *

from mango import models

android = Blueprint('android', __name__)

NAME_REGEX = re.compile("^(\S+)$")
EPOCH_REGEX = re.compile("^(\d+)$")

@android.route("/alarm/<name>/", methods=["GET"])
def display_alarm(alarm_name):
    if not NAME_REGEX.match(alarm_name):
        abort(400)

    alarms = models.Alarm.objects(name=alarm_name)
    if not len(alarms):
        abort(404)

    alarm = alarms.next()
    return alarm.to_json()

@android.route("/alarm/<name>/", methods=["DELETE"])
def display_alarm(alarm_name):
    if not NAME_REGEX.match(alarm_name):
        abort(400)

    alarms = models.Alarm.objects(name=alarm_name)
    if not len(alarms):
        abort(404)

    alarm = alarms.next()
    alarm.delete()

    return "OK"

@android.route("/alarm/", methods=["POST"])
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
