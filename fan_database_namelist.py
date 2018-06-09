#coding=utf-8
#转换生成机组在数据库中数据库名称列表···
import MySQLdb

def fan_database_namelist(number):
    fan_database=[]
    for i in range(2,number+2):
     
        database_buf='86_99_'
        fanid=i        
        fan_database.append(database_buf+str(fanid)+'_130')

    return fan_database


def fan_database_namelist():
    fan_list=[]
    try:     
        conn=MySQLdb.connect(host='localhost',user='root',passwd='mysql',db='setupdb')
        cur=conn.cursor()
        sql="select fanid,fanName,fanip,fantype,plctype from fanset;"
        cur.execute(sql)
        results=cur.fetchall()
        
        for row in results:
            row_buf=list(row)
            row_buf[2]=row_buf[2].replace('.','_')
            fan_list.append(list(row_buf))
        cur.close()        
        conn.close()        
    except:
        print "mysql opration is false!"

    return fan_list

