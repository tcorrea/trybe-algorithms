![TRYBE_ALGORITHMS](https://user-images.githubusercontent.com/20843662/203112333-6e945e15-cca5-4428-987b-8b689d8770ab.png)

![GitHub top language](https://img.shields.io/github/languages/top/tcorrea/trybe-algorithms)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat-square&logo=linkedin&logoColor=white&color=ffb86c)](https://www.linkedin.com/in/thiago-de-carvalho-correa/)

# Descrição

Esse projeto tem o foco em resolver problemas e otimizar algoritmos desenvolvendo a capacidade de implementar soluções para os mais diversos problemas do dia a dia!

🚵 Habilidades exercitadas:

Lógica;

Capacidade de interpretação de problemas;

Capacidade de interpretação de um código legado;

Capacidade de otimizar a resolução de problemas e;

Resolver problemas/Otimizar algoritmos sob pressão.

# Estrutura do projeto

Estrutura do projeto e descrição dos arquivos que foram desenvolvidos por mim e pela Trybe.

```
Legenda:
  🔸Arquivos desenvolvidos pela Trybe (não foram alterados).
  🔹Arquivos desenvolvidos por mim.

  .
  ├── challenges
  │   ├──🔹 challenge_anagrams.py
  │   ├──🔸 challenge_encrypt_message.py
  │   ├──🔹 challenge_find_the_duplicate.py
  │   ├──🔹 challenge_palindromes_iterative.py
  │   ├──🔹 challenge_palindromes_recursive.py
  │   ├──🔹 challenge_study_schedule.py
  │   └──🔹 quick_sort.py
  ├── tests
  │   ├── encrypt
  │   │   ├──🔸 __init__.py
  │   │   ├──🔸 conftest.py
  │   │   ├──🔸 mocks.py
  │   │   └──🔹 test_encrypt.py
  │   ├── resultados
  │   │   └──🔸 .gitignore
  │   ├──🔸 __init__.py
  │   ├──🔸 complexities.py
  │   ├──🔸 geradores.py
  │   ├──🔸 marker.py
  │   ├──🔸 test_anagrams.py
  │   ├──🔸 test_find_the_duplicate.py
  │   ├──🔸 test_palindromes_iterative.py
  │   ├──🔸 test_palindromes_recursive.py
  │   └──🔸 test_study_schedule.py
  ├──🔸 dev-requirements.txt
  ├──🔸 pyproject.toml
  ├──🔹 README.md
  ├──🔸 requirements.txt
  ├──🔸 setup.cfg
  ├──🔸 setup.py
  ├──🔸 trybe-filter-repo.sh
  └──🔸 trybe.yml

```

# Instalação

1. Clone o repositório

- Use o comando: `git clone git@github.com:tcorrea/trybe-algorithms.git`.
- Entre na pasta do repositório:
  - `cd trybe-algorithms`

2. Crie o ambiente virtual

- `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências

- `python3 -m pip install -r dev-requirements.txt`

# Requisitos e soluções

## 1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)

> **Implementado em:** [`challenges/challenge_study_schedule.py`](https://github.com/tcorrea/trybe-algorithms/blob/main/challenges/challenge_study_schedule.py)

<details>
  <summary>Expandir</summary>
Você trabalha na maior empresa de educação do Brasil. Certo dia, a pessoa Product Manager `(PM)` quer saber qual horário tem a maior quantidade de pessoas estudantes acessando o conteúdo da plataforma. Com esse dado em mãos, a pessoa PM saberá qual é o melhor horário para disponibilizar os materiais de estudo para ter o maior engajamento possível.

O horário de entrada e saída do sistema é cadastrado no banco de dados toda vez que uma pessoa estudante entra e sai do sistema. Esses dados estarão contidos em uma lista de tuplas (`permanence_period`) em que cada tupla representa o período de permanência de uma pessoa estudante no sistema com seu horário de entrada e de saída.

Seu trabalho é descobrir qual o melhor horário para disponibilizar os conteúdos de estudo. Para isso, utilize a estratégia de resolução de problemas chamada `força bruta` em que a função desenvolvida por você será chamada várias vezes com valores diferentes para a variável `target_time` e serão analisados os retornos da função.

### _Solução_

![carbon](https://user-images.githubusercontent.com/20843662/203116693-844da297-45ef-4b10-bd36-130727c2a80d.png)

</details>

## 2 - Criptografia de inversões (Testes)

> **Implementado em:** [`tests/encrypt/test_encrypt.py`](https://github.com/tcorrea/trybe-algorithms/blob/main/tests/encrypt/test_encrypt.py)

<details>
  <summary>Expandir</summary>
Durante a dinâmica em grupos de um processo seletivo, a empresa contratante definiu um desafio em duplas, e cada pessoa terá um papel. A primeira pessoa deve criar uma função de criptografia, e a segunda pessoa deve implementar os testes da função implementada pela primeira pessoa.

Você fará o papel da _**segunda pessoa**_ nessa dinâmica, ou seja: deve implementar os testes de uma função de criptografia.

Esse teste deve se chamar `test_encrypt_message`, e ele deve garantir que a função de criptografia `encrypt_message` deve respeitar uma lógica específica.

### _Solução_

![carbon (1)](https://user-images.githubusercontent.com/20843662/203117786-0068bc8e-2860-4386-baa2-7998d8ec9ffb.png)

</details>

## 3 - Palíndromos (Recursividade)

> **Implementado em:** [`challenges/challenge_palindromes_recursive.py`](https://github.com/tcorrea/trybe-algorithms/blob/main/challenges/challenge_palindromes_recursive.py)

<details>
    <summary>Expandir</summary>
    Escreva uma função que irá determinar se uma palavra é um palíndromo ou não. A função irá receber uma string de parâmetro e o retorno será um _booleano_, `True` ou `False`.

Mas o que é um palíndromo?

> Um palíndromo é uma palavra, frase ou número que mantém seu sentido mesmo sendo lido de trás para frente. Por exemplo, `"ABCBA"`.

:warning: Neste projeto iremos focar somente em **palavras palíndromas** e não em frases ou números.

### _Solução_

![carbon (2)](https://user-images.githubusercontent.com/20843662/203118725-893d92f8-81e6-40ae-becf-df923dc3e4b0.png)

</details>

## 4 - Anagramas (Algoritmo de ordenação)

> **Implementado em:** [`challenges/challenge_anagrams.py`](https://github.com/tcorrea/trybe-algorithms/blob/main/challenges/challenge_anagrams.py)

<details>
    <summary>Expandir</summary>

Faça um algoritmo que consiga comparar duas _strings_, ordená-las e identificar se uma é um anagrama da outra. Ou seja, sua função irá receber duas strings de parâmetro e o retorno da função será uma tupla `()` com a primeira string ordenada, a segunda string ordenada e um _booleano_, `True` ou `False` representando se são anagramas.

O algoritmo deve considerar letras _maiúsculas_ e _minúsculas_ como iguais durante a comparação das entradas, ou seja, ser _case insensitive_.

Mas o que é um anagrama?

> "Um anagrama é uma espécie de jogo de palavras criado com a reorganização das letras de uma palavra ou expressão para produzir outras palavras ou expressões, utilizando todas as letras originais exatamente uma vez."

- Utilize algoritmos de ordenação para realizar este requisito.

  - Utilize qualquer algoritmo que quiser (_Selection sort_, _Insertion sort_, _Bubble sort_, _Merge sort_, _Quick sort_ ou _TimSort_), desde que atinja a complexidade `O(n log n)`.
  - :warning: Você deverá implementar **sua própria função de ordenação**, ou seja, o uso de funções prontas **não** é permitido.
    - Exemplos de funções não permitidas: _*sort*, *sorted* e *Counter*_;

- :warning: **Não** será permitido realizar nenhuma **importação** neste arquivo!

### _Solução_

![carbon (3)](https://user-images.githubusercontent.com/20843662/203119757-2cb42529-3077-435f-8095-54a323a916bb.png)

</details>

## 5 - Encontrando números repetidos (Algoritmo de busca)

> **Implementado em:** [`challenge_find_the_duplicate.py`](https://github.com/tcorrea/trybe-algorithms/blob/main/challenges/challenge_find_the_duplicate.py)

<details>
    <summary>Expandir</summary>

Dada um _array_ de números inteiros contendo `n + 1` inteiros, chamado de `nums`, em que cada inteiro está no intervalo `[1, n]`.

Retorne apenas um número duplicado em `nums`.

### _Solução_

![carbon (4)](https://user-images.githubusercontent.com/20843662/203120375-f587c929-afc3-4791-9244-c432ecc992b9.png)

</details>

## 6 - Palíndromos (Iteratividade)

> **Implementado em:** [`challenge_palindromes_iterative.py`]()

<details>
    <summary>Expandir</summary>

Resolva o mesmo problema apresentado no `requisito 2 - Palíndromos`, porém dessa vez utilizando a solução iterativa.

- Este requisito será testado executando milhares de vezes sobre várias entradas com o tamanho variável. Tais execuções **no avaliador** irão determinar de maneira empírica, através de cálculos, a complexidade assintótica do seu algoritmo.

  - O tempo de execução do código na sua máquina pode variar em relação ao avaliador, mas o cálculo será feito em cima do comportamento, e não do tempo de execução. Ainda assim, o que vale é o resultado do avaliador, e não o local. Na dúvida, busque ajuda do time de instrução;

- O algoritmo deve utilizar a solução iterativa;

- O código deve ser feito dentro do arquivo `challenge_palindromes_iterative.py`.

### _Solução_

![carbon (5)](https://user-images.githubusercontent.com/20843662/203120978-b425976a-fdcb-4977-b18b-680db9a26314.png)

</details>
