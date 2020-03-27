import lightgbm as lgb
import numpy as np
import pandas as pd
import joblib

#从feature_4文件夹里面合成训练数据集train_data
feature_B = pd.read_csv('./feature_4/feature_B.csv')        #此路径为feature_B.csv文件所在路径
feature_IR = pd.read_csv('./feature_4/feature_IR.csv')      #同上
feature_NORMAL = pd.read_csv('./feature_4/feature_NORMAL.csv')  #同上
feature_OR = pd.read_csv('./feature_4/feature_OR.csv')          #同上
frames = [feature_B,feature_IR,feature_NORMAL,feature_OR]

train_data = pd.concat(frames)             

def train():
    # 模型初始化，设置random_state保证可复现性，便于观察优化
    #train_data = pd.read_csv('F:/qimo/feature/feature_B.csv')     #4合1变成train_data
    train_data_y = train_data['label']
    # 除去标签的所有列就是特征
    train_data_x = train_data.drop(['label'], axis=1)
    model_lgb_default = lgb.LGBMClassifier(random_state=2019)
    # 模型训练
    model_lgb_default.fit(train_data_x, train_data_y)
    joblib.dump(model_lgb_default, 'F:/qimo/model/lightgbm_model.model')   #此路径为模型保存的路径

# 这里首先定义judge函数，以threhold为阈值，根据模型给出的分类概率进行判断，大于
# threhold为正常样本，反之为故障征兆样
def judge(input_pred, threshold):
    return_pred = list(np.zeros(len(input_pred)))
    for i in range(0, len(input_pred)):
        if (input_pred[i][0] > threshold):
            return_pred[i] = 0
        else:
            return_pred[i] = 1
    return return_pred


def test_lightgbm():
    # 加载模型
    model = joblib.load('F:/qimo/model/lightgbm.model')             
    # 读取测试集,来源的特征文件同样经过特征提取和选择，只是不加标签，'label'列中表示
    # 其机组和数据组的信息，例如'M11_1'，方便我们统计各数据组的分类概率统计值进行排序
    test_m11 = pd.read_csv('F:/qimo/feature/feature_B.csv')          
    
    """ 
    test_m12 = pd.read_csv('F:/qimo/feature/feature_IR.csv')
    test_m13 = pd.read_csv('F:/qimo/feature/feature_NORMAL.csv')
    test_m14 = pd.read_csv('F:/qimo/feature/feature_OR.csv')
    
    test_m15 = pd.read_csv('F:/zhuanzi/featureset/test15_selected.csv')
    test_m16 = pd.read_csv('F:/zhuanzi/featureset/test16_selected.csv')
    test_m17 = pd.read_csv('F:/zhuanzi/featureset/test17_selected.csv')
    test_m18 = pd.read_csv('F:/zhuanzi/featureset/test18_selected.csv')
    # 对8个测试集循环进行测试
   
    h = 11
    #！for test_i in [test_m11, test_m12, test_m13, test_m14]:
        test_name = 'test_m' + str(h)
        print('The result of test is:')
        print('filename  datagroup  normal  fault  fault-probability-of-datagroup')
        #max_j = {}
        #！for j in range(1, 6):
         #！   labelname = 'M' + str(h) + '_' + str(j)
            labelname='B'
            test_j = test_i[test_i['label'] == labelname]
            test_feature = test_j.drop(['label'], axis=1)
            y_pred = model.predict_proba(test_feature)
            y_pred_binary = judge(y_pred, 0.5)
            y_pred_mean = np.mean([x[1] for x in y_pred])
            max_j[j] = y_pred_mean
            print(test_name, j, y_pred_binary.count(0), y_pred_binary.count(1),
                  y_pred_mean)
        h = h + 1
        print("The order a-e is:")
        for k in sorted(max_j, key=max_j.__getitem__, reverse=True):
            print(k, max_j[k])
"""
    print('The result of test is:')
    #print('filename  datagroup  normal  fault  fault-probability-of-datagroup')
    labelname = 'B'
    i=11
    test_j = test_m11[test_m11['label'] == labelname]
    test_feature = test_j.drop(['label'], axis=1)
    y_pred = model.predict_proba(test_feature)
    y_pred_binary = judge(y_pred, 0.5)
    y_pred_mean = np.mean([x[1] for x in y_pred])
    print( y_pred_binary.count(0), y_pred_binary.count(1),
          y_pred_mean)




train()
test_lightgbm()
