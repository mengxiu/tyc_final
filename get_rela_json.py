import json
import random
import time
import requests
from config import *

count = 0


def get_relation_dict(tycid_one: str, tycid_two: str) -> dict:
    global count
    count += 1
    if count % (14*len(proxy)) == 0:
        time.sleep(25)
    # 注意获取时间戳
    int(round(time.time() * 1000))
    params = {
        'fromCompanyGid': tycid_one,
        'toCompanyGid': tycid_two,
        '_': str(int(round(time.time() * 1000))),
    }
    while True:
        try:
            response = requests.get('https://www.tianyancha.com/relation/shortpath.json', params=params,
                                    cookies=cookies,
                                    headers=headers, proxies=proxy[count % len(proxy)])
            break
        except requests.exceptions.ConnectionError:

            print('ip被封或者网络失去链接，正在暂停5分钟')
            time.sleep(300)
        except requests.exceptions.ReadTimeout:
            print('链接超时，请检查网络，正在暂停5分钟')
            time.sleep(300)
    time.sleep((sleep_time_s+ random.random() * sleep_time_r)/len(proxy))
    if response.status_code == 200:
        j = json.loads(response.text)
    else:
        print('爬取太快被抓了，稍等一会再试')
        print('此处正在暂停5分钟，可以等待或直接重启脚本')
        time.sleep(300)
        # restart()
        # exit()
    response.close()
    try:
        isLogin = j['isLogin']
        if isLogin != 0:
            print('cookie已经失效或vip过期,请更新cookie')
            return {}
    except:
        return {}
    try:
        data = json.loads(j['data'])
    except :
        print('天眼查id为{}与{}的公司获取关系json成功，但是data为null'.format(tycid_one,tycid_two))
        return {}
    return data


def get_rela_p2p_json(tycid_one: str, tycid_two: str) -> dict:
    try:
        with open('./src/rela_p2p/{}&{}.json'.format(tycid_one, tycid_two), 'r') as f:
            rela_p2p = json.load(f)
    except:
        rela_p2p = get_relation_dict(tycid_one, tycid_two)
        # if rela_p2p!={}:
        with open('./src/rela_p2p/{}&{}.json'.format(tycid_one, tycid_two), 'w') as f:
            f.write(json.dumps(rela_p2p))
    if len(rela_p2p) <= 0:
        return {}
    if len(rela_p2p['p_0']['relationships']) <= 0:
        return {}
    return rela_p2p

