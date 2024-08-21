import numpy as np

class NeuralNetwork:
    def __init__(self, layers):
        """
        初始化神经网络
        :param layers: 一个列表，表示每层的神经元数量
        """
        self.layers = layers
        self.weights = []
        self.biases = []
        # 初始化权重和偏置
        for i in range(len(layers) - 1):
            weight = self.create_weight(layers[i], layers[i + 1])
            bias = self.create_bias(layers[i + 1])
            self.weights.append(weight)
            self.biases.append(bias)

    def create_weight(self, inputs, outputs):
        '''
        创建权重
        :param inputs: 输入神经元数量
        :param nerons: 输出神经元数量
        '''
        return np.random.rand(inputs, outputs)
    
    def create_bias(self, nerons):
        '''
        创建偏置
        :param nerons: 神经元数量
        '''
        return np.random.rand(1, nerons)
        
    def sigmoid(self, x):
        """
        Sigmoid 激活函数
        :param x: 输入数据
        """
        return 1 / (1 + np.exp(-x))
    
    def forward(self, x):
        """
        向前传播
        :param x: 输入数据
        :return: 输出结果
        """
        a = x
        for i in range(len(self.weights)):
            z = np.dot(a, self.weights[i]) + self.biases[i]
            a = self.sigmoid(z)
        return a

# 示例使用
if __name__ == "__main__":
    # 定义一个 3 层神经网络，输入层 2 个神经元，隐藏层 3 个神经元，输出层 1 个神经元
    nn = NeuralNetwork([2, 3, 1])
    # 输入数据
    x = np.array([[0.5, 0.1]])
    # 执行向前传播
    output = nn.forward(x)
    print("输出结果:", output.reshape(-1))