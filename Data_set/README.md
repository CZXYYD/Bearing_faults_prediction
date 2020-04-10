# 原始数据集
<br>https://csegroups.case.edu/bearingdatacenter/pages/welcome-case-western-reserve-university-bearing-data-center-website
## 数据说明
<br>官网下的：
<br>Normal Baseline Data   正常轴承数据
<br>12k Drive End Bearing Fault Data   三种异常轴承数据
<br>老师给的：
<br>train，用作训练集，相比上面两个数据少一点
<br>test，用作测试集

### feature_4
接口文件，数据处理产出文件，机器学习输入文件

### train
train文件夹中有多个数据文件，文件名含义如下：   
B代表故障发生在Ball位置，同理IR代表故障发生在inner race位置，OR代表故障发生在outer race位置，NORMAL代表数据文件是正常数据文件；   
每个数据文件可能包含如下多维信号（部分文件可能其中不包括某些维度的信号）：   
DE_time:驱动端加速度数据   
FE_time:风扇端加速度数据   
BA_time:基本加速度数据   
RPM:每分钟转速数据，在提取时实际上RPM对于每个文件只有一个值，但为了文件格式整齐，扩展成了一列，即实际上这一列都是同一个值，代表该文件的RPM
### test
test文件夹中包含多个数据文件，文件名并不包含含义，仅用作记号。    
每个数据文件可能包含如下多维信号（部分文件可能其中不包括某些维度的信号）：   
DE_time:驱动端加速度数据   
FE_time:风扇端加速度数据   
BA_time:基本加速度数据   
RPM:每分钟转速数据，在提取时实际上RPM对于每个文件只有一个值，但为了文件格式整齐，扩展成了一列，即实际上这一列都是同一个值，代表该文件的RPM

特别说明：TEST08的原始数据不含RPM，经查，该数据的RPM是1750，有需要的可以使用该数值作为TEST08中RPM的参考值

## 备注
(12K)Digital data was collected at 12,000 samples per second
<br>所以若1796rpm，每秒转1796/60，每一转60/1796s，每一转采样60*12000/1796=400个数据，所以划分时间片为400
