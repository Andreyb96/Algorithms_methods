# Задача на программирование: различные слагаемые

def calculation(n):
    terms = []
    a, b = 1, n - 1
    while b > a:
        terms.append(a)
        a += 1
        b = b - a
    terms.append(n-sum(terms))
    return terms


def main():
    n = int(input())
    result = calculation(n)
    print(len(result))
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()