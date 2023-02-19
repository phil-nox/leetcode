# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/
import time


class Solution:
    def _remapping(self, num: int, target: str, ignore: str) -> int:
        pre_rlt: list[str] = []
        replacer: dict[str, str] = dict()
        for el in str(num):
            if el is ignore:
                pre_rlt.append(el)
                continue
            if len(replacer) < 1:
                replacer[el] = target
            pre_rlt.append(replacer.get(el, el))
        return int(''.join(pre_rlt))

    def minMaxDifference(self, num: int) -> int:
        return self._remapping(num=num, target='9', ignore='9') - self._remapping(num=num, target='0', ignore='')


if __name__ == '__main__':
    tests = [
        ('test_00', (11891,), 99009),
        ('test_01', (90,), 99),
    ]

    foo = Solution()
    method2test = Solution.minMaxDifference

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
