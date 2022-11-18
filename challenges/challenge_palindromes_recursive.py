def is_palindrome_recursive(
    word: str, low_index: int, high_index: int
) -> bool:
    """
    Parameters
    ----------
    word: str
    low_index: int
    high_index: int

    Returns
    -------
    bool

    """
    # verifica se existe word: retorna False
    if not word:
        return False

    # retorna True se for passado somente uma letra no parametro word
    if low_index == high_index:
        return True

    # se a letra no começo da palavra não corresponde com a letra do final
    if word[low_index] != word[high_index]:
        return False

    # parada recursividade
    # enquanto low for menor que high, a propria função será chamada
    if low_index < high_index:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return True
