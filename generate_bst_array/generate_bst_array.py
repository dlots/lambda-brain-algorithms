def get_left_child_index(current_index):
    return 2 * current_index + 1


def get_right_child_index(current_index):
    return 2 * current_index + 2


def recursively_generate_balanced_bst_array(a, begin, end, result, subtree_root_index):
    array_length = end - begin
    if array_length < 0:
        raise IndexError('somethings wrong with array bounds')
    if array_length == 0:
        return
    if array_length == 1:
        result[subtree_root_index] = a[begin]
    middle_index = begin + int(array_length / 2)
    result[subtree_root_index] = a[middle_index]
    recursively_generate_balanced_bst_array(a, begin, middle_index, result, get_left_child_index(subtree_root_index))
    recursively_generate_balanced_bst_array(a, middle_index + 1, end, result, get_right_child_index(subtree_root_index))


def GenerateBBSTArray(a):
    a.sort()
    result = [None] * len(a)
    recursively_generate_balanced_bst_array(a, 0, len(a), result, 0)
    return result
