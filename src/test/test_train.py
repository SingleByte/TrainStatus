#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试Train类


import sys
sys.path.append("../")
from Train import Train
from Station import Station

train = Train("K920", "2015-01-27")
print train.getAllNumbers()

for item in train.getStationList():
    print item.name, item.date, item.arrive_time, item.leave_time, item.distance

print train.getArriveMoment(u"许昌")
print train.getArriveMoment(u"驻马店")
print train.getArriveMoment(u"西平")


