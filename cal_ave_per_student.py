# import pandas as pd
#
# stu_scores = pd.read_csv('my_database_score.csv')
# stu_scores.columns = ['id', 'stu_id', 'course_id', 'num']
# stu_ave_score = stu_scores.groupby('stu_id')['num'].mean()
# stu_ave_score.to_csv('stu_ave_score.csv')




from decimal import Decimal
with open("my_database_score.csv","r") as file:
    lines = file.readlines()
    dict_array = {}
    for line in lines:
        cols = line.split(",")
        stu_id = cols[1]
        course_id = cols[2]
        num = cols[3].replace("\n","")

        if dict_array.get(stu_id) is None:
            dict_array[stu_id] = [num]
        else:
            dict_array[stu_id].append(num)

    dict_avg = {}
    for key,value in dict_array.items():
        score_sum = Decimal(0)
        for item in value:
            score_sum = Decimal(item) + score_sum
        dict_avg[key] = str(round(score_sum / len(value),2))

    print(dict_avg)


class Node:

    def __init__(self, num):
        self.num = num
        self.ltree=None
        self.rtree=None

    def set_ltree(self,ltree):
        self.ltree = ltree

    def set_rtree(self,rtree):
        self.rtree = rtree



ls = [4,2,5,7,3]
root = Node(ls[0])
ls.remove(4)

def show_tree(num,tree):
    if num > tree.num:
        if tree.rtree is None:
            tree.rtree = Node(num)
            return
        else:
            show_tree(num,tree.rtree)
    if num < tree.num:
        if tree.ltree is None:
            tree.ltree = Node(num)
            return
        else:
            show_tree(num,tree.ltree)


def print_tree(tree):
    if tree is None:
        return
    print_tree(tree.ltree)
    print(tree.num)
    print_tree(tree.rtree)


for l in ls:
    show_tree(l,root)

print_tree(root)


