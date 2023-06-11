# https://leetcode.com/problems/snapshot-array/description/
# timing 00:37:31
import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.index_s_to_snap: set[int] = set()  # index_s which required to be snap
        self.current: list[int] = [0] * length  # current value of index_s

        self.snap_count: int = 0
        self.vault: list[list[tuple[int, int]]] = []
        for _ in range(length):
            self.vault.append([(-1, 0)])

    def set(self, index: int, val: int) -> None:
        self.current[index] = val
        if val == self.vault[index][-1][1]:
            self.index_s_to_snap.discard(index)  # remove from snapping
        else:
            self.index_s_to_snap.add(index)  # add for future snapping

    def snap(self) -> int:
        for idx in self.index_s_to_snap:  # process index_s which required to snap
            self.vault[idx].append((self.snap_count, self.current[idx]))
        self.index_s_to_snap.clear()
        self.snap_count += 1
        return self.snap_count - 1

    def get(self, index: int, snap_id: int) -> int:
        selected_idx = self.vault[index]
        # bisect - return one position to right from the target position (this is why -1)
        target_snap = bisect.bisect(selected_idx, snap_id, key=lambda x: x[0]) - 1
        return selected_idx[target_snap][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


if __name__ == '__main__':
    pass
