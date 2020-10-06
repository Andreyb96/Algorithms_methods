#Задача на программирование: непрерывный рюкзак

def calculation(c, items):
    capacity = c
    sack_value = 0
    while len(items) > 0:
        value, volume, value_per_unit = items[0]
        if capacity > 0:
            if capacity >= volume:
                sack_value += volume * value_per_unit
                capacity -= volume
            else:
                sack_value += capacity * value_per_unit
                break
        items = items[1:]
    return '%.3f' % sack_value


def main():
    n, c = map(int, input().split())
    items = []

    for i in range(n):
        total_value, volume = map(int, input().split())
        value_per_unit = total_value / volume
        items.append((total_value, volume, value_per_unit))

    items.sort(key=lambda x: x[2], reverse=True)
    print(calculation(c, items))

if __name__ == "__main__":
    main()