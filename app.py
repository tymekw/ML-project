
dataset_path = "C:\\Users\\P1\\Desktop\\githubRepos\\OIDv4_ToolKit\\OID\\Dataset\\validation"
csv_folder = "C:\\Users\\P1\\Desktop\\githubRepos\\OIDv4_ToolKit\\OID\\csv_folder"


def get_class_map():
    f = open("C:\\Users\\P1\\Desktop\\githubRepos\\OIDv4_ToolKit\\OID\\csv_folder\\class-descriptions-boxable.csv")
    class_map = {}
    for line in f:
        data_line = line.rstrip().split(',')
        class_map[data_line[0]] = data_line[1]
    return class_map

# directory_contents = os.listdir(dataset_path)
#
# class_path_list = []
#
# for subdirectory in directory_contents:
#     images = os.listdir(dataset_path + "\\" + subdirectory)
#
#     for image in images:
#         if image.endswith(".jpg"):
#             full_image_path = dataset_path + "\\" + subdirectory + "\\" + image
#             class_path_list.append((subdirectory.lower(), full_image_path))
#
# print(class_path_list)