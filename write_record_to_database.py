#coding=utf-8
import MySQLdb
import datetime

def write_windpower_record(search_time,fan_data,wind_cut):
    try:
        startdate=datetime.datetime.fromtimestamp(search_time[0])
        enddate=datetime.datetime.fromtimestamp(search_time[1])
        
        string=''
        normal_power=[]
        str_normal_power=''
        db = MySQLdb.connect("localhost","root","mysql",'setupdb')
        cursor=db.cursor()
        #判断是否需要插入数据···
        sql1="select fanid from wind_power where startdate>=%s and startdate<%s;"%('\''+str(startdate)+'\'','\''+str(enddate)+'\'')
        cursor.execute(sql1)
        results = cursor.fetchall()
        if len(results)==0:            
            #for i in range(len(wind_cut)):
            for i in wind_cut:
                string+=',windspeed'+str(int(i*10))
       
            for fan_databasename in fan_data:
                if len(fan_databasename.split('_'))==4:        
                    for wind in wind_cut:                   
                        normal_power.append(round(fan_data[fan_databasename]['normal_power_curve'][round(wind,1)]['poweravg']))
                        
                    str_normal_power=str(normal_power).strip('[]')           
                    sql="insert into wind_power(fanid,fanname,startdate,enddate %s) values(%d,%s,%s,%s,%s);"%(string,fan_data[fan_databasename]['fanset_information']['fanid'],'\''+fan_data[fan_databasename]['fanset_information']['fanname']+'\'','\''+str(startdate)+'\'',
                                                                                                              '\''+str(enddate)+'\'',str_normal_power)
     
                    normal_power=[]
                    cursor.execute(sql)
                    db.commit()
        cursor.close()
        db.close()
    except:
        print "mysql operation wind_power table is false!"
    

def write_windfarm_record(search_time,fan_data):
    try:
        startdate=datetime.datetime.fromtimestamp(search_time[0])
        db = MySQLdb.connect("localhost","root","mysql",'setupdb')
        cursor=db.cursor()
        #判断是否需要插入数据····
        sql1="select fanid from windfarm_statistics where startdate=%s;"%('\''+str(startdate)+'\'')
        cursor.execute(sql1)
        results = cursor.fetchall()
        if len(results)==0:            
            for fan_databasename in fan_data:
                fanid=0
                fanname=''
                WindSpeedAvg=0.0
                TotalPower=0.0
                TotalAvailablehour=0.0
                AveragePower=0.0
                WindNoPower=0.0
                WindNoPowerTime=0.0
                SelfLimitTime=0.0
                SelfLimitPower=0.0
                fChoGenTemAveTime=0.0
                fGeaBeaTemAveTime=0.0
                fGeaOilTemAveTime=0.0
                fGenTemAveTime=0.0
                fGenBeaDriTemAve=0.0
                fConGsclgbTemAve=0.0
                TotalLimitPower=0.0
                TotalLimitTime=0.0
                GeneratTime=0.0
                WaitTime=0.0
                StartTime=0.0
                ServeLossPower=0.0
                ServeLossTime=0.0
                ErrorLossPower=0.0
                ErrorLossTime=0.0
                ErrorNumber=0
                TheoryPower=0.0         
                if len(fan_databasename.split('_'))==4:
                    fanid=fan_data[fan_databasename]['fanset_information']['fanid']
                    fanname=fan_data[fan_databasename]['fanset_information']['fanname']
                    TotalPower=fan_data[fan_databasename]['tenminlog']['totalpower']
                    TotalAvailablehour=round(float(fan_data[fan_databasename]['tenminlog']['totalpower'])/1500)
                    WindNoPowerTime=fan_data[fan_databasename]['tenminlog']['stop_totaltime']
                    WindNoPower=fan_data[fan_databasename]['tenminlog']['stop_reducepower']
                    
                    SelfLimitTime=fan_data[fan_databasename]['tenminlog']['selflimite_totaltime']
                    SelfLimitPower=fan_data[fan_databasename]['tenminlog']['selflimite_reducepower']

                    fChoGenTemAveTime=fan_data[fan_databasename]['tenminlog']['over_temperature']['fChoGenTemAve']['total_time']
                    fGeaBeaTemAveTime=fan_data[fan_databasename]['tenminlog']['over_temperature']['fGeaBeaTemAve']['total_time']
                    fGeaOilTemAveTime=fan_data[fan_databasename]['tenminlog']['over_temperature']['fGeaOilTemAve']['total_time']
                    fGenTemAveTime=fan_data[fan_databasename]['tenminlog']['over_temperature']['fGenTemAve']['total_time']
                    fGenBeaDriTemAve=fan_data[fan_databasename]['tenminlog']['over_temperature']['fGenBeaDriTemAve']['total_time']
                    fConGsclgbTemAve=fan_data[fan_databasename]['tenminlog']['over_temperature']['fConGsclgbTemAve']['total_time']
                    
                    TotalLimitTime=fan_data[fan_databasename]['tenminlog']['limite_totaltime']
                    TotalLimitPower=fan_data[fan_databasename]['tenminlog']['limite_reducepower']

                    
                    for index in range(len(fan_data['all_data_statistic']['aver_wind']['fanid'])):
                        if fan_data['all_data_statistic']['aver_wind']['fanid'][index]==str(fanid):
                            WindSpeedAvg=fan_data['all_data_statistic']['aver_wind']['fan_aver_wind'][index]
                            AveragePower=fan_data['all_data_statistic']['aver_power']['fan_aver_power'][index]
                            GeneratTime=fan_data['all_data_statistic']['generat_time']['fan_totalgenerat_time'][index]

                            WaitTime=fan_data['all_data_statistic']['wait_time']['fan_totalwait_time'][index]
                            StartTime=fan_data['all_data_statistic']['start_time']['fan_totalstart_time'][index]
                            
                            ServeLossPower=fan_data['all_data_statistic']['totalserver4_reducepower']['fan_totalserver4_reducepower'][index]
                            ServeLossTime=fan_data['all_data_statistic']['server_time']['fan_totalserver_time'][index]
                            ErrorLossPower=fan_data['all_data_statistic']['totalerror3_reducepower']['fan_totalerror3_reducepower'][index]
                            ErrorLossTime=fan_data['all_data_statistic']['error_time']['fan_totalerror_time'][index]

                            ErrorNumber=fan_data['all_data_statistic']['total_errornumber']['fan_totalerror_number'][index]
                            TheoryPower=TotalPower+SelfLimitPower+TotalLimitPower+ServeLossPower+ErrorLossPower

                    sql="insert into windfarm_statistics(fanid,fanname,startdate,WindSpeedAvg,TotalPower,TotalAvailablehour,AveragePower,WindNoPower,WindNoPowerTime,SelfLimitTime,SelfLimitPower,fChoGenTemAveTime,fGeaBeaTemAveTime,fGeaOilTemAveTime,"+\
                        "fGenTemAveTime,fGenBeaDriTemAve,fConGsclgbTemAve,TotalLimitPower,TotalLimitTime,GeneratTime,WaitTime,StartTime,ServeLossPower,ServeLossTime,ErrorLossPower,ErrorLossTime,ErrorNumber,TheoryPower) values(%d,%s,%s,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%d,%.1f);"%(fanid,'\''+fanname+'\'','\''+str(startdate)+'\'',WindSpeedAvg,TotalPower,TotalAvailablehour,AveragePower,WindNoPower,WindNoPowerTime,SelfLimitTime,SelfLimitPower,fChoGenTemAveTime,fGeaBeaTemAveTime,fGeaOilTemAveTime,fGenTemAveTime,fGenBeaDriTemAve,fConGsclgbTemAve,TotalLimitPower,TotalLimitTime,GeneratTime,WaitTime,StartTime,ServeLossPower,ServeLossTime,ErrorLossPower,ErrorLossTime,ErrorNumber,TheoryPower)
                    #print sql
                    cursor.execute(sql)
                    db.commit()
        cursor.close()
        db.close()
    except:
        print "mysql operation windfarm_statistics table is false!"
        
        
