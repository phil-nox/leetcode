# https://leetcode.com/problems/snakes-and-ladders/description/
import time
from dataclasses import dataclass, field
import heapq


@dataclass(slots=True)
class Path:
    moves: int
    position: int
    seen: set[int] = field(default_factory=set)

    def __lt__(self, other):
        return (self.moves, -self.position) < (other.moves, -other.position)

    def process(self, route: list[int]) -> list['Path']:
        rlt = []
        organic_move = None
        for idx in range(1, 7):
            if self.position + idx >= len(route):
                break
            nxt_pos = self.position + idx
            if route[nxt_pos] != -1 and nxt_pos not in self.seen:
                self.seen.add(nxt_pos)
                rlt.append(Path(moves=self.moves+1, position=route[nxt_pos]-1, seen=self.seen.copy()))
                continue
            organic_move = nxt_pos

        if organic_move is not None and organic_move not in self.seen:
            self.seen.add(organic_move)
            self.moves += 1
            self.position = organic_move
            rlt.append(self)
        return rlt


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        route: list[int] = list()
        direct = True
        for el in reversed(board):
            if direct:
                route.extend(el)
            else:
                route.extend(reversed(el))
            direct = not direct

        ways: list[Path] = list()
        heapq.heappush(ways, Path(moves=0, position=0))

        while len(ways) > 0:
            cur = heapq.heappop(ways)
            for el in cur.process(route):
                if el.position == len(route) - 1:
                    return el.moves
                heapq.heappush(ways, el)
        return -1


if __name__ == '__main__':
    tests = [
        ('test_00', ([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]],), 4),
        ('test_02', ([[-1,-1],[-1,3]],), 1),
        ('test_06', ([[1, 1, -1], [1, 1, 1], [-1, 1, 1]],), -1),
    ]

    foo = Solution()
    method2test = Solution.snakesAndLadders

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
