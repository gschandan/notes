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
def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)

print("Test 1:", isAnagram("racecar", "carrace"))
print("Test 2:", isAnagram("jar", "jam"))
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
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    char_count = [0] * 26
    for i in range(len(s)):
        char_count[ord(s[i]) - ord('a')] += 1
        char_count[ord(t[i]) - ord('a')] -= 1
    

    return all(count == 0 for count in char_count)

print("Test 1:", isAnagram("racecar", "carrace")) 
print("Test 2:", isAnagram("jar", "jam"))          
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
from collections import defaultdict

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    char_count = defaultdict(int)
    
    # Count characters in both strings
    for s_char, t_char in zip(s, t):
        char_count[s_char] += 1
        char_count[t_char] -= 1
    
    # Check if all counts are zero
    return all(count == 0 for count in char_count.values())

# Test cases
print("Test 1:", isAnagram("racecar", "carrace"))  # True
print("Test 2:", isAnagram("jar", "jam"))          # False
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
