# https://leetcode.com/problems/jump-game/description/
import time
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        required_val = 0
        for el in reversed(nums[:-1]):
            required_val += 1
            if el >= required_val:
                required_val = 0
        return not required_val


if __name__ == '__main__':
    foo = Solution()
    time_diff = -time.perf_counter()
    for name, inpt, outpt in [
        ('test_00', ([2,3,1,1,4],), True),
        ('test_01', ([3,2,1,0,4],), False),
        ('test_02', ([0,1],), False),
    ]:
        if name == 'test_0':
            print(foo.canJump(*inpt))
            quit()
        assert foo.canJump(*inpt) == outpt, print('👉', name, foo.canJump(*inpt), 'vs', outpt)
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

