# https://leetcode.com/problems/maximum-running-time-of-n-computers/description/
import time

''' n = 3    [9, 8, 5, 3, 1]  

* * *
* * 
* * 
* *
* * *
* * *
* * * | *
* * * | *
* * * | * *

full_price - 3
1 discount_with_price   - 2
3 discount_s_with_price - 1
rlt = 5
rest = 4
--
return 8
'''


class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        batteries.sort(reverse=True)
        discount_s: list[tuple[int, int]] = []  # tuple[price, count_s]

        rlt: int = batteries[n - 1]
        rest: int = sum(batteries[n:])

        cur: int = batteries[0]
        for idx, el in enumerate(batteries[1:n]):
            idx += 1
            if el != cur:
                discount_s.append((n - idx, cur - el))
                cur = el

        while rest != 0 and discount_s:
            price, count = discount_s.pop()
            if count > rest // price:
                rlt += rest // price
                return rlt
            rlt += count
            rest -= count * price

        rlt += rest // n
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', (3, [9, 8, 5, 3, 1]), 8),
    ]

    foo = Solution()
    method2test = Solution.maxRunTime
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
