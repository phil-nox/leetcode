# https://leetcode.com/problems/domino-and-tromino-tiling/description/
import time

'''
   ─┬────
   1│       |
   ─┘       |
        ─────────
     all=1     1=self


   ─┬────
   2│    ||   --
   ─┘    ||   --
        ─────────
     all=2     1=self


   ─┬────
   3│    |||          |--          ┌-|
   ─┘    |||          |--          |-┘


         --|                       |-┐
         --|                       └-|

        ────────────────────────────────
  5=all= all_of_2   + all_of_1   + self =2
         *self_of_1   *self_of_2



   ─┬────
   4│    ||||  |--|  ┌-||        ||--            |┌-|           ┌--┐
   ─┘    ||||  |--|  |-┘|        ||--            ||-┘           |--|


         --||        |-┐|        ----            ||-┐           |--|
         --||        └-||        ----            |└-|           └--┘

        ─────────────────────────────────────────────────────────────
 11=all= all_of_3              + all_of_2      + all_of_1     + self =2
         *self_of_1              *self_of_2      *self_of_3

'''


class Solution:
    def numTilings(self, n: int) -> int:
        pre_result = [1, 2]
        if n < 2:
            return pre_result[n-1]

        for idx in range(n):
            total = 2 + pre_result[-1] + pre_result[-2]
            for pre_rlt in pre_result[:-2]:
                total += pre_rlt * 2
            pre_result.append(total)

        return pre_result[n-1] % (10**9 + 7)


if __name__ == '__main__':
    foo = Solution()
    time_diff = -time.perf_counter()
    for name, inpt, outpt in [
        ('test_00', (3,), 5),
        ('test_01', (1,), 1),
        ('test_02', (4,), 11),
    ]:
        if name == 'test_0':
            print(foo.numTilings(*inpt))
            quit()
        assert foo.numTilings(*inpt) == outpt, print('👉', name, foo.numTilings(*inpt), 'vs', outpt)
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

