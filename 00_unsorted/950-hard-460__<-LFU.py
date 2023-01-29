# https://leetcode.com/problems/lfu-cache/description/
import time
from collections import OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self._limit:    int = capacity
        self._len:      int = 0
        self.count:     dict[int, OrderedDict] = dict()
        self.key2count: dict[int, int] = dict()

    def debug(self):
        print(self.key2count)
        for key, val in sorted(self.count.items()):
            print(key, val)

    def _push(self, key: int, value: int, cnt: int):
        nxt_vault: OrderedDict = self.count.get(cnt, OrderedDict())
        nxt_vault[key] = value
        self.count[cnt] = nxt_vault
        self.key2count[key] = cnt

    def _pop(self, key: int, cnt: int) -> int:
        vault: OrderedDict = self.count.get(cnt)
        rlt = vault.pop(key)
        if len(vault) == 0:
            del self.count[cnt]
        return rlt

    def get(self, key: int) -> int:
        if (cnt := self.key2count.get(key, None)) is None:
            return -1
        value = self._pop(key, cnt)
        self._push(key, value, cnt+1)
        return value

    def put(self, key: int, value: int) -> None:
        if self._limit == 0:
            return
        if (cnt := self.key2count.get(key, None)) is not None:
            self._pop(key, cnt)
            self._push(key, value, cnt+1)
            return

        if self._len < self._limit:
            self._len += 1
        else:                                       # remove
            val_count, vault = min(self.count.items())
            to_remove, _ = vault.popitem(last=False)
            if len(vault) == 0:
                del self.count[val_count]
            del self.key2count[to_remove]
        self._push(key, value, 1)


if __name__ == '__main__':
    time_diff = -time.perf_counter()
    a = ["LFUCache",LFUCache.put,LFUCache.put,LFUCache.get,LFUCache.put,LFUCache.get,LFUCache.get,LFUCache.put,LFUCache.get,LFUCache.get,LFUCache.get]
    b = [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]

    foo = LFUCache(10)
    for el_a, el_b in zip(a[1:], b[1:]):
        print()
        print(el_b)
        print(el_a(foo, *el_b))
        foo.debug()

    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
