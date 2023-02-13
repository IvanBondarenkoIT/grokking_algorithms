def binary_search(list_of_values: list, value_for_search: int) -> int:
    """search the value_for_search in sorted list_of_values. Return position in list_of_values or None"""
    low = 0
    high = len(list_of_values) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list_of_values[mid]

        if guess == value_for_search:
            return mid
        elif guess < value_for_search:
            low = mid + 1
        elif guess > value_for_search:
            high = mid - 1

    return None
