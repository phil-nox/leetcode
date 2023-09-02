# https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/description/
# git commit -m "2023_09_02 - 845 - hard - 2842"
import time
import math


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        vault: dict[str, int] = dict()
        desc: list[int]

        for el in s:
            vault[el] = vault.get(el, 0) + 1

        desc = sorted(vault.values(), reverse=True)         # [3, 2, 2, 2, 2, 1]
                                                    # k==3  #  _  _  _          = math.prod

        if k > len(desc):
            return 0

        val, n_comb, idx = desc[0], 1, 1
        while idx < k:
            if desc[idx] == val:
                n_comb += 1
            else:
                n_comb, val = 1, desc[idx]
            idx += 1
                                                            # [3, 2, 2, 2, 2, 1]
        k_comb = n_comb                                     #     -  -          # k_comb==2
        while idx < len(desc) and val == desc[idx]:
            n_comb += 1
            idx += 1
                                                            # [3, 2, 2, 2, 2, 1]
                                                            #     ^  ^  ^  ^    # n_comb==4

        return math.prod(desc[:k]) * math.comb(n_comb, k_comb) % (10**9 + 7)
        

if __name__ == '__main__':
    tests = [
        ('test_00', ('abbcd', 4), 2),
    ]

    foo = Solution()
    method2test = Solution.countKSubsequencesWithMaxBeauty
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
