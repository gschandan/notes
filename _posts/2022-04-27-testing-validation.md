---
toc: true
layout: post
description: Defining the concepts of testing, training and validation sets
categories: [data, ML, training, testing, validation, cross-validation]
title: Training, Testing, Validation Datasets and Cross-Validation
---

# Datasets

To build a mathematical model to make predictions, data is needed to train and test the model, for which three data sets are usually used. Typically, the data is split into a training set and testing set (80-20 or 70-30 etc.), or a training, testing and validation set. Cross-Validation can be particularly helpful for smaller datasets, helping to avoid over-fitting and hyperparameter tuning.

## Training Set

Dataset used to create a model to be used for predictions. The model can then be applied to the training data sets to assess the accuracy of predictions against labelled data. The model can then be tuned if necessary.

## Testing Set

The model can then be applied to a testing set, data which has not been used to make the model, from which an error rate can be estimated (_generalisation error_).

If the training set error rate is low and the testing set error rate is high, it suggests the model has been over-fitted to the training data set.

## Validation Set

Another holdout dataset can be used is the validation set. It provides an unbiased estimation of the performance of the model which can be useful when assessing multiple models to minimise over-fitting. Multiple models can be trained with different hyperparameters, and evaluated against the validation set, with the best performing hyperparameters and model being used on the test dataset to estimate the generalisation error. They can also be used to stop training early on a model where the error on the validation set increases beyond a specified limit.

## Cross-Validation

If the dataset size is relatively smaller to begin with, to avoid issues with trying to train a model on less data, cross-validation can be used. The training dataset can be split up into subsets or subsamples. Each model can be trained against combinations of these and validated against the remaining ones. Then the final model can be trained, using the best performing hyperparameters, on the complete training set, so all observations have been used.

### Forms of Cross-Validation

- **K-folding**
  - Split the data int k-subsets e.g. 3,5, 10 etc.
  - Build k models, each trained on k-1 and tested on the datasets they haven't been trained on
- **Leave $p$ out**
  - Use $p$ observations as the validation set, and the remaining as the training set
  - This is repeated for as many variations of sampling p elements out of the total observations
  - if $p>1$, this will mean training and validating $C{n \choose p}$ times, where $n$ is the number of observations in the original sample
  - if $p=1$, as in leave-one-out, this will mean training and validating $C{n \choose 1}$ times. If $n$ is large, k-fold may be less computationally expensive.
- **Stratified k-fold**
  - Ensure that each fold is a representative sample of the whole population of observations e.g. mean is similar in all the subsets or proportions for binary classifiers
- **Repeated random sub-sampling**
  - Monte Carlo cross validation - create multiple random training and validation subsets, then for each split, fit the model to the training subset and assess the accuracy on the validation subset. Then average the results over the subsets.
  - Validation subsets may overlap, or some data points may never be used due to the random sampling.
  - Can also be stratified by the mean of the subsets

## No Free Lunch Theorem[^1]

- Any two optimisation algorithms are equivalent when their performance is averaged across all possible problems, if no assumptions are made about the data.

# References

[^1] Wolpert, D.H., Macready, W.G. (1997). No Free Lunch Theorems for Optimization. IEEE Transactions on Evolutionary Computation 1, 67

- Burkov, A. (2019) The Hundred-Page Machine Learning Book.
- Geron, A. (2017) Hands-On Machine Learning with Scikit-Learn & TensorFlow : concepts, tools, and techniques to build intelligent systems.
