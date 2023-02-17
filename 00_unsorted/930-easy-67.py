# https://leetcode.com/problems/add-binary/description/
import time


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rlt, rest = [], 0
        small, big = (a, b) if len(a) < len(b) else (b, a)
        idx, jdx = len(small), len(big)
        while (jdx := jdx - 1) > -1:
            if (idx := idx - 1) > -1:
                rest += 1 if small[idx] == '1' else 0
            rest += 1 if big[jdx] == '1' else 0
            rest, tmp = divmod(rest, 2)
            rlt.append('1' if tmp else '0')
        if rest:
            rlt.append('1')
        return ''.join(reversed(rlt))


if __name__ == '__main__':
    tests = [
        ('test_00', ('11', '1'), '100'),
        ('test_01', ('1010', '1011'), '10101'),  # 11110
    ]

    foo = Solution()
    method2test = Solution.addBinary

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
