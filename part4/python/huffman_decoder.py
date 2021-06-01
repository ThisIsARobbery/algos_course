
line = input()

num_chars = int(line.split()[0])
num_code_chars = int(line.split()[1])

huffman_mapping = {}
for _ in range(num_chars):
    read_str = input().split(': ')
    char_val = read_str[0]
    code_val = read_str[1]
    huffman_mapping[code_val] = char_val

code_string = input()

expected_codeval = ''
prev_codevalue = ''
result_string = ''
expected_codeval = ''
for i in range(0, len(code_string)):
    character = code_string[i]
    expected_codeval += character
    if expected_codeval in huffman_mapping:
        result_string += huffman_mapping[expected_codeval]
        expected_codeval = ''

print(result_string)
