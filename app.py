#
# dataset_path = "C:\\Users\\P1\\Desktop\\githubRepos\\OIDv4_ToolKit\\OID\\Dataset\\validation"
# csv_folder = "C:\\Users\\P1\\Desktop\\githubRepos\\OIDv4_ToolKit\\OID\\csv_folder"
#
#
# def get_class_map():
#     f = open("C:\\Users\\P1\\Desktop\\githubRepos\\OIDv4_ToolKit\\OID\\csv_folder\\class-descriptions-boxable.csv")
#     class_map = {}
#     for line in f:
#         data_line = line.rstrip().split(',')
#         class_map[data_line[0]] = data_line[1]
#     return class_map

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

w = 1024
h = 648
a=[2.96614259e-01, 2.26320758e-01, 7.78682113e-01, 5.01484871e-01]
b=[3.21174473e-01, 4.48274255e-01, 7.57149994e-01, 6.20503068e-01]
c=[3.17986786e-01, 6.33381009e-01, 7.62762785e-01, 8.27470541e-01]

anew = [w*a[1], h*a[0], "x", w*a[3], h*a[2]]
bnew = [w*b[1], h*b[0], "x", w*b[3], h*b[2]]
cnew = [w*c[1], h*c[0], "x", w*c[3], h*c[2]]
print(anew)
print(bnew)
print(cnew)

#ymin, xmin, ymax, xmax
#box= [0,0.1,0]
