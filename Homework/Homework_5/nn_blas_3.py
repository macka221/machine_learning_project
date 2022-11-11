from numpy import exp, dot


inputLayer = [
        .05,
        .1,
        1
        ]
matrix1 = [
        [.15, .20],
        [.25, .30]
    ]
matrix2 = [
        [.4, .45],
        [.5, .55]
    ]

outputLayer = [
        .01,
        .99
    ]

biases = [.35, .6]


# ===========================================================================
# Homework Question 1:
# ===========================================================================

def sigmoid(x):
    return 1/(1 + exp(-x))


def addBias(cLayer:list, biases:list, index:int):
    for layer in cLayer:
        layer.append(biases[index])

def blas3(inLayer: list, matrix:list):
    return dot(matrix, inLayer)


def forwardPass(iLayer:list, weights:list, biases:list):
    index = 0
    hiddenLayerInput = hOutput = None
    for weight in weights:
        addBias(cLayer=weight, biases=biases, index=index) # Adds the bias to the matrix of weights
        hiddenLayerInput = blas3(inLayer=hOutput, matrix=weight) if hOutput else blas3(inLayer=iLayer, matrix=weight) # Performs the blas 3 operations.
        hOutput = [sigmoid(x) for x in hiddenLayerInput] # Produces the input for the next layer
        hOutput.append(1)
        index += 1
    return hOutput

def calculateOutput(oLayer:list, iLayer:list, weights:list):
    pass


#print(blas3(inLayer=inputLayer, matrix=matrix1))
weights = [matrix1, matrix2]

print("Question 1:\nForward Pass of the neural network produces the following: ", end='')
print(forwardPass(iLayer=inputLayer, weights=weights, biases=biases)[:-1])

# ================================================================================
# Homework Question 2:
# ================================================================================
# TODO: Write a program to use Matrix Multiplication to back propogate.


# ================================================================================
# Homework Question 3:
# ================================================================================
# TODO: Design a 2, 2, 2 neural network that outputs the logical AND


