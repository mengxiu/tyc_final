import json
import random
import time
import pandas as pd
from lxml import etree
import urllib3
import requests
from config import *

urllib3.disable_warnings()  #关闭ssl证书缺失的警告

with open('result/tyc_info.json', 'r', encoding='utf-8')as f:
    tyc_info_dict = json.load(f)


def get_name_and_tycid(code_list:list)->list:
    # global tyc_info_dic
    rec=[]
    count=0
    for code in code_list:
        count+=1
        print('\r', '正在获取相应的天眼查id，已经完成了{}个'.format(count), end='')
        info=tyc_info_dict.get(code)
        if not info is None:
            #['社会统一编号', '天眼查公司id', '企业名称']
            rec.append([code,info[0],info[1]])
        else:
            while True:
                tmp_dict=get_name_and_tycid_by_network(code)
                if tmp_dict!={}:
                    break
            info = tmp_dict.get(code)
            rec.append([code, info[0], info[1]])
            tyc_info_dict.update(tmp_dict)
            with open('result/tyc_info.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(tyc_info_dict))
    return rec
#联网获取企业名称和对应的天眼查id
def get_name_and_tycid_by_network(id:str)->dict:
    try:
        time.sleep(sleep_time_s+random.random()*sleep_time_r)
        context = requests.get("https://www.tianyancha.com/search?key={}".format(id), headers=headers, verify=False,
                           allow_redirects=False)
    except:
        print('获取页面失败，当前需要获取的id为{}，正在重试，若重试次数过多，请重启脚本'.format(id))
        return {}
    html = etree.HTML(context.text)
    href = html.xpath('//*[@id="page-container"]/div/div[2]/section/main/div[2]/div[2]/div[1]/div/div[last()]/div[2]/div[1]/div[1]/a/@href')
    #企业名称的xpath和浏览器上实时展示的位置不一样
    name=html.xpath('//*[@id="page-container"]/div/div[2]/section/main/div[2]/div[2]/div[1]/div/div[last()]/div[2]/div[1]/div[1]/a/span')
    context.close()
    if href == []:
        print('获取页面失败，当前需要获取的id为{},正在重试，若重试次数过多，请重启脚本'.format(id))
        return {}
    return {id:[href[0].split('/')[-1],name[0].text]}


major_list=get_name_and_tycid(list(pd.read_excel(major_excel_name, usecols=[major_colums_name],sheet_name=major_excel_sheet)[major_colums_name]))
target_list=get_name_and_tycid(list(pd.read_excel(target_excel_name, usecols=[target_colums_name],sheet_name=target_excel_sheet)[target_colums_name]))

with open('result/tyc_info.json', 'w', encoding='utf-8')as f:
    f.write(json.dumps(tyc_info_dict))

