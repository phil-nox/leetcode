# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/
import time


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        vault: dict[str, set[str]] = dict()
        for one, two in zip(s1, s2):
            s_one, s_two = vault.get(one, None), vault.get(two, None)
            if (s_one, s_two) == (None, None):
                tmp = {one, two}
                vault[one], vault[two] = tmp, tmp
                continue

            if None in (s_one, s_two):
                to_add, target = (one, s_two) if s_one is None else (two, s_one)
                target.add(to_add)
                vault[to_add] = target
                continue

            if s_one is not s_two:
                s_one.update(s_two)
                for el in s_two:
                    vault[el] = s_one

        converter: dict[str, str] = {key: min(val) for key, val in vault.items()}
        return ''.join([converter.get(el, el) for el in baseStr])


if __name__ == '__main__':
    tests = [
        ('test_00', ("parker", "morris", "parser"), "makkek"),
        ('test_01', ("hello", "world", "hold"), "hdld"),
        ('test_02', ("leetcode", "programs", "sourcecode"), "aauaaaaada"),
    ]

    foo = Solution()
    method2test = Solution.smallestEquivalentString   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
