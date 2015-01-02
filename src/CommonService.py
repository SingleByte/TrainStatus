__author__ = 'lvkunyuan'

import httplib
class CommonService():

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