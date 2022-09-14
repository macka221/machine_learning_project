from matplotlib import pyplot

# Rectified linear function

def rectified(x):
    return max(0.0, x)

# Define input data
inputs = [x for x in range(-10, 10)]

# Calculate Inputs
outputs = [rectified(x) for x in inputs]
pyplot.plot(inputs, outputs)
pyplot.show()