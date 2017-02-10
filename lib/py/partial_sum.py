def print_query(a, l, r):
    """
    >>> print_query([1], 0, 0)
    1
    >>> print_query([1, 2], 0, 0)
    1
    >>> print_query([1, 2], 0, 1)
    3
    >>> print_query([1, 2], 1, 1)
    2
    >>> print_query([1, 2, 3], 0, 1)
    3
    >>> print_query([1, 2, 3], 1, 2)
    5
    >>> print_query([1, 2, 3], 0, 2)
    6
    """
    prefix_sums = []
    val = 0
    for i in a:
        val += i
        prefix_sums.append(val)
    return prefix_sums[r] - (prefix_sums[l - 1] if l != 0 else 0)


def modify_queries(a, queries):
    """
    # [1 + 2 + 3, 2 + 3 + 4 + 5, 3 + 5 + 6]
    >>> modify_queries([0, 0, 0], [(0, 0, 1), (0, 1, 2), (0, 2, 3), (1, 1, 4), (1, 2, 5), (2, 2, 6)])
    [6, 14, 14]
    """
    ps = [0] * len(a)
    for l, r, v in queries:
        ps[l] += v
        if r != len(a) - 1:
            ps[r + 1] -= v
    for i in xrange(1, len(a)):
        ps[i] += ps[i - 1]
    return [i + p for i, p in zip(a, ps)]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

