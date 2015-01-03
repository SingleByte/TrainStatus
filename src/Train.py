#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 火车的数据结构以及方法


from WebModel import WebModel
from CommonService import CommonService
from Station import Station
import json


class Train:
    """代表一辆火车"""


    def __init__(self, number, launch_date):
        self.number = number
        self.launch_date = launch_date
        self.stations = None
        self.all_numbers = None

    def getAllNumbers(self):
        """鉴于一辆火车可能有多个名字，该方法用于获取所有名字的列表
        Returns: 车次的列表
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
        self.all_numbers = result.split('/')
        return self.all_numbers


    def getStationList(self):
        """获取该火车经过的所有站点
        Returns: Station对象的列表
        """

        if self.stations != None:
            return self.stations

        # 获取key，由所有车次名组装而成
        query_key = '/'.join(self.getAllNumbers())
        query_url = str.format(WebModel.QUERY_TRAIN_STATIONS_URL, query_key)

        # 请求途径车站列表
        result = CommonService.HttpGetRequest(WebModel.QUNAR_COMMON_HOST, query_url)
        result = CommonService.TrimNiMa(result)
        schedule_dict = json.loads(result, encoding = 'utf-8')
        schedule_list = []
        for item in schedule_dict['trainScheduleBody']:
            content = item['content']
            del content[-1]
            del content[-1]
            del content[-1]
            del content[-2]
            del content[0]

            IDX_DIST = -1
            content[IDX_DIST] = int(content[IDX_DIST][:-2]) if content[IDX_DIST] != 0 else 0

            # 排序时刻表
            station = Station.parseStation(content)
            if not schedule_list or schedule_list[-1].distance < station.distance:
                schedule_list.append(station)
                continue
            elif schedule_list[0].distance > station.distance:
                schedule_list.insert(0, station)
                continue
            
            low = 0
            high = len(schedule_list) - 1
            while low < high:
                mid = (low + high) / 2
                if station.distance < schedule_list[mid].distance:
                    high = mid - 1
                else:
                    low = mid + 1

            schedule_list.insert(high + 1, station)

        self.stations = schedule_list
        return schedule_list



    def getDelayTime(self, station_name):
        """获取某个站点的延迟信息"""
        pass


