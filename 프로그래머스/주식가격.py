"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

https://programmers.co.kr/learn/courses/30/lessons/42584

설명: 설명은 주석에 적어놓음

space complexity : O(prices)
time complextity : O(prices*2)

"""



def solution(prices):
    length = len(prices)
    answer = [i for i in range(length - 1, -1, -1)] #initialize

    stack = [0]
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]: #지금 prices가 전에 쌓아놓은 prices보다 클경우와 쌓아놓은 prices들이 있을경우
            # 쌓여있는 prices의 의미는 이전까지 가격 하락이 한번도 없엇던 애들임
            j = stack.pop() # 지금 prices보다 작은 애를 가져와서
            answer[j] = i - j # 지금 prices에서 쌓아놓은 prices를 빼줌

        stack.append(i)
    return answer
prices	=[1, 2, 3, 2, 3]

print(solution(prices))
#[4, 3, 1, 1, 0]

