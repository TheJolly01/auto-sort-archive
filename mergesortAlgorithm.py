# This algorithm is used to  sort elements in an array, that in future will be files in a directoru
def merge_sort(arr):  # receive the array to sort
    if len(arr) > 1:
        # SPLITTING
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        # MERGING
        a = b = c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                arr[c] = left[a]
                a += 1
            else:
                arr[c] = right[b]
                b += 1
            c += 1

        while a < len(left):
            arr[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            arr[c] = right[b]
            b += 1
            c += 1

    return arr  # return the array sorted
