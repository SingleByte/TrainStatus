#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试Train类


import sys
sys.path.append("../")
from Train import Train
from Station import Station

train = Train("K917", "2015-1-26")
print train.getAllNumbers()

for item in train.getStationList():
    print item.name, item.date, item.arrive_time, item.leave_time, item.distance

train.getDelayTime(u"许昌")


