
"""
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

https://programmers.co.kr/learn/courses/30/lessons/42895

설명: 주어진 N이 1개 사용가능할때 가능한 조합수(A)를 저장해놓고 2개 가능할때 조합수를 구할때 A를 이용하여 조합수를 저장함(B) 그리고 3개 가능할때 저장된 A,B를 이용해 조합수 구함
이렇게 계속 dynamic programming을 통해 M번 사용됐을 경우에 찾고싶은 수가 있는지 확인하여 return


space complexity : O() 모르겟다
time complextity : O() 모르겟다

"""

def solution(N, number):

    combination = [{int(str(N)*i)}for i in range(1, 9)]
    combination.insert(-1000000, 0) #dummy
    print(combination)
    for i in range(1, 9):
        for j in range(1, i):
            for x in combination[j]:
                for y in combination[i-j]:
                    combination[i].add(x+y)
                    combination[i].add(x-y)
                    combination[i].add(x*y)

                    if y !=0:
                        combination[i].add(x//y)
        if number in combination[i]:
            return i
    return -1



N = 2
number = 11

print(solution(N, number))