def is_perm(string1: str, string2: str) -> bool:
    # O(nlog(n)) time
    if len(string1) != len(string2):
        return False
    string1 = "".join(sorted(string1))
    string2 = "".join(sorted(string2))
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            return False
    return True
