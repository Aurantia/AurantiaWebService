from flask import Flask 
import os

app = Flask("aurantia_webservice")
app.config.from_object(os.environ["APP_SETTINGS"])