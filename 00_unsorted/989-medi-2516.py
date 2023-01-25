# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/
import time


class Solution:

    def r_idx(self, r_step: int, s_len: str) -> int:
        return len(s_len) - r_step

    def l_idx(self, l_step: int) -> int:
        return -1 + l_step

    def valut_is_good(self, vault: dict[str, int]) -> bool:
        return all([val < 1 for val in vault.values()])

    def takeCharacters(self, s: str, k: int) -> int:
        vault = {'a': k, 'b': k, 'c': k}
        r_step, l_step = 0, 0

        while not self.valut_is_good(vault):
            l_step += 1
            if l_step >= len(s) + 1:
                return -1
            vault[s[self.l_idx(l_step)]] = vault[s[self.l_idx(l_step)]] - 1

        rlt = l_step
        while l_step > 0:
            vault[s[self.l_idx(l_step)]] = vault[s[self.l_idx(l_step)]] + 1
            l_step -= 1

            if not self.valut_is_good(vault):
                rlt = min(rlt, l_step + 1 + r_step)  # previous good combination
                while not self.valut_is_good(vault):
                    r_step += 1
                    vault[s[self.r_idx(r_step, s)]] = vault[s[self.r_idx(r_step, s)]] - 1
            elif l_step == 0:  # l_step == 0 and vault_is_good - only_right case
                rlt = min(rlt, r_step)
        return rlt


if __name__ == '__main__':
    foo = Solution()
    time_diff = -time.perf_counter()
    for name, inpt, outpt in [
        ('test_00', ("aabaaaacaabc", 2), 8),
        ('test_01', ("a", 1), -1),
        ('test_02', ("a", 0), 0),
        ('test_03', ("cbaabccac", 3), -1),
        ('test_04', ("aacbca", 1), 3),
        ('test_04', ("abc", 1), 3),
        ('test05', ("aacc", 2), -1),
        ('test06', ("acba", 1), 3),
    ]:
        if name == 'test_0':
            print(foo.takeCharacters(*inpt))
            quit()
        assert foo.takeCharacters(*inpt) == outpt, print('👉', name, foo.takeCharacters(*inpt), 'vs', outpt)
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

