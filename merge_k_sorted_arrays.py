def merge_sorted_arrays(arr1, arr2):
    merged_array = []     # storing the result array here in merged_array
    i, j = 0, 0     # merging sorted arrays

    while i < len(arr1) and j < len(arr2):
        # normal logic of merging two arrays similar to merge sort
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # appending the extra elements if arrays are of unequal length
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])
    return merged_array

def merge_caller(sorted_arrays):
    if not sorted_arrays:
        return []

    while len(sorted_arrays) > 1:
        merged_arrs = []
        # incrementing the counter by 2
        for i in range(0, len(sorted_arrays), 2):
            if i + 1 < len(sorted_arrays):
                # sending two arrays at a time to be merged
                merged = merge_sorted_arrays(sorted_arrays[i], sorted_arrays[i + 1])
            else:
                merged = sorted_arrays[i]
            merged_arrs.append(merged)
        # new list of sorted arrays will contain n/2 sorted arrays
        sorted_arrays = merged_arrs

    return sorted_arrays[0]


k_sorted_arrays = [
    [1, 18, 53],
    [2, 14, 43, 63],
    [0, 7, 8],
    [-1, 4, 100, 105, 110]
]

merged_array = merge_caller(k_sorted_arrays)
print("The final merged Sorted Array:", merged_array)
