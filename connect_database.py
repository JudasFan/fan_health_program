#coding=utf-8
import MySQLdb
import read_stames_table as rst
import read_error_table as ret
import copy
import all_data_statistic as ads
import check_database_name as cdn


def connect_fan_database_statistics_normal_windpower(fan_array,search_time,fan_dict,fan_tuple):
    mysql_databasename=[]
    real_fan_list=[]    

    mysql_databasename=cdn.check_database_name(fan_array)

    #判断选出的数据库中的数据表个数是否符合要求···
    real_fan_list=cdn.check_database_table(mysql_databasename)    

    
    for fan_databasename in real_fan_list:
        try:            
            #print fan_databasename
            if fan_databasename in mysql_databasename:
                if fan_databasename not in fan_dict:
                    fan_dict[fan_databasename]=copy.deepcopy(fan_tuple[1])    #初始化风机根数据结构字典···
                    for  fan_row in fan_array:                        
                        if fan_databasename == fan_row[2]:
                            fan_dict[fan_databasename]['fanset_information']['fanid']=fan_row[0]
                            fan_dict[fan_databasename]['fanset_information']['fanname']=fan_row[1]
                            fan_dict[fan_databasename]['fanset_information']['fanip']=fan_row[2].replace('_','.')
                            fan_dict[fan_databasename]['fanset_information']['fantype']=fan_row[3]
                            fan_dict[fan_databasename]['fanset_information']['plctype']=fan_row[4]
                    
                #print fan_databasename               
                db = MySQLdb.connect("localhost","root","mysql",fan_databasename)
                cursor=db.cursor()            
                fan_data=copy.deepcopy(rst.read_tenminlog_table_normal_windpower(cursor,fan_databasename,search_time,fan_dict))            
                cursor.close()
                db.close()  
            else:
                print 'the databases:'+fan_databasename+' is not exit!'
        except:
            print fan_databasename+'the curve of windpower can not calculate!'
    return fan_data



def connect_fan_database(search_time,fan_dict_parameter,fan_tuple):
    fan_dict={}
    mysql_databasename=[]
    real_fan_list=[]
    db = MySQLdb.connect("localhost","root","mysql")
    cursor=db.cursor()    
    sql="show databases;"       
    cursor.execute(sql)
    all_database = cursor.fetchall()
    #print all_database,type(all_database),all_database[0]
    for row in all_database:
        if row[0] in fan_dict_parameter:
            mysql_databasename.append(row[0])
    cursor.close()
    db.close()


    for fan_databasename in mysql_databasename:
        #print fan_databasename
        if fan_databasename in fan_dict_parameter:
            #每次计算前清空数据结构···
            fan_dict[fan_databasename]=copy.deepcopy(fan_tuple[1])
            #每次计算前将已经计算好的机组功率曲线数据拷贝进来····
            fan_dict[fan_databasename]['normal_power_curve']=copy.deepcopy(fan_dict_parameter[fan_databasename]['normal_power_curve'])
            fan_dict[fan_databasename]['fanset_information']=copy.deepcopy(fan_dict_parameter[fan_databasename]['fanset_information'])
            
            db = MySQLdb.connect("localhost","root","mysql",fan_databasename)
            cursor=db.cursor()
            fan_dict=copy.deepcopy(rst.read_stames_table(cursor,fan_databasename,search_time,fan_dict,fan_tuple))
            
            #print fan_databasename,fan_dict[fan_databasename]['stames'][7]['stamescode_time'],fan_dict[fan_databasename]['stames'][7]['stamescode_number']
            fan_data=copy.deepcopy(rst.read_tenminlog_table(cursor,fan_databasename,search_time,fan_dict))
            fan_data=copy.deepcopy(ret.read_error_table(fan_data,cursor,fan_databasename,search_time))
            cursor.close()
            db.close()             
        else:
            print 'the databases:'+fan_databasename+' is not exit!'
    
    #整场数据统计···
    fan_data=copy.deepcopy(ads.all_data_statistic(fan_data))    
    #print fan_data['all_data_statistic']['total_firwaring']
    return fan_data
    
