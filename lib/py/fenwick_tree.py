class FenwickTree(object):
    def __init__(self, array, func=lambda x, y: x + y, preserve=False):
        self._array = array
        self._tree = [0] * len(array)
        self._func = func
        self._preserve = preserve

    def func(self, left, right):
        return self._count(right) - self._count(left - 1)

    def inc(self, index, count):
        while index < len(self._tree):
            self._tree[index] += 1

    def _count(self, index):
        result = 0
        while index >= 0:
            result = self._func(result, self._tree[index])
            index = (index & (index + 1)) - 1
        return result
