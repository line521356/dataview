# 树
## 二叉树 多叉树 红黑树 B树 B+树
class Tree:
    def __init__(self,data,left_tree=None,right_tree=None):
        self.data = data
        self.left_tree = left_tree
        self.right_tree = right_tree

lgs = Tree({"num":1,"index":4})
rgs = Tree({"num":3,"index":5})
lc = Tree({"num":2,"index":2},lgs,rgs)
rc = Tree({"num":5,"index":3})
root = Tree({"num":4,"index":1},lc,rc)

# 实现函数 交换一个树的左右子树
def find_by_tree(tree,target_num):

    if tree.left_tree is not None:
        return find_by_tree(tree.left_tree,target_num)

    if tree.data['num'] == target_num:
        print(tree.data['index'])
        return tree.data['index']

    if tree.right_tree is not None:
        return find_by_tree(tree.right_tree,target_num)
    return -1

# 二叉树 堆
leaf_child = -99999
l = [0,1,2,3,leaf_child,5,6]

#位运算 << >> & | ^

def find_by_heap(index,target_num):
    if l[index] == target_num:
        return index
    if ((1 << index) + 1) < len(l) and l[((1 << index) + 1)] != leaf_child:
        return find_by_heap((1 << index) + 1,target_num)
    if ((1 << index) + 2) < len(l) and l[((1 << index) + 2)] != leaf_child:
        return find_by_heap((1 << index) + 2,target_num)

# print(find_by_heap(0,5))
# index_of_list_is_None(l,7)

# 排序算法
# 选择排序 冒泡排序
ss = [6,5,8,3,7,0,1]
# for i in range(len(ss)):
#     for j in range(i+1,len(ss)):
#         if ss[i] > ss[j]:
#             tmp = ss[i]
#             ss[i] = ss[j]
#             ss[j] = tmp
# 算法导论
for i in range(len(ss)):
    for j in range(len(ss) - i -1):
        if ss[j] > ss[j+1]:
            tmp = ss[j]
            ss[j] = ss[j+1]
            ss[j+1] = tmp
for s in ss:
    print(s)