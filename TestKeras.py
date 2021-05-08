from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import pathlib
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds

def predict(my_image):
    # img = image.load_img(img_path, target_size=(224, 224))
    my_image = image.smart_resize(my_image, size=(224, 224))
    x = image.img_to_array(my_image)
    x = np.expand_dims(x, axis=0)
    # x = preprocess_input(x)

    preds = model.predict(x)
    print('Predicted:', decode_predictions(preds, top=3)[0])


model = ResNet50(weights='imagenet')

(train_ds, val_ds, test_ds), metadata = tfds.load(
    'tf_flowers',
    split=['train[:80%]', 'train[80%:90%]', 'train[90%:]'],
    with_info=True,
    as_supervised=True,
)

num_classes = metadata.features['label'].num_classes

for i in range(0,10):
    image1, label1 = next(iter(train_ds))
    predict(image1)