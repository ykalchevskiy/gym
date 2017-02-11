#include <vector>


struct DSU {
    vector<int> ids;
    vector<int> sizes;

    DSU(int n) {
        ids.resize(n);
        for (int i = 0; i < n; ++i)
            ids[i] = i;
        sizes.resize(n, 1);
    }

    int root(int x) {
        while (x != ids[x])
            x = ids[x];
        return x;
    }

    int is_connected(int u, int v) {
        return root(u) == root(v);
    }

    void connect(int u, int v) {
        int ru = root(u);
        int rv = root(v);
        if (ru == rv) {
            return;
        }
        if (sizes[ru] < sizes[rv]) {
            ids[ru] = rv;
            sizes[rv] += sizes[ru];
        }
        else {
            ids[rv] = ru;
            sizes[ru] += sizes[rv];
        }
    }
};
