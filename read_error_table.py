#coding=utf-8
#import plot_chat as pc

def read_error_table(fan_data,cursor,fan_databasename,search_time):
    sql="SELECT dtStaTim,uiHubErr001,uiHubErr002,uiHubErr003,uiErrFir001,uiErrFir002,uiErrFir003,uiErrFir004,uiErrFir005,uiErrFir006,uiErrFir007,uiErrFir008,uiConErr,uiYawErr,\
    uiWarFir001,uiWarFir002,uiWarFir003,uiWarFir004,uiWarFir005,uiWarFir006,uiWarFir007,uiWarFir008 FROM error where dtStaTim>=%d and dtStaTim<%d;" %(search_time[0],search_time[1])
    #print search_time[0],search_time[1]
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        #print len(results)
        for row in results:
            #print row[4:12]
            for huberr in row[1:4]:
                if huberr!=0:                    
                    if huberr not in fan_data[fan_databasename]['error']['uiHubErr']['HubErr_code']:
                        fan_data[fan_databasename]['error']['uiHubErr']['HubErr_code'][huberr]=1
                    else:
                        fan_data[fan_databasename]['error']['uiHubErr']['HubErr_code'][huberr]+=1
                    
            for errfir in row[4:12]:
                #print row[4:12]
                #print errfir 
                if errfir!=0:                    
                    if errfir not in fan_data[fan_databasename]['error']['uiErrFir']['ErrFir_code']:
                        fan_data[fan_databasename]['error']['uiErrFir']['ErrFir_code'][errfir]=1
                    else:
                        fan_data[fan_databasename]['error']['uiErrFir']['ErrFir_code'][errfir]+=1

            for conerr in row[12:13]:
                if conerr!=0:                    
                    if conerr not in fan_data[fan_databasename]['error']['uiConErr']['ConErr_code']:
                        fan_data[fan_databasename]['error']['uiConErr']['ConErr_code'][conerr]=1
                    else:
                        fan_data[fan_databasename]['error']['uiConErr']['ConErr_code'][conerr]+=1
            for yawerr in row[13:14]:
                if yawerr!=0:                    
                    if yawerr not in fan_data[fan_databasename]['error']['uiYawErr']['YawErr_code']:
                        fan_data[fan_databasename]['error']['uiYawErr']['YawErr_code'][yawerr]=1
                    else:
                        fan_data[fan_databasename]['error']['uiYawErr']['YawErr_code'][yawerr]+=1

            for warfir in row[14:21]:
                if warfir!=0:                    
                    if warfir not in fan_data[fan_databasename]['error']['uiWarFir']['WarFir_code']:
                        fan_data[fan_databasename]['error']['uiWarFir']['WarFir_code'][warfir]=1
                    else:
                        fan_data[fan_databasename]['error']['uiWarFir']['WarFir_code'][warfir]+=1                    
        
        #pc.plotting_huberror_registe_bar(fan_databasename,fan_data[fan_databasename]['error'])
        #pc.plotting_errorfir_registe_bar(fan_databasename,fan_data[fan_databasename]['error'])
        #pc.plotting_errorcon_registe_bar(fan_databasename,fan_data[fan_databasename]['error'])
        #pc.plotting_erroryaw_registe_bar(fan_databasename,fan_data[fan_databasename]['error'])
        #pc.plotting_warfir_registe_bar(fan_databasename,fan_data[fan_databasename]['error'])
        
    except:            
        print ':  Error: serach statistics_limitpower unable to fecth data of tenminlog'
    #print fan_data[fan_databasename]['error']['uiHubErr']
    #print fan_data[fan_databasename]['error']['uiErrFir']['ErrFir_code'][536]

    return fan_data

