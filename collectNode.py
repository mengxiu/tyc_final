#此文件会将所有在'./src/rela_p2p'的json中出现过的nodes记录下来
import json
import os
with open('result/{}.json'.format('nodes'), 'r',encoding='utf-8') as f:
    node_dict = json.load(f)

fileList=os.listdir('./src/rela_p2p')
for file in fileList:
    # if file=='721378286.json':
    #     continue
    fileName=file.split('.')[0]
    try:
        with open('./src/rela_p2p/{}'.format(file), 'r',encoding='gbk') as f:
            relation = json.load(f)
    except:
        with open('./src/rela_p2p/{}'.format(file), 'r',encoding='utf-8') as f:
            relation = json.load(f)
    try:
      nodes=relation['data']['nodes']
    except:
        continue
    for node in nodes:
        node_dict.update({node['id']:node['properties']['name']})
with open('result/{}.json'.format('nodes'), 'w',encoding='utf-8') as f:
    f.write(json.dumps(node_dict))
