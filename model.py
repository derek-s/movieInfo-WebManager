# !/usr/bin/python
# -*- coding: utf-8 -*-
# File:model.py
# File Created:2020-03-01 08:46:45
# Author:Derek.S(derekseli@outlook.com)
# -----
# Last Modified:2020-03-01 08:46:45
# -----

from app import mongo
from math import ceil
import json

from config import limitNum

def indexData():
    """
    首页
    :return:
    """

    try:
        allData = mongo.db.movieInfo.find({})
        totalNum = allData.count()
        totalPNum = ceil(totalNum / limitNum)
        return allData, totalNum, totalPNum
    except Exception as e:
        print(e)

class Pagination:
    def __init__(self, items, page, per_page, total_items):
        self.items = items
        self.page = page
        self.per_page = per_page
        self.total_items = total_items
        self.num_pages = int(ceil(total_items / per_page))

    @property
    def has_next(self):
        return self.page < self.num_pages

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def next_page(self):
        return self.page + 1

    @property
    def prev_page(self):
        return self.page - 1

    def iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
        last = 0
        for num in range(1, self.num_pages + 1):
            if num <= left_edge or \
                    (num > self.page - left_current - 1 and \
                    num < self.page + right_current) or \
                    num > self.num_pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num


def paginate(queryset, page=1):
    """
    分页
    :param queryset: 查询数据集
    :param page: 页码
    :return: 分页信息
    """
    per_page = limitNum
    skip  = (page - 1)*per_page
    limit = per_page

    return Pagination(queryset.limit(limit).skip(skip), page=page, per_page=per_page, total_items=queryset.count())


def searchAll(keyword, pageNumber):
    """
    搜索
    :param keyword: 搜索关键字
    :return: 查询集
    """
    try:
        limit_start = (pageNumber - 1)*limitNum
        searchResult = mongo.db.movieInfo.find({
            "chineseName": {"$regex": str(keyword)}
        }).limit(limitNum).skip(limit_start)
        totalNum = searchResult.count()
        totalPNum = ceil(totalNum / limitNum)
        return searchResult, totalPNum, totalNum
    except Exception as e:
        print(e)