"""
208. Implement Trie (Prefix Tree)  ·  Medium  ·  Graph (design)
===============================================================
(run: python3 0208_implement_trie.py)

Implement a trie supporting insert(word), search(word) (exact), and startsWith
(prefix).

PATTERN: nested dict of children plus an end-of-word flag; walk character by
character for each operation. Each op O(len(word)).
"""


class Trie:
    def __init__(self):
        # TODO
        raise NotImplementedError

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def startsWith(self, prefix: str) -> bool:
        raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    t = Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.startsWith("app") is True
    t.insert("app")
    assert t.search("app") is True
    assert t.startsWith("apx") is False
    assert t.search("apple") is True
    t2 = Trie()
    assert t2.search("a") is False
    assert t2.startsWith("") is True


if __name__ == "__main__":
    try:
        test()
        print("PASS  0208 Trie")
    except NotImplementedError:
        print("----  0208 Trie — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0208 Trie: {e}")
