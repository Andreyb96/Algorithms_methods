# Задача на программирование: число инверсий

def inversions_count(unsorted_list):
    """Time complexity: O(n * log(n)), where n = len(unsorted_list)
    Inversions count task is called "Yodaness problem"
    Based on merge sort recursive algorithm
    """
    if len(unsorted_list) <= 1:
        return unsorted_list, 0

    middle_index = len(unsorted_list) // 2

    left_list, left_list_inv_count = inversions_count(unsorted_list[:middle_index])
    right_list, right_list_inv_count = inversions_count(unsorted_list[middle_index:])

    merged_list, current_merge_inv_count = merge(left_list, right_list)
    return merged_list, (left_list_inv_count + right_list_inv_count + current_merge_inv_count)


def merge(left_list, right_list):
    """Time complexity: O(n), where n = len(left_list) + len(right_list)"""
    merged_list = []
    i, j = 0, 0
    current_merge_inv_count = 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            current_merge_inv_count += (len(left_list) - i)  # the number of elements remaining in the left list
            j += 1

    # at least one of the lists (left_list[i:], right_list[j:]) is empty
    merged_list.extend(left_list[i:] + right_list[j:])
    return merged_list, current_merge_inv_count


def main():
    n_ = input()
    unsorted_list = [int(i) for i in input().split()]

    sorted_list_, inv_count = inversions_count(unsorted_list)
    print(inv_count)


if __name__ == '__main__':
    main()