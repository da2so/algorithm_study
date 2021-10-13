
alphabet = str(input())

a_to_ascii = 97

result = []
for i_ascii in range(a_to_ascii, 10000):
    result.append(alphabet.find(chr(i_ascii)))

    if chr(i_ascii) == 'z':
        break

[print(i_result, end=' ') for i_result in result]