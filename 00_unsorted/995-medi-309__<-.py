# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
import time
from typing import List

'''
🔹 States: #####################################################################

Exist 5 states - [no_stock_do_nothing] [no_stock_buy] [one_stock_do_nothing] [one_stock_sell] [no_stock_cooldown]
but [no_stock_do_nothing] == [no_stock_cooldown]
So exist 4 states :)
👉 [no_stock_do_nothing] [no_stock_buy] [one_stock_do_nothing] [one_stock_sell]


🔹 Change state: ##########################################################

Passing to next day we can should choice next state. But there are restrictions. 
Let's describe possible state2state rules.

[no_stock_do_nothing]     -> [no_stock_do_nothing]
                        -> [no_stock_buy]

[no_stock_buy]            -> [one_stock_do_nothing]
                        -> [one_stock_sell]

[one_stock_do_nothing]    -> [one_stock_do_nothing]
                        -> [one_stock_sell]

[one_stock_sell]        -> [no_stock_do_nothing]


🔹 Graph_form: #################################################################

There are two ways to get at states: [no_stock_do_nothing], [one_stock_do_nothing], [one_stock_sell]
And one way to get to state: [no_stock_buy]

>>Graph for [no_stock_do_nothing] & [no_stock_buy]

  no_stock       no_stock       one_stock      one_stock
  do_nothing     buy            do_nothing     sell

  ┌──┐ ┌──┐           ┌──┐      ┌──┐ ┌──┐      ┌──┐ ┌──┐
  │  │ │  │           │  │      │  │ │  │      │  │ │  │
  └──┴┬┴──┘           └─┬┘      └──┘ └──┘      └──┘ └──┘
      │                 │
      │                 │
      │                 └────────┬──────────────┐
      └─┬──────────────┐         │              │
        │              │         │              │
  ┌──┐ ┌▼─┐           ┌▼─┐      ┌▼─┐ ┌──┐      ┌▼─┐ ┌──┐
  │  │ │  │           │  │      │  │ │  │      │  │ │  │
  └──┘ └──┘           └──┘      └──┘ └──┘      └──┘ └──┘

<<<<<<<<

>>Graph for [one_stock_do_nothing] & [one_stock_sell]

  no_stock       no_stock       one_stock      one_stock
  do_nothing     buy            do_nothing     sell

  ┌──┐ ┌──┐           ┌──┐      ┌──┐ ┌──┐      ┌──┐ ┌──┐
  │  │ │  │           │  │      │  │ │  │      │  │ │  │
  └──┘ └──┘           └──┘      └──┴┬┴──┘      └──┴┬┴──┘
                                    │              │
───┐                                │              └──────
   │                                │
   │                                └─┬───────────────┐
   │                                  │               │
  ┌▼─┐ ┌──┐           ┌──┐      ┌──┐ ┌▼─┐      ┌──┐ ┌─▼┐
  │  │ │  │           │  │      │  │ │  │      │  │ │  │
  └──┘ └──┘           └──┘      └──┘ └──┘      └──┘ └──┘

<<<<<<<<

🔹 Example [1, 2, 3, 0, 2]: ####################################################


     no_stock       no_stock       one_stock      one_stock
     do_nothing     buy            do_nothing     sell

     ┌──┐ ┌──┐           ┌──┐      ┌──┐ ┌──┐      ┌──┐ ┌──┐
1    │  │ │ 0│           │-1│      │  │ │  │      │  │ │  │
     └──┘ └──┘           └──┘      └──┘ └──┘      └──┘ └──┘

     ┌──┐ ┌──┐           ┌──┐      ┌──┐ ┌──┐      ┌──┐ ┌──┐
2    │  │ │ 0│           │-2│      │-1│ │  │      │ 1│ │  │
     └──┘ └──┘           └──┘      └──┘ └──┘      └──┘ └──┘

     ┌──┐ ┌──┐           ┌──┐      ┌──┐ ┌──┐      ┌──┐ ┌──┐   # so here each state has a two possible value
3    │ 1│ │ 0│           │-3│      │-2│ │-1│      │ 1│ │ 2│   # for each state we should choice max and go on
     └──┘ └──┘           └──┘      └──┘ └──┘      └──┘ └──┘   # 🔻 the way to the state is doesn't matter, 
                                                              # 🔻 best possible value does
     ┌──┐ ┌──┐           ┌──┐      ┌──┐ ┌──┐      ┌──┐ ┌──┐
0    │ 2│ │ 1│           │ 1│      │-3│ │-1│      │-3│ │-1│
     └──┘ └──┘           └──┘      └──┘ └──┘      └──┘ └──┘

     ┌──┐ ┌──┐           ┌──┐      ┌──┐ ┌──┐      ┌──┐ ┌──┐
2    │-1│ │ 2│           │ 0│      │ 1│ │-1│      │ 3│ │ 1│
     └──┘ └──┘           └──┘      └──┘ └──┘      └──┘ └──┘

    ────────────────────────────────────────────────────────
     ┌──┐ ┌──┐           ┌──┐      ┌──┐ ┌──┐      ┌──┐ ┌──┐
     │  │ │ 2│           │  │      │  │ │ 1│      │  │ │ 3│
     └──┘ └──┘           └──┘      └──┘ └──┘      └──┘ └──┘
    ────────────────────────────────────────────────────────
                                            return max - 3


'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        value_to_init = -max(prices)
        ns_dn = 0  # state no_stock_do_nothing
        ns_b = value_to_init  # state no_stock_buy
        s_dn = value_to_init  # state stock_do_nothing
        s_s = value_to_init  # state stock_sell

        for price in prices:
            next_ns_dn = max(ns_dn, s_s)  # optimisation_is_possible: next_ns_b can be remove and etc.
            next_ns_b = ns_dn - price
            next_s_dn = max(s_dn, ns_b)
            next_s_s = max(s_dn, ns_b) + price

            ns_dn, ns_b, s_dn, s_s = next_ns_dn, next_ns_b, next_s_dn, next_s_s
        return max(ns_dn, s_dn, s_s)


if __name__ == '__main__':
    foo = Solution()
    time_diff = -time.perf_counter()
    for name, inpt, outpt in [
        ('test_00', ([1, 2, 3, 0, 2],), 3),
        ('test_01', ([1],), 0),
    ]:
        if name == 'test_0':
            print(foo.maxProfit(*inpt))
            quit()
        assert foo.maxProfit(*inpt) == outpt, print('👉', name, foo.maxProfit(*inpt), 'vs', outpt)
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

