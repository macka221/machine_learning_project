from numpy import exp

def softmax(x):
  """
  This function is used to represent the softmax function in machine learning.
      :param x: the variable x in the softma function
  :return: the result of the softmax function.
  """
  return exp(x)/exp(x).sum()


inputs = [1.0, 5.0, 2.0]
outputs = softmax(inputs)

print(f"Softmaxes: {outputs}")
print(f"Softmax sum: {outputs.sum()}")
