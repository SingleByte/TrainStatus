#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试站点解析代码

import sys
sys.path.append("../")
from Station import Station

station = Station.parseStation(["深圳西", "2015-1-2", "12:23", "13:34", 500])
print station.name, station.date, station.arrive_time, station.leave_time, station.distance

