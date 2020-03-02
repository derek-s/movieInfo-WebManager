# !/usr/bin/python
# -*- coding: utf-8 -*-
# File:index.py
# File Created:2020-03-01 08:05:25
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2020-03-01 08:05:25
# -----

from flask import Flask, render_template, Blueprint, request, abort

from model import indexData, paginate, searchAll

indexViews = Blueprint("indexViews", __name__)

@indexViews.route("/")
def index():
    pageNum = int(request.args.get("page", 1))
    allData, totalNum, totalPNum = indexData()
    if (pageNum <= totalPNum or totalPNum == 0):
                return render_template(
                    "index.html",
                    allData=allData,
                    pagination=paginate(allData, pageNum),
                    totalNum=totalNum
                )
    else:
        abort(404)


@indexViews.route("/search")
def search():
    pageNum = int(request.args.get("page", 1))
    search_Args = request.args
    keyWord = search_Args["keyword"]
    searchResult, totalPNum, totalNum  = searchAll(keyWord, pageNum)
    if (pageNum <= totalPNum or totalPNum == 0):
            return render_template(
                "search.html",
                result=searchResult,
                pagination=paginate(searchResult, pageNum),
                totalNum=totalNum,
                keyword=keyWord
            )
    else:
        abort(404)
