---
toc: true
layout: post
description: Rescaling, normalisation, standardisation
categories: [data, maths, statistics, ML, feature-scaling]
title: Feature Scaling in ML
---

# Feature Scaling

definition here

## Normalisation

- Prevents the scale of the variable from over-influencing the model due to unit difference
- Scale features or variables to a common scale without distortion of differences in the range
  - e.g. $0-1$
-

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

### References

-
