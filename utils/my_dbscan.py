from sklearn.cluster import DBSCAN
import numpy as np


# 根据数据中的坐标计算当前坐标的点的颜色
def get_labels(data):
    data_np = np.array(data)
    labels = DBSCAN(eps=100, min_samples=20).fit(data_np).labels_
    label_size = len(set(labels))
    step_size = int(0xFFFF00 / label_size)
    colors = []
    for label in labels:
        # label == -1时，该点坐标视为噪音
        if label == -1:
            colors.append("#FFFFFF")
        else:
            colors.append(hex2color(hex((step_size * int(label)))))
    result_data = []
    for index in range(len(labels)):
        line = [data[index][0], data[index][1], data[index][2], colors[index]]
        result_data.append(line)
    return result_data


# 将16进制数转为#开头的6位16进制颜色
def hex2color(hex_str: str):
    hex_str = hex_str.replace("0x", "")
    return "#" + hex_str.rjust(6, "0")


# 统计相同颜色的坐标的最大值和最小值
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


# 二维数组，取中其中一列
def get_colum_by_index(data, index):
    data_np = np.array(data)
    return data_np[:, index].tolist()
