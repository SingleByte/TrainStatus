#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试Train类


import sys
sys.path.append("../")
from Train import Train
from Station import Station

train = Train("K600", "2014-1-2")
print train.getAllNumbers()

for item in train.getStationList():
    print item.name, item.date, item.arrive_time, item.leave_time, item.distance



