from flask import *
import mongoengine

from mango import models

app = Flask(__name__)

@app.prerequest
def insert_connection():
    g.mongo = mongoengine.connect('mango')

from .android import android
app.register_blueprint(android, url_prefix="/android")
