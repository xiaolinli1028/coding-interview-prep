"""
394. Decode String  ·  Medium  ·  Stack
========================================
(run: python3 0394_decode_string.py)

Decode a string encoded as k[encoded] meaning the bracketed part repeated k
times. k is a positive integer; brackets may nest.

  "3[a]2[bc]"  ->  "aaabcbc"
  "3[a2[c]]"   ->  "accaccacc"

PATTERN: stack of (prev_string, repeat_count); on '[' push and reset, on ']' pop
and expand. Time O(output length), space O(depth).
"""


def decode_string(s: str) -> str:
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert decode_string("abc") == "abc"
    assert decode_string("10[a]") == "a" * 10


if __name__ == "__main__":
    try:
        test()
        print("PASS  0394 decode_string")
    except NotImplementedError:
        print("----  0394 decode_string — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0394 decode_string: {e}")
