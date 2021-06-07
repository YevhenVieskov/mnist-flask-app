
"""
module classifier.py
"""

import tensorflow as tf
import numpy as np
from tensorflow import keras

global model,graph

model_json = open('model/model.json','r').read()
model = keras.models.model_from_json(model_json)
model.load_weights('model/model.h5')
#model = keras.models.load_model('model.h5')
#graph = tf.compat.v1.get_default_graph()  #tf.get_default_graph()

def classify(x):
   # with graph.as_default():
   #     y = model.predict(x.reshape((1,28,28,1))).reshape((10,))
   #     n = int(np.argmax(y,axis=0))
   #     y = [float(i) for i in y]
   #     return (y,n)
  
    y = model.predict(x.reshape((1,28,28,1))).reshape((10,))
    n = int(np.argmax(y, axis=0))
    y = [float(i) for i in y]

    #return jsonify({'result':y, 'digit':n})
    return (y,n)

   