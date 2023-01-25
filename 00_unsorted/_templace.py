import time


class Solution:
    pass


if __name__ == '__main__':
    tests = [
        ('test_00', ([0, 1], 20), 2),
    ]

    foo = Solution()
    method2test = Solution.__name_of_the_method__

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
