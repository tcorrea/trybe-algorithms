from challenges.quick_sort import quick_sort


def is_anagram(first_string: str, second_string: str) -> tuple[str, str, bool]:
    """
    Parameters
    ----------
    first_string: str
    second_string: str

    Returns
    -------
    tutle[str, str, bool]

    """
    # first_string = "amor"
    # second_string = "roma"
    # saída: ('amor', 'amor', True)

    first_lower: str = first_string.lower()
    second_lower: str = second_string.lower()

    list_first: list = list(first_lower)
    list_second: list = list(second_lower)

    quick_sort(list_first, 0, len(list_first) - 1)
    quick_sort(list_second, 0, len(list_second) - 1)

    sorted_first: str = "".join(list_first)
    sorted_second: str = "".join(list_second)

    if not sorted_first or not sorted_second:
        return (sorted_first, sorted_second, False)

    return (sorted_first, sorted_second, sorted_first == sorted_second)
