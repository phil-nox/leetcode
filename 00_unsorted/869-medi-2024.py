# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/
import time


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_s, l_s, low = 0, 0, 0
        for top in range(len(answerKey)):
            t_s, l_s = (t_s + 1, l_s) if answerKey[top] == 'T' else (t_s, l_s + 1)
            if min(t_s, l_s) > k:
                t_s, l_s = (t_s - 1, l_s) if answerKey[low] == 'T' else (t_s, l_s - 1)
                low += 1
        return len(answerKey) - low


if __name__ == '__main__':
    tests = [
        ('test_00', ('TTFTTFTT', 1), 5),
        ('test_01', ('TFFT', 1), 3),
    ]

    foo = Solution()
    method2test = Solution.maxConsecutiveAnswers
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
