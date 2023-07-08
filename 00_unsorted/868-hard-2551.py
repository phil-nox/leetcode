# https://leetcode.com/problems/put-marbles-in-bags/description/
import time


class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        if k == 1:
            return 0
        vault = [weights[idx - 1] + weights[idx] for idx in range(1, len(weights))]
        vault.sort()
        return sum(vault[-k+1:]) - sum(vault[:k-1])


if __name__ == '__main__':
    tests = [
        ('test_00', (__test_args__), 2),
    ]

    foo = Solution()
    method2test = Solution.putMarbles
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
