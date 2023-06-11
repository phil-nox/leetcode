# https://leetcode.com/problems/find-the-substring-with-maximum-cost/description/
import time


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        vault: dict[str, int] = {el: idx + 1 for idx, el in enumerate('abcdefghijklmnopqrstuvwxyz')}
        for c, v in zip(chars, vals):
            vault[c] = v
        rlt, pos, neg = 0, 0, 0
        collecting_pos = True  # False - collecting_negative
        for el in s:
            val = vault[el]
            if collecting_pos and val > -1:
                pos += val
            elif not collecting_pos and val < 0:
                neg += val
            elif collecting_pos and val < 0:             # switch to negative collecting
                neg = val
                collecting_pos = not collecting_pos
            else:  # not collecting_pos and val > -1     # switch to positive collecting
                rlt = max(rlt, pos)
                pos = val if pos < -neg else val + pos + neg
                neg = 0
        return max(rlt, pos, pos + neg)
        

if __name__ == '__main__':
    tests = [
        ('test_00', ('adaa', 'd', [-1000]), 2),
        ('test_01', ('abc', 'abc', [-1, -1, -1]), 0),
    ]

    foo = Solution()
    method2test = Solution.maximumCostSubstring

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
