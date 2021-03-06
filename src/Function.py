__author__ = 'lvkunyuan'
#coding:utf-8
import json
import httplib
from WebModel import WebModel
#转为utf8字节编码
def Convert2utf8(content):
    content = content.decode('utf-8')
    tmp = bytearray(content, 'utf-8')
    retstr = ''
    for item in tmp:
        retstr += ('-' + hex(item)[2:])
    return retstr


def HttpGetRequest(host, url, decode='utf-8'):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request(method="GET", url=url)
        response = conn.getresponse()
        res = response.read()
        res = res.decode(decode, 'ignore').encode('utf-8').strip()

        if res.__contains__('\n'):
            print 'error 500'
        else:
            return res
    except Exception,e:
        print e


def TrimNiMa(result):
    if result.startswith('NIMA'):
        return result[result.find('NIMA')+5: -2]
    else:
        return result[result.find('NIMA')+5: -7]

if __name__ == '__main__':

    print 'enter main'
    station = '郴州'
    station_utf8byte = Convert2utf8(station)
    trainNo = 'K600'
    trainDate = '2014-12-13'

    queryIsTrainValidUrl = str.format(WebModel.CheckTrainQueryUrl_qunar, trainNo)
    result = HttpGetRequest(WebModel.HostName_qunar, queryIsTrainValidUrl)
    result = TrimNiMa(result)

    result_dic = json.loads(result)
    print result_dic
    result_list = result_dic[u'result']
    if not result_list:
        print 'trainNo is not exist'

    else:
        result = result_list[0][u'key']

    queryTrainScheduleUrl = str.format(WebModel.ScheduleTrainQueryUrl_qunar, result)
    TrainSchedule = HttpGetRequest(WebModel.HostName_qunar, queryTrainScheduleUrl)

    TrainSchedule = TrimNiMa(TrainSchedule)
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


'''
    queryLateUrl = str.format(WebModel.lateQueryUrl_12306, station, trainNo, trainDate, station_utf8byte)
    HttpGetRequest(WebModel.HostName_12306, queryLateUrl, 'gbk')
'''