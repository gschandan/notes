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
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_array = [1, 3, 4, 6, 8, 9, 11]
target = 6
result = binary_search(sorted_array, target)
print(f"Target {target} found at index: {result}")
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
import numpy as np
import matplotlib.pyplot as plt
import time
import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def measure_search_time(search_func, arr, target):
    start_time = time.time()
    search_func(arr, target)
    end_time = time.time()
    return end_time - start_time

# Generate data points
sizes = np.logspace(1, 6, num=20, dtype=int)  # 10 to 1,000,000
linear_times = []
binary_times = []

for size in sizes:
    arr = sorted(random.sample(range(size * 10), size))
    target = random.choice(arr)
    
    linear_time = measure_search_time(linear_search, arr, target)
    binary_time = measure_search_time(binary_search, arr, target)
    
    linear_times.append(linear_time)
    binary_times.append(binary_time)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(sizes, linear_times, label='Linear Search', color='red', marker='o')
plt.plot(sizes, binary_times, label='Binary Search', color='green', marker='o')

plt.title('Binary Search vs Linear Search: Actual Performance')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.legend()

# Use log scale for both axes
plt.xscale('log')
plt.yscale('log')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Print some statistics
print(f"Largest input size: {sizes[-1]}")
print(f"Linear search time for largest input: {linear_times[-1]:.6f} seconds")
print(f"Binary search time for largest input: {binary_times[-1]:.6f} seconds")
print(f"Speedup factor for largest input: {linear_times[-1] / binary_times[-1]:.2f}x")
```
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
