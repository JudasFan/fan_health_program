#coding=utf-8
import os

def write_to_txt(curve_data_x,curve_data_y,average_lines):

    write_txt_path="E:\\fan_gaoshanzi_new"
    '''
    #serach_datetime=excel_title
    
    #excel_headdata=[u'风机号', u'平均风速', u'总发电量',u'总发电时间', u'平均每小时发电量']
    #fan_dict=['windspeed','power','generate_time','generate_efficient']
    
    excel_workbook=Workbook()
    excel_sheet_name=serach_datetime
    excel_sheet=excel_workbook.add_sheet(excel_sheet_name)
    
    head_index=0
    sheet_row=1
    for headdata_column in range(len(excel_headdata)):
        excel_sheet.write(head_index,headdata_column,excel_headdata[headdata_column])
    
    for fan in fan_data_dict:
        
        for headdata_column in range(len(excel_headdata)):
            if headdata_column==0:
                excel_sheet.write(sheet_row,headdata_column,fan)
            else:
                excel_sheet.write(sheet_row,headdata_column,fan_data_dict[fan][fan_dict[headdata_column-1]])
        sheet_row+=1

    excel_workbook.save(write_excel_path+'\\'+serach_datetime+'.xls')
        
'''
    os.chdir(write_txt_path)
    fo=open("fandata.txt","w")
    fo.write('风机号：\t')
    for i in curve_data_x:
        fo.write(str(i)+'\t')
    fo.write('\n')
    fo.write('发电量：\t')
    for data in curve_data_y:
        fo.write(str(round(data,0))+'\t')
    fo.write('\n')
    
    fo.write('同发电量均值比较：\t')
    for data in curve_data_y:
        fo.write(str(round((data-average_lines)/average_lines*100,1))+'\t')
    fo.write('\n')
    
    fo.close()

    
