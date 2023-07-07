# https://leetcode.com/problems/merge-sorted-array/description/
import time


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        m, n = m - 1, n - 1
        for idx in range(m + n + 1, -1, -1):
            if n < 0:
                nums1[idx], m = nums1[m], m - 1
                continue

            if m < 0:
                nums1[idx], n = nums2[n], n - 1
                continue

            if nums1[m] < nums2[n]:
                nums1[idx], n = nums2[n], n - 1
                continue

            nums1[idx], m = nums1[m], m - 1



if __name__ == '__main__':
    tests = [
        ('test_00', (__test_args__), 2),
    ]

    foo = Solution()
    method2test = Solution.merge
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
