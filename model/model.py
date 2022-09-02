# @Time    : 2019/12/15 
# @Author  : LeronQ
# @github  : https://github.com/LeronQ

from keras.layers import Dense, Dropout, Activation
from keras.layers.recurrent import LSTM, GRU
from keras.models import Sequential

# 网络层次配置

def get_lstm(units,activation):
    """
    :param units: units是一个数组,包含输入输出的数据数量,隐藏层数量
    :return: 返回模型
    """
    model = Sequential()
    model.add(LSTM(units[1], input_shape=(units[0], 1), return_sequences=True))
    model.add(LSTM(units[2]))
    model.add(Dropout(0.2))
    model.add(Dense(units[3], activation=activation))

    return model


def get_gru(units,activation):
    """
    :param units: units是一个数组,包含输入输出的数据数量,隐藏层数量
    :return: 返回模型
    """
    model = Sequential()
    model.add(GRU(units[1], input_shape=(units[0], 1), return_sequences=True))
    model.add(GRU(units[2]))
    model.add(Dropout(0.2))
    model.add(Dense(units[3], activation=activation))

    return model

def _get_sae(inputs, hidden, output, activation):
    """
    :param inputs: 输入数量
    :param hidden: 隐层数量
    :param output: 输出层数量
    :return: 返回模型
    """
    model = Sequential()
    model.add(Dense(hidden, input_dim=inputs, name='hidden'))
    model.add(Activation(activation))
    model.add(Dropout(0.2))
    model.add(Dense(output, activation=activation))

    return model


def get_saes(layers,activation):
    """
    :param layers: 输入输出数据数量,隐层数量
    :return:  返回模型
    """
    sae1 = _get_sae(layers[0], layers[1], layers[-1], activation)
    sae2 = _get_sae(layers[1], layers[2], layers[-1], activation)
    sae3 = _get_sae(layers[2], layers[3], layers[-1], activation)

    saes = Sequential()
    saes.add(Dense(layers[1], input_dim=layers[0], name='hidden1'))
    saes.add(Activation(activation))
    saes.add(Dense(layers[2], name='hidden2'))
    saes.add(Activation(activation))
    saes.add(Dense(layers[3], name='hidden3'))
    saes.add(Activation(activation))
    saes.add(Dropout(0.2))
    saes.add(Dense(layers[4], activation=activation))

    models = [sae1, sae2, sae3, saes]

    return models