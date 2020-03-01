# !/usr/bin/python
# -*- coding: utf-8 -*-
# File:index.py
# File Created:2020-03-01 08:05:25
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2020-03-01 08:05:25
# -----

from flask import Flask, render_template, Blueprint

indexViews = Blueprint("indexViews", __name__)

@indexViews.route("/")
def index():
    return render_template("index.html")


@indexViews.route("/search")
def search():
    pass