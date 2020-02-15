#!/usr/bin/python3
# -*- coding:utf-8 -*-
# project:
# user:QiDaChen
# Author: chen.qi
# Mail:chenphoun#outlook.com
# createtime: 2020/2/15 0:14

class HotWaterListen():
    def __init__(self):
        self.m_lineTemp = 20
        self.m_lineTime = 10
        self.m_temp = 0
        self.upTemp()
    def upTemp(self):
        self.m_tem+=1 