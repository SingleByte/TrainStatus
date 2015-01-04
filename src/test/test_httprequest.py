#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
sys.path.append("../")
from CommonService import CommonService

print CommonService.HttpGetRequest("https://kyfw.12306.cn", "/otn/lcxxcx/init")

