# https://leetcode.com/problems/handling-sum-queries-after-update/description/
import time
import data_for_922


class Solution:
    def handleQuery(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        rlt: list[int] = []
        cur: int = sum(nums2)                                                               # example
        ones: int = int(''.join([str(el) for el in nums1]), 2)                              # 0101010101
        mask: int
        for opr in queries:
            if opr[0] == 1:
                # mask = (1 << len(nums1)) - 1                                              # 11111111   len(nums1) = 8
                # mask >>= opr[1]                                                           # 00011111        start = 3
                # mask = mask >> (len(nums1) - opr[2] - 1) << (len(nums1) - opr[2] - 1)     # 00011110          end = 6

                mask = (1 << (opr[2] - opr[1] + 1)) - 1                                     # 00001111  short_version
                mask <<= len(nums1) - opr[2] - 1                                            # 00011110
                ones ^= mask
            elif opr[0] == 2:
                cur += ones.bit_count() * opr[1]
            else:
                rlt.append(cur)
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 0, 1], [0, 0, 0], [[1, 1, 1], [2, 1, 0], [3, 0, 0]]), [3]),
        ('test_01', ([1], [5], [[2, 0, 0], [3, 0, 0]]), [5]),
        ('test_72', data_for_922.test_72, data_for_922.outpt_72),
    ]

    foo = Solution()
    method2test = Solution.handleQuery

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
    # 1th solution - 22+ sec
    # 2th solution -  6+ sec
    # 3th solution -  3+ sec    # tmp3.py
