import numpy as np

# 选择Sigmoid函数为激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 初始化权重
def initialize_weights(input_size, hidden_size, output_size):
    np.random.seed(42)  # 设置随机种子以保证结果可重复
    W1 = np.random.randn(input_size, hidden_size) * 0.01
    W2 = np.random.randn(hidden_size, output_size) * 0.01
    return W1, W2

#定义神经网络类
class NetWork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
    
    # 前向传播
    def forward(self, X):
        self.input = X
        W1, W2 = initialize_weights(self.input_size, self.hidden_size, self.output_size)
        Z =  sigmoid(np.dot(X, W1))      
        self.output = sigmoid(np.dot(Z, W2))
        return self.output

#实例化对象
N1 = NetWork(3, 4, 2)

# 示例数据
X = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 1], [1, 1, 0]])
Y = N1.forward(X)

print(X) # [[0 0 1][0 1 0][1 0 1][1 1 0]]
print(Y) # [[0.49574436 0.49554][0.49573316 0.49553304][0.49573386 0.49552237][0.49572266 0.49551542]]
