import tensorflow as tf
# from tensorflow.contrib import learn
from tensorflow.contrib.layers import convolution2d
from tensorflow.contrib.framework.python.ops import variables
from tensorflow.contrib.layers.python.layers import utils
from tensorflow.contrib.layers.python.layers import initializers

# method 1: contirb API
net = convolution2d(net,
                    num_outputs=num_ker,
                    kernel_size=[ker_size,1],
                    stride=[stride,1]
                    padding='SAME',
                    activation_fn=None,
                    normalizer_fn=None,
                    weights_initializer=initializers.variance_scaling_initializer(),
                    biases_initializer=init_ops.zeros_initializer,)

# method 2: original conv2d API
weights = variables.model_variable(
    'weights',
    shape=[ker_size, 1, num_ker_in, num_ker],
    dtype=dtype,
    initializer=initializers.variance_scaling_initializer(),
    trainable=True)
biases = variables.model_variable(
    'biases',
    shape=[num_ker],
    dtype=dtype,
    initializer=tf.zeros_initializer,
    trainable=True)
net = tf.nn.conv2d(net, weights, [1, stride, 1, 1], padding='SAME')
net = tf.nn.bias_add(net, biases)
