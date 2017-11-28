# -*- coding: utf-8 -*-
from typing import List
from typing import Tuple
from math import sqrt
from itertools import count, islice
from contracts import contract
import calendar
""" Repaso interactivo de python
"""


@contract(lower='int,>0', upper='int,>0', returns=None)
def lower_up(lower: int, upper: int) -> None:
    for lower in range(lower, upper + 1):
        print(lower)
""" 1: Returns a list of numbers from the lower number to the upper number:
>>>lower_up(5,15)
5
6
7
8
9
10
11
12
13
14
15
"""


@contract(args='tuple[N],N>0', kwargs='dict(str: (int))', returns=None)
def all_the_args(*args: str, **kwargs: str) -> None:
    print(args)
    print(kwargs)
""" 2: Return an array. Use * to expand positional args and use ** to expand
keyword args
>>>all_the_args(1, 2, a=3, b=4)
(1, 2)
{"a": 3, "b": 4}
"""


@contract(tup='tuple[N],N>0', returns=None)
def may_20(tup: Tuple[int]) -> None:
    cad_sup = ""
    for x in tup:
        cad_sup = compara_20(cad_sup, x)
    print(cad_sup)


@contract(cadenaTMP='str', cadena='int,>0', returns='str')
def compara_20(cadenaTMP: str, cadena: int) -> str:
    if cadena > 20:
        cadenaTMP = concatena_20(cadenaTMP, cadena)
    return cadenaTMP

@contract(cadenaTMP='str', cadena='int,>0', returns='str')
def concatena_20(cadenaTMP: str, cadena: int) -> str:
    if cadenaTMP == "":
        cadenaTMP = str(cadena)
    else:
        cadenaTMP = cadenaTMP + ", " + str(cadena)
    return cadenaTMP
""" 3: Definir una tupla con 10 números. Imprimir la cantidad de números
superiores a 20.
>>>may_20(10, 16, 22, 26, 27, 30)
22, 26, 27, 30
"""


@contract(list_='list(str)', n='int,>0', returns='list(str)')
def word_filter(list_of_words: List[str], n: int) -> List[str]:
    a = 1
    for i in range(len(list_of_words)):
        list_of_words = word_list(list_of_words, n, a, i)
        a = word_accepted(list_of_words, n, a, i)
    return list_of_words


@contract(li='list(str)', n='int,>0', a='int,>0', i='int', returns='list(str)')
def word_list(list_of_words: List[str], n: int, a: int, i: int) -> List[str]:
    if len(list_of_words[i-a]) <= n:
        list_of_words.remove(list_of_words[i-a])
    return list_of_words


@contract(list_='list(str)', n='int,>0', a='int,>0', i='int', returns='int')
def word_accepted(list_of_words: List[str], n: int, a: int, i: int) -> int:
    if len(list_of_words[i-a]) <= n:
        a = a + 1
    return a
""" 4: Filtra las palabras que contienen más de n caracteres.
>>>word_filter([hello, bye, computer, software, python], 5)
[computer, software, python]
"""


@contract(list='str', returns='int')
def string_length(list: str) -> int:
    return len(list)
""" 5: imprime el largo de una cadena de caracteres
>>>string_length("popularity")
10
"""


@contract(x='str', returns='bool')
def is_vocal(x: str) -> bool:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        return True
    else:
        return False
""" 6: Determines if it is vocal
>>>is_vocal(a)
True
>>>is_vocal(b)
False
"""


@contract(year='int', returns=None)
def is_leap_year(year: int) -> None:
    print(calendar.isleap(year))
""" 7: Determines if a year is a leap year.
>>>is_leap_year(2016)
True
"""


@contract(word='str', returns=None)
def has_uppercase(word: str) -> None:
    print(sum(1 for x in word if x.isupper()))
""" 8: Evaluate if a word has uppercase letters
>>>has_uppercase(MayuSculA)
3
"""


@contract(cadena='str', returns='int')
def contar_vocales(cadena: str) -> int:
    count = 0
    for i in cadena.strip():
        count = separa_vocal(i) + count
    return count


@contract(i='str', returns='int')
def separa_vocal(i: str) -> int:
    if is_vocal(i):
        return 1
    return 0
""" 9: Return number of vocales in a word.
>>>contar_vocales(murcielago)
5
"""


@contract(list='list(int)', returns=None)
def square(list: List[int]) -> None:
    ls = []
    for i in range(len(list)):
        ls.append(list[i]*list[i])
    print(ls)
""" 10: Calculate the square of the numbers in a list
>>> l = [0, 1, 2, 3]
>>> square(l)
[0, 1, 4, 9]
"""


@contract(n='int', returns='bool')
def is_prime(n: int) -> bool:
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))
""" 11:  Return if n is prime.
>>>is_prime(5)
True
>>>is_prime(6)
False
"""


@contract(n='int', returns='int')
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return int(n * factorial(n-1))
""" 12: Return the factorial of n, an exact integer >= 0.
If the result is small enough to fit in an int, return an int.
Else return a long.
>>>[factorial(n) for n in range(6)]
[1, 1, 2, 6, 24, 120]
>>>[factorial(long(n)) for n in range(6)]
[1, 1, 2, 6, 24, 120]
>>>factorial(30)
265252859812191058636308480000000L
"""


@contract(n='int', returns='list(str)')
def to_roman(n: int) -> List[str]:
    val = (1000, 900,  500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    syb = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V',
           'IV', 'I')
    roman_num = ""
    list = []
    for i in range(len(val)):
        count = int(n / val[i])
        roman_num += syb[i] * count
        n -= val[i] * count
        list.append(roman_num)
    return list
""" 13: Convert number integer to Roman numeral
>>>to_roman(598)
[DXCVIII]
"""


@contract(word1='str', word2='str', returns=None)
def rima(word1: str, word2: str) -> None:
    x = ""
    x = rima_comparation(word1, word2, 2)
    if x == "rima un poco":
        x = rima_comparation2(word1, word2, 3)
    print(x)


@contract(word1='str', word2='str', n='int', returns='str')
def rima_comparation(word1: str, word2: str, n: int) -> str:
    if word1[len(word1)-n:len(word1)] == word2[len(word2)-n:len(word2)]:
        return "rima un poco"
    return "no rima"


@contract(word1='str', word2='str', n='int', returns='str')
def rima_comparation2(word1: str, word2: str, n: int) -> str:
    if word1[len(word1)-n:len(word1)] == word2[len(word2)-n:len(word2)]:
        return "rima"
    return "rima un poco"
""" 14: Indica si dos palabrar riman. Si coinciden las 3 ultimas letras rima,
si ncoinciden solo 2 rima un poco, si coincide solo 1 no rima.
>>>rima(flor, coliflor)
rima
>>>rima(amar, plantar)
rima un poco.
>>>rima(azucar, barrer)
no rima
"""


@contract(pesos='float', interes='float', anios='float', returns=None)
def capital(pesos: float, interes: float, anios: float) -> None:
    total = pesos*(1 + interes/100)**anios
    print("%.2f" % total)
""" 15: Pide una cantidad de pesos, una tasa de interés y un numero de años.
Muestra en cuanto se habrá convertido el capital inicial transcurridos esos
años si cada año se aplica la tasa de interés introducida.
>>>capital(10000, 4.5, 20)
24117.14
"""
