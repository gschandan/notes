---
aliases:
- /data/maths/statistics/ML/2022/04/19/data-types
categories:
- data
- maths
- statistics
- ML
date: '2022-04-19'
description: Data Types, Quality & Quantity
layout: post
title: Data in ML
toc: true

---

# Types

Common taxonomy of data types when considering machine learning

- **Categorical**: _qualitative_

  - _Ordinal_: innate ordered values with unknown distances between them that cannot be measured
    - e.g. first/second/third, good/bad
  - _Nominal_: values (text or numbers) with no order
    - e.g. cat/dog, genre, ethnicity

- **Numerical**: _quantitative_
  - Discrete: quantitative whole number values
    - e.g. step count
  - Continuous: quantitative decimal values
    - e.g. width, height

# Quality

- Training data should be _representative_ of the data that will be predicted with
- _Sampling noise_: small sample leads to models that provide imprecise predictions due to chance [^1]
- _Sampling bias_: data in the sample may have a higher or lower probability of occurring compared to the original data
- Discard outliers
- Ignore or impute missing values, or train models with and without those values and compare their performances
- _Feature engineering_ - feature selection (useful data), feature extraction (combining features to make more useful ones, e.g. dimensionality reduction), feature creation (new data)

# Quantity

- More data supplied to simple algorithms can perform better than complex algorithms trained on smaller datasets
- Trade off- cost of acquiring and storing more data vs tuning algorithms

# References & Further Reading

[^1]: http://economistjourney.blogspot.com/2018/06/what-is-sampling-noise.html.

- Banko, M. and Eric Brill. 2001. [Scaling to very very large corpora for natural language disambiguation.](https://doi.org/10.3115/1073012.1073017) Association for Computational Linguistics, USA, 26–33.
- Halevy, A., Norvig, P. and Fernando, N. (2009). [The Unreasonable Effectiveness of Data.](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf) Intelligent Systems, IEEE. 24. 8 - 12. 10.1109/MIS.2009.36.
- Geron, A. (2017) Hands-On Machine Learning with Scikit-Learn & TensorFlow : concepts, tools, and techniques to build intelligent systems.
