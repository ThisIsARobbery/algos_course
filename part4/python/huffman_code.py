
def huffman_code(string: str):
    # проводим частотный анализ строки и строим список кортежей с частотами
    freq_dict = {}
    for char in string:
        if char not in freq_dict:
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1
    # print("Freq dict: ", freq_dict, end='\n')
    leaves = []
    for char in freq_dict:
        leaves.append((char, freq_dict[char]))

    def sort_leaves(leaves: (str, int)):
        leaves = leaves.copy()
        leaves.sort(key=lambda x: x[1], reverse=True)
        return leaves
    # print("Leaves list: ", sort_leaves(leaves))
    code_list = []
    char_num = len(freq_dict)
    leaves = sort_leaves(leaves)
    while len(leaves) > 1 and len(string) > 1 and len(freq_dict) > 1:
        left, right = leaves[-2:]
        code_list.append((left[0], left[1], '0'))
        code_list.append((right[0], right[1], '1'))
        new_leaf = (left[0] + right[0], left[1] + right[1])
        leaves = leaves[:-2]
        leaves.append(new_leaf)
        leaves = sort_leaves(leaves)
        if (len(leaves) == 1):
            bit_length = leaves[0][1]
        # print(leaves)
    code_list.reverse()
    # print("Char_num: ", char_num)
    # print("Bit length: ", bit_length)
    # print("Code list: ", code_list)

    def encode(code_list, char):
        word = ""
        for code_word in code_list:
            if char in code_word[0]:
                word += code_word[2]
        return word

    def encode_word(code_list, word):
        code = ""
        for char in word:
            code += encode(code_list, char)
        return code

    word_len = len(encode_word(code_list, string))
    encoded_word = encode_word(code_list, string)
    # print("Decoded word " + string + " -> " + decode_word(code_list, string))
    # print("Len: ", word_len)
    if len(freq_dict) == 1:
        code_list = [(string, 1, '1')]
        word_len = len(string)
        encoded_word = '1' * len(string)
    elif len(string) == 1:
        word_len = 1
        code_list = [(string, 1, '1')]
        encoded_word = '1'

    print(str(char_num) + " " + str(word_len))
    # print(code_list)
    for char in sorted(freq_dict.keys()):
        print(char + ": " + encode(code_list, char))
    print(encoded_word)
    # упорядочиваем список по частотам
    # берём две минимальные частоты, добавляем к коду большей 0, меньшей - 1
    # добавляем элемент - сумму букв, с суммой частот
huffman_code(input())