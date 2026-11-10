"""Повышенное задание 2: собственная реализация алгоритма Евклида."""


def euclidean_gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    print(euclidean_gcd(48, 18))
