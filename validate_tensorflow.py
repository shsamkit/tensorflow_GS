import tensorflow as tf
hello = tf.constant('Hello, tensorflow!')
session = tf.Session()
print(session.run(hello))
