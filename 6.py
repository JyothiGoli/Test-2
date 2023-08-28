def mergeArrays(l1, l2, n1, n2):
    l3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:
        if l1[i] < l2[j]:
            l3[k] = l1[i]
            k = k + 1
            i = i + 1
        else:
            l3[k] = l2[j]
            k = k + 1
            j = j + 1
    while i < n1:
        l3[k] = l1[i]
        k = k + 1
        i = i + 1
    while j < n2:
        l3[k] = l2[j]
        k = k + 1
        j = j + 1
    for i in range(n1 + n2):
        print(str(l3[i]), end = " ")
l1 = [1, 3, 5, 7]
n1 = len(l1)
l2 = [2, 4, 6, 8]
n2 = len(l2)
mergeArrays(l1, l2, n1, n2)
