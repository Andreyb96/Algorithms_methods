#Задача на программирование: последняя цифра большого числа Фибоначчи
def fib_digit(n):
    if n<=2:
        return 1
    fib1 = 1
    fib2 = 1
    for i in range(2,n):
        tmp = fib1 % 10
        fib1 = fib2 % 10
        fib2 = (tmp + fib1) % 10
    return fib2

def main():
    n = int(input())
    print(fib_digit(n)%10)


if __name__ == "__main__":
    main()