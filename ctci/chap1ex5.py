

def one_away(string1: str, string2: str) -> bool:
    if len(string1) == len(string2):
        # either same string or one character is different
        edits = 0
        for c, d in zip(string1, string2):
            if c != d:
                edits += 1
        return edits <= 1
    elif abs(len(string1)-len(string2)) == 1:
        # one extra character
        short = min(string1, string2, key=len)
        long = max(string1, string2, key=len)
        if len(short) == 0:
            return True

        pos = 0
        for c, d in zip(short, long):
            if c != d:
                break
            pos += 1
        # works even if we didn't break out the for loop
        # in that case, pos == len(short)-1
        return short[:pos]+long[pos]+short[pos:] == long
    else:
        # two extra characters is too much
        return False
