# 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
def containsDuplicate(nums):
    return len(nums) != len(set(nums))


if __name__ == '__main__':
    ls = [1, 2, 3, 1]
    print(containsDuplicate(ls))
    ls2 = [1, 2, 3, 4]
    print(containsDuplicate(ls2))
