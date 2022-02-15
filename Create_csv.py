import os
import re
import csv
import sys

from config import *

txt_data = []
with open(txt_filename, encoding='utf8', mode='r') as txt_file:
    for line in txt_file:
        txt_data.append(line.rstrip())

txt_formatting = []
if 1==1:    #ジョルダン
    for i, line in enumerate(txt_data):
        #日付データ抽出
        date_data = jorudan_datapattern_date
        trigger = re.search(jorudan_datapattern_date,line)
        if(trigger):
            txt_formatting.append("DATE," + str(trigger.group()))
        
        #乗り換えデータ抽出
        if(i == len(txt_data)-1):     #最終行はスキップ
            break
        train_data = jorudan_datapattern_train
        trigger = re.match(jorudan_datapattern_train,line)
        if(trigger):
            datalist = ['1']
            datalist.append(trigger.group()[1:])                                                #発駅
            datalist.append(txt_data[i+2][3:8])                                                 #発時間
            datalist.append(re.match(jorudan_datapattern_train,txt_data[i+4]).group()[1:])      #着駅
            datalist.append(txt_data[i+2][9:14])                                                #着時間
            datalist.append(re.match("[^( |'\uFF08')]+",txt_data[i+1][3:]).group())             #路線
            datalist.append('')                                                                 #列車番号
            datalist.append('')                                                                 #列車種別
            datalist.append(re.search("\(\D+行\)",txt_data[i+1]).group()[1:-1])                 #行先
            if(re.search("\d+番線発",txt_data[i])):
                datalist.append(re.search("\d+番線発",txt_data[i]).group()[:-3])
            else:
                datalist.append('')
            if(re.search("\d+番線着",txt_data[i+4])):
                datalist.append(re.search("\d+番線着", txt_data[i+4]))
            else:
                datalist.append('')
                
            txt_formatting.append(','.join(map(str,datalist)))
            

