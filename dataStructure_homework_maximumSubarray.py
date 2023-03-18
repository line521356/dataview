# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组 是数组中的一个连续部分。

def maxSubArray(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] = nums[i] + nums[i - 1]
    return max(nums)


if __name__ == '__main__':
    ls = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(ls))
