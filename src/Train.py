#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 火车的数据结构以及方法


from WebModel import WebModel
from CommonService import CommonService
import json


class Train:
    """代表一辆火车"""


    def __init__(self, number, launch_date):
        self.number = number
        self.launch_date = launch_date
        self.stations = None
        self.all_numbers = None

    def getAllNumbers(self):
        """鉴于一辆火车可能有多个名字，该方法用于获取所有名字的集合
        Returns: 车次的集合
        """

        if self.all_numbers != None:
            return self.all_numbers

        # 组装完整URL并调用查询
        query_url = str.format(WebModel.QUERY_FULL_TRAIN_NO_URL, self.number)
        result = CommonService.HttpGetRequest(WebModel.QUNAR_COMMON_HOST, query_url)
        result = CommonService.TrimNiMa(result)
        result_list = (json.loads(result))[u'result']
        if not result:
            return None

        result = result_list[0][u'key']
        self.all_numbers = set(result.split('/'))
        return self.all_numbers


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


