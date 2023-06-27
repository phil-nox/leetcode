# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
# 00 : 48 : 05 (00 : 30 : 00 - bad_logic)
import time
import heapq

'''
(0,0) (0,1) (0,2) | x n | x n | x x n |
(1,0) (1,1) (1,2) | n   | x   | x n   |
(2,0) (2,1) (2,2) |     | n   | n     |
'''


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        vault = [(nums1[0] + nums2[0], 0, 0)]
        rlt = []
        while k > 0 and vault:
            k -= 1
            _, idx, jdx = heapq.heappop(vault)
            rlt.append([nums1[idx], nums2[jdx]])
            if idx + 1 < len(nums1):
                heapq.heappush(vault, (nums1[idx + 1] + nums2[jdx], idx + 1, jdx))
            if idx == 0 and jdx + 1 < len(nums2):
                heapq.heappush(vault, (nums1[idx] + nums2[jdx + 1], idx, jdx + 1))
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 1, 2], [1, 2, 3], 10),
         [[1, 1], [1, 1], [2, 1], [1, 2], [1, 2], [2, 2], [1, 3], [1, 3], [2, 3]]),
    ]

    foo = Solution()
    method2test = Solution.kSmallestPairs
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
