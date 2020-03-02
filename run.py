# !/usr/bin/python
# -*- coding: utf-8 -*-
# File:run.py
# File Created:2020-03-01 09:01:05
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2020-03-01 09:01:05
# -----
from app import app
from views.index import indexViews

app.register_blueprint(indexViews)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050)