# http://homepages.dcc.ufmg.br/~cunha/teaching/20121/aeds2/shellsort.pdf
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheShellSort.html#fig-incrementsa


def shell_sort(nums):
    h = 1
    n = len(nums)
    # knuth
    while h < n:
        h = h * 3 + 1

    while h > 0:
        h = (h - 1) // 3
        for i in range(h, n):
            current = nums[i]
            j = i
            while j >= h and nums[j - h] > current:
                nums[j] = nums[j - h]
                j -= h
            nums[j] = current
    return nums
