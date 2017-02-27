# E. Сортировка
#import no_standard_sort
def quick_sort(arr):
    if arr:
        return quick_sort([x for x in arr if x < arr[0]]) + [x for x in arr if x == arr[0]] + quick_sort(
            [x for x in arr if x > arr[0]])
    return []


val_arr = open('input.txt').read().strip().split()
a = quick_sort(val_arr)
print(' '.join(a), end='')
