#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 火车的数据结构以及方法


from WebModel import WebModel
from CommonService import CommonService
from Station import Station
import json
import re


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
            
            low = -1 
            high = len(schedule_list)
            # 初始化： list[low] <= x && list[high] > x
            while (low + 1) != high:
                mid = (low + high) / 2
                if station.distance < schedule_list[mid].distance:
                    # 保持：list[high] > x
                    high = mid
                else:
                    # 保持：list[low] <= x
                    low = mid

            # 终止：(low + 1) == high && list[low] <= x && list[high] > x
            # 则list[low + 1]即为插入位置
            schedule_list.insert(low + 1, station)

        self.stations = schedule_list
        return schedule_list



    def getExactlyTrainNumber(self, station_name):
        """获取列车到达某个站点时的精确车次"""
        return self.number


    def encodeStationName(self, station_name):
        """将站名编码为12306使用的UTF-8形式"""
        bytes_str = station_name.encode("utf-8")
        result = "".join(["-" + x.encode("hex") for x in bytes_str])
        return result.upper()


    def getArriveMoment(self, station_name):
        """获取列车到达某个站点的时刻
        Returns: hh:mm形式的时间字符串或None
        """

        # 获取精确车次
        train_no = self.getExactlyTrainNumber(station_name)
        # 组装URL
        query_url = str.format(WebModel.DELAY_TIME_URL, station_name.encode("utf-8"), train_no,\
                self.launch_date, self.encodeStationName(station_name))
        
        # 请求
        result = CommonService.HttpGetRequest(WebModel.DELAY_TIME_HOST, query_url,\
                decode="gbk")

        if not result:
            return None

        # 解析时间
        TIME_PATTERN = re.compile("\d+\:\d+")
        matchs = re.search(TIME_PATTERN, result)
        if not matchs:
            return None

        arrive_time = matchs.group(0)
        return arrive_time 


