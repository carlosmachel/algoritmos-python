# http://www2.dcc.ufmg.br/disciplinas/aeds2_turmaA1/bubblesort.pdf


def bubble_sort(nums):
    n = len(nums)

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

