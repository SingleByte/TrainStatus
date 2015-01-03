#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试Train类


import sys
sys.path.append("../")
from Train import Train

train = Train("K600", "2014-1-2")
print train.getAllNumbers()


