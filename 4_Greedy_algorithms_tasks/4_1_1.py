# Задача на программирование: покрыть отрезки точками

def dots(segments):
    resulting_segments = []
    while len(segments) > 0:
        if len(segments) < 2:
            seg = segments.pop()
            resulting_segments.append(seg)
        else:
            a, b = segments[0], segments[1]
            if b[0] <= a[1]:
                left, right = b[0], b[1] if b[1] <= a[1] else a[1]
                overlapping = (left, right)
                segments = segments[2:]
                segments = [overlapping] + segments
            else:
                resulting_segments.append(segments[0])
                segments = segments[1:]
    return [x[1] for x in resulting_segments]


def main():
    n = int(input())
    segments = []
    for i in range(n):
        segments.append(tuple(map(int, input().split())))
    segments.sort(key=lambda x: (x[0], x[1]))
    result = dots(segments)
    print(len(result))
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()