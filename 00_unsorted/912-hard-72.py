# https://leetcode.com/problems/edit-distance/description/
# Solution from https://www.youtube.com/watch?v=qaOtdWO47b4&t=267s
import time


'''
             d
         - d i
           
     -   0 1 2
     d   1 0
   d i   2  0



'''


class Solution:
    debug: bool = False
    d_path: set[tuple[int, int]] = set()

    def _debug(self, matrix: list[list[int]], target: tuple[int, int], back: set[tuple[int, int]], step: list[tuple[int, int]]):
        if not self.debug:
            return
        print()
        for idx in range(len(matrix)):
            row = []
            for jdx in range(len(matrix[0])):
                if (idx, jdx) == target:
                    row.append(f'\033[35m{matrix[idx][jdx]:02}\033[0m')
                elif (idx, jdx) in back:
                    row.append(f'\33[102m{matrix[idx][jdx]:02}\033[0m')
                elif (idx, jdx) in self.d_path:
                    row.append(f'\033[37m{matrix[idx][jdx]:02}\033[0m')
                else:
                    row.append(f'{matrix[idx][jdx]:02}')
            print(' '.join(row))
        self.d_path.update(step)

    def minDistance(self, word1: str, word2: str) -> int:
        matrix: list[list[int]] = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for jdx in range(len(word2) + 1):
            matrix[0][jdx] = jdx
        for idx in range(len(word1) + 1):
            matrix[idx][0] = idx
        self.d_path.clear()

        for idx in range(1, len(word1) + 1):
            for jdx in range(1, len(word2) + 1):
                if word1[idx - 1] == word2[jdx - 1]:
                    matrix[idx][jdx] = matrix[idx - 1][jdx - 1]
                    self._debug(matrix, target=(idx, jdx), back={(idx - 1, jdx - 1)}, step=[])
                    continue
                to_check = ((idx - 1, jdx), (idx - 1, jdx - 1), (idx, jdx - 1))
                value = min((matrix[i][j] for i, j in to_check))
                no_path = [(i, j) for i, j in to_check if matrix[i][j] != value]
                matrix[idx][jdx] = 1 + value

                self._debug(matrix, target=(idx, jdx), back={(idx - 1, jdx), (idx - 1, jdx - 1), (idx, jdx - 1)}, step=no_path)

        self._debug(matrix, target=(len(word1), len(word2)), back=set(), step=[])
        return matrix[len(word1)][len(word2)]


if __name__ == '__main__':
    tests = [
        ('test_00', ('horse', 'ros'), 3),
        ('test_02', ('2foobar', 'foobar3'), 2),
        ('test_26', ('spartan', 'part'), 3),
        ('test_27', ('plasma', 'altruism'), 6),
        ('test_03', ('ab', 'b'), 1),
        ('test_01', ('intention', 'execution'), 5),
        ('test_04', ('', ''), 0),
        ('test_21', ('park', 'spake'), 3),
        ('test_25', ('mart', 'karma'), 3),
        ('test_1104', ('dinitrophenylhydrazine', 'dimethylhydrazine'), 7),
        ('test_1136', ('pneumonoultramicroscopicsilicovolcanoconiosis', 'ultramicroscopically'), 27),
    ]

    foo = Solution()
    method2test = Solution.minDistance

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
