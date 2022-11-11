import tensorflow as tf
import numpy as np


nn_input = tf.constant([
    [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]],
    [[0,0,0], [2,2,0], [2,2,0], [2,0,1], [2,2,2], [0,1,2], [0,1,2]],
    [[0,0,0], [0,1,0], [2,2,1], [1,2,0], [1,2,1], [2,1,1], [0,0,0]],
    [[0,0,0], [2,2,0], [2,2,0], [2,2,1], [1,1,0], [0,0,1], [0,0,0]],
    [[0,0,0], [2,1,2], [2,2,2], [1,2,0], [1,0,1], [1,1,2], [0,0,0]],
    [[0,0,0], [2,0,0], [1,0,1], [2,1,1], [2,1,0], [1,1,2], [0,0,0]],
    [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0] ]],
    shape=[1,7,7,3], dtype=tf.float32)

print("Dimension of input = ", nn_input.shape)
nn_filter = tf.constant([[
    [[1, -1], [0, 0], [0, 1]],
    [[0,-1], [1,-1], [0,-1]],
    [[-1,-1], [1,0], [0,-1]]],
    [[[-1,-1], [1,-1], [0,-1]],
     [[1,0], [-1,1], [0,-1]],
     [[-1,1], [-1,1], [1,1]]],
    [[[0,-1], [0,-1], [1,1]],
     [[1,1], [1,0], [0,0]],
     [[0,-1], [0,1], [0,1]]]],
    shape=[3,3,3,2], dtype=tf.float32)

print("Dimension of Filter = ", nn_filter.shape)
bias = tf.constant([1,0], shape=[2], dtype=tf.float32)

# Question 1.A
print("The output values after the convolution step are: ")
# 
qa = tf.nn.conv2d(nn_input, nn_filter, strides=[1,2,2,1], padding='VALID') + bias
print("Dimension of qa = ", qa.shape)

# Question 1.B
qb = tf.nn.relu(qa)
print("Dimension of qb = ", qb.shape)
print(qb.numpy())

# Question 1.C
print("The output values after the max pooling operation are: ")
qc = tf.nn.max_pool(qb, [1,2,2,1], [1,1,1,1], padding='VALID')
print("Dimension of qc = ", qc.shape)
print(qc.numpy())

# Question 1.D
print("The values of the vector after it is flattened based on the row major counting system are: ")
qd = tf.reshape(tf.constant([[[9,9], [9,9]], [[7,1], [6,0]]]), [-1,8])
print("Dimension of qd = ", qd.shape)
print(qd.numpy())

# Question 1.E
print("The total number of trainable parameters is: ")
params = 3*3*3*2 + 2 + 0 + 8*8 + 8 + 8*2 + 2
print(params)


# Question 2: Softmax Output
flat_float = tf.constant([9, 9, 9, 9, 7, 1, 6, 0], dtype=tf.float32)
output = tf.nn.softmax(flat_float)
print("The outputs of the softmax function are: ")
print("Dimension of output = ", output.shape)
print(output.numpy())


