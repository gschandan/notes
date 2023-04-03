---
title: "Inductive Program Synthesis"
categories:
- programming
- inductive-synthesis
- algorithm
date: '2023-04-03'
description: Notes about inductive program synthesis
layout: post
toc: true
format:
  html:
    html-math-method: katex
---

# Inductive Synthesis

## Explicit
### Bottom-Up Search
  A simple implementation would be to construct all possible programs from the terminals of a grammar. This can be inefficient as the space of all expressions can grow quickly. Observationally equivalent (i.e. if the same output is generated based on the same input, the primitive can be discarded). 
```
function synthesise (inputs, outputs):
  terms := set_of_all_terminals
  while(true):
    terms := grow(terms)
    terms := eliminate_observational_equivalents(terms, inputs);
    foreach(t in terms):
      if(is_correct(t, inputs, outputs)):
        return t;
```
  
# References

[^1] A. Solar-Lezama, MIT 6.S981 <a href="https://people.csail.mit.edu/asolar/SynthesisCourse/index.htm">Introduction to Program Synthesis</a>
  

