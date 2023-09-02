# https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/description/
# git commit -m "2023_09_02 - 846 - medi - 2841"
import time


class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        win: dict[int, int] = dict()
        rlt: int = 0
        cur: int

        for el in nums[:k]:
            win[el] = win.get(el, 0) + 1
        cur = sum([k * v for k, v in win.items()])
        if len(win) >= m:           # almost_unique
            rlt = cur if cur > rlt else rlt

        low, top = 0, k
        while top < len(nums):
            rm = win.pop(nums[low])                         # +- remove tail
            if rm > 1:                                      # |
                win[nums[low]] = rm - 1                     # |
            cur -= nums[low]                                # |

            win[nums[top]] = win.get(nums[top], 0) + 1      # +- add head
            cur += nums[top]                                # |

            if len(win) >= m:                               # +- update rlt
                rlt = cur if cur > rlt else rlt             # |

            low, top = low + 1, top + 1                     # +- next_iteration

        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([2, 6, 7, 3, 1, 7], 3, 4), 18),
    ]

    foo = Solution()
    method2test = Solution.maxSum
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
