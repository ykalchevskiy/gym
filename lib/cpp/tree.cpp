// http://stackoverflow.com/questions/11230734/order-statistic-tree-in-c
// http://codeforces.com/blog/entry/11080
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

typedef
tree<
  int,
  null_type,
  less<int>,
  rb_tree_tag,
  tree_order_statistics_node_update>
set_t;

set_t s;
s.order_of_key(0);
s.find_by_order(0);
