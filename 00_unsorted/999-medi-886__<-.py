# https://leetcode.com/problems/possible-bipartition/description/
from typing import List, Optional


class VsGroup:  # versus_group

    def __init__(self, left_elem: int, right_elem: int):
        self.left = {left_elem}
        self.right = {right_elem}

    def add(self, elem_to_add: int, versus_to: int) -> bool:
        if elem_to_add in self.get_kit_of(versus_to):
            return True  # element is already in group of the hater

        kit_4_new_elem = self.get_not_kit_of(versus_to)
        kit_4_new_elem.add(elem_to_add)
        return False

    def merge(self, hater: int, target: int, vs_group_of_target) -> bool:  # typing (vs_group_of_target: VsGroup)
        kit_of_hater = self.get_kit_of(hater)
        kit_of_hater |= vs_group_of_target.get_not_kit_of(target)

        kit_4_target = self.get_not_kit_of(hater)
        kit_4_target |= vs_group_of_target.get_kit_of(target)

        if kit_of_hater.intersection(kit_4_target):
            return True  # conflict between kits
        return False

    def get_kit_of(self, elem: int) -> Optional[set]:  # todo case elem not in vs_group
        return self.left if elem in self.left else self.right

    def get_not_kit_of(self, elem: int) -> Optional[set]:  # todo case elem not in vs_group
        return self.right if elem in self.left else self.left

    def get_all_elem(self) -> set[int]:
        return self.left.union(self.right)


class Solution:

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n == 1:
            return True

        vault = dict()
        for hater, target in dislikes:
            vs_g_hater, vs_g_target = vault.get(hater, None), vault.get(target, None)

            if (None, None) == (vs_g_hater, vs_g_target):
                tmp = VsGroup(hater, target)
                vault[hater] = tmp
                vault[target] = tmp

            elif None in (vs_g_hater, vs_g_target):
                tmp_vs_g = vs_g_hater if vs_g_target is None else vs_g_target
                elem_to_add, versus_to = (target, hater) if vs_g_hater is not None else (hater, target)
                tmp_vs_g.add(elem_to_add, versus_to)
                vault[elem_to_add] = tmp_vs_g

            elif vs_g_hater == vs_g_target:  # don't need to add_2_vault because both are already in vault
                if vs_g_hater.add(elem_to_add=target, versus_to=hater):
                    return False

            else:  # case of merge two groups
                if vs_g_hater.merge(hater, target, vs_g_target):
                    return False
                for elem in vs_g_target.get_all_elem():
                    vault[elem] = vs_g_hater
        return True


if __name__ == '__main__':
    foo = Solution

    for name, inpt, outpt in [
        ('test_00', (4, [[1, 2], [1, 3], [2, 4]]), True),
        ('test_01', (3, [[1, 2], [1, 3], [2, 3]]), False),
        ('test_02', (5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]), False),
        ('test_03', (10, [[1, 2], [3, 4], [5, 6], [6, 7], [8, 9], [7, 8]]), True),
    ]:
        if name == 'test_0':
            print(Solution.possibleBipartition(foo, *inpt))
            quit()
        assert Solution.possibleBipartition(foo, *inpt) == outpt, print('👉', name)

# true:		1 3 5 7 8
# false:	2 4 6 9

