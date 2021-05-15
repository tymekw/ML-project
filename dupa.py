
import sys

import tensorflow_hub as hub
from tensorflow.keras.preprocessing import image
import urllib3  # self explanatory
from PIL import Image
import numpy as np
import os
import csv
import cv2
import tensorflow as tf

# img = cv2.imread('your_image.jpg')
# res = cv2.resize(img, dsize=(54, 140), interpolation=cv2.INTER_CUBIC)
#%%

# detector = hub.load("https://tfhub.dev/tensorflow/centernet/resnet50v1_fpn_512x512/1") # WORKS dope
# detector = hub.load("https://tfhub.dev/tensorflow/faster_rcnn/resnet50_v1_1024x1024/1") # ALSO works dope but waaaay slower
detector = hub.load("https://tfhub.dev/tensorflow/ssd_mobilenet_v2/fpnlite_320x320/1") # WORKS FAAST



path="D:\\AGH\\VI semestr\\ML\\datasetGoogle\\OIDv4_ToolKit\\OID\\Dataset\\test\\Baseball glove\\0298c70279b6e842.jpg"
image_ = Image.open(path)
x = image.img_to_array(image_)
x1 = tf.image.resize(x, [3840, 2160], preserve_aspect_ratio=True)
x2 = np.expand_dims(x1, axis=0)
preds = detector(x2)
results = {key:value.numpy() for key,value in preds.items()}
print(results)


#
# def resize_image_keep_aspect(image, lo_dim=LO_DIM):
#   # Take width/height
#   initial_width = tf.shape(image)[0]
#   initial_height = tf.shape(image)[1]
#
#   # Take the greater value, and use it for the ratio
#   min_ = tf.minimum(initial_width, initial_height)
#   ratio = tf.to_float(min_) / tf.constant(lo_dim, dtype=tf.float32)
#
#   new_width = tf.to_int32(tf.to_float(initial_width) / ratio)
#   new_height = tf.to_int32(tf.to_float(initial_height) / ratio)
#
#   return tf.image.resize_images(image, [new_width, new_height])
#

