__author__ = 'lvkunyuan'


class WebModel():
    HostName_12306 = 'dynamic.12306.cn'
    lateQueryUrl_12306 = '/map_zwdcx/cx.jsp?cz={0}&cc={1}&cxlx=0&rq={2}&czEn={3}'

    HostName_qunar = 'train.qunar.com'
    CheckTrainQueryUrl_qunar = '/qunar/checiSuggest.jsp?include_coach_suggest=false&lang=zh&q={0}&sa=true&format=js&callback=NIMA'
    ScheduleTrainQueryUrl_qunar = '/qunar/checiInfo.jsp?method_name=buy&ex_track=&q={0}&date=&format=json&cityname=123456&ver=1420092773443&callback=NIMA'