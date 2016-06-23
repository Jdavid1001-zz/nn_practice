
# coding: utf-8

# # Neural Network Practice
# ** objectives: **
# 1. Create my own neural network implementation
# 1. Explain the math behind each aspect of neural network
# 1. Use clean code (esp dependency ejection) practices
# 
# \* Using Welch Lab's Youtube video series: Neural Networks Demystified as reference

# ## Neural Network Implementation
# ### Multilayer Perceptron
# The our current implementation of neural network will be a multilayer perceptron model. Here, we will have multiple perceptrons connected that pass information between forward to each other.

# In[2]:

class Neural_Network():
    def __init__(self, layers=[2, 1, 3]):
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3
    def forward(self, X):
        #Propagate inputs through network
        pass
    

