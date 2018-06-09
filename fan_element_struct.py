#coding=utf-8
import numpy as np
import copy

def fan_element_struct():
    #机组状态码暂时不确定，因此后续动态添加···，做单台机组状态码频率分布···,'stames_alive_list'是不同机组状态的存活列表···
    stames_code={'stamescode_number':0,'stamescode_time':0,'reduce_power':0,'stames_alive_list':[]}
    #机组故障及其次数统计
    error={'uiHubErr':{'HubErr_code':{},'starttime':[]},           
           'uiErrFir':{'ErrFir_code':{},'starttime':[]},       
           'uiConErr':{'ConErr_code':{},'starttime':[]},
           'uiYawErr':{'YawErr_code':{},'starttime':[]},           
           'uiWarFir':{'WarFir_code':{},'starttime':[]}           
           }
    #windspeed_array=[set_wind_cut for set_wind_cut in np.arange(3,20,0.1)]
    #存储计算机组正常的功率曲线数据···,可以基于此数据，统计风况概率分布，不同风况下机组总发电量分布```
    normal_power_curve={}
    windspeed_array=np.arange(3,20,0.2)
    for wind_cut in windspeed_array:
        if wind_cut not in normal_power_curve:
            normal_power_curve[round(wind_cut,1)]={'total_power':0,'registe_number':0,'poweravg':0}

    hzth_standard_wind_power={}
    hzth_power_list=[123,142,164,189,213,239,268,300,331,366,398,434,470,514,552,593,630,661,707,742,806,843,893,953,1001,1049,1095,1147,1204,1248,1293,
                     1353,1398,1428,1465,1481,1493,1501,1514,1528,1540,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,
                     1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552,1552
                     ]    
    windspeed_array=np.arange(3,20,0.2)
    for wind_cut_id in range(len(windspeed_array)):
        if windspeed_array[wind_cut_id] not in hzth_standard_wind_power:
            hzth_standard_wind_power[round(windspeed_array[wind_cut_id],1)]={'poweravg':0}
            hzth_standard_wind_power[round(windspeed_array[wind_cut_id],1)]['poweravg']=hzth_power_list[wind_cut_id]            
            
    #用于存储风机全部出口功率频率分布···
    power_status_distribute={}
    power_status=np.arange(0,1800,10)
    for power_cut in power_status:
        if power_cut not in power_status_distribute:
            power_status_distribute[power_cut]={'registe_number':0}
            
    #用于统计存储风机风况频率分布···     
    wind_status_distribute={}
    wind_array=np.arange(0,20,0.2)
    for wind_cut in wind_array:
        if wind_cut not in wind_status_distribute:
            wind_status_distribute[round(wind_cut,1)]={'registe_number':0}

    fChoGenTemAve_status_distribute={}
    temperature1_cut=np.arange(0,200,2)
    for temp1_cut in temperature1_cut:
        if temp1_cut not in fChoGenTemAve_status_distribute:
            fChoGenTemAve_status_distribute[temp1_cut]={'registe_number':0}

    fGeaBeaTemAve_status_distribute={}
    temperature1_cut=np.arange(0,150,2)
    for temp1_cut in temperature1_cut:
        if temp1_cut not in fGeaBeaTemAve_status_distribute:
            fGeaBeaTemAve_status_distribute[temp1_cut]={'registe_number':0}

    fGeaOilTemAve_status_distribute={}
    temperature1_cut=np.arange(0,150,2)
    for temp1_cut in temperature1_cut:
        if temp1_cut not in fGeaOilTemAve_status_distribute:
            fGeaOilTemAve_status_distribute[temp1_cut]={'registe_number':0}

    fGenTemAve_status_distribute={}
    temperature1_cut=np.arange(0,200,2)
    for temp1_cut in temperature1_cut:
        if temp1_cut not in fGenTemAve_status_distribute:
            fGenTemAve_status_distribute[temp1_cut]={'registe_number':0}

    fGenBeaDriTemAve_status_distribute={}
    temperature1_cut=np.arange(0,150,2)
    for temp1_cut in temperature1_cut:
        if temp1_cut not in fGenBeaDriTemAve_status_distribute:
            fGenBeaDriTemAve_status_distribute[temp1_cut]={'registe_number':0}

    fConGsclgbTemAve_status_distribute={}
    temperature1_cut=np.arange(0,150,2)
    for temp1_cut in temperature1_cut:
        if temp1_cut not in fConGsclgbTemAve_status_distribute:
            fConGsclgbTemAve_status_distribute[temp1_cut]={'registe_number':0}
              
    
    tenminlog={'wind_status_distribute':{},#存储风况频率分布
               'power_status_distribute':{},#存储正常功率频率分布
               'fChoGenTemAve_distribute':{},#存储机组发电机感应线圈温度频率分布···
               'fGeaBeaTemAve_distribute':{},#存储机组齿轮箱温度频率分布···
               'fGeaOilTemAve_distribute':{},#存储机组齿轮箱油温频率分布···
               'fGenTemAve_distribute':{},
               'fGenBeaDriTemAve_distribute':{},
               'fConGsclgbTemAve_distribute':{},
               
               'normal_power_splat':{'wind_list':[],'power_list':[]},#存储正常功率风速散点···
               'all_power_splat':{'wind_list':[],'power_list':[]},#存储所有功率风速散点···
               'selflimite_power_splat':{'wind_list':[],'power_list':[]},#存储超温限功率散点···
               'limite_power_splat':{'wind_list':[],'power_list':[]},
               'stop_power_splat':{'wind_list':[],'power_list':[]},
               #超温限功率数据统计···
               'over_temperature':{'fChoGenTemAve':{'number':0,'total_time':0}, 
                                   'fGeaBeaTemAve':{'number':0,'total_time':0},
                                   'fGeaOilTemAve':{'number':0,'total_time':0},
                                   'fGenTemAve':{'number':0,'total_time':0},
                                   'fGenBeaDriTemAve':{'number':0,'total_time':0},
                                   'fConGsclgbTemAve':{'number':0,'total_time':0}
                                   },
               'totalpower':0,#机组总发电量···
               'normal_totalpower':0,#机组正常发电总的发电量存储···
               'selflimite_totaltime':0,
               'limite_totaltime':0,
               'stop_totaltime':0,
               'over_temperature_totaltime':0,
               'hzth_increase_totalpower':0,
               'selflimite_reducepower':0, #限功率损失发电量统计···
               'limite_reducepower':0,
               'stop_reducepower':0,
               
               'fChoGenTemAve':{'registe_id':[],'temperature':[]},
               'fGeaBeaTemAve':{'registe_id':[],'temperature':[]},
               'fGeaOilTemAve':{'registe_id':[],'temperature':[]},
               'fGenTemAve':{'registe_id':[],'temperature':[]},
               'fGenBeaDriTemAve':{'registe_id':[],'temperature':[]},
               'fConGsclgbTemAve':{'registe_id':[],'temperature':[]}               
               #机组部件温度数据概率分布统计···                                        
               }
    #初始化‘tenminlog’结构变量···
    tenminlog['wind_status_distribute']=copy.deepcopy(wind_status_distribute)
    tenminlog['power_status_distribute']=copy.deepcopy(power_status_distribute)    
    tenminlog['fChoGenTemAve_distribute']=copy.deepcopy(fChoGenTemAve_status_distribute)
    tenminlog['fGeaBeaTemAve_distribute']=copy.deepcopy(fGeaBeaTemAve_status_distribute)
    tenminlog['fGeaOilTemAve_distribute']=copy.deepcopy(fGeaOilTemAve_status_distribute)
    tenminlog['fGenTemAve_distribute']=copy.deepcopy(fGenTemAve_status_distribute)
    tenminlog['fGenBeaDriTemAve_distribute']=copy.deepcopy(fGenBeaDriTemAve_status_distribute)
    tenminlog['fConGsclgbTemAve_distribute']=copy.deepcopy(fConGsclgbTemAve_status_distribute)
    
    
    fan_element={'stames':{},'error':{},'tenminlog':{},'normal_power_curve':{},'fanset_information':{'fanid':0,'fanname':'','fanip':'','fantype':0,'plctype':0}}

    fan_element['error']=copy.deepcopy(error)
    fan_element['tenminlog']=copy.deepcopy(tenminlog)
    fan_element['normal_power_curve']=copy.deepcopy(normal_power_curve)
    fan_element['hzth_standard_wind_power']=copy.deepcopy(hzth_standard_wind_power)

    fan_root_dict={}

    return fan_root_dict,fan_element,stames_code
    

    
    
