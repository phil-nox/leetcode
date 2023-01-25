# https://leetcode.com/problems/sum-of-distances-in-tree/description/
# Inspire: https://leetcode.com/problems/sum-of-distances-in-tree/solutions/130567/two-traversals-o-n-python-solution-with-explanation/

import data_for_996
import time

from typing import List, Any
from dataclasses import dataclass, field

'''
##############################################
#                                            #                          ┌──┐
#  depth_first_search - backward_calculation #                          │  ◄── number_of_sub_nodes
#                                            #     number_of_sub_edge ──►  │
##############################################                          └──┘

                                     ┌──┐
                                     │  │
                                     │  │
                                     └┬─┘
                                      │
                                      │             step_03                 step_06                 step_08
                                     ┌┴─┐               |                       |                       |
                      ┌──────────────┤ 3│= 2 + 1        |      5 │+= 1 + 1      |      6 │+= 0 + 1      |
                      │              │ 6│= 2 + 1 + 3    |      9 │+= 1 + 1 + 1  |     10 │+= 0 + 1 + 0  |
                      │       ┌──────┴┬─┘  --------------            ------------            ------------
                      │       │       │
                      │       │       │             step_02
                     ┌┴─┐    ┌┴─┐    ┌┴─┐               |
                     │ 0│    │ 1│    │ 2│= 1 + 1        |
                     │ 0│    │ 1│    │ 3│= 1 + 1 + 1    |
                     └──┘    └┬─┘    └┬─┘  --------------
                              │       │
                              │       │             step_01
                             ┌┴─┐    ┌┴─┐               |
                             │ 0│    │ 1│= 0 + 1        | = previous_num_of_sub_nodes + 1
                             │ 0│    │ 1│= 0 + 1 + 0    | = previous_num_of_sub_nodes + 1 + previous_num_sub_edge
                             └──┘    └┬─┘  --------------
                                      │
                                      │
                                     ┌┴─┐
                                     │ 0│
                                     │ 0│
                                     └──┘


##############################################
#                                            #
#  depth_first_search - forward__calculation #
#                                            #
##############################################

                                        ┌──┐
                                        │ 7│
                                        │17│
                                        └┬─┘
                                         │
                                         │                # step_01
                                        ┌┴─┐             -----------
                         ┌──────────────┤ 6│  7 │ = previous_num_of_sub_nodes
                         │              │10│ 11 │ = previous_num_of_sub_edges 
                         │       ┌──────┴┬─┘                        - (num_of_sub_nodes + 1 + num_sub_edge)
                         │       │       │                          + (previous_num_of_sub_nodes - num_of_sub_node)
                         │       │       │                          + num_sub_edge
                         │       │       │          SHORT_FORM:
                         │       │       │   11 │ = pre_num_sub_edge + pre_num_sub_node - 2*num_sub_node - 1
                         │       │       │
                         │       │       │
                         │       │       │
                         │       │       │                # step_02
                        ┌┴─┐    ┌┴─┐    ┌┴─┐             -----------
                        │ 0│    │ 1│    │ 2│  7 │ = 7
                        │ 0│    │ 1│    │ 3│ 13 │ = 11 + 7 - 2*2 - 1
                        └──┘    └┬─┘    └┬─┘
                                 │       │
                                 │       │
                                ┌┴─┐    ┌┴─┐   
                                │ 0│    │ 1│
                                │ 0│    │ 1│
                                └──┘    └┬─┘
                                         │
                                         │
                                        ┌┴─┐
                                        │ 0│
                                        │ 0│
                                        └──┘        
'''


@dataclass(slots=True)
class Node:
    idx: int
    links: list[Any] = field(default_factory=list)  # list[Node]
    sub_nodes: int = 0
    sub_edge: int = 0


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return [0]
        # init graph in form of nodes
        graph: list[Node] = [Node(idx) for idx in range(n)]  # just a list of all nodes
        for node_a, node_b in edges:
            graph[node_a].links.append(graph[node_b])
            graph[node_b].links.append(graph[node_a])

        root = graph[0]
        self._dfr_back_calc(root)
        self._dfr_forward_calc(root)
        return [el.sub_edge for el in graph]

    def _dfr_back_calc(self, root: Node) -> None:
        vault_seen: set[int] = set()
        stack2visit: list[Node] = list()

        pre_nd: Node = root
        stack2visit.append(root)
        while len(stack2visit) != 0:
            nd: Node = stack2visit.pop()
            if nd.idx not in vault_seen:  # forward pass logic
                for child_nd in nd.links:  # add children to dfs process
                    if child_nd.idx not in vault_seen:
                        stack2visit.append(nd)  # need for backward pass
                        stack2visit.append(child_nd)
                vault_seen.add(nd.idx)
            else:  # backward pass logic
                nd.sub_nodes += pre_nd.sub_nodes + 1
                nd.sub_edge += pre_nd.sub_nodes + 1 + pre_nd.sub_edge
            pre_nd = nd

    def _dfr_forward_calc(self, root: Node) -> None:
        vault_seen: set[int] = set()
        stack2visit: list[tuple[Node, Node]] = list()  # element is a (node2visit, parent_node)

        stack2visit.append((root, root))
        while len(stack2visit) != 0:
            nd, pr_nd = stack2visit.pop()  # nd - node, pr_nd - parent_node
            # forward pass logic
            for child_nd in nd.links:  # add children to dfs process
                if child_nd.idx not in vault_seen:
                    stack2visit.append((child_nd, nd))
            vault_seen.add(nd.idx)

            if nd is pr_nd:  # corner case for root node
                continue

            nd.sub_edge = pr_nd.sub_edge + pr_nd.sub_nodes - 2 * nd.sub_nodes - 1  # calc
            nd.sub_nodes = pr_nd.sub_nodes


if __name__ == '__main__':
    foo = Solution()
    time_diff = -time.perf_counter()
    for name, inpt, outpt in [
        ('test_00', (6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]), [8, 12, 6, 10, 10, 10]),
        ('test_01', (1, []), [0]),
        ('test_02', (2, [[1, 0]]), [1, 1]),
        data_for_996.test_64,
    ]:
        if name == 'test_0':
            print(foo.sumOfDistancesInTree(*inpt))
            quit()
        # print(foo.sumOfDistancesInTree(*inpt))
        assert foo.sumOfDistancesInTree(*inpt) == outpt, print('👉', name, foo.sumOfDistancesInTree(*inpt), 'vs', outpt)
    time_diff += time.perf_counter()
    print('done', time_diff)  # 16.163291250006296

