#!/usr/bin/env python
# coding=utf-8
# Python 2.7.3
# File: GetCityWeather.py
# 获得城市天气数据  
import urllib2
import httplib
import json

def GetCityWeather(cityURL):
    response = urllib2.urlopen(cityURL)
    htmlByte = response.read()
    print htmlByte
    htmlStr = htmlByte.decode("utf8")
    st = json.loads(htmlStr)
    return st

if __name__ == '__main__':
    cityURL = "http://m.weather.com.cn/data/101280101.html"
    st = GetCityWeather(cityURL)
    ss = st["weatherinfo"]
    print ss["city"]
    print ss["date_y"]
    print ss["week"]
    print ss["temp1"]
    print ss["weather1"]