# https://leetcode.com/problems/longest-common-prefix/description/
import time


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        end = len(strs[0])

        for idx in range(1, len(strs)):
            cur_word, prev_word = strs[idx], strs[idx-1]
            new_end = 0                                     # next is empty string
            for jdx in range(min(end, len(cur_word))):          # this _for_ don't work for empty string
                new_end = jdx + 1                           # current rune is ok
                if cur_word[jdx] != prev_word[jdx]:         # current rune is no_ok
                    new_end = jdx
                    break
            end = new_end
        return strs[0][:end]


if __name__ == '__main__':
    tests = [
        ('test_00', (["flower","flow","flight"], ), "fl"),
        ('test_01', (["dog","racecar","car"],), ""),
        ('test_02', (["dog",],), "dog"),
        ('test_03', (["flower", "flow", "flow"],), "flow"),
        ('test_04', (["abab","aba",""],), ""),

    ]

    foo = Solution()
    method2test = Solution.longestCommonPrefix   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
