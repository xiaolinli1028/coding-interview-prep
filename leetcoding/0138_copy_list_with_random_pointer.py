"""
138. Copy List with Random Pointer  ·  Medium  ·  Linked List
=============================================================
(run: python3 0138_copy_list_with_random_pointer.py)

Each node has a `next` pointer and a `random` pointer to any node (or None). Make
a deep copy of the list: new nodes, with next/random wired among the copies.

  [[7,None],[13,0],[11,4],[10,2],[1,0]]  ->  identical structure, all-new nodes

PATTERN: hash map old-node -> new-node in one pass, then wire next/random in a
second pass (or interleave copies inline). Time O(n), space O(n).
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Optional[Node]" = None, random: "Optional[Node]" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: Optional["Node"]) -> Optional["Node"]:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def _build(spec):
    """spec: list of (val, random_index|None) -> head with random pointers."""
    nodes = [Node(v) for v, _ in spec]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, r) in enumerate(spec):
        nodes[i].random = nodes[r] if r is not None else None
    return nodes[0] if nodes else None


def _serialize(head):
    """Return list of (val, random_index|None) keyed by position in the copy."""
    order = {}
    cur = head
    seq = []
    while cur:
        order[id(cur)] = len(seq)
        seq.append(cur)
        cur = cur.next
    out = []
    for node in seq:
        out.append((node.val, order[id(node.random)] if node.random else None))
    return out


def test():
    spec = [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]
    orig = _build(spec)
    copy = copy_random_list(orig)
    assert _serialize(copy) == spec
    # New nodes, not aliases of the originals.
    o, c = orig, copy
    while o:
        assert o is not c
        o, c = o.next, c.next

    assert copy_random_list(None) is None
    single = _build([(1, 0)])  # random points to self
    cp = copy_random_list(single)
    assert _serialize(cp) == [(1, 0)] and cp is not single


if __name__ == "__main__":
    try:
        test()
        print("PASS  0138 copy_random_list")
    except NotImplementedError:
        print("----  0138 copy_random_list — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0138 copy_random_list: {e}")
