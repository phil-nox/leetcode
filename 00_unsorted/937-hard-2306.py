# https://leetcode.com/problems/naming-a-company/description/
import time
import data_for_937

'''
"alrgtxxdj"
"illqfngl"
"rlrgtxxdj"

            {'a': 1, 'i': 1, 'r': 1}
lrgtxxdj    {'i': 1}                    +1 False must be +2
llqfngl     {'r': 1, 'a': 1}            +2

##################

"coffee"
"donuts"
"time"
"toffee"

        {'c': 1, 'd': 1, 't': 2}
offee   {'d': 1}                        +1 
onuts   {'c': 1, 't': 2}                +3
ime     {'c': 1, 'd': 1}                +2  False - time+coffee - no_valid
'''


class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        rune2tails: dict[str, set[str]] = dict()

        # phase_0 - setup
        for el in ideas:
            tmp = rune2tails.get(el[0], set())
            tmp.add(el[1:])
            rune2tails[el[0]] = tmp

        # phase_1 - counting
        rlt = 0
        key = list(rune2tails.keys())
        for idx in range(len(key)):
            for jdx in range(idx + 1, len(key)):
                common = rune2tails[key[idx]].intersection(rune2tails[key[jdx]])
                rlt += (len(rune2tails[key[idx]]) - len(common)) * (len(rune2tails[key[jdx]]) - len(common)) * 2
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', (["coffee", "donuts", "time", "toffee"],), 6),
        ('test_01', (["lack", "back"],), 0),
        ('test_02', (["alrgtxxdj", "illqfngl", "rlrgtxxdj"],), 4),
        ('test_75', (data_for_937.test_75,), 24648826),
    ]

    foo = Solution()
    method2test = Solution.distinctNames

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
