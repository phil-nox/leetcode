# https://leetcode.com/problems/lfu-cache/description/
import time
from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class Node:                                         # Doubly_Linked_List
    key:    int
    val:    int     # value
    cnt:    int     # count
    nxt:    Optional['Node'] = None
    prv:    Optional['Node'] = None

    def pop(self) -> Optional['Node']:              #      ┌──────┐     ┌──────┐     ┌──────┐
        after: Optional['Node'] = self.nxt          #      │    ──┼───► │    ──┼───► │    ──┼─►
        before: Optional['Node'] = self.prv         #   ◄──┼──    │ ◄───┼──    │ ◄───┼──    │
        if after is not None:                       #      │before│     │self  │     │after │
            after.prv = before                      #      └──────┘     └──────┘     └──────┘
        if before is not None:                      #                    ↓ ↓ ↓
            before.nxt = after                      #      ┌──────┐                  ┌──────┐
        self.prv, self.nxt = None, None             #      │    ──┼────────────────► │    ──┼─►
        return after if before is None else None    #   ◄──┼──    │ ◄────────────────┼──    │
                                                    #      │before│                  │after │
        # if 'self' is a last (tail) node           #      └──────┘     ┌──────┐     └──────┘
        # return 'after' node as a new_tail         #                   │    ──┼──►
                                                    #               ◄───┼──    │
                                                    #                   │self  │
                                                    #                   └──────┘
                                                    ####################################################################

    def push_forward(self, other: 'Node') -> None:  #           ┌──────┐
        after: Optional['Node'] = self.nxt          #           │    ──┼─►
        if after is not None:                       #         ◄─┼──    │
            after.prv = other                       #           │other │
        other.prv, other.nxt = self, self.nxt       #           └──────┘
        self.nxt = other                            #    ┌──────┐     ┌──────┐
                                                    #    │    ──┼───► │    ──┼─►
                                                    #  ◄─┼──    │ ◄───┼──    │
                                                    #    │self  │     │after │
                                                    #    └──────┘     └──────┘
                                                    #            ↓ ↓ ↓
                                                    #    ┌──────┐     ┌──────┐    ┌──────┐
                                                    #    │    ──┼───► │    ──┼──► │    ──┼─►
                                                    #  ◄─┼──    │ ◄───┼──    │ ◄──┼──    │
                                                    #    │self  │     │other │    │after │
                                                    #    └──────┘     └──────┘    └──────┘
                                                    ####################################################################

    def push_backward(self, other: 'Node') -> None: #           ┌──────┐
        before: Optional['Node'] = self.prv         #           │    ──┼─►
        if before is not None:                      #         ◄─┼──    │
            before.nxt = other                      #           │other │
        other.prv, other.nxt = self.prv, self       #           └──────┘
        self.prv = other                            #    ┌──────┐     ┌──────┐
                                                    #    │    ──┼───► │    ──┼─►
                                                    #  ◄─┼──    │ ◄───┼──    │
                                                    #    │before│     │self  │
                                                    #    └──────┘     └──────┘
                                                    #            ↓ ↓ ↓
                                                    #    ┌──────┐     ┌──────┐    ┌──────┐
                                                    #    │    ──┼───► │    ──┼──► │    ──┼─►
                                                    #  ◄─┼──    │ ◄───┼──    │ ◄──┼──    │
                                                    #    │before│     │other │    │self  │
                                                    #    └──────┘     └──────┘    └──────┘
                                                    ####################################################################


''' Graphic for "class LFUCache"

ket2node dict
         {
           g: ──────────────────────────────────────────────────────────────────────────────────────┐
           f: ─────────────────────────────────────────────────────────────────────────┐            │
           e: ────────────────────────────────────────────────────────────┐            │            │
           d: ───────────────────────────────────────────────┐            │            │            │
           c: ──────────────────────────────────┐            │            │            │            │
           b: ─────────────────────┐            │            │            │            │            │
           a: ────────┐            │            │            │            │            │            │
         }            │            │            │            │            │            │            │
                      ▼            ▼            ▼            ▼            ▼            ▼            ▼
                   ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐
tail ────────────► │cnt: 1│     │cnt: 1│     │cnt: 2│     │cnt: 2│     │cnt: 2│     │cnt: 3│     │cnt: 3│
                   │key: a│     │key: b│     │key: c│     │key: d│     │key: e│     │key: f│     │key: g│
                   │val   │     │val   │     │val   │     │val   │     │val   │     │val   │     │val   │
                   │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼─►
                ◄──┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │
                   │      │     │      │     │      │     │      │     │      │     │      │     │      │
                   └──────┘     └──────┘     └──────┘     └──────┘     └──────┘     └──────┘     └──────┘
                                   ▲                                      ▲                         ▲
count2last dict                    │                                      │                         │
         {                         │                                      │                         │
           1: ─────────────────────┘                                      │                         │
           2: ────────────────────────────────────────────────────────────┘                         │
           3: ──────────────────────────────────────────────────────────────────────────────────────┘
         }
'''


class LFUCache:

    def __init__(self, capacity: int):
        self._limit:        int = capacity
        self._len:          int = 0
        self.tail:          Optional[Node] = None
        self.key2node:      dict[int, Node] = dict()
        self.cnt2last:    dict[int, Node] = dict()

    def debug(self):
        cur = self.tail
        while cur is not None:
            print(f'🔑:{cur.key}', f'📦:{cur.val}', f'⏲️:{cur.cnt}', ' > ', end='')
            cur = cur.nxt
        print()

    def _pop_n_tail(self, trg: Node):
        """part_of 'def incm'"""
        if (new_tail := trg.pop()) is not None:
            self.tail = new_tail

    def _update_count(self, trg: Node):
        """part_of 'def incm'"""
        self.cnt2last[trg.cnt + 1] = trg
        trg.cnt += 1

    def _replace_count(self, trg: Node):
        """part_of 'def incm'"""
        if trg.prv is None or trg.prv.cnt != trg.cnt:
            del self.cnt2last[trg.cnt]
            return
        self.cnt2last[trg.cnt] = trg.prv

    def incm(self, trg: Node) -> None:
        """increment a counter for a target node"""
        if self.cnt2last.get(trg.cnt) is not trg:       # trg ─────────────────┐
            last = self.cnt2last.get(trg.cnt + 1, None) #                      ▼
            if last is None:                            #      ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐
                last = self.cnt2last.get(trg.cnt)       #      │cnt: 2│     │cnt: 2│     │cnt: 2│     │cnt: 3│     │cnt: 3│
            self._pop_n_tail(trg)                       #      │key: a│     │key: b│     │key: c│     │key: d│     │key: f│
            last.push_forward(trg)                      #      │val   │     │val   │     │val   │     │val   │     │val   │
            self._update_count(trg)                     #      │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼─►
            return                                      #  ◄───┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │
                                                        #      │      │     │target│     │      │     │      │     │      │
                                                        #      └──────┘     └──────┘     └──────┘     └──────┘     └──────┘
                                                        #                                   ▲                         ▲
                                                        # count2last                        │                         │
                                                        # {                                 │                         │
                                                        #  2: ──────────────────────────────┘                         │
                                                        #  3: ────────────────────────────────────────────────────────┘
                                                        # }
                                                        #                     ↓ ↓ ↓
                                                        #
                                                        # trg ─────────────────────────────────────────────────────────────────────┐
                                                        #                                                                          ▼
                                                        #      ┌──────┐                  ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐
                                                        #      │cnt: 2│                  │cnt: 2│     │cnt: 3│     │cnt: 3│     │cnt: 3│
                                                        #      │key: a│                  │key: c│     │key: d│     │key: f│     │key: b│
                                                        #      │val   │                  │val   │     │val   │     │val   │     │val   │
                                                        #      │    ──┼───────────────►  │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼─►
                                                        #  ◄───┼──    │  ◄───────────────┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │
                                                        #      │      │                  │      │     │      │     │      │     │target│
                                                        #      └──────┘                  └──────┘     └──────┘     └──────┘     └──────┘
                                                        #                                   ▲                                      ▲
                                                        # count2last                        │                                      │
                                                        # {                                 │                                      │
                                                        #  2: ──────────────────────────────┘                                      │
                                                        #  3: ─────────────────────────────────────────────────────────────────────┘
                                                        # }

        if self.cnt2last.get(trg.cnt + 1, None):        # trg ──────────────────────────────┐
            self._replace_count(trg)                    #                                   ▼
            self._pop_n_tail(trg)                       #      ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐
            last = self.cnt2last.get(trg.cnt + 1)       #      │cnt: 2│     │cnt: 2│     │cnt: 2│     │cnt: 3│     │cnt: 3│
            last.push_forward(trg)                      #      │key: a│     │key: b│     │key: c│     │key: d│     │key: f│
            self._update_count(trg)                     #      │val   │     │val   │     │val   │     │val   │     │val   │
            return                                      #      │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼─►
                                                        #  ◄───┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │
                                                        #      │      │     │      │     │target│     │      │     │      │
                                                        #      └──────┘     └──────┘     └──────┘     └──────┘     └──────┘
                                                        #                                   ▲                         ▲
                                                        # count2last                        │                         │
                                                        # {                                 │                         │
                                                        #  2: ──────────────────────────────┘                         │
                                                        #  3: ────────────────────────────────────────────────────────┘
                                                        # }
                                                        #                     ↓ ↓ ↓
                                                        #
                                                        # trg ─────────────────────────────────────────────────────────────────────┐
                                                        #                                                                          ▼
                                                        #      ┌──────┐     ┌──────┐                  ┌──────┐     ┌──────┐     ┌──────┐
                                                        #      │cnt: 2│     │cnt: 2│                  │cnt: 3│     │cnt: 3│     │cnt: 3│
                                                        #      │key: a│     │key: b│                  │key: d│     │key: f│     │key: c│
                                                        #      │val   │     │val   │                  │val   │     │val   │     │val   │
                                                        #      │    ──┼───► │    ──┼───────────────►  │    ──┼───► │    ──┼───► │    ──┼─►
                                                        #  ◄───┼──    │ ◄───┼──    │ ◄────────────────┼──    │ ◄───┼──    │ ◄───┼──    │
                                                        #      │      │     │      │                  │      │     │      │     │target│
                                                        #      └──────┘     └──────┘                  └──────┘     └──────┘     └──────┘
                                                        #                      ▲                                                   ▲
                                                        # count2last           │                                                   │
                                                        # {                    │                                                   │
                                                        #  2: ─────────────────┘                                                   │
                                                        #  3: ─────────────────────────────────────────────────────────────────────┘
                                                        # }

        self._replace_count(trg)                        # trg ──────────────────────────────┐
        self._update_count(trg)                         #                                   ▼
        return                                          #      ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐
                                                        #      │cnt: 2│     │cnt: 2│     │cnt: 2│     │cnt: 4│     │cnt: 4│
                                                        #      │key: a│     │key: b│     │key: c│     │key: d│     │key: f│
                                                        #      │val   │     │val   │     │val   │     │val   │     │val   │
                                                        #      │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼─►
                                                        #  ◄───┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │
                                                        #      │      │     │      │     │target│     │      │     │      │
                                                        #      └──────┘     └──────┘     └──────┘     └──────┘     └──────┘
                                                        #                                   ▲                         ▲
                                                        # count2last                        │                         │
                                                        # {                                 │                         │
                                                        #  2: ──────────────────────────────┘                         │
                                                        #  3:                                                         │
                                                        #  4: ────────────────────────────────────────────────────────┘
                                                        # }
                                                        #                     ↓ ↓ ↓
                                                        #
                                                        # trg ──────────────────────────────┐
                                                        #                                   ▼
                                                        #      ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐
                                                        #      │cnt: 2│     │cnt: 2│     │cnt: 3│     │cnt: 4│     │cnt: 4│
                                                        #      │key: a│     │key: b│     │key: c│     │key: d│     │key: c│
                                                        #      │val   │     │val   │     │val   │     │val   │     │val   │
                                                        #      │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼───► │    ──┼─►
                                                        #  ◄───┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │ ◄───┼──    │
                                                        #      │      │     │      │     │target│     │      │     │      │
                                                        #      └──────┘     └──────┘     └──────┘     └──────┘     └──────┘
                                                        #                      ▲            ▲                         ▲
                                                        # count2last           │            │                         │
                                                        # {                    │            │                         │
                                                        #  2: ─────────────────┘            │                         │
                                                        #  3: ──────────────────────────────┘                         │
                                                        #  4: ────────────────────────────────────────────────────────┘
                                                        # }

    def get(self, key: int) -> int:
        if (trg := self.key2node.get(key, None)) is None:
            return -1
        self.incm(trg)
        return trg.val

    def _put_remove_lfu(self):
        if self.cnt2last.get(self.tail.cnt) is self.tail:
            del self.cnt2last[self.tail.cnt]
        del self.key2node[self.tail.key]
        new_tail = self.tail.pop()
        self.tail = new_tail

    def put(self, key: int, value: int) -> None:
        if self._limit == 0:
            return
        if (trg := self.key2node.get(key, None)) is not None:
            self.incm(trg)
            trg.val = value
            return
        if self._len < self._limit:
            self._len += 1
        else:
            self._put_remove_lfu()

        if (last := self.cnt2last.get(1, None)) is not None:
            tmp = Node(key=key, val=value, cnt=1)
            last.push_forward(tmp)
            self.cnt2last[1], self.key2node[key] = tmp, tmp
            return

        tmp = Node(key=key, val=value, cnt=1)
        self.cnt2last[1], self.key2node[key] = tmp, tmp
        if self.tail is not None:
            self.tail.push_backward(tmp)
        self.tail = tmp


if __name__ == '__main__':
    time_diff = -time.perf_counter()
    a = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    b = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

    foo = LFUCache(*b[0])
    for el_a, el_b in zip(a[1:], b[1:]):
        print()
        print(el_a, el_b)
        print(getattr(foo, el_a)(*el_b))
        #foo.debug()

    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
