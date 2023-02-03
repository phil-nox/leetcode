# https://leetcode.com/problems/zigzag-conversion/description/
import time


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        words = [[] for el in range(numRows)]
        idx, diff = 0, +1
        for el in s:
            words[idx].append(el)
            idx += diff
            if idx == numRows:
                idx, diff = numRows - 2, -1     # boundary_corner_case: numRows > 1
            elif idx == -1:
                idx, diff = 1, +1
        return ''.join([''.join(word) for word in words])


if __name__ == '__main__':
    tests = [
        ('test_00', ("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
        ('test_01', ("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),

    ]

    foo = Solution()
    method2test = Solution.convert

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
