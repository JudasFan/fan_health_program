#coding=utf-8
#import plot_chat as pc


def all_data_statistic(fan_data):
    total_firerror_code=[]
    total_huberror_code=[]
    total_conerror_code=[]
    total_yawerror_code=[]
    total_firwaring_code=[]
    
    fan_data['all_data_statistic']={}
    fan_data['all_data_statistic']['totalpower']={'fanid':[],'fan_totalpower':[]}
    fan_data['all_data_statistic']['total_reducepower']={'fanid':[],'fan_total_reducepower':[]}
    fan_data['all_data_statistic']['totallimit_reducepower']={'fanid':[],'fan_totallimit_reducepower':[]}
    fan_data['all_data_statistic']['totalselflimit_reducepower']={'fanid':[],'fan_totalselflimit_reducepower':[]}
    fan_data['all_data_statistic']['totalerror3_reducepower']={'fanid':[],'fan_totalerror3_reducepower':[]}
    fan_data['all_data_statistic']['totalserver4_reducepower']={'fanid':[],'fan_totalserver4_reducepower':[]}
    #汇智天华新中控程序将增加的发电量···
    fan_data['all_data_statistic']['normal_totalpower']={'fanid':[],'fan_normal_totalpower':[]}
    fan_data['all_data_statistic']['hzth_increase_totalpower']={'fanid':[],'fan_hzth_increase_totalpower':[]}

    fan_data['all_data_statistic']['generat_time']={'fanid':[],'fan_totalgenerat_time':[]}
    fan_data['all_data_statistic']['limit_time']={'fanid':[],'fan_totallimit_time':[]}
    fan_data['all_data_statistic']['selflimit_time']={'fanid':[],'fan_totalselflimit_time':[]}
    fan_data['all_data_statistic']['error_time']={'fanid':[],'fan_totalerror_time':[]}
    fan_data['all_data_statistic']['server_time']={'fanid':[],'fan_totalserver_time':[]}    
    fan_data['all_data_statistic']['wait_time']={'fanid':[],'fan_totalwait_time':[]}
    fan_data['all_data_statistic']['start_time']={'fanid':[],'fan_totalstart_time':[]}

    
    fan_data['all_data_statistic']['total_errornumber']={'fanid':[],'fan_totalerror_number':[]}
    
    fan_data['all_data_statistic']['total_firerror']={'fanid':[],'fan_totalfirerror_number':[]}
    fan_data['all_data_statistic']['total_huberror']={'fanid':[],'fan_totalhuberror_number':[]}
    fan_data['all_data_statistic']['total_conerror']={'fanid':[],'fan_totalconerror_number':[]}
    fan_data['all_data_statistic']['total_yawerror']={'fanid':[],'fan_totalyawerror_number':[]}
    fan_data['all_data_statistic']['total_firwaring']={'fanid':[],'fan_totalfirwaring_number':[]}

    fan_data['all_data_statistic']['aver_wind']={'fanid':[],'fan_aver_wind':[]}
    fan_data['all_data_statistic']['aver_power']={'fanid':[],'fan_aver_power':[]}
    fan_data['all_data_statistic']['all_overtemperature_pie']={'fChoGenTemAve':{'total_time':0},'fGeaBeaTemAve':{'total_time':0},'fGeaOilTemAve':{'total_time':0},'fGenTemAve':{'total_time':0},'fGenBeaDriTemAve':{'total_time':0},'fConGsclgbTemAve':{'total_time':0}}
    
    for fan_databasename in fan_data:
        #排除“all_data_statistic”字典的影响···
        if len(fan_databasename.split('_'))==4:            
            fanid_buf=fan_databasename.split('_')[2]
            #print fanid_buf 输出将要统计总数据的风机ID号码···
            fan_data['all_data_statistic']['totalpower']['fanid'].append(fanid_buf)
            fan_data['all_data_statistic']['totalpower']['fan_totalpower'].append(fan_data[fan_databasename]['tenminlog']['totalpower'])

            #此时预计将要把原来机组正常最优发电时发电量同HZTH技改后的最优发电量做在同一张柱状图表上来做对比···
            fan_data['all_data_statistic']['normal_totalpower']['fanid'].append(fanid_buf)
            fan_data['all_data_statistic']['normal_totalpower']['fan_normal_totalpower'].append(fan_data[fan_databasename]['tenminlog']['normal_totalpower'])            

            fan_data['all_data_statistic']['hzth_increase_totalpower']['fanid'].append(fanid_buf)
            fan_data['all_data_statistic']['hzth_increase_totalpower']['fan_hzth_increase_totalpower'].append(fan_data[fan_databasename]['tenminlog']['hzth_increase_totalpower'])

            fan_data['all_data_statistic']['total_reducepower']['fanid'].append(fanid_buf)
            fan_data['all_data_statistic']['total_reducepower']['fan_total_reducepower'].append(fan_data[fan_databasename]['tenminlog']['stop_reducepower'])

            fan_data['all_data_statistic']['totallimit_reducepower']['fanid'].append(fanid_buf)
            fan_data['all_data_statistic']['totallimit_reducepower']['fan_totallimit_reducepower'].append(fan_data[fan_databasename]['tenminlog']['limite_reducepower'])

            fan_data['all_data_statistic']['totalselflimit_reducepower']['fanid'].append(fanid_buf)
            fan_data['all_data_statistic']['totalselflimit_reducepower']['fan_totalselflimit_reducepower'].append(fan_data[fan_databasename]['tenminlog']['selflimite_reducepower'])

            fan_data['all_data_statistic']['totalerror3_reducepower']['fanid'].append(fanid_buf)


            #此时统计平均风速数据···
            #此时统计平均功率数据···
            
            fan_data['all_data_statistic']['aver_wind']['fanid'].append(fanid_buf)
            if len(fan_data[fan_databasename]['tenminlog']['all_power_splat']['wind_list'])==0:
                fan_data['all_data_statistic']['aver_wind']['fan_aver_wind'].append(0)
            else:                
                fan_data['all_data_statistic']['aver_wind']['fan_aver_wind'].append(sum(fan_data[fan_databasename]['tenminlog']['all_power_splat']['wind_list'])/len(fan_data[fan_databasename]['tenminlog']['all_power_splat']['wind_list']))

            fan_data['all_data_statistic']['aver_power']['fanid'].append(fanid_buf)
            if len(fan_data[fan_databasename]['tenminlog']['all_power_splat']['power_list'])==0:
                fan_data['all_data_statistic']['aver_power']['fan_aver_power'].append(0)
            else:                
                fan_data['all_data_statistic']['aver_power']['fan_aver_power'].append(sum(fan_data[fan_databasename]['tenminlog']['all_power_splat']['power_list'])/len(fan_data[fan_databasename]['tenminlog']['all_power_splat']['power_list']))
            
            #此时统计超温比例数据···
            #此时统计超温比例数据···
            #此时统计超温比例数据···
            #此时统计超温比例数据···
            fan_data['all_data_statistic']['all_overtemperature_pie']['fChoGenTemAve']['total_time']+=fan_data[fan_databasename]['tenminlog']['over_temperature']['fChoGenTemAve']['total_time']
            fan_data['all_data_statistic']['all_overtemperature_pie']['fGeaBeaTemAve']['total_time']+=fan_data[fan_databasename]['tenminlog']['over_temperature']['fGeaBeaTemAve']['total_time']
            fan_data['all_data_statistic']['all_overtemperature_pie']['fGeaOilTemAve']['total_time']+=fan_data[fan_databasename]['tenminlog']['over_temperature']['fGeaOilTemAve']['total_time']
            fan_data['all_data_statistic']['all_overtemperature_pie']['fGenTemAve']['total_time']+=fan_data[fan_databasename]['tenminlog']['over_temperature']['fGenTemAve']['total_time']
            fan_data['all_data_statistic']['all_overtemperature_pie']['fGenBeaDriTemAve']['total_time']+=fan_data[fan_databasename]['tenminlog']['over_temperature']['fGenBeaDriTemAve']['total_time']
            fan_data['all_data_statistic']['all_overtemperature_pie']['fConGsclgbTemAve']['total_time']+=fan_data[fan_databasename]['tenminlog']['over_temperature']['fConGsclgbTemAve']['total_time']

            

            # 当风机使用abb新程序的情况下：···
            # 当风机使用abb新程序的情况下：···
            # 当风机使用abb新程序的情况下：···
            try:
                if 7 not in fan_data[fan_databasename]['stames']:
                    if 3 in fan_data[fan_databasename]['stames']:
                        fan_data['all_data_statistic']['totalerror3_reducepower']['fan_totalerror3_reducepower'].append(fan_data[fan_databasename]['stames'][3]['reduce_power'])
                    else:
                        fan_data['all_data_statistic']['totalerror3_reducepower']['fan_totalerror3_reducepower'].append(0)
                        print 'the statue 3 is not in this fan```'

                    fan_data['all_data_statistic']['totalserver4_reducepower']['fanid'].append(fanid_buf)
                    if 4 in fan_data[fan_databasename]['stames']:                
                        fan_data['all_data_statistic']['totalserver4_reducepower']['fan_totalserver4_reducepower'].append(fan_data[fan_databasename]['stames'][4]['reduce_power'])
                    else:
                        fan_data['all_data_statistic']['totalserver4_reducepower']['fan_totalserver4_reducepower'].append(0)
                        print 'the statue 4 is not in this fan```'


                    fan_data['all_data_statistic']['generat_time']['fanid'].append(fanid_buf)
                    if 2 in fan_data[fan_databasename]['stames']:                
                        fan_data['all_data_statistic']['generat_time']['fan_totalgenerat_time'].append(fan_data[fan_databasename]['stames'][2]['stamescode_time'])
                    else:
                        fan_data['all_data_statistic']['generat_time']['fan_totalgenerat_time'].append(0)
                        print 'the statue 2 is not in this fan```'

                    fan_data['all_data_statistic']['limit_time']['fanid'].append(fanid_buf)            
                    fan_data['all_data_statistic']['limit_time']['fan_totallimit_time'].append(fan_data[fan_databasename]['tenminlog']['limite_totaltime'])

                    fan_data['all_data_statistic']['selflimit_time']['fanid'].append(fanid_buf)
                    fan_data['all_data_statistic']['selflimit_time']['fan_totalselflimit_time'].append(fan_data[fan_databasename]['tenminlog']['over_temperature_totaltime'])

                    fan_data['all_data_statistic']['error_time']['fanid'].append(fanid_buf)
                    if 3 in fan_data[fan_databasename]['stames']:   
                        fan_data['all_data_statistic']['error_time']['fan_totalerror_time'].append(fan_data[fan_databasename]['stames'][3]['stamescode_time'])
                    else:
                        fan_data['all_data_statistic']['error_time']['fan_totalerror_time'].append(0)

                    fan_data['all_data_statistic']['server_time']['fanid'].append(fanid_buf)
                    if 4 in fan_data[fan_databasename]['stames']:   
                        fan_data['all_data_statistic']['server_time']['fan_totalserver_time'].append(fan_data[fan_databasename]['stames'][4]['stamescode_time'])
                    else:
                        fan_data['all_data_statistic']['server_time']['fan_totalserver_time'].append(0)

                    fan_data['all_data_statistic']['wait_time']['fanid'].append(fanid_buf)
                    if 0 in fan_data[fan_databasename]['stames']:   
                        fan_data['all_data_statistic']['wait_time']['fan_totalwait_time'].append(fan_data[fan_databasename]['stames'][0]['stamescode_time'])
                    else:
                        fan_data['all_data_statistic']['wait_time']['fan_totalwait_time'].append(0)
                        print 'the statue 0 is not in this fan```'

                    fan_data['all_data_statistic']['start_time']['fanid'].append(fanid_buf)
                    if 1 in fan_data[fan_databasename]['stames']:   
                        fan_data['all_data_statistic']['start_time']['fan_totalstart_time'].append(fan_data[fan_databasename]['stames'][1]['stamescode_time'])
                    else:
                        fan_data['all_data_statistic']['start_time']['fan_totalstart_time'].append(0)
                        print 'the statue 1 is not in this fan```'

                    fan_data['all_data_statistic']['total_errornumber']['fanid'].append(fanid_buf)
                    if 3 in fan_data[fan_databasename]['stames']:                
                        fan_data['all_data_statistic']['total_errornumber']['fan_totalerror_number'].append(fan_data[fan_databasename]['stames'][3]['stamescode_number'])
                    else:
                        fan_data['all_data_statistic']['total_errornumber']['fan_totalerror_number'].append(0)


                #当使用旧的abb程序十几种状态码···
                #当使用旧的abb程序十几种状态码···
                #当使用旧的abb程序十几种状态码···
                #当使用旧的abb程序十几种状态码···
                else :
                    if 1 in fan_data[fan_databasename]['stames']:
                        fan_data['all_data_statistic']['totalerror3_reducepower']['fan_totalerror3_reducepower'].append(fan_data[fan_databasename]['stames'][1]['reduce_power'])
                    else:
                        fan_data['all_data_statistic']['totalerror3_reducepower']['fan_totalerror3_reducepower'].append(0)
                        print 'the statue 3 is not in this fan```'

                    fan_data['all_data_statistic']['totalserver4_reducepower']['fanid'].append(fanid_buf)
                    if 13 in fan_data[fan_databasename]['stames']:                
                        fan_data['all_data_statistic']['totalserver4_reducepower']['fan_totalserver4_reducepower'].append(fan_data[fan_databasename]['stames'][13]['reduce_power'])
                    else:
                        fan_data['all_data_statistic']['totalserver4_reducepower']['fan_totalserver4_reducepower'].append(0)
                        print 'the statue 4 is not in this fan```'


                    fan_data['all_data_statistic']['generat_time']['fanid'].append(fanid_buf)
                    if 7 in fan_data[fan_databasename]['stames']:                
                        fan_data['all_data_statistic']['generat_time']['fan_totalgenerat_time'].append(fan_data[fan_databasename]['stames'][7]['stamescode_time'])
                    else:
                        fan_data['all_data_statistic']['generat_time']['fan_totalgenerat_time'].append(0)
                        print 'the statue 2 is not in this fan```'

                    fan_data['all_data_statistic']['limit_time']['fanid'].append(fanid_buf)            
                    fan_data['all_data_statistic']['limit_time']['fan_totallimit_time'].append(fan_data[fan_databasename]['tenminlog']['limite_totaltime'])

                    fan_data['all_data_statistic']['selflimit_time']['fanid'].append(fanid_buf)
                    fan_data['all_data_statistic']['selflimit_time']['fan_totalselflimit_time'].append(fan_data[fan_databasename]['tenminlog']['over_temperature_totaltime'])

                    fan_data['all_data_statistic']['error_time']['fanid'].append(fanid_buf)
                    if 1 in fan_data[fan_databasename]['stames']:   
                        fan_data['all_data_statistic']['error_time']['fan_totalerror_time'].append(fan_data[fan_databasename]['stames'][1]['stamescode_time'])
                    else:
                        fan_data['all_data_statistic']['error_time']['fan_totalerror_time'].append(0)

                    fan_data['all_data_statistic']['server_time']['fanid'].append(fanid_buf)
                    if 13 in fan_data[fan_databasename]['stames']:   
                        fan_data['all_data_statistic']['server_time']['fan_totalserver_time'].append(fan_data[fan_databasename]['stames'][13]['stamescode_time'])
                    else:
                        fan_data['all_data_statistic']['server_time']['fan_totalserver_time'].append(0)

                    fan_data['all_data_statistic']['wait_time']['fanid'].append(fanid_buf)
                    if 4 in fan_data[fan_databasename]['stames']:   
                        fan_data['all_data_statistic']['wait_time']['fan_totalwait_time'].append(fan_data[fan_databasename]['stames'][4]['stamescode_time'])
                    else:
                        fan_data['all_data_statistic']['wait_time']['fan_totalwait_time'].append(0)
                        print 'the statue 0 is not in this fan```'

                    fan_data['all_data_statistic']['start_time']['fanid'].append(fanid_buf)
                    if 5 in fan_data[fan_databasename]['stames']:   
                        fan_data['all_data_statistic']['start_time']['fan_totalstart_time'].append(fan_data[fan_databasename]['stames'][5]['stamescode_time'])
                    else:
                        fan_data['all_data_statistic']['start_time']['fan_totalstart_time'].append(0)
                        print 'the statue 1 is not in this fan```'

                    fan_data['all_data_statistic']['total_errornumber']['fanid'].append(fanid_buf)
                    if 1 in fan_data[fan_databasename]['stames']:                
                        fan_data['all_data_statistic']['total_errornumber']['fan_totalerror_number'].append(fan_data[fan_databasename]['stames'][1]['stamescode_number'])
                    else:
                        fan_data['all_data_statistic']['total_errornumber']['fan_totalerror_number'].append(0)
            except:
                print 'the function of all_data_statistic is error!'
                

            for firerror_code in fan_data[fan_databasename]['error']['uiErrFir']['ErrFir_code']:
                if firerror_code not in total_firerror_code:
                    total_firerror_code.append(firerror_code)

            for huberror_code in fan_data[fan_databasename]['error']['uiHubErr']['HubErr_code']:
                if huberror_code not in total_huberror_code:
                    total_huberror_code.append(huberror_code)
                    
            for conerror_code in fan_data[fan_databasename]['error']['uiConErr']['ConErr_code']:
                if conerror_code not in total_conerror_code:
                    total_conerror_code.append(conerror_code)

            for yawerror_code in fan_data[fan_databasename]['error']['uiYawErr']['YawErr_code']:
                if yawerror_code not in total_yawerror_code:
                    total_yawerror_code.append(yawerror_code)

            for firwaring_code in fan_data[fan_databasename]['error']['uiWarFir']['WarFir_code']:
                if firwaring_code not in total_firerror_code:
                    total_firwaring_code.append(firwaring_code)
                    
    #计算总风场的各个模块类型的故障的数量···
    for firerror_code in total_firerror_code:
        #print firerror_code
        fan_data['all_data_statistic']['total_firerror']['fanid'].append(firerror_code)
        total_number=0
        for fan_databasename in fan_data:
            if len(fan_databasename.split('_'))==4:
                #print fan_data[fan_databasename]['error']['uiErrFir']['ErrFir_code'][536]
                if firerror_code in fan_data[fan_databasename]['error']['uiErrFir']['ErrFir_code']:
                    total_number+=fan_data[fan_databasename]['error']['uiErrFir']['ErrFir_code'][firerror_code]
        fan_data['all_data_statistic']['total_firerror']['fan_totalfirerror_number'].append(total_number)

    for huberror_code in total_huberror_code:
        fan_data['all_data_statistic']['total_huberror']['fanid'].append(huberror_code)
        total_number=0
        for fan_databasename in fan_data:
            
            if len(fan_databasename.split('_'))==4:
                if huberror_code in fan_data[fan_databasename]['error']['uiHubErr']['HubErr_code']:
                    total_number+=fan_data[fan_databasename]['error']['uiHubErr']['HubErr_code'][huberror_code]
        fan_data['all_data_statistic']['total_huberror']['fan_totalhuberror_number'].append(total_number)

    for conerror_code in total_conerror_code:
        fan_data['all_data_statistic']['total_conerror']['fanid'].append(conerror_code)
        total_number=0
        for fan_databasename in fan_data:
            
            if len(fan_databasename.split('_'))==4:
                if conerror_code in fan_data[fan_databasename]['error']['uiConErr']['ConErr_code']:
                    total_number+=fan_data[fan_databasename]['error']['uiConErr']['ConErr_code'][conerror_code]
        fan_data['all_data_statistic']['total_conerror']['fan_totalconerror_number'].append(total_number)

    for yawerror_code in total_yawerror_code:
        fan_data['all_data_statistic']['total_yawerror']['fanid'].append(yawerror_code)
        total_number=0
        for fan_databasename in fan_data:
            
            if len(fan_databasename.split('_'))==4:
                if yawerror_code in fan_data[fan_databasename]['error']['uiYawErr']['YawErr_code']:
                    total_number+=fan_data[fan_databasename]['error']['uiYawErr']['YawErr_code'][yawerror_code]
        fan_data['all_data_statistic']['total_yawerror']['fan_totalyawerror_number'].append(total_number)

    for firwaring_code in total_firwaring_code:
        fan_data['all_data_statistic']['total_firwaring']['fanid'].append(firwaring_code)
        total_number=0
        for fan_databasename in fan_data:
            
            if len(fan_databasename.split('_'))==4:
                if firwaring_code in fan_data[fan_databasename]['error']['uiWarFir']['WarFir_code']:
                    total_number+=fan_data[fan_databasename]['error']['uiWarFir']['WarFir_code'][firwaring_code]
        fan_data['all_data_statistic']['total_firwaring']['fan_totalfirwaring_number'].append(total_number)
                 
                
        

    return  fan_data      

    '''        
    pc.plotting_all_power(1,fan_data['all_data_statistic']['totalpower'])
    #绘制理论发电量均值图···
    pc.plotting_all_part_power(25,fan_data['all_data_statistic']['totalpower'],fan_data['all_data_statistic']['totallimit_reducepower'],fan_data['all_data_statistic']['totalselflimit_reducepower'],
                               fan_data['all_data_statistic']['totalerror3_reducepower'],fan_data['all_data_statistic']['totalserver4_reducepower'])
    #根据每台机组发电量数据绘制折合可利用小时柱状图···
    pc.plotting_all_available_hour(2,fan_data['all_data_statistic']['totalpower'])
    pc.plotting_increase_power(3,fan_data['all_data_statistic']['normal_totalpower'],fan_data['all_data_statistic']['hzth_increase_totalpower'])

    pc.plotting_all_reducepower(4,fan_data['all_data_statistic']['total_reducepower'])
    pc.plotting_all_limitepower(5,fan_data['all_data_statistic']['totallimit_reducepower'])
    pc.plotting_all_selflimitpower(6,fan_data['all_data_statistic']['totalselflimit_reducepower'])
    pc.plotting_all_errorpower(7,fan_data['all_data_statistic']['totalerror3_reducepower'])
    pc.plotting_all_serverpower(8,fan_data['all_data_statistic']['totalserver4_reducepower'])


    pc.plotting_all_generat_time(9,fan_data['all_data_statistic']['generat_time'])
    pc.plotting_all_limit_time(10,fan_data['all_data_statistic']['limit_time'])
    pc.plotting_all_selflimit_time(11,fan_data['all_data_statistic']['selflimit_time'])
    pc.plotting_all_error_time(12,fan_data['all_data_statistic']['error_time'])
    pc.plotting_all_server_time(13,fan_data['all_data_statistic']['server_time'])
    pc.plotting_all_wait_time(14,fan_data['all_data_statistic']['wait_time'])
    pc.plotting_all_start_time(15,fan_data['all_data_statistic']['start_time'])
    

    pc.plotting_all_errornumber(16,fan_data['all_data_statistic']['total_errornumber'])
    pc.plotting_all_firerror(17,fan_data['all_data_statistic']['total_firerror'])
    pc.plotting_all_huberror(18,fan_data['all_data_statistic']['total_huberror'])
    pc.plotting_all_conerror(19,fan_data['all_data_statistic']['total_conerror'])
    pc.plotting_all_yawerror(20,fan_data['all_data_statistic']['total_yawerror'])
    pc.plotting_all_firwaring(21,fan_data['all_data_statistic']['total_firwaring'])
    pc.plotting_all_avrg_wind(22,fan_data['all_data_statistic']['aver_wind'])
    pc.plotting_all_avrg_power(23,fan_data['all_data_statistic']['aver_power'])
    pc.plotting_all_overtemperature_pie(24,fan_data['all_data_statistic']['all_overtemperature_pie'])
    '''
     
    



