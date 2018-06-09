#coding=utf-8
import MySQLdb
def write_windpower_record(search_time,fan_data,wind_cut):
    try:
        print '\n\n\n\nthread write_wind_power\n\n\n'
        string=''
        normal_power=[]
        str_normal_power=''
        db = MySQLdb.connect("localhost","root","mysql",'setupdb')
        cursor=db.cursor()
        
        for i in range(len(wind_cut)):
            string+=',windspeed'+str(i)
        for fan_databasename in fan_data:
            if len(fan_databasename.split('_'))==4:
                for wind in wind_cut:
                    normal_power.append(fan_data[fan_databasename]['normal_power_curve'][wind]['poweravg'])
                str_normal_power=str(normal_power).strip('[]')
                
                sql="insert into wind_power(fanid,fanname,startdate,enddate %s) values(%d,%s,%s,%s,%s);"%(string,fan_data[fan_databasename]['fanset_information']['fanid'],'\''+fan_data[fan_databasename]['fanset_information']['fanname']+'\'','\''+str(search_time[0])+'\'',
                                                                                                  '\''+str(search_time[1])+'\'',str_normal_power)
                #normal_power=[]
                #cursor.execute(sql)
                #db.commit()
        cursor.close()
        db.close()
    except:
        print "mysql operation wind_power table is false!"
    
def write_windpower_records(search_time,fan_data,wind_cut):
    
    print search_time

def this():
    print 'this'
