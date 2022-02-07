
# 파이썬의 장점을 살린 퀵 정렬
def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1: return array

    pivot, tail = array[0], array[1:]

    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]

    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)

A = [38, 27, 43, 3, 9, 82, 10]
print(quick_sort(A))
