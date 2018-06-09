#coding=utf-8
import time
import datetime

#生成查询时间戳元组···

def check_time(start_time,end_time):
    #start_time=raw_input('输入查询的起始日期：')
    #end_time=raw_input('输入查询的结束日期：')    
    #start_time='2016-7-1'
    #end_time='2016-8-1'
    #times=time.mktime(time.strptime(end_time,'%Y-%m-%d'))-time.mktime(time.strptime(start_time,'%Y-%m-%d'))
    l_start_time=time.mktime(time.strptime(start_time,'%Y-%m-%d'))
    l_end_time=time.mktime(time.strptime(end_time,'%Y-%m-%d'))
    return l_start_time,l_end_time


def check_datetime(start_time,end_time):
    #start_time=raw_input('输入查询的起始日期：')
    #end_time=raw_input('输入查询的结束日期：')    
    #start_time='2016-7-1'
    #end_time='2016-8-1'
    #times=time.mktime(time.strptime(end_time,'%Y-%m-%d'))-time.mktime(time.strptime(start_time,'%Y-%m-%d'))
    #l_start_time=time.mktime(time.strptime(start_time,'%Y-%m-%d'))
    #l_end_time=time.mktime(time.strptime(end_time,'%Y-%m-%d'))

    l_start_time=time.mktime(start_time.timetuple())
    l_end_time=time.mktime(end_time.timetuple())
    
    
    return l_start_time,l_end_time


