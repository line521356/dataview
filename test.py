l = [1, 2, 3, 4, 5, 6]
# 找出数组中元素位3的下表

# O(n)
for index, item in enumerate(l):
    if item == 3:
        print(index)

# 二分查找法 O(log2 n) 作业 递归

# 顺序表
## 线性表 内存中的排列都是挨着的
## 链表 链型的 内存中排列未必是挨着的
## 单向链表
## 双向链表
## 栈
## 队列
# 散列表 hash
# ssl 私钥 公钥 内存快照
class Node:
    def __init__(self,data,next_pointer=None):
        self.data = data
        self.next_pointer = next_pointer

xiaoli = Node("小李")
xiaoqiang = Node("小强",xiaoli)
xiaozhang = Node("小张",xiaoqiang)
xiaowang = Node("小王",xiaozhang)

head = xiaowang
while head is not None:
    print(head.data)
    head = head.next_pointer


# 二分查找
# 实现链表
# 实现一个函数，找到单向链表的倒数第K的元素 step 两个指针

