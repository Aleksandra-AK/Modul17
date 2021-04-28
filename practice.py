import sys


def split_array(array):
    if len(array) == 1:
        return array
    middle = len(array)//2
    return merge_array(split_array(array[0:middle:]), split_array(array[middle:]))


def merge_array(left_array, right_array):
    print(left_array)
    print(right_array)
    result_array = list()
    while len(left_array) > 0 and len(right_array) > 0:
        if left_array[0] < right_array[0]:
            result_array.append(left_array[0])
            left_array.pop(0)
        else:
            result_array.append(right_array[0])
            right_array.pop(0)
    if len(left_array):
        result_array.extend(left_array)
    else:
        result_array.extend(right_array)
    return result_array


def binary_search(array, element, left, right):

    if left >= right:
        return False

    middle = (right + left) // 2
    if array[middle] < element <= array[middle + 1]:
        return middle
    elif element <= array[middle]:
        return binary_search(array, element, left, middle)
    else:
        return binary_search(array, element, middle + 1, right)


if __name__ == '__main__':
    try:
        input_set = list(sys.argv[1].split(" "))
    except IndexError:
        input_set = input("Enter numbers separated by a space, warning non-numbers symbols will ignore: ").split(" ")
    array = list()
    for value in input_set:
        try:
            array.append(int(value))
        except ValueError:
            print(f"The value \"{value}\" does't meet the condition")
            continue
    while True:
        try:
            user_value = int(input("Enter the digit: "))
            break
        except ValueError:
            print("Enter the valid digit")
            continue
    sorted_array = split_array(array)
    print(sorted_array)
    print(binary_search(sorted_array, user_value, 0, len(sorted_array) - 1))

