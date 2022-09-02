import train
import predict

trainSetDir = {"通过前3天数据进行预测": 'trainThreeDay.csv', "通过前7天数据进行预测": 'trainSevenDay.csv',
               "通过1个月数据进行预测": 'trainOneMonth.csv',
               "通过前3个月数据进行预测": 'trainThreeMonth.csv', "通过前6个月数据进行预测": 'trainSixMonth.csv',
               "通过前1年数据进行预测": 'trainOneYear.csv'}
trainAlgorithm = {"LSTM": "lstm", "GRU": "gru", "SAEs": "saes"}


def dataFromWeb_train(trainSet, activeFunc, algorithm):
    train.main(trainAlgorithm[algorithm], trainSetDir[trainSet], activeFunc)
    f = open('log.txt', mode="w")
    f.write(trainSetDir[trainSet] + " " + trainAlgorithm[algorithm])
    f.close()


def dataFromWeb_Predict(timeSet, startTime):
    f = open('log.txt', mode="r")
    content = f.read().split(" ")
    transBack = {"lstm": "LSTM", "gru": "GRU", "saes": "SAEs"}
    trainSet = content[0]
    algorithm = transBack[content[1]]
    data = predict.main(trainSet, algorithm, timeSet, startTime)
    return data
