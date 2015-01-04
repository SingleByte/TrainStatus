#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试日志辅助类

import sys
sys.path.append("../")
from LogHelper import Log

TAG = "Test"

Log.d(TAG, "Hello")
Log.e(TAG, "World!")
Log.i(TAG, "Hehe")
Log.w(TAG, "XXXX")


