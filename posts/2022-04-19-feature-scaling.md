---
aliases:
- /data/maths/statistics/ML/feature-scaling/2022/04/19/feature-scaling
categories:
- data
- maths
- statistics
- ML
- feature-scaling
date: '2022-04-19'
description: Rescaling, normalisation, standardisation
layout: post
title: Feature Scaling in ML
toc: true
format:
  html:
    html-math-method: katex
---

# Feature Scaling

For classifiers that calculate distances between points, e.g. Euclidean kNN or SVM, one feature can dominate the others purely due to scale when proportional contributions of all the features are wanted. Feature scaling (particularly standardisation) can also increase the convergence speed of gradient descent algorithms by altering the step size for each feature. Tree based algorithms and others (e.g. NB, LDA) are insensitive to the scale of the features as the decision to split at that node is not influenced by other features, rather the decision to split is usually based on what will decrease the variance or increase the homogeneity in the sub-nodes.

Generally, normalisation is applied when the distribution of the data is known to not be gaussian, e.g. for algorithms that do not presume a distribution e.g. kNN. It is important to consider outliers as normalising data with outliers will scale potentially important features into a small interval, so they must be handled first.

## Normalisation

- Prevents the scale of the variable from over-influencing the model due to unit difference
- Scale features or variables to a common scale without distortion of differences in the range
  - e.g. $[0,1]$
- Examples
  - Rescaling (min-max normalisation) to a range of $[0,1]$ or $[-1,-1]$ or $[a,b]$
    - $x'= \frac {x-min(x)} {max(x)-min(x)}$
    - $x'= \frac {(x-min(x))(b-a)} {max(x)-min(x)}$
  - Mean normalisation
    - $x'= \frac {x-average(x)} {max(x)-min(x)}$

## Standardisation

- Standardise to find out how many standard deviations the values have from the mean
- Standardisation will scale the data to have a mean of 0 and standard deviation of 1
- No specific upper or lower bound of values
- Methods:
  - Z-Score: for population mean and std.dev.
    - $\LARGE z = \frac{x - \mu}{\sigma}$
  - Z-Score (estimated): for sample mean and std.dev.($\large S$)
    - $\LARGE z = \frac{x - \bar x}{S}$
- Usages:
  - Standardising regression coefficients
  - Standardising variables prior to PCA

## Scaling to Unit Length

- Scale the components of a feature vector such that the overall vector has length 1
- e.g. dividing by the Euclidean length of the vector  
  $\large x'= \frac {x} {||x||}$

## References

- Wikipedia - [Feature Scaling](https://en.wikipedia.org/wiki/Feature_scaling#Methods)
- KDNuggets - [Feature Scaling](https://www.kdnuggets.com/2020/04/data-transformation-standardization-normalization.html)
