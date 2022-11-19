def is_palindrome_iterative(word: str):
    """
    Parameters
    ----------
    word: str

    Returns
    -------
    bool

    """
    if not word:
        return False

    start: int = 0
    end: int = len(word) - 1

    while start < end:
        if word[start] != word[end]:
            return False

        start = start + 1
        end = end - 1

    return True
