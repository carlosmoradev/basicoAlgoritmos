def particion(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[1], arr[j] = arr[j], arr[i]

    arr[i+1]. arr[high] = arr[high],arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if low < high:
        pi = particion(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

arr = [1992, 1990, -2, 2000, 37 ]
n = len(arr)
quickSort(arr, 0, n-1)
print("Arrelgo ordenado:")
for i in range(n):
    print("%d" %arr[i])