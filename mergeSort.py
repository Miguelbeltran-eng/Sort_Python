def merge(arr, l, m, r):
    # Crear subarreglos temporales
    L = arr[l:m+1]
    R = arr[m+1:r+1]

    i = 0  # índice de L
    j = 0  # índice de R
    k = l  # índice de arr

    # Mezclar los subarreglos en arr
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar elementos restantes de L
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar elementos restantes de R
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        # Ordenar ambas mitades
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)

        # Mezclar las mitades
        merge(arr, l, m, r)


def main():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    merge_sort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    for x in arr:
        print(x, end=" ")
    print()


# Ejecutar programa principal
main()
