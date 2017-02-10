def merge(items, l, m, r):
    i, il = l, m + 1
    j, jl = m + 1, r + 1
    rv = []
    inv = 0
    while i < il and j < jl:
        if items[i] <= items[j]:
            rv.append(items[i])
            i += 1
        else:
            inv += m + 1 - i
            rv.append(items[j])
            j += 1
    if i < il:
        rv += items[i:il]
    if j < jl:
        rv += items[j:jl]
    items[l:r + 1] = rv
    return inv


def count_inversions(items, l=0, r=None):
    if r is None:
        r = len(items) - 1
    if l >= r:
        return 0
    count = 0
    m = (l + r) // 2
    count += count_inversions(items, l, m)
    count += count_inversions(items, m + 1, r)
    count += merge(items, l, m, r)
    return count
