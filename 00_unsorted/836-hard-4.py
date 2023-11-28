# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/2471/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation/
import time

'''
idea_00:    one_formula for even & odd
         
            even [2 3 5 7]  ->  [2 3 | 5 7]  -> (3+5)/2

            odd [2 3 4 5 6] -> [2 3 4|4 5 6] -> (4+4)/2
            
            index_s:    len = 0 : l = 0 | 0 = r
                        len = 1 : l = 0 | 1 = r
                        len = 2 : l = 1 | 1 = r
                        len = 3 : l = 1 | 2 = r
                        len = 4 : l = 2 | 2 = r
                        len = 5 : l = 2 | 3 = r
                        
                     l = (len - 1) / 2  | len / 2 = r
        
                        
idea_01:    double_plus_one_indexing: division_by_2 <-> multiply_by_2
        
             odd * 2 = even  |  odd * 2 + 1 = odd
            even * 2 = even  | even * 2 + 1 = odd

            [1 3 6 9]    ->  [_ 1 _ 3 _ 6 _ 9 _]         # 4 -> 9
                                      ^
            [1 3 5 6 9]  ->  [_ 1 _ 3 _ 5 _ 6 _ 9 _ ]    # 5 -> 11
                                        ^
            >>> init_median_index = len <<<
            
            
idea_02:    median_s are interconnected <-> if we move one we should move other 
                 
            [1 1 1 1 1]  ->  [1 1 1 1 1]
                 ^                  ^
            [5 5 5 5 5]      [5 5 5 5 5]
                 ^              ^

                                         + ---------------------------------------- +
            in double_plus_one_indexing: | med_1 = k      med_2 = len_1 + len_2 - k |
                                         + ---------------------------------------- +


idea_03:    condition_s: l1 <= r2 && l2 <= r1
                            
                             3|           |2 
            if l1 > r2 : [1 2 3 4 5] [2 2 2 5 6]
                              ^           ^
                              
                           2|               |5 
                         [1 2 3 4 5] [2 2 2 5 6]
                            ^               ^
                              
'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        short, other = (nums2, nums1) if len(nums1) > len(nums2) else (nums1, nums2)

        bot, top = 0, len(short) * 2

        while bot <= top:
            mid_s = (top + bot) // 2
            mid_o = len(other) + len(short) - mid_s

            l_s = short[(mid_s - 1) // 2] if mid_s != 0 else -10**7
            l_o = other[(mid_o - 1) // 2] if mid_o != 0 else -10**7
            r_s = short[mid_s // 2] if mid_s != len(short) * 2 else 10**7
            r_o = other[mid_o // 2] if mid_o != len(other) * 2 else 10**7

            if l_o > r_s:
                bot = mid_s + 1
            elif l_s > r_o:
                top = mid_s - 1
            else:
                return (max(l_o, l_s) + min(r_o, r_s)) / 2
        return -1


if __name__ == '__main__':
    tests = [
        ('test_01',
         ([1, 1, 5, 8, 9, 13, 18, 23, 23, 28, 30, 31, 31, 35, 37, 42, 45, 50, 55, 59, 59, 59, 60, 64, 67, 70, 72, 77]
          , [1, 6, 11, 15, 19, 24, 24, 29, 33, 36, 39, 39, 44, 49, 51, 54, 59, 59, 59, 59, 59, 62, 62, 63, 65, 70, 71,
             74]), 43.0),
        ('test_01', ([1, 3], [2, 7]), 2.5),
        ('test_01', ([0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 1]), 0.0),
        ('test_00', ([1, 3], [2]), 2.0),
        ('test_01', ([1, 2], [3, 4]), 2.5),
    ]

    foo = Solution()
    method2test = Solution.findMedianSortedArrays
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

'''
35 - 49 - 7step
35 - 29 - 3step
35 - 39 - 1step
35 - 36 - 0step

51 + 35 vs 54 + 70

[01, 01, 05, 08, 09, 13, 18, 23, 23, 28, 30, 31, 31, 35, 37, 42, 45, 50, 55, 59, 59, 59, 60, 64, 67, 70, 72, 77]
                [01, 06, 11, 15, 19, 24, 24, 29, 33, 36, 39, 39, 44, 49, 51, 54, 59, 59, 59, 59, 59, 62, 62, 63, 65, 70, 71, 74]
                                                      ^

'''