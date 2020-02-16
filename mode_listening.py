#!/usr/bin/python3
# -*- coding:utf-8 -*-
# project:
# user:QiDaChen
# Author: chen.qi
# Mail:chenphoun#outlook.com
# createtime: 2020/2/15 0:14

'''
基于观察者模式，实现一个简单的消息队列，当队列中有消息时，将消息发送给监听者
'''
class MyQueue(Observable):
    def __init__(self):
        super().__init__()
        self.__resource = []

    def has_message(self):
        return True if self.__resource else False

    def queue_size(self):
        return len(self.__resource)

    def add_resource(self, res):
        self.__resource.append(res)
        print("新消息进入，推送...")
        self.listener(obj=res)


class MySubOdd(Observer):
    def update(self, observable, obj):
        if isinstance(observable, MyQueue) and int(obj) % 2 != 0:
            print("I'm MySubOdd, Get Message {} from MyQueue.".format(obj))