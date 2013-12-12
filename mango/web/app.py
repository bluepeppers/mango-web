from flask import *
import mongoengine

app = Flask(__name__)

@app.before_request
def insert_connection():
    g.mongo = mongoengine.connect('mango')

from .alarm import alarm
app.register_blueprint(alarm, url_prefix="/")
