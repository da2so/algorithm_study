#한번의 거래에 최대 이익을 산출하라
from typing import List
import sys
def maxProfit(nums: List[int]) -> int:
    profit = 0
    min_val = sys.maxsize

    for num in nums:
        min_val = min(num, min_val)
        profit = max(profit, num - min_val)
    return profit

nums = [7, 1, 5, 3, 6, 4]
print(maxProfit(nums))