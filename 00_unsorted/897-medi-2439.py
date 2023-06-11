# https://leetcode.com/problems/minimize-maximum-of-array/description/
import time

# 5, 5, 5, 5, 7
# holes = -2
# divmod(2, 5) = 0, 2 ->    top = 6, holes = 3
#                           top += core+1, holes = elem - rest

# 5, 5, 5, 5, 10
# holes = -5
# divmod(5, 5) = 1, 0 ->    top = 7, holes = 0
#                           top += core+1, holes = 0

# 5, 5, 5, 5, 11
# holes = -6
# divmod(6, 5) = 1, 1 ->    top = 7, holes = elem - rest


class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        top, holes, elems = nums[0], 0, 1
        for el in nums[1:]:
            elems, holes = elems + 1, holes - el + top  # holes -= el - top
            if holes < 0:
                core, rest = divmod(-holes, elems)
                top, holes = (top + core, 0) if rest == 0 else (top + 1 + core, elems - rest)
        return top
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([3, 7, 1, 6],), 5),
    ]

    foo = Solution()
    method2test = Solution.minimizeArrayValue

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
