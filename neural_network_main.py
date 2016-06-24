
# coding: utf-8

# In[4]:

import numpy as np


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
    


# ## Activation Function
# - Defines the output of a node given inputs.
# - In the biological sense, the activation function is a way to represent the rate of action potential firing in a call.
# - In the most simple form, the activation function is binary (either the node/cell is firing or not).
# - The activation function can be any type of function as long as the function:
#     - is motonically increasing/decreasing
#     - is continuously differentiable (for backpropagation)
#     - is smooth; has a monotonic derivative
#     - is preferably not linear (for qucker and more stable convergence)
#     - has $f(x) \approx x$ when $x \approx 0$ characteristic (so that training is more efficient after the weights have been initialized w/ small random values)

# ### Sigmoid Function
# Sigmoid function is any mathematical function having an "S" shape. These "S" shapes functions meet the aforementioned requirements.
# 
# #### Logistic Function
# Most popular sigmoid function. The function was named when studying population growth--the initial stage of growth is approx exponential and then, as saturation begins, the growth slows and, at maturity (at/near $+\infty$), growth stops.
# 
# Function given by:
# \begin{align}
# f(x) = \dfrac{L}{1+e^{-k(x-x_0)}}
# \end{align}
# Where $L$ is the curve's maximum value, $x_0$ is the curve's midpoint in the x-axis and $k$ is the curve's steepness.
# 
# For our purposes, we want the the maximum value to be 1. We also want the midpoint to be 0, so that way, if the input is positive, then the output will tend to 1 and, if the input is negative, the output will tend to 0. The steepness $k$ of the function helps with how quickly and well the network converges.
# 
# Therefore, our function becomes:
# \begin{align}
# f(x) = \dfrac{1}{1+e^{-k(x)}}
# \end{align}
# 
# The logistic function's derivative is:
# \begin{align}
# f'(x) = \dfrac{ke^{-kx}}{1+e^{-k(x)}}
# \end{align}
# 
# Or written differently:
# \begin{align}
# f'(x) = \dfrac{1}{1+e^{-k(x)}}(1 - \dfrac{1}{1+e^{-k(x)}})
# \end{align}
# or:
# \begin{align}
# f'(x) = f(x)(1 - f(x))
# \end{align}

# In[5]:

def logistic(z, k=1.0):
    return 1/(1 + np.exp(-k*z))


# In[ ]:



