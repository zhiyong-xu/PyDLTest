#测试第一个TensorFlow
import tensorflow as tf
print('TensorFlow版本：',tf.__version__)
hello = tf.constant('Hello World!')
sess = tf.Session()
print(sess.run(hello))