# Задача на программирование: расстояние редактирования

def edit_dist(s, d):
    m = len(s)+1
    n = len(d)+1
    a = [[-1] * n for _ in range(m)]
    for i in range(m):
        a[i][0] = i
    for i in range(n):
        a[0][i] = i
    for i in range(1, m):
        for j in range(1, n):
            diff = int(s[i-1] != d[j-1])
            a[i][j] = min(a[i-1][j]+1, a[i][j-1]+1, a[i-1][j-1]+diff)
    return a[m-1][n-1]

edit_dist("short", "ports")
print(edit_dist(input(), input()))