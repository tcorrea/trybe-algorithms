# função retirado do course
def quick_sort(some_list, start, end):
    if start < end:
        p = partition(some_list, start, end)
        # Os menores em relação ao pivô ficarão à esquerda
        quick_sort(some_list, start, p - 1)
        # Os maiores elementos em relação ao pivô ficarão à direita
        quick_sort(some_list, p + 1, end)


# função auxiliar responsável pela partição do array
# escolhendo um pivô e fazendo movimentações dos sub arrays gerados
def partition(some_list, start, end):
    pivot = some_list[end]
    delimiter = start - 1

    for index in range(start, end):
        # o índice será o elemento em análise no momento,
        # ele passará por todos os elementos
        if some_list[index] <= pivot:
            delimiter = delimiter + 1
            some_list[index], some_list[delimiter] = (
                some_list[delimiter],
                some_list[index],
            )

    some_list[delimiter + 1], some_list[end] = (
        some_list[end],
        some_list[delimiter + 1],
    )

    return delimiter + 1
