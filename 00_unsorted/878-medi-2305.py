# https://leetcode.com/problems/fair-distribution-of-cookies/description/
# git commit -m "2023_07_01 - 878 - medi - 2305"
import time

'''
# Solution without dataclass

class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        rlt = 10**6
        stack = [(tuple(), k, 0)]

        while stack:
            child_s, waiting, nxt_idx = stack.pop()
            if not nxt_idx < len(cookies):
                rlt = min(rlt, max(child_s))
                continue

            for idx in range(len(child_s)):
                if (tmp := child_s[idx] + cookies[nxt_idx]) > rlt:
                    continue
                stack.append(((*child_s[:idx], tmp, *child_s[idx + 1:]), waiting, nxt_idx + 1,))
            if waiting > 0:
                stack.append(((*child_s, cookies[nxt_idx]), waiting - 1, nxt_idx + 1,))

        return rlt
'''

from dataclasses import dataclass


@dataclass(slots=True)
class Task:
    child_s: tuple[int, ...]
    waiting: int
    nxt_idx: int

    def nxt(self, cookies: list[int], top: int) -> list['Task']:
        rlt: list['Task'] = []
        for idx in range(len(self.child_s)):
            if self.child_s[idx] + cookies[self.nxt_idx] > top:
                continue
            rlt.append(Task(
                child_s=(*self.child_s[:idx], self.child_s[idx] + cookies[self.nxt_idx], *self.child_s[idx+1:]),
                waiting=self.waiting,
                nxt_idx=self.nxt_idx + 1,
            ))
        if self.waiting > 0:
            rlt.append(Task(
                child_s=(*self.child_s, cookies[self.nxt_idx]),
                waiting=self.waiting - 1,
                nxt_idx=self.nxt_idx + 1,
            ))
        return rlt


class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        rlt = 10**6
        stack = [Task(child_s=tuple(), waiting=k, nxt_idx=0)]

        while stack:
            cur = stack.pop()
            if not cur.nxt_idx < len(cookies):   # task is done
                rlt = min(rlt, max(cur.child_s))
                continue

            stack.extend(cur.nxt(cookies, top=rlt))

        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 2, 3], 2), 3),
        ('test_29', ([76265, 7826, 16834, 63341, 68901, 58882, 50651, 75609], 8), 76265),
    ]

    foo = Solution()
    method2test = Solution.distributeCookies
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
