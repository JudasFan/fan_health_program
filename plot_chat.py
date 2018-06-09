#coding=utf-8
import numpy as np
from matplotlib import pyplot as plt
import convert_array_order as cao
import copy
import write_to_txt as wtt
#设置图像可以显示中文及可以设置字体大小····
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']

def plotting_normal_powercurve(fan_databasename,power_curve):
    x_wind=[]
    y_power=[]    
    for wind_cut in power_curve:
        x_wind.append(wind_cut)
        y_power.append(round(power_curve[wind_cut]['poweravg'],1))
    
    curve_data=copy.deepcopy(cao.array_order(x_wind,y_power))
    #print curve_data['y']
    plt.plot(curve_data['x'],curve_data['y'],c='g',label='F'+':normal power curve')
    plt.xlabel(u'风速',fontproperties='SimHei')
    plt.ylabel(u'有功功率',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组正常功率曲线图',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.xlim(0,16)
    plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\wind_power\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\wind_power\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图


def plotting_all_powercurve(fan_databasename,normal_power_splat):
    plt.scatter(normal_power_splat['wind_list'],normal_power_splat['power_list'],c='b',s=0.5,alpha=0.7,marker='*',label='all power scatter')
    plt.xlabel(u'风速',fontproperties='SimHei')
    plt.ylabel(u'有功功率',fontproperties='SimHei')
    #plt.xticks(range(-170,1000,20), group_xlables, rotation=45,fontsize=6) #对X轴坐标做相应的修改```
    plt.legend(loc='upper right')
    plt.title(str(fan_databasename)+u':全部发电功率散点图',fontproperties='SimHei')
    plt.xlim(0,25)
    plt.ylim(0,1750)
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\power_scatter\\all_powerMyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\power_scatter\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_normal_power_scatter(fan_databasename,normal_power_splat):
    plt.scatter(normal_power_splat['wind_list'],normal_power_splat['power_list'],c='b',s=0.5,alpha=0.7,marker='*',label='normal power scatter')
    plt.xlabel(u'风速',fontproperties='SimHei')
    plt.ylabel(u'有功功率',fontproperties='SimHei')
    #plt.xticks(range(-170,1000,20), group_xlables, rotation=45,fontsize=6) #对X轴坐标做相应的修改```
    plt.legend(loc='upper right')
    plt.title(str(fan_databasename)+u':正常发电功率散点图',fontproperties='SimHei')
    plt.xlim(0,25)
    plt.ylim(0,1750)
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\power_scatter\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\power_scatter\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_selflimit_power_scatter(fan_databasename,selflimite_power_splat):
    plt.scatter(selflimite_power_splat['wind_list'],selflimite_power_splat['power_list'],c='r',s=0.5,alpha=0.7,marker='*',label='selflimit power scatter')
    plt.xlabel(u'风速',fontproperties='SimHei')
    plt.ylabel(u'有功功率',fontproperties='SimHei')
    #plt.xticks(range(-170,1000,20), group_xlables, rotation=45,fontsize=6) #对X轴坐标做相应的修改```
    plt.legend(loc='upper right')
    plt.title(str(fan_databasename)+u':高温限功率功率散点图',fontproperties='SimHei')
    #plt.show()
    plt.xlim(0,25)
    plt.ylim(0,1750)
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\selflimit_power\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\selflimit_power\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_wind_status_distribute(fan_databasename,wind_status_distribute): 
    x_wind=[]
    y_distribute=[]    
    for wind_cut in wind_status_distribute:
        x_wind.append(wind_cut)
        y_distribute.append(wind_status_distribute[wind_cut]['registe_number'])        
    
    curve_data=copy.deepcopy(cao.array_order(x_wind,y_distribute))
    plt.scatter(curve_data['x'],curve_data['y'],c='g',s=5,alpha=0.7,label='F'+':wind frequency distribute')
    plt.xlabel(u'风速',fontproperties='SimHei')
    plt.ylabel(u'频数值(10分钟/每条记录)',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组风况频数分布',fontproperties='SimHei')
    plt.ylim(0,2000)
    plt.xlim(0,25)
    plt.legend(loc='upper right')
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\wind_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\wind_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图


def plotting_wind_status_distribute_bar(fan_databasename,wind_status_distribute):
    x_wind=[]
    y_distribute_buf=[]
    y_sum=0
    y_distribute=[]
    y_max=0
    for wind_cut in wind_status_distribute:
        x_wind.append(wind_cut)
        y_distribute_buf.append(wind_status_distribute[wind_cut]['registe_number'])        
    y_sum=sum(y_distribute_buf)
    #获取其数据总的和值···
    #print y_sum
    for x_ in x_wind:
        y_distribute.append(float(wind_status_distribute[x_]['registe_number'])/y_sum)
    y_max=max(y_distribute)
    #获取其数据列表中最大的数···
    curve_data=copy.deepcopy(cao.array_order(x_wind,y_distribute))
    #plt.scatter(curve_data['x'],curve_data['y'],c='g',s=2,alpha=0.7,label='F'+':wind frequency distribute')
    plt.bar(curve_data['x'],curve_data['y'],width=0.15,label='F'+':wind frequency distribute')
    plt.xlabel(u'风速',fontproperties='SimHei')
    plt.ylabel(u'百分比（%）',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组风况频数分布',fontproperties='SimHei')
    plt.ylim(0,1.2*y_max)
    plt.xlim(0,25)
    plt.legend(loc='upper right')
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\wind_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_jiaxin_new\\wind_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图


def plotting_power_status_distribute(fan_databasename,power_status_distribute):
    x_power=[]
    y_distribute=[]    
    for power_cut in power_status_distribute:
        x_power.append(power_cut)
        y_distribute.append(power_status_distribute[power_cut]['registe_number'])        
    
    curve_data=copy.deepcopy(cao.array_order(x_power,y_distribute))
    plt.scatter(curve_data['x'],curve_data['y'],c='g',s=5,alpha=0.7,label='F'+':power frequency distribute')
    plt.xlabel(u'出口有功(kw)',fontproperties='SimHei')
    plt.ylabel(u'频数值(10分钟/每条记录)',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组出口有功频数分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,1000)
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\power_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\power_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图


def plotting_fChoGenTemAve_status_distribute(fan_databasename,fChoGenTemAve_status_distribute):
    x_power=[]
    y_distribute=[]    
    for power_cut in fChoGenTemAve_status_distribute:
        x_power.append(power_cut)
        y_distribute.append(fChoGenTemAve_status_distribute[power_cut]['registe_number'])        
    
    curve_data=copy.deepcopy(cao.array_order(x_power,y_distribute))
    plt.plot(curve_data['x'],curve_data['y'],c='g',label='F'+':fChoGenTemAve frequency distribute')
    plt.xlabel(u'发电机感应线圈温度',fontproperties='SimHei')
    plt.ylabel(u'频数值(10分钟/每条记录)',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组发电机感应线圈温度频数分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,3000)
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\fChoGenTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\fChoGenTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_fGeaBeaTemAve_status_distribute(fan_databasename,fChoGenTemAve_status_distribute):
    x_power=[]
    y_distribute=[]    
    for power_cut in fChoGenTemAve_status_distribute:
        x_power.append(power_cut)
        y_distribute.append(fChoGenTemAve_status_distribute[power_cut]['registe_number'])        
    
    curve_data=copy.deepcopy(cao.array_order(x_power,y_distribute))
    plt.plot(curve_data['x'],curve_data['y'],c='g',label='F'+':fGeaBeaTemAve frequency distribute')
    plt.xlabel(u'齿轮箱轴承温度',fontproperties='SimHei')
    plt.ylabel(u'频数值(10分钟/每条记录)',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组齿轮箱轴承温度频数分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,3000)
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\fGeaBeaTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\fGeaBeaTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_fGeaOilTemAve_status_distribute(fan_databasename,fChoGenTemAve_status_distribute):
    x_power=[]
    y_distribute=[]    
    for power_cut in fChoGenTemAve_status_distribute:
        x_power.append(power_cut)
        y_distribute.append(fChoGenTemAve_status_distribute[power_cut]['registe_number'])        
    
    curve_data=copy.deepcopy(cao.array_order(x_power,y_distribute))
    plt.plot(curve_data['x'],curve_data['y'],c='g',label='F'+':fGeaOilTemAve frequency distribute')
    plt.xlabel(u'齿轮箱油温',fontproperties='SimHei')
    plt.ylabel(u'频数值(10分钟/每条记录)',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组齿轮箱油温频数分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,3000)
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\fGeaOilTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\fGeaOilTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_fGenTemAve_status_distribute(fan_databasename,fChoGenTemAve_status_distribute):
    x_power=[]
    y_distribute=[]    
    for power_cut in fChoGenTemAve_status_distribute:
        x_power.append(power_cut)
        y_distribute.append(fChoGenTemAve_status_distribute[power_cut]['registe_number'])        
    
    curve_data=copy.deepcopy(cao.array_order(x_power,y_distribute))
    plt.plot(curve_data['x'],curve_data['y'],c='g',label='F'+':fGenTemAve frequency distribute')
    plt.xlabel(u'发电机温度',fontproperties='SimHei')
    plt.ylabel(u'频数值(10分钟/每条记录)',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组发电机温度频数分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,3000)
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\fGenTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\fGenTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_fGenBeaDriTemAve_status_distribute(fan_databasename,fChoGenTemAve_status_distribute):
    x_power=[]
    y_distribute=[]    
    for power_cut in fChoGenTemAve_status_distribute:
        x_power.append(power_cut)
        y_distribute.append(fChoGenTemAve_status_distribute[power_cut]['registe_number'])        
    
    curve_data=copy.deepcopy(cao.array_order(x_power,y_distribute))
    plt.plot(curve_data['x'],curve_data['y'],c='g',label='F'+':fGenBeaDriTemAve frequency distribute')
    plt.xlabel(u'发电机轴承温度',fontproperties='SimHei')
    plt.ylabel(u'频数值(10分钟/每条记录)',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组发电机轴承温度频数分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,3000)
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\fGenBeaDriTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\fGenBeaDriTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_fConGsclgbTemAve_status_distribute(fan_databasename,fChoGenTemAve_status_distribute):
    x_power=[]
    y_distribute=[]    
    for power_cut in fChoGenTemAve_status_distribute:
        x_power.append(power_cut)
        y_distribute.append(fChoGenTemAve_status_distribute[power_cut]['registe_number'])        
    
    curve_data=copy.deepcopy(cao.array_order(x_power,y_distribute))
    plt.plot(curve_data['x'],curve_data['y'],c='g',label='F'+':fConGsclgbTemAve frequency distribute')
    plt.xlabel(u'IGBT温度',fontproperties='SimHei')
    plt.ylabel(u'频数值(10分钟/每条记录)',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组IGBT温度频数分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,3000)
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\fConGsclgbTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\fConGsclgbTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图



def plotting_overtemperature_pie(fan_databasename,over_temperature):
    labels=[u'fChoGenTemAve','fGeaBeaTemAve',u'fGeaOilTemAve','fGenTemAve','fGenBeaDriTemAve','fConGsclgbTemAve']
    overtemperature_data = [0,0,0,0,0,0]
    colors = ['green', 'yellow', 'blue', 'red','cyan','magenta']
    overtemperature_data[0]=over_temperature['fChoGenTemAve']['total_time']
    overtemperature_data[1]=over_temperature['fGeaBeaTemAve']['total_time']
    overtemperature_data[2]=over_temperature['fGeaOilTemAve']['total_time']
    overtemperature_data[3]=over_temperature['fGenTemAve']['total_time']
    overtemperature_data[4]=over_temperature['fGenBeaDriTemAve']['total_time']
    overtemperature_data[5]=over_temperature['fConGsclgbTemAve']['total_time']
    #print fan_databasename,overtemperature_data
    explode = [0.1,0.1,0,0,0,0]
    plt.axes(aspect=1)
    plt.pie(x=overtemperature_data, labels=labels, colors=colors,explode=explode,autopct='%3.1f %%',shadow=False, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
    plt.legend(loc='upper left',fontsize=5)  #设置图例字体大小
    plt.title(str(fan_databasename)+u':号机组部件超温饼图',fontproperties='SimHei')
    #plt.ylim(0,3000)
    #plt.show()
    #plt.grid(color='b' , linewidth='0.3' ,linestyle='--')  #绘制饼图不能用这个网格函数···
    
    plt.savefig('E:\\fan_hekou_new\\overtemperature_pie\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\overtemperature_pie\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_power_bar(fan_databasename,totalpower,selfreducepower,stames_code):
    x_len=1+len(stames_code)

    x_ticks=['selfreducepower']
    x_values=[i for i in range(x_len)]

    y_values=[selfreducepower]

    stames_buf=[]
    for stamescode in stames_code:
 
        stames_buf.append(stamescode)        
    stames_buf=copy.deepcopy(stames_buf)

    for stames in stames_buf:
        x_ticks.append(stames)
        y_values.append(stames_code[stames]['reduce_power'])

    plt.bar(x_values,y_values,color="green",width=0.5)
    
    for a,b in zip(x_values,y_values):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)       
    
    plt.xticks(x_values,x_ticks)
    plt.title(str(fan_databasename)+u':号损失发电量柱形图(总亏损电量：'+str(round(totalpower,0))+')',fontproperties='SimHei')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    plt.xlabel(u'机组状态码',fontproperties='SimHei')
    plt.ylabel(u'损失发电量(kw*h)',fontproperties='SimHei')
    #plt.show()
    plt.ylim(0,600000)
    plt.savefig('E:\\fan_hekou_new\\reduce_power\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_stames_time_bar(fan_databasename,stames_code):
    x_len=len(stames_code)
    x_ticks=[]
    x_values=[i for i in range(x_len)]
    y_values=[]
    stames_buf=[]
    for stamescode in stames_code: 
        stames_buf.append(stamescode)        
    stames_buf=copy.deepcopy(stames_buf)
    for stames in stames_buf:
        x_ticks.append(stames)
        y_values.append(stames_code[stames]['stamescode_time'])
    plt.bar(x_values,y_values,color="b",width=0.5)    
    for a,b in zip(x_values,y_values):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)  
    
    plt.xticks(x_values,x_ticks)
    plt.title(str(fan_databasename)+u':号机组状态持续时间柱形图',fontproperties='SimHei')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    plt.xlabel(u'机组状态码',fontproperties='SimHei')
    plt.ylabel(u'持续时间(h)',fontproperties='SimHei')
    #plt.show()
    plt.ylim(0,7000)
    plt.savefig('E:\\fan_hekou_new\\stames_time_bar\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图    




#绘制温度数据时序图形····
#绘制温度数据时序图形····
    
def plotting_fChoGenTemAve_status(fan_databasename,fChoGenTemAve,totalovertemptime,overtemptime):    
    plt.scatter(fChoGenTemAve['registe_id'],fChoGenTemAve['temperature'],c='c',s=0.5,alpha=1,marker='x',label='F'+':fChoGenTemAve temperature')
    plt.xlabel(u'记录ID'+u'(超温限电总时长：'+str(totalovertemptime)+'h)'+u'(感应线圈超温时长('+str(overtemptime)+'h)',fontproperties='SimHei')
    plt.ylabel(u'发电机感应线圈温度',fontproperties='SimHei')

    plt.axhline(y=145,linewidth=2,color='y')  #画水平横线···
    #plt.axvline()  #画垂直横线···

    plt.title(str(fan_databasename)+u':号机组发电机感应线圈温度时序分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,200)
    #plt.xlim()
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\fChoGenTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\fChoGenTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_fGeaBeaTemAve_status(fan_databasename,fChoGenTemAve,totalovertemptime,overtemptime):
    
    plt.scatter(fChoGenTemAve['registe_id'],fChoGenTemAve['temperature'],c='c',s=0.5,alpha=1,marker='x',label='F'+':fGeaBeaTemAve temperature')
    plt.xlabel(u'记录ID'+u'(超温限电总时长：'+str(totalovertemptime)+'h)'+u'(齿轮箱轴承超温时长('+str(overtemptime)+'h)',fontproperties='SimHei')
    plt.ylabel(u'齿轮箱轴承温度',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组齿轮箱轴承温度时序分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,150)
    plt.axhline(y=90,linewidth=2,color='y')  #画水平横线···
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\fGeaBeaTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\fGeaBeaTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_fGeaOilTemAve_status(fan_databasename,fChoGenTemAve,totalovertemptime,overtemptime):
   
    plt.scatter(fChoGenTemAve['registe_id'],fChoGenTemAve['temperature'],c='c',s=0.5,alpha=1,marker='x',label='F'+':fGeaOilTemAve temperature')
    plt.xlabel(u'记录ID'+u'(超温限电总时长：'+str(totalovertemptime)+'h)'+u'(齿轮箱油温超温时长('+str(overtemptime)+'h)',fontproperties='SimHei')
    plt.ylabel(u'齿轮箱油温',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组齿轮箱油温时序分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,150)
    plt.axhline(y=74,linewidth=2,color='y')  #画水平横线···
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\fGeaOilTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\fGeaOilTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_fGenTemAve_status(fan_databasename,fChoGenTemAve,totalovertemptime,overtemptime):
    
    plt.scatter(fChoGenTemAve['registe_id'],fChoGenTemAve['temperature'],c='c',s=0.5,alpha=1,marker='x',label='F'+':fGenTemAve temperature')
    plt.xlabel(u'记录ID'+u'(超温限电总时长：'+str(totalovertemptime)+'h)'+u'(发电机温度超温时长('+str(overtemptime)+'h)',fontproperties='SimHei')
    plt.ylabel(u'发电机温度',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组发电机温度时序分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,200)
    plt.axhline(y=150,linewidth=2,color='y')  #画水平横线···
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\fGenTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\fGenTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_fGenBeaDriTemAve_status(fan_databasename,fChoGenTemAve,totalovertemptime,overtemptime):
    
    plt.scatter(fChoGenTemAve['registe_id'],fChoGenTemAve['temperature'],c='c',s=0.5,alpha=1,marker='x',label='F'+':fGenBeaDriTemAve temperature')
    plt.xlabel(u'记录ID'+u'(超温限电总时长：'+str(totalovertemptime)+'h)'+u'(发电机轴承超温时长('+str(overtemptime)+'h)',fontproperties='SimHei')
    plt.ylabel(u'发电机轴承温度',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组发电机轴承温度时序分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,150)
    plt.axhline(y=100,linewidth=2,color='y')  #画水平横线···
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\fGenBeaDriTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\fGenBeaDriTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_fConGsclgbTemAve_status(fan_databasename,fChoGenTemAve,totalovertemptime,overtemptime):
    
    plt.scatter(fChoGenTemAve['registe_id'],fChoGenTemAve['temperature'],c='c',s=0.5,alpha=1,marker='x',label='F'+':fConGsclgbTemAve temperature')
    plt.xlabel(u'记录ID'+u'(超温限电总时长：'+str(totalovertemptime)+'h)'+u'(IGBT温度超温时长('+str(overtemptime)+'h)',fontproperties='SimHei')
    plt.ylabel(u'IGBT温度',fontproperties='SimHei')
    plt.title(str(fan_databasename)+u':号机组IGBT温度时序分布',fontproperties='SimHei')
    plt.legend(loc='upper right')
    plt.ylim(0,150)
    plt.axhline(y=94,linewidth=2,color='y')  #画水平横线···
    #plt.show()
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\fConGsclgbTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\fConGsclgbTemAve_distribute\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图


#绘制故障代码对应的记录数据···
#绘制故障代码对应的记录数据···
#绘制故障代码对应的记录数据···


def plotting_huberror_registe_bar(fan_databasename,error):
    x_errorcode=[]
    y_registnumber=[]    
    x_values=[i for i in range(len(error['uiHubErr']['HubErr_code'])) ]
    for code_cut in error['uiHubErr']['HubErr_code']:        
        x_errorcode.append(code_cut)
        y_registnumber.append(error['uiHubErr']['HubErr_code'][code_cut])    
    curve_data=copy.deepcopy(cao.array_order2(y_registnumber,x_errorcode))    
    plt.bar(x_values,curve_data['x'],color="b",width=0.5)    
    for a,b in zip(x_values,curve_data['x']):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.xticks(x_values,curve_data['y'])    
    plt.title(str(fan_databasename)+u':号机组变桨故障次数柱形图',fontproperties='SimHei')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    plt.xlabel(u'变桨故障状态码',fontproperties='SimHei')
    plt.ylabel(u'故障次数(次)',fontproperties='SimHei')
    #plt.show()
    plt.ylim(0,200)
    plt.savefig('E:\\fan_hekou_new\\hub_err_bar\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图 

def plotting_errorfir_registe_bar(fan_databasename,error):
    x_errorcode=[]
    y_registnumber=[]    
    x_values=[i for i in range(len(error['uiErrFir']['ErrFir_code'])) ]
    for code_cut in error['uiErrFir']['ErrFir_code']:        
        x_errorcode.append(code_cut)
        y_registnumber.append(error['uiErrFir']['ErrFir_code'][code_cut])    
    curve_data=copy.deepcopy(cao.array_order2(y_registnumber,x_errorcode))    
    plt.bar(x_values[:13],curve_data['x'][:13],color="b",width=0.5)    
    for a,b in zip(x_values[:13],curve_data['x'][:13]):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.xticks(x_values[:13],curve_data['y'][:13])    
    plt.title(str(fan_databasename)+u':号机组首故障次数柱形图',fontproperties='SimHei')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    plt.xlabel(u'首故障状态码',fontproperties='SimHei')
    plt.ylabel(u'故障次数(次)',fontproperties='SimHei')
    #plt.show()
    plt.ylim(0,200)
    plt.savefig('E:\\fan_hekou_new\\fir_err_bar\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图 

def plotting_errorcon_registe_bar(fan_databasename,error):
    x_errorcode=[]
    y_registnumber=[]    
    x_values=[i for i in range(len(error['uiConErr']['ConErr_code'])) ]
    for code_cut in error['uiConErr']['ConErr_code']:        
        x_errorcode.append(code_cut)
        y_registnumber.append(error['uiConErr']['ConErr_code'][code_cut])    
    curve_data=copy.deepcopy(cao.array_order2(y_registnumber,x_errorcode))    
    plt.bar(x_values,curve_data['x'],color="b",width=0.5)    
    for a,b in zip(x_values,curve_data['x']):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.xticks(x_values,curve_data['y'])    
    plt.title(str(fan_databasename)+u':号机组变频器故障次数柱形图',fontproperties='SimHei')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    plt.xlabel(u'变频器故障状态码',fontproperties='SimHei')
    plt.ylabel(u'故障次数(次)',fontproperties='SimHei')
    #plt.show()
    plt.ylim(0,200)
    plt.savefig('E:\\fan_hekou_new\\fir_err_con\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_erroryaw_registe_bar(fan_databasename,error):
    x_errorcode=[]
    y_registnumber=[]    
    x_values=[i for i in range(len(error['uiYawErr']['YawErr_code'])) ]
    for code_cut in error['uiYawErr']['YawErr_code']:        
        x_errorcode.append(code_cut)
        y_registnumber.append(error['uiYawErr']['YawErr_code'][code_cut])    
    curve_data=copy.deepcopy(cao.array_order2(y_registnumber,x_errorcode))    
    plt.bar(x_values,curve_data['x'],color="b",width=0.5)    
    for a,b in zip(x_values,curve_data['x']):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.xticks(x_values,curve_data['y'])    
    plt.title(str(fan_databasename)+u':号机组偏航故障次数柱形图',fontproperties='SimHei')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    plt.xlabel(u'偏航故障状态码',fontproperties='SimHei')
    plt.ylabel(u'故障次数(次)',fontproperties='SimHei')
    #plt.show()
    plt.ylim(0,200)
    plt.savefig('E:\\fan_hekou_new\\fir_err_yaw\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图

def plotting_warfir_registe_bar(fan_databasename,error):
    x_errorcode=[]
    y_registnumber=[]    
    x_values=[i for i in range(len(error['uiWarFir']['WarFir_code'])) ]
    for code_cut in error['uiWarFir']['WarFir_code']:        
        x_errorcode.append(code_cut)
        y_registnumber.append(error['uiWarFir']['WarFir_code'][code_cut])    
    curve_data=copy.deepcopy(cao.array_order2(y_registnumber,x_errorcode))    
    plt.bar(x_values[:13],curve_data['x'][:13],color="b",width=0.5)    
    for a,b in zip(x_values[:13],curve_data['x'][:13]):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.xticks(x_values[:13],curve_data['y'][:13])    
    plt.title(str(fan_databasename)+u':号机组告警次数柱形图',fontproperties='SimHei')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    plt.xlabel(u'告警故障状态码',fontproperties='SimHei')
    plt.ylabel(u'告警次数(次)',fontproperties='SimHei')
    #plt.show()
    plt.ylim(0,200)
    plt.savefig('E:\\fan_hekou_new\\fir_war_bar\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图     




##########################################################################################################################################
    #######################################################################################################################################
#整场数据统计计算····
#整场数据统计计算····
#整场数据统计计算····
    
def plotting_all_power(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    print type(power_curve),power_curve.keys()
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalpower']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    print x_xticks
    print y_power
    x_values=[i for i in range(len(x_xticks))]
    print 'this is error place!'
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    print 'this is error place pass !'
    print curve_data['y']
    print curve_data['x']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=1,color='y',label=u'单机发电量均值:'+str(round(float(average_lines)/1000))+u'MWh')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'发电量(kWh)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组发电量统计(总发电量：'+str(round(float(all_data)/1000))+'MWh)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalpower_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图

    wtt.write_to_txt(curve_data['x'],curve_data['y'],average_lines)


def plotting_all_part_power(fan_group,power_curve,totallimit_reducepower,totalselflimit_reducepower,totalerror3_reducepower,totalserver4_reducepower):
    x_xticks=[]    
    y_power=[]    
    print type(power_curve),power_curve.keys()
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalpower']
    
    '''
    y_totallimit_reducepower=np.array(totallimit_reducepower['fan_totallimit_reducepower'])
    y_totalselflimit_reducepower=np.array(totalselflimit_reducepower['fan_totalselflimit_reducepower'])
    y_totalerror3_reducepower=np.array(totalerror3_reducepower['fan_totalerror3_reducepower'])
    y_totalserver4_reducepower=np.array(totalserver4_reducepower['fan_totalserver4_reducepower'])
    '''
    #此计算放到后边····
    #all_data=sum(y_power+y_totallimit_reducepower+y_totalselflimit_reducepower+y_totalerror3_reducepower+y_totalserver4_reducepower)
    #average_lines=all_data/len(power_curve['fanid'])
    print x_xticks
    print y_power
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    print curve_data['y']
    print curve_data['x']

    y_totallimit_reducepower_buf=[]
    for _fanid in range(len(curve_data['x'])):
        for y_fanid in range(len(totallimit_reducepower['fanid'])):
            if curve_data['x'][_fanid]==totallimit_reducepower['fanid'][y_fanid]:
                y_totallimit_reducepower_buf.append(totallimit_reducepower['fan_totallimit_reducepower'][y_fanid])
    
    y_totalselflimit_reducepower_buf=[]
    for _fanid in range(len(curve_data['x'])):
        for y_fanid in range(len(totalselflimit_reducepower['fanid'])):
            if curve_data['x'][_fanid]==totalselflimit_reducepower['fanid'][y_fanid]:
                y_totalselflimit_reducepower_buf.append(totalselflimit_reducepower['fan_totalselflimit_reducepower'][y_fanid])

    y_totalerror3_reducepower_buf=[]
    for _fanid in range(len(curve_data['x'])):
        for y_fanid in range(len(totalerror3_reducepower['fanid'])):
            if curve_data['x'][_fanid]==totalerror3_reducepower['fanid'][y_fanid]:
                y_totalerror3_reducepower_buf.append(totalerror3_reducepower['fan_totalerror3_reducepower'][y_fanid])

    y_totalserver4_reducepower_buf=[]
    for _fanid in range(len(curve_data['x'])):
        for y_fanid in range(len(totalserver4_reducepower['fanid'])):
            if curve_data['x'][_fanid]==totalserver4_reducepower['fanid'][y_fanid]:
                y_totalserver4_reducepower_buf.append(totalserver4_reducepower['fan_totalserver4_reducepower'][y_fanid])

    curve_data['y']=np.array(curve_data['y'])            
    y_totallimit_reducepower=np.array(y_totallimit_reducepower_buf)
    y_totalselflimit_reducepower=np.array(y_totalselflimit_reducepower_buf)
    y_totalerror3_reducepower=np.array(y_totalerror3_reducepower_buf)
    y_totalserver4_reducepower=np.array(y_totalserver4_reducepower_buf)
    
    all_data=sum(curve_data['y']+y_totallimit_reducepower+y_totalselflimit_reducepower+y_totalerror3_reducepower+y_totalserver4_reducepower)
    average_lines=all_data/len(power_curve['fanid'])
    
    plt.bar(x_values,curve_data['y'],color='g',label=u"实际发电量")
    plt.bar(x_values,y_totallimit_reducepower,bottom=curve_data['y'],color='b',label=u"电网限功率损失电量")
    plt.bar(x_values,y_totalselflimit_reducepower,bottom=curve_data['y']+y_totallimit_reducepower,color='r',label=u"超温限功率损失电量")
    plt.bar(x_values,y_totalerror3_reducepower,bottom=curve_data['y']+y_totallimit_reducepower+y_totalselflimit_reducepower,color='k',label=u"故障状态损失电量")
    plt.bar(x_values,y_totalserver4_reducepower,bottom=curve_data['y']+y_totallimit_reducepower+y_totalselflimit_reducepower+y_totalerror3_reducepower,color='y',label=u"服务状态损失电量")
    
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=1,color='y',linestyle="--",label=u':理论发电量均值:'+str(round(float(average_lines)/1000))+'MWh')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'电量(kWh)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组理论发电量构成(总计:'+str(round(float(all_data)/1000,0))+'MWh)',fontproperties='SimHei')
    plt.legend(loc='upper right',fontsize=4)
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\total_part_of_power_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图

    

def plotting_increase_power(fan_group,power_curve,hzth_power_curve):
    x_xticks=[]    
    y_power=[]
    #存储汇智天华提升功率柱形图···
    hztn_power=[]
    #print type(power_curve),power_curve.keys()
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_normal_totalpower']
    hztn_power=[]
    all_data=sum(y_power)
    
    average_lines=all_data/len(power_curve['fanid'])
    all_data2=sum(hzth_power_curve['fan_hzth_increase_totalpower'])
    average_lines2=all_data2/len(power_curve['fanid'])
    #print x_xticks
    #print y_power
    x_values=[i for i in range(len(x_xticks))]
    x_values=np.array(x_values)
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    for fan in curve_data['x']:
        for hzth_fanid in range(len(hzth_power_curve['fanid'])):
            if fan==hzth_power_curve['fanid'][hzth_fanid]:
                hztn_power.append(hzth_power_curve['fan_hzth_increase_totalpower'][hzth_fanid])       
    
    #print curve_data['y']
    #print curve_data['x']
    plt.bar(x_values,curve_data['y'],0.45,color='b',label=':BEFORE')
    plt.bar(x_values+0.45,hztn_power,0.45,color='r',label=':AFTER')
    
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='b',linestyle=':',label=u'更新主控前发电量均值:'+str(round(float(average_lines)))+'MWh')  #画水平均值横线···
    plt.axhline(y=average_lines2,linewidth=2,color='r',linestyle='--',label=u'更新主控后发电量均值:'+str(average_lines2))  #画水平均值横线···
    
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'总发电量(kWh)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':预计提升发电量：('+str(round(all_data2-all_data,0))+'kw*h)'+u'提升比率:'+str(round(((all_data2-all_data)/all_data)*100*0.15,2))+u'%',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalincrease_power_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图



def plotting_all_available_hour(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    print type(power_curve),power_curve.keys()
    x_xticks=power_curve['fanid']
    #将功率转换成折合可利用小时数···
    y_power=[power/1500 for power in power_curve['fan_totalpower']]
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    print x_xticks
    print y_power
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    print curve_data['y']
    print curve_data['x']
    plt.bar(x_values,curve_data['y'],color='g')
    for a,b in zip(x_values,curve_data['y']):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=3)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'折合可利用小时均值:'+str(round(average_lines))+'h')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'折合可利用小时(h)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组折合可利用小时统计(总计：'+str(round(all_data,0))+'h)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalavailable_hour_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图
    

def plotting_all_reducepower(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_total_reducepower']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'停机损失发电量均值:'+str(round(float(average_lines)/1000))+'MWh')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'停机损失发电量(kWh)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组停机损失发电量统计(总计'+str(round(float(all_data)))+'MWh)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalreducepower_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图


def plotting_all_limitepower(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totallimit_reducepower']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'电网限功率损失电量均值:'+str(round(float(average_lines)/1000))+'MWh')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'电网限功率损失电量(kWh)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组电网限功利性损失电量统计(总计：'+str(round(float(all_data)/1000))+'MWh)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totallimitreducepower_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图

def plotting_all_selflimitpower(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalselflimit_reducepower']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'超温自限功率损失电量均值:'+str(round(float(average_lines)/1000))+'MWh')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'机组超温自限电损失电量(kWh)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组超温自限功率损失电量统计(总计：'+str(round(float(all_data)/1000))+'MWh)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalselflimitpower_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图

def plotting_all_errorpower(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalerror3_reducepower']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'故障损失电量均值:'+str(round(float(average_lines)/1000))+'MWh')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'故障损失电量(kWh)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组故障损失电量统计(总计：'+str(round(float(all_data)/1000))+'MWh)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalerrorpower_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图

def plotting_all_serverpower(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalserver4_reducepower']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'服务损失电量均值:'+str(round(float(average_lines)/1000))+'MWh')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'服务损失电量(kWh)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组服务损失电量统计(总计：'+str(round(float(all_data)/1000))+'MWh)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalserverpower_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图

def plotting_all_avrg_wind(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_aver_wind']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'风速均值:'+str(round(average_lines)))  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'平均风速(m/s)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组平均风速统计',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\all_avrg_wind_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图

def plotting_all_avrg_power(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_aver_power']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'机组功率均值:'+str(round(average_lines))+'kW')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'平均功率(kW)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组平均功率统计(总计：'+str(round(all_data))+'kW)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\all_avrg_power_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图




#绘制所有机组状态时间图
#绘制所有机组状态时间图
#绘制所有机组状态时间图

def plotting_all_generat_time(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    print type(power_curve),power_curve.keys()
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalgenerat_time']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    print x_xticks
    print y_power
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    print curve_data['y']
    print curve_data['x']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'发电时间均值:'+str(round(average_lines))+'h')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'发电时间(h)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组发电时间统计(总计：'+str(round(all_data))+'h)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalgenerat_time_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图


def plotting_all_limit_time(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    print type(power_curve),power_curve.keys()
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totallimit_time']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    print x_xticks
    print y_power
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    print curve_data['y']
    print curve_data['x']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'电网限电时间均值:'+str(round(average_lines))+'h')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'电网限功率时间(h)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组电网限功率时间统计(总计：'+str(round(all_data))+'h)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totallimit_time_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图


def plotting_all_selflimit_time(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    print type(power_curve),power_curve.keys()
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalselflimit_time']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    print x_xticks
    print y_power
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    print curve_data['y']
    print curve_data['x']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'超温限功率时间均值:'+str(round(average_lines))+'h')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'超温限功率时间(h)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组超温限功率时间统计(总计：'+str(round(all_data))+'h)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalselflimit_time_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图


def plotting_all_error_time(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalerror_time']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'故障时间均值:'+str(round(average_lines))+'h')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'故障时间(h)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组故障时间统计(总计：'+str(round(all_data))+'h)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalerror_time_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图


def plotting_all_server_time(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalserver_time']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'服务时间均值:'+str(round(average_lines))+'h')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'服务时间(h)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组服务时间统计(总计：'+str(round(all_data))+'h)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalserver_time_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图

def plotting_all_wait_time(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalwait_time']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'待机时间均值:'+str(round(average_lines))+'h')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'待机时间(h)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组待机时间统计(总计'+str(round(all_data))+'h)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalwait_time_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图

def plotting_all_start_time(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalstart_time']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'启动时间均值:'+str(round(average_lines))+'h')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'启动时间(h)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组启动时间统计(总计：'+str(round(all_data))+'h)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalstart_time_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图



def plotting_all_overtemperature_pie(fan_group,over_temperature):
    '''
    labels=[u'fChoGenTemAve',u'fGeaBeaTemAve',u'fGeaOilTemAve',u'fGenTemAve',u'fGenBeaDriTemAve',u'fConGsclgbTemAve']
    '''
    labels=[u'发电机自感线圈温度',u'齿轮箱轴承温度',u'齿轮箱油温',u'发电机温度',u'发电机驱动侧轴承温度',u'感应IGBT温度']
    overtemperature_data = [0,0,0,0,0,0]
    colors = ['green', 'yellow', 'blue', 'red','cyan','magenta']
    overtemperature_data[0]=over_temperature['fChoGenTemAve']['total_time']
    overtemperature_data[1]=over_temperature['fGeaBeaTemAve']['total_time']
    overtemperature_data[2]=over_temperature['fGeaOilTemAve']['total_time']
    overtemperature_data[3]=over_temperature['fGenTemAve']['total_time']
    overtemperature_data[4]=over_temperature['fGenBeaDriTemAve']['total_time']
    overtemperature_data[5]=over_temperature['fConGsclgbTemAve']['total_time']
    #print fan_databasename,overtemperature_data
    explode = [0.1,0.1,0,0,0,0]
    fig = plt.figure(1, figsize=(6,6))
    ax = fig.add_subplot(111)
    ax.axis('equal')
    patches, texts, autotexts = plt.pie(x=overtemperature_data, labels=labels, colors=colors,explode=explode,autopct='%3.1f %%',shadow=False, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
    plt.legend(loc='upper left',fontsize=5)  #设置图例字体大小
    plt.title(u'机组总超温比例图',fontproperties='SimHei')
    for i in range(len(texts)):
        texts[i].set_fontsize(7)
    #plt.ylim(0,3000)
    #plt.show()
    #plt.grid(color='b' , linewidth='0.3' ,linestyle='--')  #绘制饼图不能用这个网格函数···
    
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\all_overtemperature_pieMyFig-F'+'.png',dpi=30*20)
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\all_overtemperature_pieMyFig-F'+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\overtemperature_pie\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图
'''
def plotting_all_overtemperature_pie(fan_group,over_temperature):
    labels=[u'fChoGenTemAve',u'fGeaBeaTemAve',u'fGeaOilTemAve',u'fGenTemAve',u'fGenBeaDriTemAve',u'fConGsclgbTemAve']
    overtemperature_data = [0,0,0,0,0,0]
    colors = ['green', 'yellow', 'blue', 'red','cyan','magenta']
    overtemperature_data[0]=over_temperature['fChoGenTemAve']['total_time']
    overtemperature_data[1]=over_temperature['fGeaBeaTemAve']['total_time']
    overtemperature_data[2]=over_temperature['fGeaOilTemAve']['total_time']
    overtemperature_data[3]=over_temperature['fGenTemAve']['total_time']
    overtemperature_data[4]=over_temperature['fGenBeaDriTemAve']['total_time']
    overtemperature_data[5]=over_temperature['fConGsclgbTemAve']['total_time']
    #print fan_databasename,overtemperature_data
    explode = [0.1,0.1,0,0,0,0]
    plt.axes(aspect=1)
    plt.pie(x=overtemperature_data, labels=labels, colors=colors,explode=explode,autopct='%3.1f %%',shadow=False, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
    plt.legend(loc='upper left',fontsize=5)  #设置图例字体大小
    plt.title(u'机组超温比例饼图',fontproperties='SimHei')
    #plt.ylim(0,3000)
    #plt.show()
    #plt.grid(color='b' , linewidth='0.3' ,linestyle='--')  #绘制饼图不能用这个网格函数···
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\all_overtemperature_pieMyFig-F'+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\overtemperature_pie\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    plt.close()#关闭图
'''


#绘制机组故障统计图···
#绘制机组故障统计图···

def plotting_all_errornumber(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    print type(power_curve),power_curve.keys()
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalerror_number']
    all_data=sum(y_power)
    average_lines=all_data/len(power_curve['fanid'])
    print x_xticks
    print y_power
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    print curve_data['y']
    print curve_data['x']
    plt.bar(x_values,curve_data['y'],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.axhline(y=average_lines,linewidth=2,color='y',label=u'故障次数均值:'+str(round(average_lines))+u'次')  #画水平均值横线···
    plt.xticks(x_values,curve_data['x'],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'机组ID',fontproperties='SimHei')
    plt.ylabel(u'机组故障数(次)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组故障次数统计(总计：'+str(round(all_data))+u'次)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalerror_number_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图


def plotting_all_firerror(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    #print type(power_curve),power_curve.keys()
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalfirerror_number']
    all_data=sum(y_power)
   # print x_xticks
    #print y_power
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    #print curve_data['x']
    plt.bar(x_values[:20],curve_data['y'][:20],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.xticks(x_values[:20],curve_data['x'][:20],fontsize=5)
    #print curve_data
    plt.yticks(fontsize=5)
    plt.xlabel(u'首故障代码',fontproperties='SimHei')
    plt.ylabel(u'首故障代码次数(次)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组首故障代码次数统计(总计：'+str(round(all_data))+u'次)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalselffirerror_number_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图


def plotting_all_huberror(fan_group,power_curve):
    #print power_curve
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalhuberror_number']
    all_data=sum(y_power)
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values[:20],curve_data['y'][:20],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.xticks(x_values[:20],curve_data['x'][:20],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'变桨故障代码',fontproperties='SimHei')
    plt.ylabel(u'变桨故障代码次数(次)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组变桨故障代码次数统计(总计'+str(round(all_data))+u'次)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #print curve_data
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalhuberror_number_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图


def plotting_all_conerror(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalconerror_number']
    all_data=sum(y_power)
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values[:20],curve_data['y'][:20],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.xticks(x_values[:20],curve_data['x'][:20],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'变频器故障代码',fontproperties='SimHei')
    plt.ylabel(u'变频器故障代码次数(次)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组变频器故障代码次数统计(总计：'+str(round(all_data))+u'次)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalconerror_number_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图

def plotting_all_yawerror(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalyawerror_number']
    all_data=sum(y_power)
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values[:20],curve_data['y'][:20],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.xticks(x_values[:20],curve_data['x'][:20],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'偏航故障代码',fontproperties='SimHei')
    plt.ylabel(u'偏航故障代码次数(次)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组偏航故障代码次数统计(总计'+str(round(all_data))+u'次)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalyawerror_number_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图

def plotting_all_firwaring(fan_group,power_curve):
    x_xticks=[]    
    y_power=[]    
    
    x_xticks=power_curve['fanid']
    y_power=power_curve['fan_totalfirwaring_number']
    all_data=sum(y_power)
    x_values=[i for i in range(len(x_xticks))]
    curve_data=copy.deepcopy(cao.all_statistics_order(x_xticks,y_power))
    #print curve_data['y']
    plt.bar(x_values[:20],curve_data['y'][:20],color='g')
    #for a,b in zip(x_values,curve_data['y']):
    #    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
    plt.xticks(x_values[:20],curve_data['x'][:20],fontsize=5)
    plt.yticks(fontsize=5)
    plt.xlabel(u'告警故障代码',fontproperties='SimHei')
    plt.ylabel(u'告警故障代码次数(次)',fontproperties='SimHei')
    plt.title(str(fan_group)+u':机组告警故障代码次数统计(总计：'+str(round(all_data))+u'次)',fontproperties='SimHei')
    plt.legend(loc='upper right')
    #plt.xlim(0,16)
    #plt.ylim(0,1750)
    #plt.show()
    #plt.savefig(str(fanid)+'.png',dpi=30*20)
    #plt.savefig('fan_picture'+'.png')
    plt.grid(color='b' , linewidth='0.3' ,linestyle='--')
    
    plt.savefig('E:\\fan_hekou_new\\all_data_plot\\totalfirwaring_number_MyFig-F'+str(fan_group)+'.png',dpi=30*20)
    #plt.savefig('E:\\fan_hekou_new\\all_data_plot\\MyFig-F'+str(fan_databasename)+'.png',dpi=30*20)
    #plt.cla()#清空轴
    #plt.clf()#清空图
    plt.close()#关闭图




