from data import *
from get_rela_json import *
import os
lenth_major_list=len(major_list)
major_list=major_list[:]
total=len(major_list)*len(target_list)
lenth_target_list=len(target_list)

for i in range(len(major_list)):
    com=major_list[i]
    # ['社会统一编号', '天眼查公司id', '企业名称']
    os.makedirs('./result/json/{}'.format(com[2]), exist_ok=True)
    tmp_target_list = target_list[:]
    tmp_lenth = len( tmp_target_list)
    while len(tmp_target_list)>0:
        print('\r', '共{}个，已经完成了{}个'.format(total, i * lenth_target_list - len(tmp_target_list)+lenth_target_list), end='')
        for target in tmp_target_list:
            rela_p2p_json = get_rela_p2p_json(com[1], target[1])
            if rela_p2p_json!={}:
                with open('./result/json/{}/{}.json'.format(com[2], target[2]), 'w', encoding='utf-8') as f:
                    f.write(json.dumps(rela_p2p_json))
            tmp_target_list.remove(target)
            print('\r', '共{}个，已经完成了{}个'.format(total, i * lenth_target_list - len(tmp_target_list) + lenth_target_list),end='')

