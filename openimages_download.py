

def get_dict_all_labels(path = "D:\\AGH\\VI semestr\\ML\\datasetGoogle\\OIDv4_ToolKit\\OID\\csv_folder\\test-annotations-bbox.csv")
    import csv
    my_dict = {}
    with open(path, mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if row[0] not in my_dict:
                my_dict[row[0]] = []
                my_dict[row[0]].append(row[1:])
            else:
                my_dict[row[0]].append(row[1:])

    return my_dict

