"""
189. Rotate Array  ·  Medium  ·  Arrays
=======================================
(run: python3 0189_rotate_array.py)

Rotate `nums` to the right by `k` steps, IN PLACE. (k may exceed len(nums).)

  [1,2,3,4,5,6,7], k=3 -> [5,6,7,1,2,3,4]

PATTERN: the reverse trick — reverse the whole array, then reverse the first k and
the rest. O(n) time, O(1) space. Remember k %= n.
"""

from typing import List


def rotate(nums: List[int], k: int) -> None:
    """Modify nums in place. Returns None."""
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    def run(arr, k):
        rotate(arr, k)
        return arr

    assert run([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert run([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
    assert run([1, 2], 3) == [2, 1], "k > n must wrap (k %= n)"
    assert run([1], 0) == [1]
    a = [1, 2, 3]
    assert rotate(a, 1) is None and a == [3, 1, 2], "must mutate in place"


if __name__ == "__main__":
    try:
        test()
        print("PASS  0189 rotate")
    except NotImplementedError:
        print("----  0189 rotate — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0189 rotate: {e}")
