import math
import random
import matplotlib.pyplot as plt
import numpy as np

# Constants
LEARNING_RATE = 1

# Activation functions
def logistic(x):
    return 1 / (1 + math.exp(-x))

def logistic_derivative(x):
    return x * (1 - x)

# Neuron classes
class InputNeuron:
    def __init__(self, activation=1):
        self.activation = activation
        self.delta = 0

class Neuron:
    def __init__(self, previous_layer):
        self.activation = None
        self.delta = 0
        self.previous_layer = [InputNeuron()] + previous_layer  # Add bias node
        self.weights = [random.gauss(0, 1) for _ in self.previous_layer]

    def update_activation(self):
        s = sum(self.weights[i] * self.previous_layer[i].activation for i in range(len(self.previous_layer)))
        self.activation = logistic(s)

    def update_weights(self):
        for j in range(len(self.previous_layer)):
            self.weights[j] += -LEARNING_RATE * self.previous_layer[j].activation * self.delta

class OutputNeuron(Neuron):
    def update_delta(self, target):
        a = self.activation
        self.delta = logistic_derivative(a) * (a - target)
        for unit, weight in zip(self.previous_layer[1:], self.weights[1:]):
            unit.delta += weight * self.delta

class HiddenNeuron(Neuron):
    def update_delta(self):
        self.delta *= logistic_derivative(self.activation)

class Network:
    def __init__(self, sizes):
        self.layers = [None] * len(sizes)
        self.layers[0] = [InputNeuron() for _ in range(sizes[0])]
        for i in range(1, len(sizes) - 1):
            self.layers[i] = [HiddenNeuron(self.layers[i - 1]) for _ in range(sizes[i])]
        self.layers[-1] = [OutputNeuron(self.layers[-2]) for _ in range(sizes[-1])]
        self.errors = []

    def predict(self, inputs):
        for i, value in enumerate(inputs):
            self.layers[0][i].activation = value
        for layer in self.layers[1:]:
            for neuron in layer:
                neuron.update_activation()
        return [neuron.activation for neuron in self.layers[-1]]

    def reset_deltas(self):
        for layer in self.layers[1:]:
            for neuron in layer:
                neuron.delta = 0

    def update_deltas(self, targets):
        for neuron, target in zip(self.layers[-1], targets):
            neuron.update_delta(target)
        for layer in reversed(self.layers[1:-1]):
            for neuron in layer:
                neuron.update_delta()

    def update_weights(self):
        for layer in self.layers[1:]:
            for neuron in layer:
                neuron.update_weights()

    def train(self, inputs, targets):
        predictions = self.predict(inputs)
        self.reset_deltas()
        self.update_deltas(targets)
        self.update_weights()
        self.errors.append(np.mean([(t - p) ** 2 for t, p in zip(targets, predictions)]))

    def plot_errors(self):
        plt.plot(self.errors)
        plt.xlabel("Training Steps")
        plt.ylabel("Mean Squared Error")
        plt.title("Training Error over Time")
        plt.show()

    def visualize_xor_training(self, iterations=1000):
        inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
        targets = [[0], [1], [1], [0]]
        predictions = {tuple(inp): [] for inp in inputs}

        for _ in range(iterations):
            for i, t in zip(inputs, targets):
                self.train(i, t)
                predictions[tuple(i)].append(self.predict(i)[0])

        for key, values in predictions.items():
            plt.plot(values, label=f"Input {key}")
        plt.xlabel("Training Steps")
        plt.ylabel("Predicted Output")
        plt.title("XOR Learning Progress")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    net = Network([2, 2, 1])
    net.visualize_xor_training()