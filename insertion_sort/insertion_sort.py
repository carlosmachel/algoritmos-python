# https://pt.khanacademy.org/computing/computer-science/algorithms/insertion-sort/a/insertion-sort


def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        num = nums[i]
        j = i - 1
        while j >= 0 and num < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = num
    return nums
