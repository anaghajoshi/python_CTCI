def selection_sort(in_array):
    for i in range(len(in_array)):
        next_min_value = min(in_array[i:])
        next_min_value_index = in_array.index(next_min_value)
        in_array[i], in_array[next_min_value_index] = in_array[next_min_value_index], in_array[i]


def insertion_sort(in_array):
    for i in range(1, len(in_array)):
        next_value = in_array[i]
        position = i - 1
        while in_array[position] > next_value and position >= 0:
            in_array[position + 1] = in_array[position]
            position = position - 1
        in_array[position + 1] = next_value


def merge(left, right):
    l = 0
    r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1

    return result

def merge_sort(in_array):
    if len(in_array) < 2:
        return in_array
    else:
        mid = len(in_array)//2
        left = in_array[:mid]
        right = in_array[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left,right)


def quick_sort(in_array):
    if len(in_array) < 2:
        return in_array
    else:
        left = []
        right = []
        equal = []
        pivot_index = len(in_array)//2
        pivot_value = in_array[pivot_index]

        for item in in_array:
            if item == pivot_value:
                equal.append(item)
            elif item < pivot_value:
                left.append(item)
            else:
                right.append(item)
        left = quick_sort(left)
        right = quick_sort(right)

        return left + equal + right

if __name__ == '__main__':
    in_array = [22, 11, 99, 88, 9, 7, 42]
    print(in_array)
    selection_sort(in_array)
    print('after sorting - SELECTION')
    print(in_array)

    in_array = [22, 11, 99, 88, 9, 7, 42]
    print(in_array)
    insertion_sort(in_array)
    print('after sorting - INSERTION')
    print(in_array)

    a = [3, 7]
    b = [12,14]
    print(merge(a, b))

    a = [7]
    b = [3]
    print(merge(a, b))

    a = [3, 7, 12, 14]
    b = [2, 6, 9, 11]
    print(merge(a, b))


    print(merge_sort([14,7,3,12,9,11,6,2]))

    print(merge_sort([14,7,3,12,9,11,6,2,1]))

    print(quick_sort([14, 7, 3, 12, 9, 11, 6, 2]))

    print(quick_sort([14, 7, 3, 12, 9, 11, 6, 2, 1]))