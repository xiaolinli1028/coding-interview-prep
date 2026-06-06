"""
283. Move Zeroes  ·  Easy  ·  Two Pointers
==========================================
(run: python3 0283_move_zeroes.py)

Move all 0's to the end of `nums` while keeping the relative order of the non-zero
elements. Modify the array IN PLACE (don't return a copy).

  [0,1,0,3,12] -> [1,3,12,0,0]

PATTERN: a write pointer for the next non-zero slot; sweep once placing non-zeros,
then fill the rest with 0 (or swap as you go). Time O(n), O(1) space.
"""

from typing import List


def move_zeroes(nums: List[int]) -> None:
    """Modify nums in place. Returns None."""
    # TODO
    raise NotImplementedError


# ── tests ─────────────────────────────────────────────────────────────────────
def test():
    def run(arr):
        move_zeroes(arr)
        return arr

    assert run([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert run([0]) == [0]
    assert run([1, 2, 3]) == [1, 2, 3], "no zeros"
    assert run([0, 0, 1]) == [1, 0, 0]
    assert run([1, 0, 2, 0, 3]) == [1, 2, 3, 0, 0], "order preserved"
    # ensure in-place (same object mutated, not a new list returned)
    a = [0, 5, 0]
    assert move_zeroes(a) is None and a == [5, 0, 0], "must mutate in place"


if __name__ == "__main__":
    try:
        test()
        print("PASS  0283 move_zeroes")
    except NotImplementedError:
        print("----  0283 move_zeroes — not implemented yet")
    except AssertionError as e:
        print(f"FAIL  0283 move_zeroes: {e}")
