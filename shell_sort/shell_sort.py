# http://homepages.dcc.ufmg.br/~cunha/teaching/20121/aeds2/shellsort.pdf
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheShellSort.html#fig-incrementsa


def shell_sort(nums):
    n = len(nums)
    h = gap_definition(n)

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


def gap_definition(n):
    # knuth
    h = 1
    while h < n:
        h = h * 3 + 1
    return h
