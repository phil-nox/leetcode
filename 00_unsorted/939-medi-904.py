# https://leetcode.com/problems/fruit-into-baskets/description/
import time
import tmp

'''
patterns to count:
    x-y
    x-y-x
    x-y-[x-y]-
'''


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        type_count, cur_t, cur_c = [], -1, 0
        for el in fruits:
            if cur_t == el:
                cur_c += 1
                continue
            if cur_t != -1:
                type_count.append((cur_t, cur_c))
            cur_t, cur_c = el, 1
        type_count.append((cur_t, cur_c))

        rlt: int = type_count[len(type_count)-1][1]     # len(fruits) = 1   # fruits = [7]
        idx = -1
        while (idx := idx + 1) < len(type_count)-1:
            start_type, pair_type = type_count[idx][0], type_count[idx + 1][0]
            jdx, tmp = idx + 1, type_count[idx][1] + type_count[idx + 1][1]
            while (jdx := jdx + 1) < len(type_count):
                if type_count[jdx][0] not in (start_type, pair_type):
                    break
                tmp += type_count[jdx][1]
                if type_count[jdx][0] == start_type:
                    idx = jdx - 1
            rlt = tmp if tmp > rlt else rlt
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 2, 1],), 3),
        ('test_01', ([0, 1, 2, 2],), 3),
        ('test_02', ([1, 2, 3, 2, 2],), 4),
        ('test_03', ([1, 1, 2, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2],), 8),
        ('test_04', ([0],), 1),
        ('test_05', ([1, 0, 1, 4, 1, 4, 1, 2, 3],), 5),
        ('test_71', ([0, 1] * 20000,), 40000)
    ]

    foo = Solution()
    method2test = Solution.totalFruit

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
