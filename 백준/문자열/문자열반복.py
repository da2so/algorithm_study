import sys

N = int(input())

a_to_ascii = 97

result = []
for i in range(N):
    repetition, string = sys.stdin.readline().rstrip().split(' ')
    result.append(''.join([str(char)*int(repetition) for char in str(string)]))


[print(i_result) for i_result in result]