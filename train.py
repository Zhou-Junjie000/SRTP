import warnings
import numpy as np
import pandas as pd
from data.data import process_data
from model import model
from keras.models import Model

warnings.filterwarnings("ignore")


# 用来训练模型，并保存训练模型结构

def train_model(model, X_train, y_train, name, config):
    """
    :param model:  模型
    :param X_train: 训练数据X
    :param y_train: 训练数据y
    :param name:  模型名
    :param config: 配置参数,包括batch大小,epoch的数目
    :return:
    """
    model.compile(loss="mse", optimizer="rmsprop", metrics=['mape'])
    hist = model.fit(
        X_train, y_train,
        batch_size=config["batch"],
        epochs=config["epochs"],
        validation_split=0.05)

    model.save('model/' + name + '.h5')
    df = pd.DataFrame.from_dict(hist.history)
    df.to_csv('model/' + name + ' loss.csv', encoding='utf-8', index=False)


def train_seas(models, X_train, y_train, name, config):
    temp = X_train

    for i in range(len(models) - 1):
        if i > 0:
            p = models[i - 1]
            hidden_layer_model = Model(inputs=p.input,
                                       outputs=p.get_layer('hidden').output)
            temp = hidden_layer_model.predict(temp)

        m = models[i]
        m.compile(loss="mse", optimizer="rmsprop", metrics=['mape'])

        m.fit(temp, y_train, batch_size=config["batch"],
              epochs=config["epochs"],
              validation_split=0.05)

        models[i] = m

    saes = models[-1]
    for i in range(len(models) - 1):
        weights = models[i].get_layer('hidden').get_weights()
        saes.get_layer('hidden%d' % (i + 1)).set_weights(weights)

    train_model(saes, X_train, y_train, name, config)


def main(args, trainSet, activation):
    lag = 12
    config = {"batch": 256, "epochs": 10}
    trainFile = f'data/{trainSet}'
    testFile = 'data/test.csv'
    X_train, y_train, _, _, _ = process_data(trainFile, testFile, lag)

    if args == 'lstm':
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
        m = model.get_lstm([12, 64, 64, 1], activation)  # 建模
        train_model(m, X_train, y_train, args, config)
    if args == 'gru':
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
        m = model.get_gru([12, 64, 64, 1], activation)  # 建模
        train_model(m, X_train, y_train, args, config)
    if args == 'saes':
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1]))
        m = model.get_saes([12, 400, 400, 400, 1], activation)  # 建模
        train_seas(m, X_train, y_train, args, config)
