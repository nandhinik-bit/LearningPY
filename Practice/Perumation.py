# PERMUTATION
# ip : [1,2,3]
# op: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

import itertools

n = list(map(int,input().split()))
perm = itertools.permutations(n)
print(list(perm))


# PERMUTATION 2
# print without dup
import itertools

n = list(map(int,input().split()))
s = set(n)
perm = itertools.permutations(s)
print(list(s))
