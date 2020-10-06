# Задача на программирование: рюкзак

K, num = list(map(int, input().split()))

A = list(map(int, input().split()))

F = [0] * (K + 1)
F[0] = 1
Prev = [0] * (K + 1)
for i in range(len(A)):
    for k in range(K, A[i] - 1, -1):
        if F[k - A[i]] == 1:
            F[k] = 1
            Prev[k] = A[i]
i = K
while F[i] == 0:
    i -= 1
 #i - максимальная масса, которую можно набрать

Ans = []
k = i
while k > 0:
    Ans.append(Prev[k])
    k -= Prev[k]
    
print(sum(Ans))