#coding=utf-8
import os
import os.path

def create_direct():


    if os.path.exists("E:\\fan_hekou_new") is False:        
        os.mkdir("E:\\fan_hekou_new")
        os.chdir("E:\\fan_hekou_new")
        os.mkdir("E:\\fan_hekou_new\\wind_power")
        os.mkdir("E:\\fan_hekou_new\\selflimit_power")
        os.mkdir("E:\\fan_hekou_new\\power_scatter")
        os.mkdir("E:\\fan_hekou_new\\wind_distribute")
        os.mkdir("E:\\fan_hekou_new\\power_distribute")
        os.mkdir("E:\\fan_hekou_new\\fChoGenTemAve_distribute")
        os.mkdir("E:\\fan_hekou_new\\fGeaBeaTemAve_distribute")
        os.mkdir("E:\\fan_hekou_new\\fGeaOilTemAve_distribute")
        os.mkdir("E:\\fan_hekou_new\\fGenTemAve_distribute")
        os.mkdir("E:\\fan_hekou_new\\fGenBeaDriTemAve_distribute")
        os.mkdir("E:\\fan_hekou_new\\fConGsclgbTemAve_distribute")
        os.mkdir("E:\\fan_hekou_new\\overtemperature_pie")
        os.mkdir("E:\\fan_hekou_new\\reduce_power")
        os.mkdir("E:\\fan_hekou_new\\stames_time_bar")

        os.mkdir("E:\\fan_hekou_new\\hub_err_bar")
        os.mkdir("E:\\fan_hekou_new\\fir_err_bar")
        os.mkdir("E:\\fan_hekou_new\\fir_err_con")
        os.mkdir("E:\\fan_hekou_new\\fir_err_yaw")
        os.mkdir("E:\\fan_hekou_new\\fir_war_bar")
        os.mkdir("E:\\fan_hekou_new\\all_data_plot")
        os.mkdir("E:\\fan_hekou_new\\write_excel_path")
       
        
        
    else:
        os.chdir("E:\\fan_hekou_new")
        os.mkdir("E:\\fan_hekou_new\\wind_power")
        os.mkdir("E:\\fan_hekou_new\\selflimit_power")
        os.mkdir("E:\\fan_hekou_new\\power_scatter")
        os.mkdir("E:\\fan_hekou_new\\wind_distribute")
        os.mkdir("E:\\fan_hekou_new\\power_distribute")
        os.mkdir("E:\\fan_hekou_new\\fChoGenTemAve_distribute")
        os.mkdir("E:\\fan_hekou_new\\fGeaBeaTemAve_distribute")
        os.mkdir("E:\\fan_hekou_new\\fGeaOilTemAve_distribute")
        os.mkdir("E:\\fan_hekou_new\\fGenTemAve_distribute")
        os.mkdir("E:\\fan_hekou_new\\fGenBeaDriTemAve_distribute")
        os.mkdir("E:\\fan_hekou_new\\fConGsclgbTemAve_distribute")
        os.mkdir("E:\\fan_hekou_new\\overtemperature_pie")
        os.mkdir("E:\\fan_hekou_new\\reduce_power")
        os.mkdir("E:\\fan_hekou_new\\stames_time_bar")

        os.mkdir("E:\\fan_hekou_new\\hub_err_bar")
        os.mkdir("E:\\fan_hekou_new\\fir_err_bar")
        os.mkdir("E:\\fan_hekou_new\\fir_err_con")
        os.mkdir("E:\\fan_hekou_new\\fir_err_yaw")
        os.mkdir("E:\\fan_hekou_new\\fir_war_bar")
        os.mkdir("E:\\fan_hekou_new\\all_data_plot")
        os.mkdir("E:\\fan_hekou_new\\write_excel_path")
       
create_direct()
    

   
