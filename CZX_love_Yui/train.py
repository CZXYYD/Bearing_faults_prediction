import lightgbm as lgb
import numpy as np
import pandas as pd
import os
from sklearn.externals import joblib

#从feature_4文件夹里面合成训练数据集train_data
feature_B = pd.read_csv('./feature_4/feature_B.csv')
feature_IR = pd.read_csv('./feature_4/feature_IR.csv')
feature_NORMAL = pd.read_csv('./feature_4/feature_NORMAL.csv')
feature_OR = pd.read_csv('./feature_4/feature_OR.csv')
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
    joblib.dump(model_lgb_default, './model/lightgbm.model')


train()

