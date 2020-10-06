# Задача на программирование: двоичный поиск

def binary_search(A, bi):
    lo = 0
    hi = len(A) - 1
    mid = len(A) // 2
    while hi >= lo:
        if bi == A[mid]:
            return mid + 1
        if bi < A[mid]:
            hi = mid - 1
        if bi > A[mid]:
            lo = mid + 1
        mid = (lo + hi) // 2
    return -1


def main():
    first_line = map(int, input().split())
    n, *A = first_line
    second_line = map(int, input().split())
    k, *b = second_line
    results = []
    for i in range(k):
        result = binary_search(A, b[i])
        results.append(result)
    print(' '.join(map(str, results)))

if __name__ == '__main__':
    main()