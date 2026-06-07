"""
146. LRU Cache  ·  Medium  ·  Linked List (design)
==================================================
(run: python3 0146_lru_cache.py)

Design a Least-Recently-Used cache with O(1) get and put. get/put both count as
"using" a key; when capacity is exceeded, evict the least recently used key.

PATTERN: hash map (key -> node) + doubly linked list ordered by recency. Move a
touched node to the front (most recent); evict from the back. O(1) per op.
"""


class LRUCache:
    def __init__(self, capacity: int):
        # TODO
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1          # 1 is now most recent
    c.put(3, 3)                   # evicts key 2
    assert c.get(2) == -1
    c.put(4, 4)                   # evicts key 1
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4

    # Overwriting an existing key updates value and recency.
    d = LRUCache(2)
    d.put(2, 1)
    d.put(2, 2)
    assert d.get(2) == 2
    d.put(1, 1)
    d.put(4, 1)                   # evicts key 2 (LRU)
    assert d.get(2) == -1


if __name__ == "__main__":
    try:
        test()
        print("PASS  0146 LRUCache")
    except NotImplementedError:
        print("----  0146 LRUCache — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0146 LRUCache: {e}")
