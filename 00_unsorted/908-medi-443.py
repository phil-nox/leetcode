# https://leetcode.com/problems/string-compression/description/
import time


class Solution:
    def _add_number(self, chars: list[str], idx: int, count: int) -> int:
        count += 1
        sdx = idx
        while count != 0:
            chars[idx], idx = chr(count % 10 + 48), idx + 1
            count //= 10
        edx = idx - 1
        while sdx < edx:
            chars[sdx], chars[edx] = chars[edx], chars[sdx]
            sdx, edx = sdx + 1, edx - 1
        return idx

    def compress(self, chars: list[str]) -> int:
        idx, count, target = 0, 0, chars[0]
        for el in chars[1:]:
            if target == el:
                count += 1
                continue
            chars[idx], target, idx = target, el, idx + 1
            if count != 0:
                idx, count = self._add_number(chars, idx, count), 0
        chars[idx], idx = target, idx + 1
        if count != 0:
            idx = self._add_number(chars, idx, count)
        return idx


if __name__ == '__main__':
    tests = [
        ('test_00', (["a", "a", "b", "b", "c", "c", "c"],), 6),
        ('test_01', (["a"],), 1),
        ('test_02', (["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],), 4),
        ('test_03', (["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],), 3),
    ]

    foo = Solution()
    method2test = Solution.compress

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
