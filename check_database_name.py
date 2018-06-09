#coding=utf8
import MySQLdb
import numpy as np

def check_database_name(fan_array):
    try:        
        mysql_databasename=[]
        db = MySQLdb.connect("localhost","root","mysql")
        cursor=db.cursor()    
        sql="show databases;"       
        cursor.execute(sql)
        all_database = cursor.fetchall()
        for row in all_database:
            for  fan_row in fan_array:            
                if row[0] == fan_row[2]:
                    mysql_databasename.append(row[0])
        cursor.close()
        db.close()
    except:
        print 'can not find fan_database!'
    
    return mysql_databasename

#判断选出的数据库中的数据表个数是否符合要求···
def check_database_table(mysql_databasename):
    real_fan_list=[]
    for databasename in mysql_databasename:
        db2 = MySQLdb.connect("localhost","root","mysql",databasename)
        cursor2=db2.cursor()    
        sql2="show tables;"       
        cursor2.execute(sql2)
        all_database2 = cursor2.fetchall()
        if len(all_database2)==12:
            real_fan_list.append(databasename)
            #print databasename
    cursor2.close()
    db2.close()

    return real_fan_list

def create_windpower_table(databasename):    

    try:        
        wind_cut=np.arange(3,20,0.2)        
        table_buff=[]
        string=''
        db = MySQLdb.connect("localhost","root","mysql",databasename)
        cursor=db.cursor()    
        sql="show tables;"       
        cursor.execute(sql)
        all_tables = cursor.fetchall()
        
        
        for all_tables_row in all_tables:
            table_buff.append(all_tables_row[0])
        

        if 'wind_power' not in table_buff:
            #wind_cut=np.arange(3,20,0.2)            
            #for i in range(len(wind_cut)):
            for i in wind_cut:
                string+='windspeed'+str(int(i*10))+' '+'smallint,'
            
            sql="create table wind_power(id int auto_increment,startdate DATETIME not null,enddate DATETIME not null,fanid SMALLINT not null,fanname varchar(10) not null, %s primary key(id));"%(string)
            cursor.execute(sql)
            db.commit()
        else:
            print 'the table of windpower already existed!'
        cursor.close()
        db.close()
        return wind_cut
    except:
        print 'create windpower table is fall!'

def create_table_of_windfarm_statistics(databasename):
    try:
        table_buff=[]
        db = MySQLdb.connect("localhost","root","mysql",databasename)
        cursor=db.cursor()    
        sql="show tables;"       
        cursor.execute(sql)
        all_tables = cursor.fetchall()
        
        for all_tables_row in all_tables:
            table_buff.append(all_tables_row[0])
            
        if 'windfarm_statistics' not in table_buff:
            sql="create table windfarm_statistics(id int auto_increment,startdate DATETIME not null,fanid SMALLINT not null,fanname varchar(10) not null,WindSpeedAvg float,TotalPower float,TotalAvailablehour float, "+\
                " AveragePower float,SelfLimitTime float,SelfLimitPower float, fChoGenTemAveTime float, fGeaBeaTemAveTime float, fGeaOilTemAveTime float ,fGenTemAveTime float,fGenBeaDriTemAve float,fConGsclgbTemAve float,"+\
                " TotalLimitPower float,TotalLimitTime float,WindNoPower float,WindNoPowerTime float,GeneratTime float,WaitTime float,StartTime float,ServeLossPower float,ServeLossTime float,ErrorLossPower float,ErrorLossTime float,ErrorNumber int,TheoryPower float, primary key(id));"
            cursor.execute(sql)
            db.commit()
    except:
        print 'create windfart statistics tables is fall!'


        
    
