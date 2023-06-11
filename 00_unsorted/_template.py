# _link
# _git_commit
import time


# _class_Solution:


if __name__ == '__main__':
    tests = [
        ('test_00', (__test_args__), 2),
    ]

    foo = Solution()
# _method2test = Solution.

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
