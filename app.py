# !/usr/bin/python
# -*- coding: utf-8 -*-
# File:app.py
# File Created:2020-03-01 08:03:28
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2020-03-01 08:03:28
# -----

from flask import Flask
from flask_pymongo import PyMongo
from config import SECRET_KEY, dbConfig

app = Flask(__name__, template_folder="templates")

app.secret_key = SECRET_KEY

app.config.update(
    MONGO_URI=dbConfig["URI"],
    DEBUG=True
)

mongo = PyMongo(app)

app.jinja_env.auto_reload = True
