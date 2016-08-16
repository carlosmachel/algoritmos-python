

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[idx]:
                idx = j
        nums[idx], nums[i] = nums[i], nums[idx]
    return nums
