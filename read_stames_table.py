#coding=utf-8
import fan_element_struct as fes
import calculate_data as cdata
import calculate_stames_reducepower as csr
#import plot_chat as pc
import copy

#fan_tuple=copy.deepcopy(fes.fan_element_struct())
#fan_dict=copy.deepcopy(fan_tuple[0])

def read_stames_table(cursor,fan_databasename,search_time,fan_dict,fan_tuple):
    
    fan_dict[fan_databasename]['stames']={}
    
    sql="SELECT uiStaCod,dtTimSta,dtTimEnd FROM stames where dtTimSta>=%d and dtTimSta<%d;" %(search_time[0],search_time[1])
    try:
        
        cursor.execute(sql)
        results = cursor.fetchall()
        #print len(results)
        row_buf2=[]
        for row in results:            
            row_buf2.append(copy.deepcopy(row))
            if len(row_buf2)==2:
                stames_alive_buf=[0,0]
                if row_buf2[0][0] not in fan_dict[fan_databasename]['stames']:
                    fan_dict[fan_databasename]['stames'][row_buf2[0][0]]=copy.deepcopy(fan_tuple[2])  #初始化机组状态数据结构字典···
                    fan_dict[fan_databasename]['stames'][row_buf2[0][0]]['stamescode_number']=1
                    if row_buf2[1][1]>row_buf2[0][1]:
                        stames_alive_buf[0]=row_buf2[0][1]
                        stames_alive_buf[1]=row_buf2[1][1]
                        fan_dict[fan_databasename]['stames'][row_buf2[0][0]]['stamescode_time']=row_buf2[1][1]-row_buf2[0][1]
                        fan_dict[fan_databasename]['stames'][row_buf2[0][0]]['stames_alive_list'].append(copy.deepcopy(stames_alive_buf)) #状态存活数据记录···
                    
                else:
                    if row_buf2[1][0]!=row_buf2[0][0]:
                        fan_dict[fan_databasename]['stames'][row_buf2[0][0]]['stamescode_number']+=1
                    
                    if row_buf2[1][1]>row_buf2[0][1]:
                        fan_dict[fan_databasename]['stames'][row_buf2[0][0]]['stamescode_time']+=row_buf2[1][1]-row_buf2[0][1]
                        stames_alive_buf[0]=row_buf2[0][1]
                        stames_alive_buf[1]=row_buf2[1][1]
                        fan_dict[fan_databasename]['stames'][row_buf2[0][0]]['stames_alive_list'].append(copy.deepcopy(stames_alive_buf))
                        
                row_buf2.pop(0)
                
        if results[0][1]-search_time[0]>0:            
            fan_dict[fan_databasename]['stames'][results[0][0]]['stamescode_time']+=(results[0][1]-search_time[0])

        if search_time[1]-results[len(results)-1][1]>0:            
            fan_dict[fan_databasename]['stames'][results[len(results)-1][0]]['stamescode_time']+=(search_time[1]-results[len(results)-1][1])
        
        for stames_code in fan_dict[fan_databasename]['stames']:
            #fan_dict[fan_databasename]['stames'][stames_code]['stamescode_time']/=3600            
            fan_dict[fan_databasename]['stames'][stames_code]['stamescode_time']=round(float(fan_dict[fan_databasename]['stames'][stames_code]['stamescode_time'])/3600,1)
            #print len(results),fan_databasename,stames_code,fan_dict[fan_databasename]['stames'][stames_code]['stamescode_time'],fan_dict[fan_databasename]['stames'][stames_code]['stamescode_number']
    except:
        print ":  Error: unable to fecth data of dtcurday"

    return fan_dict

def read_tenminlog_table(cursor,fan_databasename,search_time,fan_dict):
    print 'read tenminlog :'+str(fan_databasename)
    sql="SELECT dtSysTim, fChoGenTemAve,fGeaBeaTemAve,fGeaOilTemAve,fGenTemAve,fGenBeaDriTemAve,fConGsclgbTemAve,ufWinSpeAve,fPowerAve,fHubPos001Ave \
             FROM tenminlog where dtSysTim>=%d and dtSysTim<%d;" %(search_time[0],search_time[1])
    registe_id=0    
    try:
        cursor.execute(sql)
        results = cursor.fetchall()            
        for row in results:
            
            registe_id+=1
            
            if row[7]>=3:
                if row[8]>0:
                    if row[1]<145 and row[2]<90 and row[3]<74 and row[4]<150 and row[5]<100 and row[6]<94:
                        if row[9]<1:
                            fan_dict[fan_databasename]['tenminlog']['normal_power_splat']['wind_list'].append(row[7])
                            fan_dict[fan_databasename]['tenminlog']['normal_power_splat']['power_list'].append(row[8])                        
                            #统计正常发电状态下机组的出口功率频数分布···
                            for power_cut in fan_dict[fan_databasename]['tenminlog']['power_status_distribute']:
                                if row[8]-power_cut>=0 and row[8]-power_cut<10:
                                    fan_dict[fan_databasename]['tenminlog']['power_status_distribute'][power_cut]['registe_number']+=1
                        else:
                            if row[8]>1400:
                                fan_dict[fan_databasename]['tenminlog']['normal_power_splat']['wind_list'].append(row[7])
                                fan_dict[fan_databasename]['tenminlog']['normal_power_splat']['power_list'].append(row[8])                        
                                #统计正常发电状态下机组的出口功率频数分布···
                                for power_cut in fan_dict[fan_databasename]['tenminlog']['power_status_distribute']:
                                    if row[8]-power_cut>=0 and row[8]-power_cut<10:
                                        fan_dict[fan_databasename]['tenminlog']['power_status_distribute'][power_cut]['registe_number']+=1
                            else:
                                fan_dict[fan_databasename]['tenminlog']['limite_power_splat']['wind_list'].append(row[7])
                                fan_dict[fan_databasename]['tenminlog']['limite_power_splat']['power_list'].append(row[8])
                               
                    else:
                        fan_dict[fan_databasename]['tenminlog']['selflimite_power_splat']['wind_list'].append(row[7])
                        fan_dict[fan_databasename]['tenminlog']['selflimite_power_splat']['power_list'].append(row[8])
                        fan_dict[fan_databasename]['tenminlog']['over_temperature_totaltime']+=1
                        if row[1]>=145:
                            fan_dict[fan_databasename]['tenminlog']['over_temperature']['fChoGenTemAve']['number']+=1
                        if row[2]>=90:
                            fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGeaBeaTemAve']['number']+=1
                        if row[3]>=74:
                            fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGeaOilTemAve']['number']+=1
                        if row[4]>=150:
                            fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGenTemAve']['number']+=1                           
                        if row[5]>=100:
                            fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGenBeaDriTemAve']['number']+=1
                        if row[6]>=94:
                            fan_dict[fan_databasename]['tenminlog']['over_temperature']['fConGsclgbTemAve']['number']+=1

                    #在发电的情况下机组的各个部件温度频率分布数据···
                    for temp_cut in fan_dict[fan_databasename]['tenminlog']['fChoGenTemAve_distribute']:
                        if row[1]-temp_cut>=0 and row[1]-temp_cut<2:
                            fan_dict[fan_databasename]['tenminlog']['fChoGenTemAve_distribute'][temp_cut]['registe_number']+=1

                    for temp_cut in fan_dict[fan_databasename]['tenminlog']['fGeaBeaTemAve_distribute']:
                        if row[2]-temp_cut>=0 and row[2]-temp_cut<2:
                            fan_dict[fan_databasename]['tenminlog']['fGeaBeaTemAve_distribute'][temp_cut]['registe_number']+=1
                    for temp_cut in fan_dict[fan_databasename]['tenminlog']['fGeaOilTemAve_distribute']:
                        if row[3]-temp_cut>=0 and row[3]-temp_cut<2:
                            fan_dict[fan_databasename]['tenminlog']['fGeaOilTemAve_distribute'][temp_cut]['registe_number']+=1
                    for temp_cut in fan_dict[fan_databasename]['tenminlog']['fGenTemAve_distribute']:
                        if row[4]-temp_cut>=0 and row[4]-temp_cut<2:
                            fan_dict[fan_databasename]['tenminlog']['fGenTemAve_distribute'][temp_cut]['registe_number']+=1
                    for temp_cut in fan_dict[fan_databasename]['tenminlog']['fGenBeaDriTemAve_distribute']:
                        if row[5]-temp_cut>=0 and row[5]-temp_cut<2:
                            fan_dict[fan_databasename]['tenminlog']['fGenBeaDriTemAve_distribute'][temp_cut]['registe_number']+=1
                    for temp_cut in fan_dict[fan_databasename]['tenminlog']['fConGsclgbTemAve_distribute']:
                        if row[6]-temp_cut>=0 and row[6]-temp_cut<2:
                            fan_dict[fan_databasename]['tenminlog']['fConGsclgbTemAve_distribute'][temp_cut]['registe_number']+=1

                    fan_dict[fan_databasename]['tenminlog']['totalpower']+=row[8]
                    fan_dict[fan_databasename]['tenminlog']['all_power_splat']['wind_list'].append(row[7])
                    fan_dict[fan_databasename]['tenminlog']['all_power_splat']['power_list'].append(row[8])

                else:
                    fan_dict[fan_databasename]['tenminlog']['stop_power_splat']['wind_list'].append(row[7])

            fan_dict[fan_databasename]['tenminlog']['fChoGenTemAve']['registe_id'].append(registe_id)
            fan_dict[fan_databasename]['tenminlog']['fChoGenTemAve']['temperature'].append(row[1])
            fan_dict[fan_databasename]['tenminlog']['fGeaBeaTemAve']['registe_id'].append(registe_id)
            fan_dict[fan_databasename]['tenminlog']['fGeaBeaTemAve']['temperature'].append(row[2])
            fan_dict[fan_databasename]['tenminlog']['fGeaOilTemAve']['registe_id'].append(registe_id)
            fan_dict[fan_databasename]['tenminlog']['fGeaOilTemAve']['temperature'].append(row[3])
            fan_dict[fan_databasename]['tenminlog']['fGenTemAve']['registe_id'].append(registe_id)
            fan_dict[fan_databasename]['tenminlog']['fGenTemAve']['temperature'].append(row[4])
            fan_dict[fan_databasename]['tenminlog']['fGenBeaDriTemAve']['registe_id'].append(registe_id)
            fan_dict[fan_databasename]['tenminlog']['fGenBeaDriTemAve']['temperature'].append(row[5])
            fan_dict[fan_databasename]['tenminlog']['fConGsclgbTemAve']['registe_id'].append(registe_id)
            fan_dict[fan_databasename]['tenminlog']['fConGsclgbTemAve']['temperature'].append(row[6])

            #统计风况频数分布数据···
            for wind_cut in fan_dict[fan_databasename]['tenminlog']['wind_status_distribute']:
                if row[7]-wind_cut>=0 and row[7]-wind_cut<0.2:
                    fan_dict[fan_databasename]['tenminlog']['wind_status_distribute'][wind_cut]['registe_number']+=1

        fan_dict[fan_databasename]['tenminlog']['totalpower']/=6
        #总发电量统计···            
        fan_dict[fan_databasename]['tenminlog']['normal_totalpower']=sum(fan_dict[fan_databasename]['tenminlog']['normal_power_splat']['power_list'])/6
        #统计自限电总时间···
        fan_dict[fan_databasename]['tenminlog']['selflimite_totaltime']=round(float(len(fan_dict[fan_databasename]['tenminlog']['selflimite_power_splat']['wind_list']))/6,1)
        #统计限电总时间···
        fan_dict[fan_databasename]['tenminlog']['limite_totaltime']=round(float(len(fan_dict[fan_databasename]['tenminlog']['limite_power_splat']['wind_list']))/6,1)
        #统计停机时间···
        fan_dict[fan_databasename]['tenminlog']['stop_totaltime']=round(float(len(fan_dict[fan_databasename]['tenminlog']['stop_power_splat']['wind_list']))/6,1)
        
        fan_dict[fan_databasename]['tenminlog']['over_temperature']['fChoGenTemAve']['total_time']=round(float(fan_dict[fan_databasename]['tenminlog']['over_temperature']['fChoGenTemAve']['number'])/6,1)
        fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGeaBeaTemAve']['total_time']=round(float(fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGeaBeaTemAve']['number'])/6,1)
        fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGeaOilTemAve']['total_time']=round(float(fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGeaOilTemAve']['number'])/6,1)
        fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGenTemAve']['total_time']=round(float(fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGenTemAve']['number'])/6,1)
        fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGenBeaDriTemAve']['total_time']=round(float(fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGenBeaDriTemAve']['number'])/6,1)
        fan_dict[fan_databasename]['tenminlog']['over_temperature']['fConGsclgbTemAve']['total_time']=round(float(fan_dict[fan_databasename]['tenminlog']['over_temperature']['fConGsclgbTemAve']['number'])/6,1)
        #fan_dict[fan_databasename]['tenminlog']['over_temperature_totaltime']/=6  #统计总超温时间···
        fan_dict[fan_databasename]['tenminlog']['over_temperature_totaltime']=round(float(fan_dict[fan_databasename]['tenminlog']['over_temperature_totaltime'])/6,1)
        #print fan_dict[fan_databasename]['tenminlog']['selflimite_totaltime']
        #计算出了标准总功率曲线···
        
        cdata.calculate_normal_power(fan_dict[fan_databasename]['normal_power_curve'],fan_dict[fan_databasename]['tenminlog']['normal_power_splat'])
        #统计自限电损失发电量···
        
        fan_dict[fan_databasename]['tenminlog']['selflimite_reducepower']=cdata.calculate_selflimit_power(fan_dict[fan_databasename]['normal_power_curve'],fan_dict[fan_databasename]['tenminlog']['selflimite_power_splat']) 
        #print   fan_dict[fan_databasename]['tenminlog']['selflimite_reducepower']
        #统计限电损失发电量···
        
        fan_dict[fan_databasename]['tenminlog']['limite_reducepower']=cdata.calculate_limit_power(fan_dict[fan_databasename]['normal_power_curve'],fan_dict[fan_databasename]['tenminlog']['limite_power_splat'])
        
        fan_dict[fan_databasename]['tenminlog']['stop_reducepower']=cdata.calculate_stop_power(fan_dict[fan_databasename]['normal_power_curve'],fan_dict[fan_databasename]['tenminlog']['stop_power_splat'])

        fan_dict[fan_databasename]['tenminlog']['hzth_increase_totalpower']=cdata.calculate_hzth_increase_totalpower(fan_dict[fan_databasename]['hzth_standard_wind_power'],fan_dict[fan_databasename]['tenminlog']['normal_power_splat'])
        
        #统计机组在不同状态下损失发电量
        csr.calculate_stames_reducepower(cursor,fan_dict[fan_databasename]['normal_power_curve'],fan_dict[fan_databasename]['stames'])
        
        #pc.plotting_normal_powercurve(fan_databasename,fan_dict[fan_databasename]['normal_power_curve'])
        #pc.plotting_all_powercurve(fan_databasename,fan_dict[fan_databasename]['tenminlog']['all_power_splat'])
        #pc.plotting_normal_power_scatter(fan_databasename,fan_dict[fan_databasename]['tenminlog']['normal_power_splat'])
        #pc.plotting_selflimit_power_scatter(fan_databasename,fan_dict[fan_databasename]['tenminlog']['selflimite_power_splat'])
        #pc.plotting_wind_status_distribute(fan_databasename,fan_dict[fan_databasename]['tenminlog']['wind_status_distribute'])
        #pc.plotting_power_status_distribute(fan_databasename,fan_dict[fan_databasename]['tenminlog']['power_status_distribute'])

        
        #绘制温度数据频数分布图···
        '''
        pc.plotting_fChoGenTemAve_status_distribute(fan_databasename,fan_dict[fan_databasename]['tenminlog']['fChoGenTemAve_distribute'])
        pc.plotting_fGeaBeaTemAve_status_distribute(fan_databasename,fan_dict[fan_databasename]['tenminlog']['fGeaBeaTemAve_distribute'])
        pc.plotting_fGeaOilTemAve_status_distribute(fan_databasename,fan_dict[fan_databasename]['tenminlog']['fGeaOilTemAve_distribute'])
        pc.plotting_fGenTemAve_status_distribute(fan_databasename,fan_dict[fan_databasename]['tenminlog']['fGenTemAve_distribute'])
        pc.plotting_fGenBeaDriTemAve_status_distribute(fan_databasename,fan_dict[fan_databasename]['tenminlog']['fGenBeaDriTemAve_distribute'])
        pc.plotting_fConGsclgbTemAve_status_distribute(fan_databasename,fan_dict[fan_databasename]['tenminlog']['fConGsclgbTemAve_distribute'])
        '''
        #绘制温度数据时序分布图···
        #pc.plotting_fChoGenTemAve_status(fan_databasename,fan_dict[fan_databasename]['tenminlog']['fChoGenTemAve'],fan_dict[fan_databasename]['tenminlog']['selflimite_totaltime'],fan_dict[fan_databasename]['tenminlog']['over_temperature']['fChoGenTemAve']['total_time'])
        #pc.plotting_fGeaBeaTemAve_status(fan_databasename,fan_dict[fan_databasename]['tenminlog']['fGeaBeaTemAve'],fan_dict[fan_databasename]['tenminlog']['selflimite_totaltime'],fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGeaBeaTemAve']['total_time'])
        #pc.plotting_fGeaOilTemAve_status(fan_databasename,fan_dict[fan_databasename]['tenminlog']['fGeaOilTemAve'],fan_dict[fan_databasename]['tenminlog']['selflimite_totaltime'],fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGeaOilTemAve']['total_time'])
        #pc.plotting_fGenTemAve_status(fan_databasename,fan_dict[fan_databasename]['tenminlog']['fGenTemAve'],fan_dict[fan_databasename]['tenminlog']['selflimite_totaltime'],fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGenTemAve']['total_time'])
        #pc.plotting_fGenBeaDriTemAve_status(fan_databasename,fan_dict[fan_databasename]['tenminlog']['fGenBeaDriTemAve'],fan_dict[fan_databasename]['tenminlog']['selflimite_totaltime'],fan_dict[fan_databasename]['tenminlog']['over_temperature']['fGenBeaDriTemAve']['total_time'])
        #pc.plotting_fConGsclgbTemAve_status(fan_databasename,fan_dict[fan_databasename]['tenminlog']['fConGsclgbTemAve'],fan_dict[fan_databasename]['tenminlog']['selflimite_totaltime'],fan_dict[fan_databasename]['tenminlog']['over_temperature']['fConGsclgbTemAve']['total_time'])

        
        #pc.plotting_overtemperature_pie(fan_databasename,fan_dict[fan_databasename]['tenminlog']['over_temperature'])
        #print fan_databasename,fan_dict[fan_databasename]['tenminlog']['normal_totalpower'],fan_dict[fan_databasename]['tenminlog']['selflimite_reducepower'],fan_dict[fan_databasename]['stames'].keys()
        #pc.plotting_power_bar(fan_databasename,fan_dict[fan_databasename]['tenminlog']['normal_totalpower'],fan_dict[fan_databasename]['tenminlog']['selflimite_reducepower'],fan_dict[fan_databasename]['stames'])
        #pc.plotting_stames_time_bar(fan_databasename,fan_dict[fan_databasename]['stames'])
             
    except:
        print ':  Error: serach statistics_limitpower unable to fecth data of tenminlog'
    
    return fan_dict


def read_tenminlog_table_normal_windpower(cursor,fan_databasename,search_time,fan_dict):
    print 'read tenminlog :'+str(fan_databasename)
    sql="SELECT dtSysTim, fChoGenTemAve,fGeaBeaTemAve,fGeaOilTemAve,fGenTemAve,fGenBeaDriTemAve,fConGsclgbTemAve,ufWinSpeAve,fPowerAve,fHubPos001Ave \
             FROM tenminlog where dtSysTim>=%d and dtSysTim<%d;" %(search_time[0],search_time[1])
    registe_id=0    
    try:
        cursor.execute(sql)
        results = cursor.fetchall()            
        for row in results:            
            registe_id+=1            
            if row[7]>=3:
                if row[8]>0:
                    if row[1]<145 and row[2]<90 and row[3]<74 and row[4]<150 and row[5]<100 and row[6]<94:
                        if row[9]<1:
                            fan_dict[fan_databasename]['tenminlog']['normal_power_splat']['wind_list'].append(row[7])
                            fan_dict[fan_databasename]['tenminlog']['normal_power_splat']['power_list'].append(row[8])                       
                        else:
                            if row[8]>1400:
                                fan_dict[fan_databasename]['tenminlog']['normal_power_splat']['wind_list'].append(row[7])
                                fan_dict[fan_databasename]['tenminlog']['normal_power_splat']['power_list'].append(row[8])                        
                                
        #计算出了标准总功率曲线···        
        cdata.calculate_normal_power(fan_dict[fan_databasename]['normal_power_curve'],fan_dict[fan_databasename]['tenminlog']['normal_power_splat'])
        #统计自限电损失发电量···       
    except:
        print ':  Error: serach statistics_limitpower unable to fecth data of tenminlog'    
    return fan_dict
