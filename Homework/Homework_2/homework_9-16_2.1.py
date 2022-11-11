from matplotlib import pyplot
from numpy import exp

def sigmoid_function(x):
  """
  This function is used to represent the sigmoid function in machine learning.
      :param x: the variable in the sigmoid equation
  :return: the evaluation of the sigmoid function
  """
  return 1 / (1 + exp(-x))


def hyperbolic_tangent_function(x):
  """
  This function represents the hyperbolic tangent function in mathematics. It
  is used as a hidden function in machine learning.
      :param x: the variable in the hyperbolic tangent function
  :return: the evaluation of the hyperbolic tangent function
  """
  return (exp(x) - exp(-x)) / (exp(x) + exp(-x))


inputs = [x for x in range(-10, 10)]
sigmoid_outputs = [sigmoid_function(x) for x in inputs]
h_tan_outputs = [hyperbolic_tangent_function(x) for x in inputs]

print("This is the sigmoid graph")
pyplot.plot(inputs, sigmoid_outputs)
pyplot.show()
input()
print("This is the htan graph")
pyplot.plot(inputs, h_tan_outputs)
pyplot.show()

