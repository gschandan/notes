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

def hasDuplicate(nums: list[int]) -> bool:
    items = set(nums)
    return len(items) != len(nums)

print('[1,2,3,3]',hasDuplicate([1,2,3,3]))
print('[1,2,3,4]',hasDuplicate([1,2,3,4]))
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

def hasDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print('[1,2,3,3]',hasDuplicate([1,2,3,3]))
print('[1,2,3,4]',hasDuplicate([1,2,3,4]))
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

def hasDuplicate(nums: list[int]) -> bool:
    counter = Counter(nums)
    return any(count > 1 for count in counter.values())

print('[1,2,3,3]',hasDuplicate([1,2,3,3]))
print('[1,2,3,4]',hasDuplicate([1,2,3,4]))
#
#
#
#
#
#
#

def hasDuplicate(nums: list[int]) -> bool:
    if not nums:
        return False
    nums.sort()
    return any(nums[i] == nums[i+1] for i in range(len(nums)-1))

print('[1,2,3,3]',hasDuplicate([1,2,3,3]))
print('[1,2,3,4]',hasDuplicate([1,2,3,4]))
#
#
#
#
#
#
#

def hasDuplicate(nums: list[int]) -> bool:
    n = len(nums)
    for i in range(n):
        index = abs(nums[i])  # Get the corresponding index
        if index >= n:        # Skip if the index is out of range
            continue
        if nums[index] < 0:   # Duplicate found
            return True
        nums[index] = -nums[index]  # Mark the number as seen
    return False


print('[1,2,3,3]',hasDuplicate([1,2,3,3]))
print('[1,2,3,4]',hasDuplicate([1,2,3,4]))
#
#
#
#
#
#
#
#
#
