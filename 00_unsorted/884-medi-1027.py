# https://leetcode.com/problems/longest-arithmetic-subsequence/description/
# 01 : 04 : 00
import time
from dataclasses import dataclass


@dataclass(slots=True)
class Subsequence:
    nxt_elem: int
    last_elem: int
    count: int = 0

    def update(self) -> int:
        self.count += 1
        self.nxt_elem, self.last_elem = 2*self.nxt_elem - self.last_elem, self.nxt_elem
        return self.nxt_elem

    @classmethod
    def create(cls, start: int, nxt: int) -> 'Subsequence':
        return Subsequence(
            nxt_elem=2*nxt - start,
            last_elem=nxt,
            count=2,
        )


class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        rlt: int = 2
        seen: set[tuple[int, int]] = set()              # (a,b) in Subsequence.create(a,b)
        vault: dict[int, list[Subsequence]] = dict()    # target 2 list_s of Subsequence
        for idx in range(len(nums)):
            cur = nums[idx]
            if cur in vault:
                seq_s = vault.pop(cur, [])
                while seq_s:
                    s = seq_s.pop()
                    nxt_el = s.update()
                    rlt = s.count if s.count > rlt else rlt
                    if nxt_el not in vault:
                        vault[nxt_el] = []
                    vault[nxt_el].append(s)
            for jdx in range(idx):
                if (nums[jdx], nums[idx]) in seen:
                    continue
                seen.add((nums[jdx], nums[idx]))
                s = Subsequence.create(nums[jdx], nums[idx])
                if s.nxt_elem not in vault:
                    vault[s.nxt_elem] = []
                vault[s.nxt_elem].append(s)
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([20, 1, 15, 3, 10, 5, 8],), 4),
    ]

    foo = Solution()
    method2test = Solution.longestArithSeqLength
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
