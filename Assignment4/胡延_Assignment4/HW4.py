import numpy as np

class NeuralNetwork:
    def __init__(self, layer_sizes):
        """
        初始化神经网络
        :param layer_sizes: 一个列表，表示每层的神经元数量
        """
        self.layer_sizes = layer_sizes
        self.weights = [np.random.randn(y, x) for x, y in zip(layer_sizes[:-1], layer_sizes[1:])]
        self.biases = [np.random.randn(y, 1) for y in layer_sizes[1:]]

    def sigmoid(self, z):
        # Sigmoid函数，用tanh函数或RELU亦可
        return 1 / (1 + np.exp(-z))

    def forward(self, input):
        """
        前向传播
        :param input: 输入向量
        :return:  输出向量
        """
        for b, w in zip(self.biases, self.weights):
            input = self.sigmoid(np.dot(w, input) + b)
        return input

if __name__ == "__main__":

    # 通过控制台输入神经网络的结构(各层神经元数量)
    x = int(input("Please input the number of neurons in the input layer: "))
    y = int(input("Please input the number of neurons in the hidden layer: "))
    z = int(input("Please input the number of neurons in the output layer: "))

    # x, y, z = 2, 3, 1   # 输入层2个神经元，隐藏层3个神经元，输出层1个神经元

    # 创建神经网络
    nn = NeuralNetwork([x, y, z])

    # 输入向量
    print(f"Please input the vector of the input layer with {x} neurons: ")
    input_vector = []
    for i in range(x):
        input_vector.append(float(input()))
    # input_vector = np.array([[0.5], [0.5]])
        
    # 前向传播
    output = nn.forward(input_vector)
    
    print("Output of the neural network:", output)