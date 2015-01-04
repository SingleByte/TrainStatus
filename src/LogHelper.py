#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 辅助日志类


class Log:
    """日志输出辅助类"""
    @staticmethod
    def d(tag, msg):
        """输出debug级别信息"""
        print "D/" + str(tag), msg

    @staticmethod
    def e(tag, msg):
        """输出error级别信息"""
        print "E/" + str(tag), msg

    @staticmethod
    def i(tag, msg):
        """输出info级别信息"""
        print "I/" + str(tag), msg

    @staticmethod
    def w(tag, msg):
        """输出warn级别信息"""
        print "W/" + str(tag), msg

