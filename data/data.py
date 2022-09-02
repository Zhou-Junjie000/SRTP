import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler,MinMaxScaler

# 数据预处理：数据的切分，数据的最大最小化
def process_data(train,test,lags):
    """

    :param train: .csv train file
    :param test:  .test test file
    :param lags:  time lag

    return:
        X_train: ndarray.
        y_train: ndarray.
        X_test: ndarray.
        y_test: ndarray.
        scaler: StandardScaler
    """
    #
    # # 导入数据
    # attr = 'Lane 1 Flow (Veh/5 Minutes)'  # 需要预测的属性
    # df1 = pd.read_csv(train,encoding='utf-8').fillna(0)
    # df2 = pd.read_csv(test, encoding='utf-8').fillna(0)
    #
    # # 最大最小化数据
    # scaler = MinMaxScaler(feature_range=(0,1)).fit(df1[attr].values.reshape(-1,1))
    # flow1 = scaler.transform(df1[attr].values.reshape(-1,1)).reshape(-1,1)[0]
    # flow2 = scaler.transform(df2[attr].values.reshape(-1,1)).reshape(1,-1)[0]
    #
    # train,test = [],[]
    # for i in range(lags,len(flow1)):
    #     train.append(flow1[i-lags:i+1])
    #
    # for i in range(lags,len(flow2)):
    #     test.append(flow2[i-lags:i+1])
    #
    # train = np.array(train)
    # test = np.array(test)
    # np.random.shuffle(train)
    #
    # X_train = train[:,:-1]
    # y_train = train[:,-1]
    # X_test = test[:,:-1]
    # y_test = test[:,-1]
    #
    # return X_train,y_train,X_test,y_test,scaler

    attr = 'Flow'
    df1 = pd.read_csv(train, encoding='utf-8').fillna(0)
    df2 = pd.read_csv(test, encoding='utf-8').fillna(0)
    # print(f"df1:{df1}\ndf2:{df2}")

    # scaler = StandardScaler().fit(df1[attr].values)
    scaler = MinMaxScaler(feature_range=(0, 1)).fit(df1[attr].values.reshape(-1, 1))
    flow1 = scaler.transform(df1[attr].values.reshape(-1, 1)).reshape(1, -1)[0]
    flow2 = scaler.transform(df2[attr].values.reshape(-1, 1)).reshape(1, -1)[0]
    # print(f"flow1:{flow1}\tlength:{len(flow1)}\nflow2:{flow2}\tlength:{len(flow2)}")

    train, test = [], []
    for i in range(lags, len(flow1)):
        train.append(flow1[i - lags: i + 1])
    for i in range(lags, len(flow2)):
        test.append(flow2[i - lags: i + 1])

    train = np.array(train)
    test = np.array(test)
    np.random.shuffle(train)

    X_train = train[:, :-1]
    y_train = train[:, -1]
    X_test = test[:, :-1]
    y_test = test[:, -1]

    return X_train, y_train, X_test, y_test, scaler

# process_data('train.csv','test.csv',12)