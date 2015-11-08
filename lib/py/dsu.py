class DSU(object):
    def __init__(self, n):
        self._ids = range(n)
        self._sizes = [1] * n

    def root(self, x):
        while x != self._ids[x]:
            x = self._ids[x]
        return x

    def is_connected(self, u, v):
        return self.root(u) == self.root(v)

    def connect(self, u, v):
        ru = self.root(u)
        rv = self.root(v)
        if self._sizes[ru] < self._sizes[rv]:
            self._ids[ru] = rv
            self._sizes[rv] += self._sizes[ru]
        else:
            self._ids[rv] = ru
            self._sizes[ru] += self._sizes[rv]
