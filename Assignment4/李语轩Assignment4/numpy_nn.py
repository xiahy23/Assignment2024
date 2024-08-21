### 李语轩 用numpy 实现神经网络的前向传播

import numpy as np

# 线性层
class Linear():

    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.weights = np.zeros((input_size, output_size))
        self.bias = np.zeros(output_size)

    def __call__(self, x):
        return self.forward(x)

    # 前向传播
    def forward(self, x):       
        self.input = x       
        self.output = np.dot(x, self.weights) + self.bias
        return self.output

    # 权重初始化，方法包括随机初始化和xavier初始化
    def init_weights(self, method='random'):
        if method == 'random':
            self.weights = np.random.randn(self.input_size, self.output_size)
            self.bias = np.random.randn(self.output_size)
        elif method == 'xavier':
            self.weights = np.random.randn(self.input_size, self.output_size) / np.sqrt(self.input_size)
            self.bias = np.zeros(self.output_size)
        else:
            raise ValueError(f'Invalid weight initialization method {method}')

# 激活函数
# 1. sigmoid
class Sigmoid():

    def __init__(self):
        pass

    def __call__(self, x):
        return self.forward(x)

    def forward(self, x):
        return 1 / (1 + np.exp(-x))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 2. ReLU
class ReLU():


    def __init__(self):
        pass

    def __call__(self, x):
        return self.forward(x)

    def forward(self, x):
        return np.maximum(0, x)

def relu(x):
    return np.maximum(0, x)

# Feed-Forward Network, 包括一个线性层、一个激活函数和一个线性层。
class FFN():

    def __init__(self, input_size, output_size, hidden_size=32, activation=ReLU(), init_method='xavier'):
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size = hidden_size

        self.linear1 = Linear(input_size, hidden_size)
        self.act = activation
        self.linear2 = Linear(hidden_size, output_size)

        self.init_weights(init_method)

    def __call__(self, x):
        return self.forward(x)
    
    def forward(self, x):
        x = self.linear1(x)
        x = self.act(x)
        x = self.linear2(x)
        return x

    def init_weights(self, method='xavier'):
        self.linear1.init_weights(method)
        self.linear2.init_weights(method)
