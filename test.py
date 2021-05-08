import tensorflow_datasets as tfds
import tensorflow_hub as hub
from tensorflow.keras.preprocessing import image
import numpy as np
import urllib3  # the lib that handles the url stuff
import ast
import matplotlib.pyplot as plt
import numpy as np

train_ds, metadata = tfds.load(
    'imagenet_v2',
    split='test',
    with_info=True,
    as_supervised=True
)

detector = hub.load("https://tfhub.dev/tensorflow/centernet/resnet50v1_fpn_512x512/1")

def predict(my_image):
    my_image = image.smart_resize(my_image, size=(1024, 1024))
    x = image.img_to_array(my_image)
    x = np.expand_dims(x, axis=0)
    preds = detector(x)
    return preds, my_image

http = urllib3.PoolManager()
r = http.request('GET', 'https://raw.githubusercontent.com/amikelive/coco-labels/master/coco-labels-paper.txt')
dane = r.data.decode('UTF-8')
my_data = dane.split('\n')

coco = {i+1: my_data[i] for i in range(0,len(my_data))}
print(coco)

http = urllib3.PoolManager()
r = http.request('GET', 'https://gist.githubusercontent.com/maraoz/388eddec39d60c6d52d4/raw/791d5b370e4e31a4e9058d49005be4888ca98472/gistfile1.txt')
dane = r.data.decode('UTF-8')

imagenet = ast.literal_eval(dane)
print(imagenet)

iterator = iter(train_ds)
for i in range(0,10):
    image1, label1 = next(iterator)
    result, x = predict(image1)
    plt.figure()
    plt.imshow(image1)
    plt.show()
    print("is: " + imagenet[label1.numpy()])

    results = {key:value.numpy() for key,value in result.items()}
    detection_classes = result['detection_classes']
    print("model thinks: " + coco[detection_classes[0][0].numpy()])