def count_letters(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    return counts
