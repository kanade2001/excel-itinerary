import os
import re
import csv
import sys
import datetime
from tracemalloc import start

from config import *

def main_Create_csv(txt_data, Csv_export = False):
    #txt_data = []
    #with open(txt_filename, encoding='utf8', mode='r') as txt_file:
    #   for line in txt_file:
    #       txt_data.append(line.rstrip())

    print('TEXTDATA')
    print(txt_data)
    print('TEXTDATA')


    #data formatting
    txt_formatting = []
    DATE_current = ''

    tag = 'jourdan'       #select website
    if tag=='jourdan':    #jourdan
        start_flag = False
        for i, line in enumerate(txt_data):
            #DATE data
            date_data = jorudan_datapattern_date
            trigger = re.search(jorudan_datapattern_date,line)
            if(trigger):
                DATE_current = str(trigger.group())
            
            #transit data
            
            trigger = re.match(jorudan_datapattern_train,line)
            if(trigger):
                if start_flag == True and trigger.group()[0] =='■':
                    break
                datalist = ['1']
                datalist.append(trigger.group()[1:])                                                #発駅
                datalist.append(DATE_current + ' ' + txt_data[i+2][3:8])                            #発時間
                datalist.append(re.match(jorudan_datapattern_train,txt_data[i+4]).group()[1:])      #着駅
                datalist.append(DATE_current + ' ' + txt_data[i+2][9:14])                           #着時間
                datalist.append(re.match('[^( |"\uFF08")]+',txt_data[i+1][3:]).group())             #路線
                datalist.append('')                                                                 #列車番号
                datalist.append('')                                                                 #列車種別
                datalist.append(re.search('\(\D+行\)',txt_data[i+1]).group()[1:-1])                 #行先
                if(re.search('\d+番線発',txt_data[i])):                                              #発番線
                    datalist.append(re.search("\d+番線発",txt_data[i]).group()[:-3])
                else:
                    datalist.append('')
                if(re.search('\d+番線着',txt_data[i+4])):                                            #着番線
                    datalist.append(re.search('\d+番線着', txt_data[i+4]).group()[:-3])
                else:
                    datalist.append('')
                    
                txt_formatting.append(datalist)
                start_flag = True

    if txt_formatting ==[]:
        return 1 #Abnormal termination
    else:
        #create csv file
        if Csv_export == True:
            with open('Sample1.csv','w',encoding='utf-8') as csv_file:
                csv.writer(csv_file).writerows(txt_formatting)
            
            return 0 #Normal termination

