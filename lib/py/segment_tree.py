class SegmentTree(object):
    def __init__(self, array, func=lambda x, y: x + y):
        self.array = array
        self.func = func
        self.tree = [None] * 4 * len(array)
        self._build(1, 0, len(array) - 1)

    def _build(self, v, l, r):
        if l == r:
            self.tree[v] = self.array[l]
        else:
            m = (l + r) // 2
            self._build(v * 2, l, m)
            self._build(v * 2 + 1, m + 1, r)
            self.tree[v] = self.func(self.tree[v * 2], self.tree[v * 2 + 1])

    def query(self, l, r):
        return self._query(1, 0, len(self.array) - 1, l, r)

    def _query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return self.func(
            self._query(v * 2, tl, tm, l, min(r, tm)),
            self._query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
        )

    def update(self, index, value):
        self._update(1, 0, len(self.array) - 1, index, value)

    def _update(self, v, tl, tr, index, value):
        if tl == tr:
            self.tree[v] = value
        else:
            tm = (tl + tr) // 2
            if index <= tm:
                self._update(v * 2, tl, tm, index, value)
            else:
                self._update(v * 2 + 1, tm + 1, tr, index, value)
            self.tree[v] = self.func(self.tree[v * 2], self.tree[v * 2 + 1])

    def inc(self, index, value):
        self._inc(1, 0, len(self.array) - 1, index, value)

    def _inc(self, v, tl, tr, index, value):
        if tl == tr:
            self.tree[v] += value
        else:
            tm = (tl + tr) // 2
            if index <= tm:
                self._inc(v * 2, tl, tm, index, value)
            else:
                self._inc(v * 2 + 1, tm + 1, tr, index, value)
            self.tree[v] = self.func(self.tree[v * 2], self.tree[v * 2 + 1])
