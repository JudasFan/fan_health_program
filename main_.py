# -*- coding: cp936 -*-
import time
import connect_database as cnd
import check_time as ct
import fan_database_namelist as fdn
import gc
import write_to_excel as wte
import copy
import init_global_variate as igv
import datetime
import check_database_name as cdn
import write_record_to_database as wrtd
#靠靠靠靠靠贩�

def main():

    #检查需要插入数据的数据表是否存在···
    wind_cut=cdn.create_windpower_table('setupdb')
    cdn.create_table_of_windfarm_statistics('setupdb')
    month_rule_list=[]
    day_rule_list=[]
    (fan_dict,fan_tuple)=copy.deepcopy(igv.init_global_variate())
    #fan_array=fdn.fan_database_namelist(2)
    fan_array=fdn.fan_database_namelist()
    #print len(fan_array)
    now_datetime=datetime.datetime(2016,2,1)
    
    while 1:
        time.sleep(3)
        #now_datetime=datetime.datetime.now()
        
        now_month=now_datetime.month
        now_day=now_datetime.day        
        last_datatime=now_datetime-datetime.timedelta(1)
        if len(month_rule_list)==0:
            month_rule_list.append(now_month)            
            start_month_date=datetime.datetime(now_datetime.year,now_datetime.month-1,1)
            end_month_date=datetime.datetime(now_datetime.year,now_datetime.month,1)
            
            #print start_month_date
            #print end_month_date
            #start_time='2016-1-1'
            #end_time='2017-2-1'  
            #search_time=ct.check_datetime(start_time,end_time)
            search_time=ct.check_datetime(start_month_date,end_month_date)
            #print search_time
            #统计标准功率曲线···
            fan_data=copy.deepcopy(cnd.connect_fan_database_statistics_normal_windpower(fan_array,search_time,fan_dict,fan_tuple))
            wrtd.write_windpower_record(search_time,fan_data,wind_cut)
            
        else:
            if now_month not in month_rule_list:
                month_rule_list.append(now_month)
                start_month_date=datetime.datetime(last_datatime.year,last_datatime.month,1)
                end_month_date=datetime.datetime(now_datetime.year,now_datetime.month,1)
                search_time=ct.check_datetime(start_month_date,end_month_date)
                fan_data=copy.deepcopy(cnd.connect_fan_database_statistics_normal_windpower(fan_array,search_time,fan_dict,fan_tuple))                
                wrtd.write_windpower_record(search_time,fan_data,wind_cut)                
                month_rule_list.pop(0)
            else:
                print month_rule_list[0]

                
        if len(day_rule_list)==0:
            day_rule_list.append(now_day)
            #start_time='2016-1-1'
            #end_time='2017-2-1'
            start_time=last_datatime
            end_time=now_datetime
            search_time=ct.check_datetime(start_time,end_time)
            fan_data=copy.deepcopy(cnd.connect_fan_database(search_time,fan_dict,fan_tuple))
            wrtd.write_windfarm_record(search_time,fan_data) 
        else:
            if now_day not in day_rule_list:
                day_rule_list.append(now_day)
                
                start_time=last_datatime
                end_time=now_datetime
                
                search_time=ct.check_datetime(start_time,end_time)
                fan_data=copy.deepcopy(cnd.connect_fan_database(search_time,fan_dict,fan_tuple))
                wrtd.write_windfarm_record(search_time,fan_data) 
                day_rule_list.pop(0)
            else:
                print day_rule_list[0]

        now_datetime+=datetime.timedelta(1)
        

if __name__=='__main__':    
    main()
    
    gc.collect()
    print 'over program!'
   
