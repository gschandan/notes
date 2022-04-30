---
toc: true
layout: post
description: Introduction and basic concepts of linear algebra
categories: [math, linear-algebra, introduction]
title: Introduction to Linear Algebra
---

# Introduction

Linear algebra deals with linear equations (no polynomial terms). However, it can still be used for approximations for non-linear systems. Uses in ML include solving for unknowns e.g. deep learning, dimensionality reduction e.g. PCA, ranking e.g. eigenvectors, associated recommendations and NLP e.g. SVD or matrix factorisation.

An example linear equation with many unknowns in a regression model of house prices:

$\large y = \alpha + \beta x{_1} + \gamma x{_2} + ... + mx{_m}$

$y$ = price, $\alpha$ = $y$-intercept, $\beta$ = number of rooms, $\gamma$ = area, $x$ = feature

When dealing with linear systems of equations, there can only be three types of solutions, none, one or infinite. Plotting the equations, if the lines are parallel, they will never intersect i.e. no solution, if the lines are overlapping, there are infinite solutions, else the lines will intersect at one point only (it is impossible for straight lines to intersect multiple times).

Using the house price regression model, we will have as many rows($n$) of these equations as we have house prices, each with its $m$ features($x$), and $m+1$ unknowns($\alpha$,$\beta$, $\gamma$) which is what we want to solve for:

$\large y = \alpha + \beta x{_1} + \gamma x{_2} + ... + mx{_m}$

$\large \begin{bmatrix}
 y{_1}  \vert  \alpha + \beta x{_{1,1}} + \gamma x{_{1,2}} + ... + mx{_{1,m}} \\
 y{_2}  \vert  \alpha + \beta x{_{2,1}} + \gamma x{_{2,2}} + ... + mx{_{2,m}} \\
\dots \\ 
 y{_n}  \vert  \alpha + \beta x{_{n,1}} + \gamma x{_{n,2}} + ... + mx{_{n,m}}
\end{bmatrix}
$

This is a set (denoted by square brackets) of linear equations.

## Tensors

Tensors are a generalisation of vectors and matrices to any number of dimensions.

| Dimension | Name       | Description       |
| --------- | ---------- | ----------------- |
| 0         | Scalar     | magnitude (value) |
| 1         | Vector     | array             |
| 2         | Matrix     | 2d array (square) |
| 3         | 3-Tensor   | 3d array (cube)   |
| $n$       | $n$-Tensor | multidimensional  |

### Scalar Tensors

Single value, no dimensions, denoted by lower case italic variable names e.g. $x$

[Scalar Tensors notebook](../_notebooks/2022-04-30-scalar-tensors.ipynb)

### Linear Algebra

Ch 1-7 Strang [^1]
Ch 2 Goodfellow [^2]

# References

[^1]: Gilbert Strang. Introduction to linear algebra. Cambridge Press, Wellesley, MA, 2016.
[^2]: Ian Goodfellow et Al. Deep learning. MIT press, 2016.
