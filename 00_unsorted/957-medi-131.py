# https://leetcode.com/problems/palindrome-partitioning/description/
import time


'''
5 aabaa
4 aaba a | a abaa ↩️ aabaa
3 aab a a | a aba a | a aba a | a a baa | aab aa | a aba a | aa baa ↩️ aaba a | a abaa ↩️ aabaa
2 


2 aa baa | a ab aa

'''


class Solution:
    def is_palindrome(self, to_test: tuple[str]) -> bool:
        idx, jdx = 0, len(to_test)-1
        while idx <= jdx:
            if to_test[idx] != to_test[jdx]:
                return False
            idx, jdx = idx + 1, jdx - 1
        return True

    def possible_parts(self, trg: tuple, size: int) -> list[tuple]:
        if len(trg) <= size:    # same length not_interesting
            return []

        to_return = []
        for idx in range(len(trg)):         # ('a', 'b', 'a')       -> (ab, a) (a, ba)
            if len(trg[idx:]) < size:       # ('a', 'b', 'a', 'c')  -> (ab, ac) (a, ba, c) (ab, ac)
                break

            tmp, jdx = [], idx
            while len(tmp) < size:
                tmp.append(trg[jdx])
                jdx += 1

            if idx == 0:
                to_return.append((tuple(tmp), trg[jdx:]))
            elif jdx == len(trg):
                to_return.append((trg[:idx], tuple(tmp)))
            else:
                to_return.append((trg[:idx], tuple(tmp), trg[jdx:]))
        return to_return

    def decay(self, target: tuple[tuple], size: int) -> set[tuple]:
        to_return = set()
        for idx in range(len(target)):
            tail, core, head = target[:idx], target[idx], target[idx+1:]
            for part in self.possible_parts(core, size):
                to_return.add((*tail, *part, *head))
        return to_return

    def partition(self, s: str) -> list[list[str]]:
        variants: set[tuple[tuple]] = {(tuple(s),)}

        for win_size in reversed(range(2, len(s))):
            for case in list(variants):
                variants |= self.decay(case, win_size)

        variants.add(tuple((el,) for el in s))  # win_size = 1 optimization

        rlt = []
        for el in variants:
            if all(map(self.is_palindrome, el)):
                rlt.append([''.join(part) for part in el])
        return rlt


if __name__ == '__main__':

    tests = [
        ('test_00', ("aab",), [["a", "a", "b"], ["aa", "b"]]),
        ('test_01', ("a",), [["a"]]),
        ('test_02', ("aabaa",), [['a','a','b','a','a'], ['aa','b','a','a'], ['a','aba','a'], ['a','a','b','aa'], ['aabaa'], ['aa', 'b', 'aa']]),
        ('test_03', ("cbbbcc", ), [["c","b","b","b","c","c"],["c","b","b","b","cc"],["c","b","bb","c","c"],["c","b","bb","cc"],["c","bb","b","c","c"],["c","bb","b","cc"],["c","bbb","c","c"],["c","bbb","cc"],["cbbbc","c"]]),
        #('test_31', ("bbbbbbbbbbbbbbbb",), [[]]),
    ]

    foo = Solution()
    method2test = Solution.partition

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert {tuple(el) for el in test_rlt} == {tuple(el) for el in outpt}, print(f'Problem ⚠️ {name}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
