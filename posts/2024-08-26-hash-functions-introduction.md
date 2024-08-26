---
categories:
  - DSA
  - data-structures
  - introduction
  - prime-numbers
  - hash-functions
date: '2024-08-26'
description: Data Structures and Algorithms - Division Based Hash Functions
layout: post
title: Division Based Hash Functions
toc: true
format:
  html:
    html-math-method: katex
---

# Hash Functions - Prime Numbers {#sec-prime-hash-div}

## Why Prime Numbers are Used in Division Based Hash Functions

A simple modulus hash function can be defined as:

$$h(x) = x \mod n$$

Where $x$ is the input value (key) and $n$ is the number of buckets in the hash table. While $n$ can be any positive integer, choosing a prime number for $n$ can significantly reduce collisions, especially for certain types of input data.

### The Importance of Prime Numbers

Prime numbers are particularly useful when the keys are of the form $a + k \times b$, where $a$ and $b$ are constants and $k$ varies. This pattern is common in many applications, such as memory addresses or sequential IDs.

Using a prime number for $n$ helps to:

1. Reduce collisions
2. Ensure a more uniform distribution of hash values
3. Minimize the impact of patterns in the input data

### Example

If we have keys of the form $100 + k \times 50$, and we need to hash these into a table.

Case 1: Non-prime number of buckets
Using 100 buckets (non-prime).  

$$h(x) = x \mod 100$$  

For our keys:  
- $h(100) = 0$  
- $h(150) = 50$  
- $h(200) = 0$  
- $h(250) = 50$  
- $h(300) = 0$  

We see that all keys hash to either 0 or 50, utilizing only 2 out of 100 buckets.

Case 2: Prime number of buckets
Now using 101 buckets (prime).  

$$h(x) = x \mod 101$$  

For the same keys:   
- $h(100) = 100$  
- $h(150) = 48$  
- $h(200) = 99$  
- $h(250) = 47$  
- $h(300) = 98$  

We get a much better distribution, using 5 different buckets for our 5 keys.

### Explanation

When $n$ is not prime, it's more likely to share factors with the step size in the key pattern (in our example, 50). This causes the hash values to repeat in a cycle much shorter than $n$.

A prime $n$ is less likely to share factors with the key pattern, ensuring that the hash values cycle through a larger portion of the available buckets before repeating.

### Summary

While using a prime number doesn't guarantee perfect distribution or zero collisions, it significantly improves the hash function's performance for many common types of input data (especially those with patterns or structures).

# References

[^1] [Why is it best to use a prime number as a mod in a hashing function?](https://cs.stackexchange.com/questions/11029/why-is-it-best-to-use-a-prime-number-as-a-mod-in-a-hashing-function/64191#64191)

