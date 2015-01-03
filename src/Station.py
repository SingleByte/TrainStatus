#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 车站数据类型


class Station:
    """代表一个车站，包含名字、车次进出时间等"""

    def __init__(self):
        pass

    def __init__(self, name, date, arrive_time, leave_time, distance):
        self.name = name
        self.date = date
        self.arrive_time = arrive_time
        self.leave_time = leave_time
        self.distance = distance

    @staticmethod
    def parse_Station(info):
        """从信息数组中解析构造一个Station对象"""
        (IDX_NAME, IDX_DATE, IDX_ARRIVE, IDX_LEAVE, IDX_DIST) = range(5)
        station = Station(info[IDX_NAME], info[IDX_DATE], info[IDX_ARRIVE] \
                info[IDX_LEAVE], info[IDX_DIST])

        return station


