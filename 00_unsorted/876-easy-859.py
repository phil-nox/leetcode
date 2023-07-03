# https://leetcode.com/problems/buddy-strings/description/
import time


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diff_s: list[tuple[str, str]] = []

        if len(s) != len(goal):                                     # + - case_00 - not equal at all
            return False                                            # |

        if s == goal:                                               # + -case_01 - identical
            return True if len(set(s)) < len(s) else False          # |

        for idx in range(len(s)):                                   # + -case_02 - swap required
            if s[idx] != goal[idx]:                                 # |
                diff_s.append((s[idx], goal[idx]))                  # |
                if len(diff_s) > 2:                                 # |
                    return False                                    # |
        return len(diff_s) == 2 and diff_s[0] == diff_s[1][::-1]    # |
        

if __name__ == '__main__':
    tests = [
        ('test_00', ('ab', 'ba'), True),
        ('test_01', ('aa', 'aa'), True),
        ('test_02', ('ab', 'ab'), False),
    ]

    foo = Solution()
    method2test = Solution.buddyStrings
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
