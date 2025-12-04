def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, low, high):
    pivot = arr[high]     # elegimos el último elemento como pivote
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # colocar el pivote en su posición correcta
    swap(arr, i + 1, high)
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # ordenar subarreglos
        quick_sort(arr, low, pi - 1)   # izquierda
        quick_sort(arr, pi + 1, high)  # derecha


def print_array(arr):
    for num in arr:
        print(num, end=" ")
    print()


def main():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    print("Arreglo original:")
    print_array(arr)

    quick_sort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    print_array(arr)


# Ejecutar el programa principal
main()
