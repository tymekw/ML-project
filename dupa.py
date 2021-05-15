
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

#%%

def predict(my_image):
    # commented for open_image_from_google
    # my_image = image.smart_resize(my_image, size=(1024, 1024))


    x = image.img_to_array(my_image)
    x = tf.image.resize(my_image, [100, 100], preserve_aspect_ratio=True)
    x = np.expand_dims(x, axis=0)
    preds = detector(x)
    return preds

def predict_single_image(path="D:\\AGH\\VI semestr\\ML\\datasetGoogle\\OIDv4_ToolKit\\OID\\Dataset\\test\\Baseball glove\\0298c70279b6e842.jpg"):
    # image_name = os.path.basename(path).split(".")[0]
    image_ = Image.open(path)
    result = predict(image_)
    results = {key:value.numpy() for key,value in result.items()}
    return results


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


result = predict_single_image()

#1024x648