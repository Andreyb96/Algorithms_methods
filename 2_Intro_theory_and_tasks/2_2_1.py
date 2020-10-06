#Задача на программирование: небольшое число Фибоначчи
def fib(n):
    if n<=2:
        return 1
    fib1 = 1
    fib2 = 1
    for i in range(2,n):
        tmp = fib1
        fib1 = fib2
        fib2 = tmp + fib1
    return fib2

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()