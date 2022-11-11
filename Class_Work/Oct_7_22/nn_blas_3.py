from numpy import exp, dot


inputLayer = [
        .05,
        .1,
        1
        ]
matrix1 = [
        [.15, .20, .35],
        [.25, .30, .35]
        ]
matrix2 = [
        [.4, .45, .6],
        [.5, .55, .6]
        ]

def sigmoid(x):
    return 1/(1 + exp(-x))

def forwardPass(oLayer:list, iLayer:list, weights:list):
    hiddenLayers = []
    for weightI in weights:
       hInput =  blas3(iLayer, weightI)
       hiddenLayers.append([sigmoid(x) for x in hInput])

    

def blas3(inLayer:list, matrix:list):
    return dot(matrix, inLayer)

