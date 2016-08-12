# http://www2.dcc.ufmg.br/disciplinas/aeds2_turmaA1/bubblesort.pdf


def bubble_sort(parameter):
    n = len(parameter)

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if parameter[j] > parameter[j + 1]:
                parameter[j], parameter[j + 1] = parameter[j + 1], parameter[j]
    return parameter



