def bubble_sort(arr):
    n = len(arr)
    
    # FOR EXTERNO
    for i in range(n - 1):
        # FOR INTERNO
        for j in range(n - i - 1):
            # CONDICIÓN DE INTERCAMBIO
            if arr[j] > arr[j + 1]:
                # INTERCAMBIO
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def print_array(arr):
    for num in arr:
        print(num, end=" ")
    print()


def main():
    arr = [5, 1, 4, 2, 8]
    n = len(arr)
    
    print("Tamaño del arreglo:", n)
    
    print("Arreglo original:")
    print_array(arr)
    
    bubble_sort(arr)
    
    print("Arreglo ordenado:")
    print_array(arr)


# Llamada al programa principal
main()
