# Задача на программирование: сортировка подсчётом 

n = int(input())

first_line = list(map(int, input().split()))

first_line.sort()

print(*first_line)