#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lvkunyuan'

import httplib
from contextlib import closing
from LogHelper import Log


TAG = "CommonService"


class CommonService():

    def Convert2utf8(content):
        content = content.decode('utf-8')
        tmp = bytearray(content, 'utf-8')
        retstr = ''
        for item in tmp:
            retstr += ('-' + hex(item)[2:])
        return retstr


    @staticmethod
    def HttpGetRequest(host, url, decode='utf-8'):
        """HTTP/HTTPS GET 方法"""
        try:
            if host.startswith("https://"):
                connect = httplib.HTTPSConnection
                host = host[8:]
            elif host.startswith("http://"):
                connect = httplib.HTTPConnection
                host = host[7:]
            else:
                connect = httplib.HTTPConnection

            with closing(connect(host)) as conn:
                conn.request(method="GET", url=url)
                response = conn.getresponse()
                if response.status != httplib.OK:
                    return None

                res = response.read()
                res = res.decode(decode, 'ignore').strip()

                return res
        except Exception as e:
            Log.d(TAG, e)


    @staticmethod
    def TrimNiMa(result):
        if result.startswith('NIMA'):
            return result[result.find('NIMA')+5: -2]
        else:
            return result[result.find('NIMA')+5: -7]
