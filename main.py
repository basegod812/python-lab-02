"""ЛР №2, вариант 2: задания 2, 4, 7, повышенные 2, 6."""
from math import gcd
from euclid import euclidean_gcd


VOWELS = set("аеёиоуыэюяaeiou")


def odd_sum(n: int) -> int:
    """Сумма нечётных натуральных чисел от 1 до n."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    total = 0
    for number in range(1, n + 1, 2):
        total += number
    return total


def greatest_common_divisor(a: int, b: int) -> int:
    """НОД двух целых чисел с помощью math.gcd."""
    return gcd(a, b)


def count_vowels(text: str) -> int:
    """Число русских/английских гласных в строке."""
    count = 0
    for char in text.lower():
        if char in VOWELS:
            count += 1
    return count


def main():
    print("1. Сумма нечётных до 10:", odd_sum(10))
    print("2. НОД 48 и 18:", greatest_common_divisor(48, 18))
    print("3. Гласные в 'Программирование':", count_vowels("Программирование"))
    print("4. Алгоритм Евклида для 48 и 18:", euclidean_gcd(48, 18))


if __name__ == "__main__":
    main()
