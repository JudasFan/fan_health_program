'''
#cording=utf-8
from matplotlib import pyplot as plt
#����ͼ�δ�С������
plt.figure(figsize=(6,9))
#�����״ͼ�ı�ǩ����ǩ���б�
labels = [u'��һ����',u'�ڶ�����',u'��������']
#ÿ����ǩռ��󣬻��Զ�ȥ��ٷֱ�
sizes = [60,30,10]
colors = ['red','yellowgreen','lightskyblue']
#��ĳ���ֱ�ը������ ʹ�����ţ�����һ��ָ��������ֵ�Ĵ�С�Ƿָ����������������ļ�϶
explode = (0.05,0,0)
patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors, labeldistance = 1.1,autopct = '%3.1f%%',shadow = False, startangle = 90,pctdistance = 0.6)
#labeldistance���ı���λ����Զ���ж�Զ��1.1ָ1.1���뾶��λ��
#autopct��Բ������ı���ʽ��%3.1f%%��ʾС������λ��������һλ�ĸ�����
#shadow�����Ƿ�����Ӱ
#startangle����ʼ�Ƕȣ�0����ʾ��0��ʼ��ʱ��ת��Ϊ��һ�顣һ��ѡ���90�ȿ�ʼ�ȽϺÿ� #pctdistance���ٷֱȵ�text��Բ�ĵľ���
#patches, l_texts, p_texts��Ϊ�˵õ���ͼ�ķ���ֵ��p_texts��ͼ�ڲ��ı��ģ�l_texts��ͼ��label���ı�
#�ı��ı��Ĵ�С #�����ǰ�ÿһ��text����������set_size����������������
for t in l_text:
    t.set_size=(30)
for t in p_text:
    t.set_size=(20)
# ����x��y��̶�һ�£�������ͼ������Բ��
plt.axis('equal')
plt.legend()
plt.show()
'''



#codint=utf-8
import numpy as np    
import matplotlib.mlab as mlab    
import matplotlib.pyplot as plt
from pylab import *

X=[0,1,2,3,4,5]  
Y=[222,42,455,664,454,334]
labels   = [u'USA', u'China', u'India', u'Japan',u'sdf',u'es']
fig = plt.figure()
plt.bar(X,Y,0.8,color="green")  
plt.xlabel(u'�ٺ�',fontproperties='SimHei')  
plt.ylabel("Y-axis")
plt.xticks(X,labels)  
plt.title("bar chart")  
plt.show()    


