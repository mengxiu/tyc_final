# 主要的企业列表的excel文件名和sheet名
major_excel_name = './src/20220906/2.xlsx'
major_excel_sheet = 'Sheet1'
major_colums_name = '统一社会信用代码'  # 社会统一编号所在列的列名

# 目标的企业列表的excel文件名和sheet名
target_excel_name = './src/20220906/target.xls'
target_excel_sheet = 'Sheet1'
target_colums_name = '统一社会信用代码'  # 社会统一编号所在列的列名

# cookie,如有必要请更新TYCID、auth_token的值
cookies = {
    'TYCID': '',
    '_bl_uid': 'gXljC6Ohu0tb7LrUn52erjaft6tg',
    'ssuid': '9835191610',
    '_ga': 'GA1.2.2073672117.1660548792',
    'bad_id658cce70-d9dc-11e9-96c6-833900356dc6': '1316d7d2-1d40-11ed-a365-5b7375bec0a5',
    'jsid': 'SEO-BAIDU-ALL-SY-000001',
    'tyc-user-info': '{%22state%22:%224%22%2C%22vipManager%22:%220%22%2C%22mobile%22:%2211111333841%22%2C%22isExpired%22:%220%22}',
    'tyc-user-info-save-time': '1661154258445',
    'auth_token': '',
    'tyc-user-phone': '%255B%252211111333841%2522%252C%2522188%25209460%25209639%2522%255D',
    'HWWAFSESID': 'ca8cd6c74466eb01ddf',
    'HWWAFSESTIME': '1662471987597',
    'csrfToken': 'FQiZCmpr3jMIIJaaz_ZHZqQn',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2235225913%22%2C%22first_id%22%3A%22182a0020f81f9-010abee4d1db56a-26021d51-1638720-182a0020f84825%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiIzNTIyNTkxMyIsIiRpZGVudGl0eV9jb29raWVfaWQiOiIxODJhMDAyMGY4MWY5LTAxMGFiZWU0ZDFkYjU2YS0yNjAyMWQ1MS0xNjM4NzIwLTE4MmEwMDIwZjg0ODI1In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2235225913%22%7D%2C%22%24device_id%22%3A%22182a0020f81f9-010abee4d1db56a-26021d51-1638720-182a0020f84825%22%7D',
    'bdHomeCount': '0',
    'Hm_lvt_e92c8d65d92d534b0fc290df538b4758': '1661234580,1661710473,1661928653,1662471996',
    'bannerFlag': 'true',
    '_gid': 'GA1.2.1402569219.1662472231',
    'cloud_token': '07d53a45c30149d5b63679713a6b8039',
    'searchSessionId': '1662477461.88249451',
    '_gat_gtag_UA_123487620_1': '1',
    'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758': '1662477890',
}
"""以上为必须填写"""

# 每次网络请求的暂停时间，总间隔时间为sleep_time_s+ random.random() * sleep_time_r
sleep_time_s = 1
sleep_time_r = 1.2

# 代理
proxy = [
    {}
]
# 代理填写实例，本脚本没有对代理做错误处理，请保证代理的可用性
# proxy = [{'http': 'ip:端口',
#           'https': 'ip:端口'
#           },
#         {'http': 'ip:端口',
#           'https': 'ip:端口'
#           },
#         {'http': 'ip:端口',
#           'https': 'ip:端口'
#           },
#          {
#          }]


headers = {
    'authority': 'www.tianyancha.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://www.tianyancha.com/relation?idsFrom=5263115676,2103295365&idsTo=2960322839,1811121487',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
