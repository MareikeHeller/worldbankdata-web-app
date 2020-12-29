from flask import Flask

app = Flask(__name__)

from worldbank_fertility_app import routes
