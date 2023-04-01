---
aliases:
- /math/linear-algebra/introduction/2022/04/30/linear-algebra-intro
categories:
- math
- linear-algebra
- introduction
date: '2022-04-30'
description: Introduction and basic concepts of linear algebra
layout: post
title: Introduction to Linear Algebra
toc: true
format:
  html:
    html-math-method: katex
---

# Introduction

Linear algebra deals with linear equations (no polynomial terms). However, it can still be used for approximations for non-linear systems. Uses in ML include solving for unknowns e.g. deep learning, dimensionality reduction e.g. PCA, ranking e.g. eigenvectors, associated recommendations and NLP e.g. SVD or matrix factorisation.

An example linear equation with many unknowns in a regression model of house prices:

$$\large y = \alpha + \beta x{_1} + \gamma x{_2} + ... + mx{_m}$$

$$y$$ = price, $$\alpha$$ = $$y$$-intercept, $$\beta$$ = number of rooms, $$\gamma$$ = area, $$x$$ = feature

When dealing with linear systems of equations, there can only be three types of solutions, none, one or infinite. Plotting the equations, if the lines are parallel, they will never intersect i.e. no solution, if the lines are overlapping, there are infinite solutions, else the lines will intersect at one point only (it is impossible for straight lines to intersect multiple times).

Using the house price regression model, we will have as many rows($$n$$) of these equations as we have house prices, each with its $$m_{-1}$$ features($$x$$) (m-1 due to alpha), and $$m+1$$ unknowns($$\alpha$$,$$\beta$$, $$\gamma$$) which is what we want to solve for:

$$ y = \alpha + \beta x{_1} + \gamma x{_2} + ... + m_{-1}x_{m_{-1}} $$

$$
\begin{bmatrix}
 y{_1} |\alpha + \beta x{_{1,1}} + \gamma x{_{1,2}} + ... + m_{-1}x{_{1,m_{-1}}} \\
 y{_2} | \alpha + \beta x{_{2,1}} + \gamma x{_{2,2}} + ... + m_{-1}x{_{2,m_{-1}}} \\
\dots \\
 y{_n} |  \alpha + \beta x{_{n,1}} + \gamma x{_{n,2}} + ... + m_{-1}x{_{n,m_{-1}}}
\end{bmatrix}
$$

This is a set (denoted by square brackets) of linear equations.

## Tensors

Tensors are a generalisation of vectors and matrices to any number of dimensions.

| Dimension | Name         | Description       |
| --------- | ------------ | ----------------- |
| 0         | Scalar       | magnitude (value) |
| 1         | Vector       | array             |
| 2         | Matrix       | 2d array (square) |
| 3         | 3-Tensor     | 3d array (cube)   |
| $$n$$     | $$n$$-Tensor | multidimensional  |

### Scalar Tensors

Single value, no dimensions, denoted by lower case italic variable names e.g. $$x$$

### Vectors

1-Dimensional ordered array of values, lower case bold italic name e.g. _$$\large \boldsymbol{x}$$_  
Elements are scalars, denoted non-bold lower case x with their index e.g. $$x{_1}$$

#### Vector Transposition

$$\begin{bmatrix}  x{_1} & x{_2} & x{_3} \end{bmatrix}{^T}$$ =

$$
\begin{bmatrix}
x{_1} \\
x{_2} \\
x{_3}
\end{bmatrix}
$$

Row vector of shape (1,3) transposed to a column vector shape (3,1).

#### Norms

Norms are functions that quantify vector magnitude (length).  
 $$\begin{bmatrix}  x{_1} & x{_2} \end{bmatrix} = \begin{bmatrix}  5 & 7 \end{bmatrix}$$ also represents a magnitude and direction from the origin.

$$\large L{^2}$$ Norm 
$$||\boldsymbol{x}||{_2} = \sqrt{\sum_{\substack{i}}x{_i}{^2}}$$  
Square each element in the vector, sum them, then take the square root.
Measures euclidean distance from the origin. Also commonly denoted $$\large||\boldsymbol{x}||$$

$$\large L{^1}$$ Norm $$||\boldsymbol{x}||{_1} = \sum_{\substack{i}}|x{_i}|$$  
Sum the absolute values in the vector. Varies linearly at all locations (not origin dependent).
Used when differences between zero and non-zero are needed.

Squared $$\large  L{^2}$$ Norm $$||\boldsymbol{x}||{_2^2} = \sum_{\substack{i}}x{_i}{^2}$$  
Similar to $$\large L{^2}$$ Norm, except we don't take the root, just return the squared value.
Computationally cheaper than $$\large L{^2}$$ Norm as sqaured $$\large L{^2}$$ Norm = $$\boldsymbol{x}{^T}\boldsymbol{x}$$. Derivative of element $$x$$ only requires that element, vs $$\large L{^2}$$ Norm which requires the vector. However, squared $$\large  L{^2}$$ Norm grows slowly near the origin so can't be used if zero/near-zero distinguishing is required.

$$\large L{^\infin}$$ Norm (or Max Norm) $$||\boldsymbol{x}||{_\infin} = max{_i}|x{_i}|$$  
Return maximum absolute value of the vector.

Generalised $$\large L{^p}$$ Norm $$||\boldsymbol{x}||{_p} = (\sum_{\substack{i}}|x{_i}|{^p}){^\frac{1}{p}}$$ for $$p$$ being a real number $$\geqslant 1$$

Norms, particularly $$\large L{^1}$$ and $$\large L{^2}$$ norms, are used to regularise objective functions

#### Unit Vectors

Unit vector is a special case where the L2 norm (length) is equal to one i.e. $$\boldsymbol{x}$$ is a unit vector with unit norm. $$\large||\boldsymbol{x}|| = 1$$

#### Basis Vectors

Basis vectors are vectors that can be scaled to represent any vector in a given vector space, typically unit vectors are used along the axes of the vector space. For example, the basis vectors $$i = (1,0)$$ and $$j=(0,1)$$, then we can represent a vector $$\boldsymbol v$$ as follows: $$\boldsymbol v = 0.5 i + 3j$$

#### Orthogonal Vectors

Sets of vectors where the dot product of the vectors are zero: $$\boldsymbol{x}{^T}\boldsymbol{y} = 0$$ i.e. assuming they are of non-zero length, they are at 90$$\degree$$ angles i.e. perpendicular. For an $$n$$-dimensional space, there are a maximum of $$n$$ mutually orthogonal vectors.

##### Orthonormal Vectors

Orthonormal vectors are orthogonal and have unit norm e.g. basis vectors.

### Matrices (2D Tensors)

Denoted uppercase, italics and bold
$$\boldsymbol X = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$$  
Notation is $$(n_{row},n_{col})$$  
Individual scalar elements denoted upper case italics only, e.g.
$$\boldsymbol X = \begin{bmatrix} X_{1,1} & X_{1,2} \\ X_{2,1} & X_{2,2} \end{bmatrix}$$

### Generalisation for $$n$$-dimensional Tensors

Upper-case, bold, italic, sans-serif font e.g. $${\char"1D5EB}$$  
For a 4-tensor $${\char"1D5EB}$$, an element at position $$(i,j,k,l)$$ would be denoted as $${\char"1D5EB} _{(i,j,k,l)}$$
