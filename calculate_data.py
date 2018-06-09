#coding=utf-8

#计算机组相关统计数据的函数···

#统计标准功率数据···
def calculate_normal_power(normal_power_curve,normal_power_splat):    
    for wind_cut in normal_power_curve:        
        for real_wind_id in range(len(normal_power_splat['wind_list'])):
            if normal_power_splat['wind_list'][real_wind_id]-wind_cut>=0:
                if normal_power_splat['wind_list'][real_wind_id]-wind_cut<0.2:
                    normal_power_curve[wind_cut]['total_power']+=normal_power_splat['power_list'][real_wind_id]
                    normal_power_curve[wind_cut]['registe_number']+=1
        if normal_power_curve[wind_cut]['registe_number']!=0:
            normal_power_curve[wind_cut]['poweravg']=normal_power_curve[wind_cut]['total_power']/normal_power_curve[wind_cut]['registe_number']


def calculate_selflimit_power(normal_power_curve,selflimite_power_splat):
    selflimit_totalpower=0
    for selflimit_windid in range(len(selflimite_power_splat['wind_list'])):
        for wind_cut in normal_power_curve:
            if selflimite_power_splat['wind_list'][selflimit_windid]-wind_cut>=0 and selflimite_power_splat['wind_list'][selflimit_windid]-wind_cut<0.2:
                if normal_power_curve[wind_cut]['poweravg']>selflimite_power_splat['power_list'][selflimit_windid]:
                    selflimit_totalpower+=normal_power_curve[wind_cut]['poweravg']-selflimite_power_splat['power_list'][selflimit_windid]
    selflimit_totalpower/=6
    return selflimit_totalpower

    
def calculate_limit_power(normal_power_curve,limite_power_splat):
    selflimit_totalpower=0
    for selflimit_windid in range(len(limite_power_splat['wind_list'])):
        for wind_cut in normal_power_curve:
            if limite_power_splat['wind_list'][selflimit_windid]-wind_cut>=0 and limite_power_splat['wind_list'][selflimit_windid]-wind_cut<0.2:
                if normal_power_curve[wind_cut]['poweravg']>limite_power_splat['power_list'][selflimit_windid]:
                    selflimit_totalpower+=normal_power_curve[wind_cut]['poweravg']-limite_power_splat['power_list'][selflimit_windid]
    selflimit_totalpower/=6
    return selflimit_totalpower

def calculate_stop_power(normal_power_curve,selflimite_power_splat):
    selflimit_totalpower=0
    for selflimit_windid in range(len(selflimite_power_splat['wind_list'])):
        for wind_cut in normal_power_curve:
            if selflimite_power_splat['wind_list'][selflimit_windid]-wind_cut>=0 and selflimite_power_splat['wind_list'][selflimit_windid]-wind_cut<0.2:
                if normal_power_curve[wind_cut]['poweravg']>0:
                    selflimit_totalpower+=normal_power_curve[wind_cut]['poweravg']
    selflimit_totalpower/=6
    return selflimit_totalpower

def calculate_hzth_increase_totalpower(hzth_standard_wind_power,normal_power_splat):
    selflimit_totalpower=0
    for selflimit_windid in range(len(normal_power_splat['wind_list'])):
        for wind_cut in hzth_standard_wind_power:
            if normal_power_splat['wind_list'][selflimit_windid]-wind_cut>=0 and normal_power_splat['wind_list'][selflimit_windid]-wind_cut<0.2:
                #if hzth_standard_wind_power[wind_cut]['poweravg']>normal_power_splat['power_list'][selflimit_windid]:#计算全功率数据模型······
                    #selflimit_totalpower+=hzth_standard_wind_power[wind_cut]['poweravg']-normal_power_splat['power_list'][selflimit_windid] #此式计算的是增加量···
                    selflimit_totalpower+=hzth_standard_wind_power[wind_cut]['poweravg']    #此式预计更新程序后的预测发电量···
    selflimit_totalpower/=6
    return selflimit_totalpower
