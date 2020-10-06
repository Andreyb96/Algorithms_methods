# Задача на программирование: декодирование Хаффмана

def huffman_decode(code_table, s):
    decoded = ''
    while len(s) > 0:
        i = 0
        acc = ''
        while i < len(s):
            current_char = s[i]
            acc += current_char
            if acc in code_table.values():
                new_dict = dict(zip(code_table.values(), code_table.keys()))
                acc = new_dict[acc]
                i += 1
                break
            i += 1
        s = s[i:]
        decoded += acc
    return decoded


def main():
    letters_amount, encoded_length = map(int, input().split())
    code_table = {}
    for _ in range(letters_amount):
        letter, code = input().split(': ')
        code_table[letter] = code
    s = input()
    print(huffman_decode(code_table, s))


if __name__ == "__main__":
    main()