from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # Recebe uma string message e um inteiro key como parâmetros

    # Se key não for um índice positivo válido de message,
    # retorna a string message invertida
    assert "edcba" == encrypt_message("abcde", -1)

    # Se key for ímpar:
    # divide message no índice key,
    # inverte os caracteres de cada parte,
    # e retorna a união das partes novamente com "_" entre elas
    assert "typ_noh" == encrypt_message("python", 3)

    # Se key for par:
    # divide message no índice key, inverte a posição das partes,
    # inverte os caracteres de cada parte, e retorna a união das partes
    # novamente com "_" entre elas
    # python = noht_py
    assert "noht_yp" == encrypt_message("python", 2)

    # Se key e message não possuírem os tipos corretos,
    # uma exceção deve ser lançada
    with pytest.raises(TypeError):
        encrypt_message(1, "test")

    assert encrypt_message("python", 2) is not None
