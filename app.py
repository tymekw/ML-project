import os

dataset_path = "C:\\Users\\P1\\Desktop\\githubRepos\\OIDv4_ToolKit\\OID\\Dataset\\validation"

directory_contents = os.listdir(dataset_path)

class_path_list = []

for subdirectory in directory_contents:
    images = os.listdir(dataset_path + "\\" + subdirectory)

    for image in images:
        if image.endswith(".jpg"):
            full_image_path = dataset_path + "\\" + subdirectory + "\\" + image
            class_path_list.append((subdirectory.lower(), full_image_path))

print(class_path_list)