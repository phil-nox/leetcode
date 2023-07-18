# https://leetcode.com/problems/lru-cache/description/
import time
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.vault: OrderedDict[int, int] = OrderedDict.fromkeys(range(-capacity, 0))

    def get(self, key: int) -> int:
        if key not in self.vault:
            return -1
        self.vault.move_to_end(key, last=True)
        return self.vault[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.vault:
            self.vault.popitem(last=False)
        else:
            self.vault.move_to_end(key, last=True)
        self.vault[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    tests = [
        ('test_00', (__test_args__), 2),
    ]

    foo = Solution()
    method2test = Solution.__init__
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
