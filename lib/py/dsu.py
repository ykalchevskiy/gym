class DSU(object):
    def __init__(self, n):
        self.ids = range(n)
        self.sizes = [1] * n

    def root(self, x):
        while x != self.ids[x]:
            x = self.ids[x]
        return x

    def is_connected(self, u, v):
        return self.root(u) == self.root(v)

    def connect(self, u, v):
        ru = self.root(u)
        rv = self.root(v)
        if self.sizes[ru] < self.sizes[rv]:
            self.ids[ru] = rv
            self.sizes[rv] += self.sizes[ru]
        else:
            self.ids[rv] = ru
            self.sizes[ru] += self.sizes[rv]
