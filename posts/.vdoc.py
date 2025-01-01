# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
nums = []
for i in range(10):
    nums.append(i)  # Seems O(1), but occasionally triggers resize
#
#
#
#
#
#
#
#
#
from collections import Counter 
counter = Counter()
for char in "hello":
    counter[char] += 1  # Usually O(1), but may trigger rehash
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
