from flask import Flask, render_template, request
import connection
import time

app = Flask(__name__)
app.config["SECRET_KEY"] = '123456'


@app.route('/')
def homePage():
    return render_template('HomePage.html')


@app.route('/predictTrainPage', methods=['GET', 'POST'])
def predictTrainPage():
    if request.method == 'POST':
        value = request.form.to_dict()

        trainSet = value["select4"]
        activationFun = value["select3"]
        algorithm = value["select2"]
        startTime = time.time()
        connection.dataFromWeb_train(trainSet, activationFun, algorithm)
        endTime = time.time()

        return render_template('trainDone.html',
                               trainSet=trainSet,
                               algorithm=algorithm,
                               activationFun=activationFun,
                               time=round((endTime - startTime), 2))

    return render_template('PredictTrain.html')


@app.route('/predictPage', methods=['GET', 'POST'])
def predictPage():
    if request.method == 'POST':
        value = request.form.to_dict()

        timeSet = value["select5"]
        position = value["select1"]
        startTime = time.time()
        imagePath = f"resultImage/{startTime}.png"
        data = connection.dataFromWeb_Predict(timeSet, startTime)

        return render_template('predictDone.html',
                               timeSet=timeSet,
                               position=position,
                               data=int(data),
                               imagePath=imagePath)
    return render_template('PredictUse.html')


@app.route('/knowledgeMap')
def knowledgeMap():
    return render_template('knowledgeMap.html')


if __name__ == '__main__':
    app.run(debug=True)
