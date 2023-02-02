# https://leetcode.com/problems/verifying-an-alien-dictionary/description/
import time


class Solution:

    def _lt_or_eq(self, word1: str, word2: str, d_order: dict[str, int]) -> bool:
        for el_1, el_2 in zip(word1, word2):
            if d_order[el_1] < d_order[el_2]:
                return True
            if d_order[el_1] > d_order[el_2]:
                return False
        return False if len(word1) > len(word2) else True

    def isAlienSorted(self, words: list[str], order: str) -> bool:
        d_order = {el: idx+1 for idx, el in enumerate(order)}
        for idx in range(1, len(words)):
            if not self._lt_or_eq(words[idx-1], words[idx], d_order):
                return False
        return True


if __name__ == '__main__':
    tests = [
        ('test_00', (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), True),
        ('test_01', (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"), False),
        ('test_02', (["apple", "app"], "abcdefghijklmnopqrstuvwxyz"), False),
    ]

    foo = Solution()
    method2test = Solution.isAlienSorted

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
