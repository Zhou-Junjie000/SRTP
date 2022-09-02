

# 基于时空知识图谱的交通流量预测系统



## 算法使用

LSTM, GRU, Saes

## 可视化界面

基于flask框架搭建的前端页面

## 运行

在终端命令行输入

```
python app.py
```

将运行所得的路由复制到浏览器即可使用

## 数据来源

PEMS数据集，存放在/data文件夹下，根据不同的时间分为不同的训练集

## 文件分析

app.py：flask前端框架

train.py：训练数据、建模

predict.py：进行预测，绘制流量折线图并且计算误差

connection.py：实现前后端的交互

draw.py：用于模拟、绘制地图