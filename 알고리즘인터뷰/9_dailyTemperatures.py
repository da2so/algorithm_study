#매일의 화씨 온도 리스트 T를 입력받아서, 더 따듯한 날씨를 위해서는 며칠을 더 기다려야 하는지 출력하라
from typing import List
def dailyTemperatures(T: List)-> List:
    stack = []
    answer = [0] * len(T)

    for i, t in enumerate(T):

        while stack and t > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))