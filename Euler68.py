import json
from copy import deepcopy
from itertools import count
from collections import defaultdict


def main():
    arr = []
    for total in range(13, 21):
        arr.extend(run(total, 10))
    arr = list(filter(lambda x: x < 1e16, arr))
    print(max(arr))


def test():
    arr = []
    for total in range(9, 13):
        arr.extend(run(total, 6))
    assert max(arr) == 432621513


def run(total, num_nodes):
    cycle_len = num_nodes // 2
    nodes = {}
    for i in range(1, num_nodes + 1):
        rem = total - i
        partners = set()
        for j in range(max(1, rem - num_nodes), (rem + 1) // 2):
            if i in [j, rem - j]:
                continue
            partners |= {j, rem - j}
        nodes[i] = partners
    mid = defaultdict(list)  # mid node -> full branch
    for a in nodes:
        for b in nodes[a]:
            c = total - a - b
            mid[b].append((a, b, c))

    def process(conn, exclude, history):
        """clockwise"""
        next = []
        for a, b, c in mid[conn]:
            if len(history) == cycle_len - 1:
                if c != history[0][1]:
                    continue
                if a in exclude:
                    continue
            else:
                if {a, c} & exclude:
                    continue
            next.append(
                (
                    c,
                    exclude | {a, b},
                    history + [(a, b, c)],
                ),
            )
        return next

    to_process = []
    for a in nodes:
        for b in nodes[a]:
            c = total - a - b
            to_process.append((c, {a, b}, [(a, b, c)]))

    for i in range(cycle_len - 1):
        next_to_process = []
        for task in to_process:
            next_to_process.extend(process(*task))
        to_process = next_to_process

    res = []
    for _, _, history in to_process:
        index = min(range(len(history)), key=lambda i: history[i][0])
        history = history[index:] + history[:index]
        h = ""
        for i, line in enumerate(history):
            h += "".join(map(str, line))
        res.append(int(h))
    return res


if __name__ == "__main__":
    test()
    main()
