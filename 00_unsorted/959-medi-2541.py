# https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/description/
import time


class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pos, neg = 0, 0
        if k == 0:
            return 0 if nums1 == nums2 else -1
        for el_1, el_2 in zip(nums1, nums2):
            val_1, check_1 = divmod(el_1, k)
            val_2, check_2 = divmod(el_2, k)
            if check_1 != check_2:
                return -1
            if el_1 > el_2:
                neg += val_1 - val_2
            else:
                pos += val_2 - val_1
        return pos if pos == neg else -1


if __name__ == '__main__':
    tests = [
        ('test_00', ([4, 3, 1, 4], [1, 3, 7, 1], 3), 2),
        ('test_01', ([3, 8, 5, 2], [2, 4, 1, 6], 1), -1),
    ]

    foo = Solution()
    method2test = Solution.minOperations   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
