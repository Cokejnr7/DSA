

num_list = [i for i in range(1, 12)]


def binary_search(search_list, item):
    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = (low + high)//2
        pointer = search_list[mid]

        if pointer == item:
            return mid

        if pointer < item:
            low = mid + 1
        else:
            high = mid - 1

    return None


if __name__ == '__main__':
    print(binary_search(num_list, 2))
