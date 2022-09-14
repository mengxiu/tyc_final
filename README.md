## 使用需知
+ 此脚本的作用是寻找主要企业与目标企业的关联，并生成excel
+ 需准备好包含主要企业和对应目标企业的社会统一编码的excel，样例见台账0819.xlsx
+ 需安装python环境
+ 需要一个天眼查vip账号（用以更新cookie）
## 使用流程
+ 根据详细流程.doc里的步骤安装好python与第三方库，获取对应页面的cookie
+ 填写配置文件config.py
+ 双击运行main.py以获取相应的关系json文件
+ 双击运行json_to_excel.py以生成excel文件


## 文件结构

### result
+ ./result/json 存放从天眼查获取的两个企业之间的关系的 json 文件
+ ./result/excel 存放最后生成的excel文件，该excel为未去重的关系链的堆叠
+ ./result/nodes.json 存放天眼查id到公司名称的映射
+ ./result/tyc_info.json 存放社会统一编号到天眼查id和公司名称的映射
### src
+ ./src/rela_p2p 存放公司到公司的关系链json文件
### main.py 
+ 主程序，填写完config.py后双击启动
### config.py
+ 配置信息填写，包括主要公司和目标公司的excel文件位置(建议将excel放在与config.py的同级目录，然后写文件名，以避免路径格式的错误)、每次网络请求的间隔、cookie、代理。
### json_to_excel.py
+ 运行以后会将./result/json中的json信息转为excel，并存放在./result/excel
### requirements.txt
+ python第三方库列表