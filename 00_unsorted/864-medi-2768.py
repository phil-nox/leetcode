# https://leetcode.com/problems/put-marbles-in-bags/description/
import time


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        vault = {idx: 0 for idx in range(5)}
        vault[0] = (m - 1) * (n - 1)
        seen = set()

        for i, j in coordinates:
            seen.add((i, j))
            for a, b, c in (
                    ((i - 1, j - 1), (i - 1, j), (i, j - 1)),
                    ((i - 1, j), (i - 1, j + 1), (i, j + 1)),
                    ((i, j - 1), (i + 1, j - 1), (i + 1, j)),
                    ((i, j + 1), (i + 1, j + 1), (i + 1, j)),
            ):
                if -1 in (*a, *b, *c) or m in (a[0], b[0], c[0]) or n in (a[1], b[1], c[1]):
                    continue
                tmp = 1
                for pnt in (a, b, c):
                    tmp = tmp + 1 if pnt in seen else tmp

                vault[tmp - 1] = vault[tmp - 1] - 1
                vault[tmp] = vault[tmp] + 1

        return [vault[idx] for idx in range(5)]


if __name__ == '__main__':
    tests = [
        ('test_00', (3, 3, [[0, 0], [1, 1], [0, 2]]), [0, 2, 2, 0, 0]),
    ]

    foo = Solution()
    method2test = Solution.countBlackBlocks
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
