# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/description/
import time


class DataStream:

    def __init__(self, value: int, k: int):
        self.target = value
        self.limit = k
        self.counter = k

    def consec(self, num: int) -> bool:
        if num == self.target and self.counter > 0:
            self.counter -= 1
        elif num != self.target:
            self.counter = self.limit
        return not bool(self.counter)


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)


if __name__ == '__main__':
    tests = [
        ('test_00', ([[4, 3], [4], [4], [4], [3]]), [False, False, True, False]),
    ]

    method2test = DataStream.consec   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        foo = DataStream(*inpt[0])
        test_rlt = [method2test(foo, *el) for el in inpt[1:]]
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

