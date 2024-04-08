from typing import TypeVar, MutableSequence
from typing_extensions import Protocol


class SupportsLowerThan(Protocol):
    def __lt__(self, other) -> bool: ...


T = TypeVar("T", bound=SupportsLowerThan)


def quicksort(seq: MutableSequence[T], low: int, high: int) -> None:
    # Complexities (in theory, don't necessarily match below implementation)
    # time : O(n²) in the worst case, O(n·log(n)) on average if randomized
    # space : O(log(n)) memory can be achieved if implemented with care
    if low < high:
        p = partition(seq, low, high)
        quicksort(seq, low, p - 1)
        quicksort(seq, p + 1, high)


def partition(seq: MutableSequence[T], low: int, high: int) -> int:
    """Partition sequence in linear time"""
    # Pick left most element as pivot
    pivot = high
    first_high = low
    print(f"Partitionning {seq}")
    for i in range(low, high):
        # Fact : ∀i, first_high ≤ i
        # Array is divided in three
        # Right of i (current) is unexplored
        # Right of first_high are values ≥ than pivot
        # Left of first_high are values < than pivot
        # Display current, pivot and first_high position
        print("".join(map(str, seq)))
        print(
            "".join(
                {i: "c", pivot: "p", first_high: ">"}.get(pos, " ")
                for pos in range(len(seq))
            )
        )
        if seq[i] < seq[pivot]:
            seq[i], seq[first_high] = seq[first_high], seq[i]
            first_high += 1
        print(
            "".join(
                {pivot: "p", first_high: ">"}.get(pos, " ") for pos in range(len(seq))
            )
        )
    seq[pivot], seq[first_high] = seq[first_high], seq[pivot]
    return first_high


if __name__ == "__main__":
    s = "quicksort"
    seq = list(s)
    quicksort(seq, 0, len(s) - 1)
    print(seq)
