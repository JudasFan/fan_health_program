#coding=utf-8
import numpy as np

def array_order(x_array,y_array):
    data_point_dict={'x':[],'y':[]}
    x_buf=np.array(x_array)
    
    for order in np.argsort(x_buf):
        data_point_dict['x'].append(x_buf[order])
        data_point_dict['y'].append(y_array[order])
    return data_point_dict

#将参数增序排序···
def array_order2(x_array,y_array):
    data_point_dict={'x':[],'y':[]}
    x_buf=np.array(x_array)
    
    for order in np.argsort(-x_buf):
        data_point_dict['x'].append(x_buf[order])
        data_point_dict['y'].append(y_array[order])
    return data_point_dict

def single_array_order(x_array):
    data_point_dict={'x':[]}
    x_buf=np.array(x_array)    
    for order in np.argsort(x_buf):
        data_point_dict['x'].append(x_buf[order])        
    return data_point_dict

def all_statistics_order(x_array,y_array):
    data_point_dict={'x':[],'y':[]}
    x_buf=np.array(y_array)
    
    for order in np.argsort(-x_buf):
        data_point_dict['x'].append(x_array[order])
        data_point_dict['y'].append(y_array[order])
    return data_point_dict
