# https://leetcode.com/problems/house-robber/description/
from typing import List

'''
   ┌───────────────────────┐
   │  pattern 0_0 or 0__0  │
   └───────────────────────┘

ex.: ('test_03', [2, 7, 3, 4, 9, 5, 1], 17)

 2, 7, 3, 4, 9, 5, 1, _, _, _, _,
 0  1  2  3  4  5  6  7  8  9  10

        + index_pyramid by pattern
       / \
      0   1              - depth=01 - 0,1
     / \ / \             
    2   3   4            - depth=02 - 2,3,4
   / \ / \ / \
  4   5   6   7          - depth=03 - 4,5,6,7
 / \ / \ / \ / \
6   7   8   9   10       - depth=04 - 6,7,8,9,a

depth = len // 2 + 1  											# 4 

depth -> array -> idx_start=2*depth-2 | idx_end=3*depth-1		# 6 | 11

list_step = 4 5 6 7					# len = depth				# 4
list_max  = 6 7 8 9 a

'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        list_max = [0] * len(nums)
        list_step = [0] * len(nums)
        depth = len(nums) // 2 + 1

        for idx, org_idx in enumerate(range(2 * depth - 2, 3 * depth - 1)):  # setup first list_step (depth - 1)
            list_max[idx] = nums[org_idx] if org_idx < len(nums) else 0

        while (depth := depth - 1) > 0:
            for idx, org_idx in enumerate(range(2 * depth - 2, 3 * depth - 1)):
                list_step[idx] = nums[org_idx] if org_idx < len(nums) else 0

            # print('\n', depth, 'after\n', list_step, '\n', list_max, '\n')
            for idx in range(depth + 1):
                list_step[idx] += max(list_max[idx], list_max[idx + 1])
                list_max[idx] = 0
            list_max[depth + 1] = 0  # clear last elem of data
            list_max, list_step = list_step, list_max
        return max(list_max[0], list_max[1])


if __name__ == '__main__':
    foo = Solution()

    for name, inpt, outpt in [
        ('test_00', [1, 2, 3, 1], 4),
        ('test_01', [2, 7, 9, 3, 1], 12),
        ('test_02', [2, 7, 3, 4, 5, 9, 1], 20),
        ('test_03', [2, 7, 3, 4, 9, 5, 1], 17),
        ('test_04', [1, 2, 2, 1], 3),
        ('test_05', [4, 1, 2, 7, 5, 3, 1], 14),
    ]:
        if name == 'test_0':
            print(foo.rob(inpt))
            quit()
        # foo.rob(inpt)
        assert foo.rob(inpt) == outpt, print('👉', name, foo.rob(inpt), 'vs', outpt)

