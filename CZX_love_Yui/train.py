import lightgbm as lgb
import numpy as np
import pandas as pd
import os
from sklearn.externals import joblib
from sklearn.metrics import classification_report

#从feature_4文件夹里面合成训练数据集train_data

feature_B = pd.read_csv('./feature_4/feature_B.csv')           #此路径为feature_B.csv文件所在路径
feature_IR = pd.read_csv('./feature_4/feature_IR.csv')          #同上
feature_NORMAL = pd.read_csv('./feature_4/feature_NORMAL.csv')  #同上
feature_OR = pd.read_csv('./feature_4/feature_OR.csv')          #同上
frames = [feature_B,feature_IR,feature_NORMAL,feature_OR]

train_data = pd.concat(frames)


def train():
    # 模型初始化，设置random_state保证可复现性，便于观察优化
    train_data_y = train_data['label']
    # 除去标签的所有列就是特征
    train_data_x = train_data.drop(['label'], axis=1)
    
    model_lgb_default = lgb.LGBMClassifier(random_state=2019)
    # 模型训练
    model_lgb_default.fit(train_data_x, train_data_y)
    joblib.dump(model_lgb_default, './model/lightgbm.model')    #此路径为模型保存的路径

#train()

#到此为止已经利用训练集数据训练出来了模型，下面调用模型来预测测试集

#测试集数据同样也要特征提取，否则输入模型的格式会报错

#特征提取后的文件已上传github，在Data_set/feature_test

#下面预测模型
#首先导入模型
model = joblib.load('./model/lightgbm1_0.model')
#经过特征处理的测试集数据路径
path = '../Data_set/feature_test'
files = os.listdir(path)

#预测，并把预测结果赋给result
result = pd.DataFrame()
index = 0
for test_file in files:
    predict_res = pd.DataFrame()
    index = index + 1 
    dftest_file = pd.read_csv(path + '/' + test_file)
    predict = model.predict(dftest_file)
    predict_res['label'] = predict
    predict_res['filename'] = 'TEST'+str(index).zfill(2)
    result = pd.concat([result,predict_res])

#预测结果导出文件路径
result.to_csv('../Data_set/result/result1_0.csv',index=False)

#给结果打分
#这是答案
switch ={'TEST01':1,
         'TEST02':1,
         'TEST03':3,   #不确定
         'TEST04':2,
         'TEST05':2,  #不确定
         'TEST06':2,
         'TEST07':2,  #
         'TEST08':0,
         'TEST09':2,
         'TEST10':2,    #
         'TEST11':2,
         'TEST12':3,
         'TEST13':3,
         'TEST14':1,}

def score(path):
    res = pd.read_csv(path)    #读取刚才预测结果文件
    y_true = []                #正确结果列表
    for ans in res['filename']:
        y_true.append(switch.get(ans))
    
    y_pred = list(res['label']) #预测结果列表
    
    #打分结果为字典格式
    Answer = classification_report(y_true=y_true, y_pred=y_pred, digits=3, output_dict = True)
    score = (0.3*(Answer['1']['f1-score']+Answer['2']['f1-score']+Answer['3']['f1-score'])+0.1*Answer['0']['f1-score'])*100

    return score


print(score('../Data_set/result/result1_0.csv'))







