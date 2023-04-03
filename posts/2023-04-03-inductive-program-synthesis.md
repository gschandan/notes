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
  A simple implementation would be to construct all possible programs from the terminals of a grammar. This can be inefficient as the space of all expressions can grow quickly. Observationally equivalent programs are discarded (i.e. if the same output is generated based on the same input, the primitive can be discarded), which reduces the solution space exponentially.
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
One characteristic is that bottom-up search explores small programs before larger ones, so it can potentially find the smallest program that satisfies the specification. Further heuristics can be applied in the grow or eliminate function level to direct the search, and it copes well with symmetry reduction. However, even with aggressive pruning, it is hard to scale beyond small lists of terms, and whilst it can connect discrete components, it is not effective at determining constants. It also may fail at pruning if the language has context dependant semantics e.g. if the same expression had dufferent values in different contexts e.g. via mutation.

### Synthesis Through Unification (STUN)
By modularising the search, i.e. search for multiple programs that work for different inputs and find a way to combine them that will work for all inputs, the scalability can be improved. The first step is a best-effort synthesis (if it works on all then it is just returned), then it can try to either improve the current program by taking a selection of the currently failing inputs alongside the correctly mapped inputs, or STUN can be called recursively on the inputs where the synthesised program failed. Then the programs can be combined.
#### Anti/Unification
If there are no top-level branches to allow unification, *antiunification* can be used. Unification is finding a common structure for two different expressions by replacing variables with expressions. Antiunification is to process of finding the common structure by replacing expressions with variables. For example, if we find 2 expressions $a \times c$ and $b \times c$ cover all inputs, antiunification can produce a common expression $v \times c$ where v stands for a code fragment that can be solved, being a much smaller synthesis problem. When a recursive call to STUN is made, additional constraints can also be passed that the expression must satisfy to avoid situations where, for example, anntiunification cannot be used e.g. $b \times c$ would be chosen over $-b$ as $b \times c$ can be antiunified with $a \times c$. $\bigoplus$ represents unification.

### Hierarchical Search
Modularisation may also be performed if the program can be split into different levels of abstraction, and the search performed independently at each level. A potential optimisation here is if we can eliminate branches where the output is not a superset of the input set.
  
### Top Down Search



# References

[^1] A. Solar-Lezama, MIT 6.S981 <a href="https://people.csail.mit.edu/asolar/SynthesisCourse/index.htm">Introduction to Program Synthesis</a>
  

