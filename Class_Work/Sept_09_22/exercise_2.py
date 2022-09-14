from numpy import exp

def softmax(x):
    return exp(x)/exp(x).sum()

inputs = [1.0, 3.0, 2.0]
outputs = softmax(inputs)

print(f"Outputs: {outputs}")
print(f"Outputs sum: {outputs.sum()}")