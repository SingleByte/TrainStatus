__author__ = 'lvkunyuan'

import json
from CommonService import CommonService
from WebModel import WebModel

class TrainInfo():

    def __init__(self, station, trainNo, trainDate):
        self.station = station
        self.trainNo = trainNo
        self.trainDate = trainDate

    def GetTrainInfo(self):
        queryIsTrainValidUrl = str.format(WebModel.CheckTrainQueryUrl_qunar, self.trainNo)
        result = CommonService.HttpGetRequest(WebModel.HostName_qunar, queryIsTrainValidUrl)
        result = CommonService.TrimNiMa(result)

        result_dic = json.loads(result)
        print result_dic
        result_list = result_dic[u'result']
        if not result_list:
            print 'trainNo is not exist'

        else:
            result = result_list[0][u'key']

        queryTrainScheduleUrl = str.format(WebModel.ScheduleTrainQueryUrl_qunar, result)
        TrainSchedule = CommonService.HttpGetRequest(WebModel.HostName_qunar, queryTrainScheduleUrl)

        TrainSchedule = CommonService.TrimNiMa(TrainSchedule)
        TrainSchedule_dic = json.loads(TrainSchedule, encoding='utf-8')

        TrainSchedule_list = []
        for item in TrainSchedule_dic['trainScheduleBody']:
             TrainSchedule_list.append(item['content'])

        TrainSchedule_list_sort = []
        for item in TrainSchedule_list:
            del item[-1]
            del item[-1]
            del item[-1]
            del item[-2]
            del item[0]
            item[-1] = int(item[-1][:-2]) if item[-1] != 0 else 0


            if TrainSchedule_list_sort == [] or TrainSchedule_list_sort[-1][-1] < item[-1]:
                TrainSchedule_list_sort.append(item)
                continue
            if TrainSchedule_list_sort[0][-1] > item[-1]:
                TrainSchedule_list_sort.insert(0, item)
                continue

            low = 0
            high = TrainSchedule_list_sort.__len__() - 1

            while low <= high:
                mid = (low + high) / 2
                if item[-1] < TrainSchedule_list_sort[mid][-1]:
                    high = mid - 1
                else:
                    low = mid + 1

            TrainSchedule_list_sort.insert(high + 1,  item)