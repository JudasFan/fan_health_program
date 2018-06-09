#coding=utf-8

#统计计算在不同状态下机组的损失发电量···


def calculate_stames_reducepower(cursor,normal_power_curve,stames_dict):
    for stames_code in stames_dict:
        for stames_alive in stames_dict[stames_code]['stames_alive_list']:           
            
            sql="SELECT ufWinSpeAve,fPowerAve FROM tenminlog WHERE dtSysTim>=%d and dtSysTim<%d;" %(stames_alive[0],stames_alive[1])
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:                    
                    for wind_cut in normal_power_curve:                        
                        if row[0]-wind_cut>=0 and row[0]-wind_cut<0.2:
                            if normal_power_curve[wind_cut]['poweravg']>row[1]:                            
                                stames_dict[stames_code]['reduce_power']+=normal_power_curve[wind_cut]['poweravg']-row[1]
            except:
                continue            
                        
        stames_dict[stames_code]['reduce_power']/=6
        #print stames_code,stames_dict[stames_code]['reduce_power']
    
