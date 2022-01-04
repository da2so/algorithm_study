# -*- coding: utf-8 -*-
"""
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.v

https://programmers.co.kr/learn/courses/30/lessons/42839

설명: 해당 숫자가 소수가 아닐경우 약수들이 대칭적으로 곱해지므로(2x8, 8x2) 해당하느 수의 반만 비교하면 된다. 그리고 permuation을 통해 순열을 제조

space complexity : O()
time complextity : O()

"""
from itertools import permutations

def solution(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1): #대칭
            if num % i == 0:
                return False
        return True

    temp = set()

    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i): #순열 제조
            if is_prime(int("".join(j))):
                temp.add(int("".join(j)))

    return len(temp)

numbers = "17"

print(solution(numbers))