import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve, confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns


# 读取训练集
train_X = np.load('./data/train/train_minist.npy')  # 数字矩阵
train_label = pd.read_csv('./data/train/train_label.csv')
train_number = train_label['number']  # 数字标签
train_size = train_label['size']  # 粗细标签
# 读取测试集
test_X = np.load('./data/test/test_minist.npy')
test_label = pd.read_csv('./data/test/test_label.csv')
test_number = test_label['number']
test_size = test_label['size']
# 查看数据集规模
print(f"训练集的尺度是：{train_X.shape}, 标签的尺度是：{test_label.shape}")
# ----------------------------->第一题（必做）
# TODO 1:使用Logistic回归拟合训练集的X数据和size标签,并对测试集进行预测

import numpy as np

class LogisticRegression:
    def __init__(self, lr=0.01, num_iter=100000, fit_intercept=True, verbose=False):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose
    
    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)
    
    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def __loss(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()
    
    def fit(self, X, y):
        if self.fit_intercept:
            X = self.__add_intercept(X)
        
        self.theta = np.zeros(X.shape[1])
        
        for i in range(self.num_iter):
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            gradient = np.dot(X.T, (h - y)) / y.size
            self.theta -= self.lr * gradient
            
            if(self.verbose == True and i % 10000 == 0):
                z = np.dot(X, self.theta)
                h = self.__sigmoid(z)
                print(f'loss: {self.__loss(h, y)} \t')
    
    def predict_prob(self, X):
        if self.fit_intercept:
            X = self.__add_intercept(X)
    
        return self.__sigmoid(np.dot(X, self.theta))
    
    def predict(self, X, threshold):
        return self.predict_prob(X) >= threshold
# 划分训练集和测试集
# 创建并训练模型

# model = LogisticRegression(lr=0.00001, num_iter=2000)
# train_X_flattened = train_X.reshape(train_X.shape[0], -1)
# model.fit(train_X_flattened, train_size)


# # 预测测试集
# test_X_flattened = test_X.reshape(test_X.shape[0], -1)

# predictions = model.predict(test_X_flattened, 0.5)

# # 计算正确率
# accuracy = accuracy_score(test_size, predictions)
# precision = precision_score(test_size, predictions)
# recall = recall_score(test_size, predictions)
# f1 = f1_score(test_size, predictions)
# auc = roc_auc_score(test_size, predictions)

# print(f'Accuracy: {accuracy * 100}%')
# print(f'Precision: {precision * 100}%')
# print(f'Recall: {recall * 100}%')
# print(f'F1 Score: {f1 * 100}%')
# print(f'auROC: {auc * 100}%')

# # 绘制ROC曲线
# fpr, tpr, _ = roc_curve(test_size, predictions)
# plt.plot(fpr, tpr)
# plt.title('ROC curve')
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.show()
#
#
#
#
#
#
#
# ---------------------------->第二题（必做）
# TODO 2:使用Softmax回归拟合训练集的X数据和number标签,并对测试集进行预测
import numpy as np

class SoftmaxRegression:
    def __init__(self, learning_rate=0.00001, epochs=70):
        self.learning_rate = learning_rate
        self.epochs = epochs

    def softmax(self, z):
        e_z = np.exp(z - np.max(z, axis=1, keepdims=True))
        return e_z / np.sum(e_z, axis=1, keepdims=True)

    def fit(self, X, y):
        self.classes = np.unique(y)
        y = self.one_hot(y)

        self.weights = np.zeros((X.shape[1], len(self.classes)))

        for _ in range(self.epochs):
            linear = np.dot(X, self.weights)
            y_pred = self.softmax(linear)

            gradient = np.dot(X.T, (y_pred - y)) / y.shape[0]
            self.weights -= self.learning_rate * gradient

    def predict(self, X):
        linear = np.dot(X, self.weights)
        y_pred = np.argmax(self.softmax(linear), axis=1)
        return self.classes[y_pred]

    def one_hot(self, y):
        one_hot = np.zeros((y.shape[0], len(self.classes)))
        for i, c in enumerate(self.classes):
            one_hot[y == c, i] = 1
        return one_hot
    
    def predict_prob(self, X):
        linear = np.dot(X, self.weights)
        return self.softmax(linear)
    
model = SoftmaxRegression()

# 将训练数据展平为二维数组
train_X_flattened = train_X.reshape(train_X.shape[0], -1)

model.fit(train_X_flattened, train_number)

# 预测测试集
# 需要将测试数据也展平为二维数组
test_X_flattened = test_X.reshape(test_X.shape[0], -1)

predictions = model.predict(test_X_flattened)

# 计算指标
accuracy = accuracy_score(test_number, predictions)
precision = precision_score(test_number, predictions, average='micro')
recall = recall_score(test_number, predictions, average='micro')
f1 = f1_score(test_number, predictions, average='micro')

print(f'Accuracy: {accuracy * 100}%')
print(f'Precision: {precision * 100}%')
print(f'Recall: {recall * 100}%')
print(f'F1 Score: {f1 * 100}%')

from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelBinarizer
# 获取每个样本属于每个类别的概率
y_score = model.predict_prob(test_X_flattened)

# 将真实标签转换为二进制形式
lb = LabelBinarizer()
lb.fit(test_number)
y_test = lb.transform(test_number)

# 计算AUC
auc = roc_auc_score(y_test, y_score, multi_class='ovr')

print(f'auROC: {auc * 100}%')
#
# 计算混淆矩阵
cm = confusion_matrix(test_number, predictions)

# 绘制混淆矩阵
plt.matshow(cm, cmap=plt.cm.Greens) 
plt.colorbar()
for i in range(len(cm)): 
    for j in range(len(cm)):
        plt.annotate(cm[i,j], xy=(i, j), horizontalalignment='center', verticalalignment='center')
plt.ylabel('True label')
plt.xlabel('Predicted label') 
plt.show()

#
#
#
#
#

