#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 火车的数据结构以及方法


def Train:
    """代表一辆火车"""


    def __init__(self, number, launch_date):
        self.number = number
        self.launch_date = launch_date
        self.stations = None


    def getStationList(self):
        """获取该火车经过的所有站点
        Returns: Station对象的列表
        """

        if self.stations != None:
            return self.stations
        # 待续
        return []


    def getDelayTime(self, station_name):
        """获取某个站点的延迟信息"""
        pass


