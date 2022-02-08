

import collections

a = [1, 2, 2, 4, 6, 6, 7]
b = collections.Counter(a)

print(b)

c = b.most_common(2)
print(c)

