def all_unique_chars_0(string: str) -> bool:
    # fastest
    return len(set(string)) == len(string)


def all_unique_chars_1(string: str) -> bool:
    counts = []
    for c in string:
        if c in counts:
            return False
    return True


def all_unique_chars_2(string: str) -> bool:
    # No extra data structure, time O(n²)
    for pos, char in enumerate(string):
        if char in string[pos + 1 :]:
            return False
    return True


def all_unique_chars_3(string: str) -> bool:
    # O(nlog(n)) time
    string = "".join(sorted(string))
    for pos, char in enumerate(string):
        if pos < len(string) - 1 and char == string[pos + 1]:
            return False
    return True


def v4(string: str) -> bool:
    vector = 0
    for c in string:
        val = ord(c)
        if vector & (1 << val):
            return False
        vector |= 1 << val
    return True


if __name__ == "__main__":
    for s in ["", "a", "aze", "azeza"]:
        print(all_unique_chars_3(s))
