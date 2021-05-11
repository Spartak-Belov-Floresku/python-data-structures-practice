def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    minN = float("inf")
    maxN = 0
    arr = d.keys()
    for val in arr:
        if isinstance(val, str):
            minN = str(minN)
            maxN = str(maxN)
        if val > maxN:
            maxN = val
        if val < minN:
            minN = val
    return (minN, maxN)