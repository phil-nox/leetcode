# https://leetcode.com/problems/fizz-buzz/description/
# git commit -m "2023_08_31 - 849 - easy -  412"
import time


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        return list(("Fizz" * (not x % 3) + "Buzz" * (not x % 5) or str(x) for x in range(1, n + 1)))
        ''' # first_try
        nxt_3: int = 3
        nxt_5: int = 5
        rlt: list[str] = []

        for i in range(1, n+1):
            if i == nxt_3 == nxt_5:
                rlt.append('FizzBuzz')
                nxt_3 += 3
                nxt_5 += 5
                continue

            if i == nxt_5:
                rlt.append('Buzz')
                nxt_5 += 5
                continue

            if i == nxt_3:
                rlt.append('Fizz')
                nxt_3 += 3
                continue

            rlt.append(str(i))

        return ['Fizz' if i % 3 == 0 else '' +]
        '''
        

if __name__ == '__main__':
    tests = [
        ('test_00', (__test_args__), 2),
    ]

    foo = Solution()
    method2test = Solution.fizzBuzz
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
