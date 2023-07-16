# https://leetcode.com/problems/smallest-sufficient-team/description/

import time
from collections import deque


class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        target = 2**len(req_skills) - 1                                     # target=0b111111 <- len(req_skills)=6
        skill2mask = {s: (1 << idx) for idx, s in enumerate(req_skills)}    # {'aws': 0b100000, ...}

        people2mask = dict()                                                # {0: 0b000111, etc}
        for p_idx, skills in enumerate(people):
            cur_mask = 0b0
            for s in skills:
                cur_mask |= skill2mask.get(s, 0b0)
            if cur_mask == 0b0:                                                 # skip person without skills
                continue
            if cur_mask == target:                                              # one_person_team
                return [p_idx]
            people2mask[p_idx] = cur_mask

        print('setup vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\n')
        print('target', bin(target), '\n')
        [print('      ', f'{bin(v):0{len(bin(target))}}', f'- people2mask[{k}]') for k, v in people2mask.items()]
        print('\nsetup_done ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')

        ref = list(people2mask.keys())                                          # common_base !
        seen = set()                                                            # seen mask_s !!!
        to_do = deque([(people2mask[ref[i]], [i]) for i in range(len(ref))])    # bfs solution
        while to_do:
            print()
            [print(f'{bin(mask):0{len(bin(target))}}', team) for mask, team in to_do]

            cur_mask, cur_team = to_do.popleft()

            for n in range(cur_team[-1] + 1, len(ref)):     # common_base used here to have
                                                            # [0, 1, 2] -> [0], [1], [2] -> [0, 1], [0, 2], [1, 2]
                                                            # and not
                                                            # [0], [1], [2] -> [0, 1], [0, 2], [1, 0], [1, 2], ...

                nxt_mask = cur_mask | people2mask[ref[n]]
                nxt_team = [*cur_team, n]

                if nxt_mask in seen:                # bfs means we searching min len solution
                    continue                        # but if team give the mask with we already
                seen.add(nxt_mask)                  # seen there is not need to process this case and branch !!!

                if nxt_mask == target:
                    print(
                        f'\n{bin(nxt_mask):0{len(bin(target))}}',
                        nxt_team, '<- common_base',
                        [ref[idx] for idx in nxt_team], '<- people index_s')
                    return [ref[idx] for idx in nxt_team]

                to_do.append((nxt_mask, nxt_team))

        return []
        

if __name__ == '__main__':
    tests = [
        ('test_00', (["algorithms", "math", "java", "reactjs", "csharp", "aws"],
                     [["biology"], ["aws", "java"], ["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], ["java", "csharp"],
                      ["reactjs", "csharp"], ["csharp", "math"]]), [1, 2, 5]),
        #('test_01', (["hfkbcrslcdjq","jmhobexvmmlyyzk","fjubadocdwaygs","peaqbonzgl","brgjopmm","x","mf","pcfpppaxsxtpixd","ccwfthnjt","xtadkauiqwravo","zezdb","a","rahimgtlopffbwdg","ulqocaijhezwfr","zshbwqdhx","hyxnrujrqykzhizm"], [["peaqbonzgl","xtadkauiqwravo"],["peaqbonzgl","pcfpppaxsxtpixd","zshbwqdhx"],["x","a"],["a"],["jmhobexvmmlyyzk","fjubadocdwaygs","xtadkauiqwravo","zshbwqdhx"],["fjubadocdwaygs","x","zshbwqdhx"],["x","xtadkauiqwravo"],["x","hyxnrujrqykzhizm"],["peaqbonzgl","x","pcfpppaxsxtpixd","a"],["peaqbonzgl","pcfpppaxsxtpixd"],["a"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk"],["hfkbcrslcdjq","xtadkauiqwravo","a","zshbwqdhx"],["peaqbonzgl","mf","a","rahimgtlopffbwdg","zshbwqdhx"],["xtadkauiqwravo"],["fjubadocdwaygs"],["x","a","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl"],["pcfpppaxsxtpixd","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","rahimgtlopffbwdg"],["zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","brgjopmm","x"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk","a","ulqocaijhezwfr"],["peaqbonzgl","x","a","ulqocaijhezwfr","zshbwqdhx"],["mf","pcfpppaxsxtpixd"],["fjubadocdwaygs","ulqocaijhezwfr"],["fjubadocdwaygs","x","a"],["zezdb","hyxnrujrqykzhizm"],["ccwfthnjt","a"],["fjubadocdwaygs","zezdb","a"],[],["peaqbonzgl","ccwfthnjt","hyxnrujrqykzhizm"],["xtadkauiqwravo","hyxnrujrqykzhizm"],["peaqbonzgl","a"],["x","a","hyxnrujrqykzhizm"],["zshbwqdhx"],[],["fjubadocdwaygs","mf","pcfpppaxsxtpixd","zshbwqdhx"],["pcfpppaxsxtpixd","a","zshbwqdhx"],["peaqbonzgl"],["peaqbonzgl","x","ulqocaijhezwfr"],["ulqocaijhezwfr"],["x"],["fjubadocdwaygs","peaqbonzgl"],["fjubadocdwaygs","xtadkauiqwravo"],["pcfpppaxsxtpixd","zshbwqdhx"],["peaqbonzgl","brgjopmm","pcfpppaxsxtpixd","a"],["fjubadocdwaygs","x","mf","ulqocaijhezwfr"],["jmhobexvmmlyyzk","brgjopmm","rahimgtlopffbwdg","hyxnrujrqykzhizm"],["x","ccwfthnjt","hyxnrujrqykzhizm"],["hyxnrujrqykzhizm"],["peaqbonzgl","x","xtadkauiqwravo","ulqocaijhezwfr","hyxnrujrqykzhizm"],["brgjopmm","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl","pcfpppaxsxtpixd"],["fjubadocdwaygs","x","a","zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","x"],["ccwfthnjt"]]), [1, 13, 30, 31, 50, 51]),
    ]

    foo = Solution()
    method2test = Solution.smallestSufficientTeam
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
