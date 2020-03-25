# Bearing_faults_prediction
轴承故障预测大作业项目
<br>2020/3/18 立项 czxyyd
<br> Data_set ：数据集文件

# 第一周任务说明
1、训练一个四分类模型，预测目标为故障发生的位置(normal, ball, inner race, outer race)   
2、以train文件夹中的数据为训练集，可自行划分数据作为验证集进行模型的验证调优。
## 可供参考的评分规则
评分score为分别单独计算四类预测结果的f1-score加权求和，
其中三个故障类的权重ball,inner race,outer race均为0.3，正常类的权重为0.1 

# 第二周任务说明
训练、优化模型，周四起每晚提交一次测试集的验证答案，根据反馈优化。
## 测试集答案提交形式
提交答案时，约定normal(NORMAL), ball(B), outer race(OR), inner race(IR)的预测输出标签为0, 1, 2, 3。   
提交csv文件，文件分两列，第一列为按序预测结果(0/1/2/3)，第二列为预测结果所在的测试集文件(字符串形式，例如TEST01)，分别以label和filename作为列名。具体形式参照提供的example.csv。
## 评分规则
使用四类的f1-score(precision和recall值的调和平均数)加权和进行评价，按照上面的标签约定，即：   
score = [0.3×f1score(class1) + 0.3×f1score(class2) + 0.3×f1score(class3) + 0.1×f1score(class0)]*100   
满分为100分。

# 关于github的使用
https://www.cnblogs.com/schaepher/p/4933873.html
