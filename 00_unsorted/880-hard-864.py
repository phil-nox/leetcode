# https://leetcode.com/problems/shortest-path-to-get-all-keys/description/

import time
from dataclasses import dataclass
from collections import deque


@dataclass(slots=True)
class WalkKeys:
    x:      int
    y:      int
    moves:  int
    keys:   frozenset


class Solution:

    def shortestPathAllKeys(self, grid: list[str]) -> int:
        goal:   int = 0
        to_do:  deque = deque([])                       # [WalkKeys]
        seen: set[int, int, frozenset] = set()          # { (x, y, keys_set) }
        for idx in range(len(grid)):
            for jdx in range(len(grid[0])):
                if grid[idx][jdx] == '@':
                    to_do.append(WalkKeys(moves=0, keys=frozenset(), x=idx, y=jdx))
                    seen.add((idx, jdx, to_do[-1].keys))
                if grid[idx][jdx] in 'abcdef':
                    goal += 1

        while to_do:
            walk: WalkKeys = to_do.popleft()
            for ndx, mdx in (
                    (walk.x + 1, walk.y),
                    (walk.x - 1, walk.y),
                    (walk.x, walk.y + 1),
                    (walk.x, walk.y - 1),
            ):
                if ndx < 0 or ndx >= len(grid) or mdx < 0 or mdx >= len(grid[0]):           # +-out_grid_logic
                    continue                                                                # |

                if (ndx, mdx, walk.keys) in seen:                                           # +-seen_logic
                    continue                                                                # | not only position matter
                seen.add((ndx, mdx, walk.keys))                                             # | but current keys_set

                if grid[ndx][mdx] == '#':                                                   # wall
                    continue

                if grid[ndx][mdx] in 'ABCDEF' and grid[ndx][mdx].lower() not in walk.keys:  # lock_without_key
                    continue

                if grid[ndx][mdx] in 'abcdef' and grid[ndx][mdx] not in walk.keys:
                    to_do.append(
                        WalkKeys(
                            moves=walk.moves + 1,
                            x=ndx,
                            y=mdx,
                            keys=frozenset(walk.keys | {grid[ndx][mdx]}),
                        )
                    )
                    if len(to_do[-1].keys) == goal:
                        return to_do[-1].moves
                    continue
                to_do.append(WalkKeys(moves=walk.moves + 1, x=ndx, y=mdx, keys=walk.keys))

        return -1


if __name__ == '__main__':
    tests = [
        ('test_00', (["@..aA", "..B#.", "....b"],), 6),
    ]

    foo = Solution()
    method2test = Solution.shortestPathAllKeys
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
