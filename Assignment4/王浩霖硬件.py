import numpy as np
def create_weight(inputs,nerons):
    return np.random.rand(inputs,nerons)
def create_bias(nerons):
    return np.random.rand(1,nerons)
def activation(x):
    return 1/(1+np.exp(-x))
class Layer:
    def __init__(self,inputs,nerons):
        self.weights = create_weight(inputs,nerons)
        self.bias = create_bias(nerons)
    def pass_forward(self,inputs):
        self.output = activation(np.dot(inputs,self.weights)+self.bias)
        return self.output
# Layer1=Layer(2,3);
# Layer1.pass_foward(np.array([[1,2]]));
# print(Layer1.weights);
# print(Layer1.bias);
# print(Layer1.pass_foward(np.array([[1,2]])));
# print(Layer1.output)
#定义一个网络类
class NetWork:
    #初始化网络
    def __init__(self,NetShape):
        self.layers = [];
        self.shape = NetShape;
        for i in range(len(NetShape)-1):
            layer = Layer(NetShape[i],NetShape[i+1])
            self.layers.append(layer)
    #前向传播
    def pass_forward(self,inputs):
        self.outputs=[inputs]
        for layer in self.layers:
            inputs = layer.pass_forward(inputs)
            self.outputs.append(inputs)
        return self.outputs
#测试网络
def main():
    NetShape = [2,3,1]
    inputs = np.array([[1,2],[1,3]])
    net = NetWork(NetShape)
    outputs = net.pass_forward(inputs)
    print(outputs)
main()