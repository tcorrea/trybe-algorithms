from challenges.quick_sort import quick_sort


def find_duplicate(nums: list) -> bool | int:
    """
    Parameters
    ----------
    nums: list

    Returns
    -------
    False | int

    """

    # sort a lista de numeros
    quick_sort(nums, 0, len(nums) - 1)

    # lista para armazenar o resultado
    numbers_found: list = []

    # enquanto existir elemento na lista nums
    while len(nums) > 0:

        # ferifica se é uma string ou um numero negativo
        if isinstance(nums[0], str) or nums[0] < 0:
            return False

        # se o numero da primeira posição for igual a da segunda
        # e for diferente do ultimo item do numbers_found
        if nums[:1] == nums[1:2] and nums[:1] != numbers_found[-1:]:
            # adiciona o numero na lista de resultado
            numbers_found.append(nums[0])

        # remove o primeiro item de nums
        nums.pop(0)

    if len(numbers_found) == 1:
        return numbers_found[0]

    return False
