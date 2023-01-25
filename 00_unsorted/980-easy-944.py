# https://leetcode.com/problems/delete-columns-to-make-sorted/description/
import time


class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        rlt = 0
        for idx in range(len(strs[0])):
            prev_rune = strs[0][idx]
            for word in strs[1:]:
                if prev_rune > word[idx]:
                    rlt += 1
                    break
                prev_rune = word[idx]
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', (["abc", "bce", "cae"],), 1),
        ('test_01', (["cba", "daf", "ghi"],), 1),
        ('test_02', (["a", "b"],), 0),
        ('test_03', (["zyx", "wvu", "tsr"],), 3),
    ]

    foo = Solution()
    method2test = Solution.minDeletionSize   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
