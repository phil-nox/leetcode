# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/
import time
from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        backward_id, forward_idx = startIndex + 1, startIndex - 1
        for step in range(len(words)):
            backward_id = backward_id - 1 if backward_id > 0 else len(words) - 1
            forward_idx = forward_idx + 1 if forward_idx < len(words) - 1 else 0
            if target == words[backward_id] or target == words[forward_idx]:
                return step
        return -1


if __name__ == '__main__':
    foo = Solution()
    time_diff = -time.perf_counter()
    for name, inpt, outpt in [
        ('test_00', (["hello","i","am","leetcode","hello"], "hello", 1), 1),
        ('test_01', (["a","b","leetcode"], "leetcode", 0), 1),
        ('test_02', (["i","eat","leetcode"], "ate", 0), -1),
    ]:
        if name == 'test_0':
            print(foo.closetTarget(*inpt))
            quit()
        assert foo.closetTarget(*inpt) == outpt, print('👉', name, foo.closetTarget(*inpt), 'vs', outpt)
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
