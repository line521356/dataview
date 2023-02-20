from sklearn.cluster import DBSCAN
import numpy as np


def get_labels(data):
    data_np = np.array(data)
    labels = DBSCAN(eps=100, min_samples=20).fit(data_np).labels_
    label_size = len(set(labels))
    step = (int)(0xFFFF00 / label_size)
    colors = []
    for label in labels:
        if label == -1:
            colors.append("#FFFFFF")
        else:
            colors.append(hex2color((hex)((step * (int)(label)))))
    result_data = []
    for index in range(len(labels)):
        line = [data[index][0], data[index][1], data[index][2], colors[index]]
        result_data.append(line)
    return result_data


def hex2color(hex_str: str):
    hex_str = hex_str.replace("0x", "")
    return "#" + hex_str.rjust(6, "0")


def count_xyz(my_data_background: list(dict())):
    count_dict = {}
    for line in my_data_background:
        label = count_dict.get(line['label'])
        if label is None:
            label = {
                "x": {
                    "max": line['x'],
                    "min": line['x']
                },
                "y": {
                    "max": line['y'],
                    "min": line['y']
                },
                "z": {
                    "max": line['z'],
                    "min": line['z']
                }
            }
            count_dict[line['label']] = label
        else:
            if label['x']['max'] < line['x']:
                label['x']['max'] = line['x']
            if label['x']['min'] > line['x']:
                label['x']['min'] = line['x']
            if label['y']['max'] < line['y']:
                label['y']['max'] = line['y']
            if label['y']['min'] > line['y']:
                label['y']['min'] = line['y']
            if label['z']['max'] < line['z']:
                label['z']['max'] = line['z']
            if label['z']['min'] > line['z']:
                label['z']['min'] = line['z']
            count_dict[line['label']] = label
    return count_dict


def get_colum_by_index(data, index):
    data_np = np.array(data)
    return data_np[:, index].tolist()
