# 原始数据集
<br>https://csegroups.case.edu/bearingdatacenter/pages/welcome-case-western-reserve-university-bearing-data-center-website
## 数据说明
<br>#两个（官网下的）：
<br>Normal Baseline Data   正常轴承数据
<br>12k Drive End Bearing Fault Data   三种异常轴承数据
<br>#一个（老师给的）：
<br>train，用作训练集，相比上面两个数据少一点


train文件夹中有多个数据文件，文件名含义如下：   
B代表故障发生在Ball位置，同理IR代表故障发生在inner race位置，OR代表故障发生在outer race位置，NORMAL代表数据文件是正常数据文件；   
每个数据文件可能包含如下多维信号（部分文件可能其中不包括某些维度的信号）：   
DE_time:驱动端加速度数据   
FE_time:风扇端加速度数据   
BA_time:基本加速度数据   
RPM:每分钟转速数据，在提取时实际上RPM对于每个文件只有一个值，但为了文件格式整齐，扩展成了一列，即实际上这一列都是同一个值，代表该文件的RPM
  

