"""
원점(0,0)에서 시작해서 아래처럼 숫자가 적힌 방향으로 이동하며 선을 긋습니다.

스크린샷 2018-09-06 오후 4.55.33.png

ex) 1일때는 오른쪽 위로 이동

그림을 그릴 때, 사방이 막히면 방하나로 샙니다.
이동하는 방향이 담긴 배열 arrows가 매개변수로 주어질 때, 방의 갯수를 return 하도록 solution 함수를 작성하세요.

설명: 갓던데를 다시 방문하면 방이 생기는 것이 중요한데 예외에 대한 정의도 중요 지그재그로 갔을때 방이 2개 생기는 문제(for j in range(2)로 해결)
    그리고 갓던데를 다시 방문하지만 와리가리치는거는 안되는 경우를 고려함

space complexity : O(2*arrows?)
time complextity : O(arrows^2)

"""

from collections import defaultdict

def solution(arrows):
    answer = 0
    prev_coord = (0, 0)
    x, y = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]
    visited_coord = defaultdict(list)

    for i_arr in arrows:
        for j in range(2):
            cur_coord = (prev_coord[0]+x[i_arr], prev_coord[1]+y[i_arr])

            if cur_coord in visited_coord and prev_coord not in visited_coord[cur_coord]:
                answer += 1
                visited_coord[cur_coord].append(prev_coord)
                visited_coord[prev_coord].append(cur_coord)
            elif cur_coord not in visited_coord:
                visited_coord[cur_coord].append(prev_coord)
                visited_coord[prev_coord].append(cur_coord)

            prev_coord = cur_coord

    return answer

arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
print(solution(arrows))