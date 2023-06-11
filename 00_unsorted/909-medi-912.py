# https://leetcode.com/problems/sort-an-array/description/
import time
from collections import deque


class Solution:
    def _merge_step(self, a: deque, b: deque) -> deque:
        """ Merging two deque """
        rlt = deque()
        while a and b:
            rlt.append(b.popleft() if a[0] > b[0] else a.popleft())
        rlt.extend(b if b else a)
        return rlt

    def _merge_setup(self, nums: list[int]) -> deque:
        """ Create an initial parts for merging
        Example:
            input : [5, 1, 1, 2, 0, 0, 7]
            output: deque([deque([5]), deque([1, 1]), deque([0, 2]), deque([0, 7])])
        """
        rlt, begin = (deque(), 1) if len(nums) % 2 == 0 else (deque((deque(nums[:1]),)), 2)
        for idx in range(begin, len(nums), 2):
            rlt.append(deque((nums[idx - 1],)))
            rlt[-1].appendleft(nums[idx]) if nums[idx - 1] > nums[idx] else rlt[-1].append(nums[idx])
        return rlt

    def sortArray(self, nums: list[int]) -> list[int]:
        wave, nxt_wave = self._merge_setup(nums), deque()
        while len(wave) > 1:
            nxt_wave.append(self._merge_step(wave.popleft(), wave.popleft()))
            if len(wave) == 1:
                nxt_wave.append(self._merge_step(nxt_wave.pop(), wave.popleft()))
            if not wave:    # process of merging parts of similar length is completely - move on
                wave, nxt_wave = nxt_wave, wave

        return list(wave[0]) if wave else []


if __name__ == '__main__':
    tests = [
        ('test_00', ([],), []),
        ('test_00', ([1],), [1]),
        ('test_01', ([5, 2, 3, 1],), [1, 2, 3, 5]),
        ('test_00', ([2, 3, 1],), [1, 2, 3]),
        ('test_02', ([5, 1, 1, 2, 0, 0, 7],), [0, 0, 1, 1, 2, 5, 7]),
    ]

    foo = Solution()
    method2test = Solution.sortArray

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
