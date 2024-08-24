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

Top down search can utilise types to assist in pruning invalid programs efficiently. A basic algorithm will start from the grammar rules and test with the inputs, pruning out programs that are fully expanded which don't return the correct output or which return incompatible types. Some languages will have infinite types, e.g. for supporting nested lists and functions.
Typing rules have the following form:
$$ \frac{premises}{context ⊢ expr : \tau } $$
 ⊢ = proves or satisfies or is derived or assuming
 expr will have type $\tau$ in a given context as long as all the premises are satisfied.
Alternatively:
$$ \frac{conditions}{Examples, ⊢ expression : \tau } $$

An example typing rule might be:
$$ \frac{\bold{\textit C},x : \tau_1 ⊢ expr : \tau_2}{\bold{\textit C} ⊢ \bold{\lambda}x.expr : \tau_1 \to \tau_2 } $$
states the following: $\bold{\lambda}x.expr$ will have type $\tau_1 \to \tau_2$ if it can be shown that $expr$ has type $\tau_2$ in a context that is like the context $\bold{\textit C}$ but that also has $x$ as having type $\tau_1$.

The search space can also be further restricted in further iterations/generations for functions like map; if the expected output is an array of integer arrays, the first expression must correspond to a function with a type of integer array, allowing filtering of programs that won't have the desired type before evaluating any concrete input values.

#### Deductive Rules

Type rules are a form of deductive rule; information about inputs/outputs are propogated to potential sub-expressions. Additional rules for different constructs in the language can prune the solution space. Given a candidate expression with an unknown subexpression 
$\bold{\textit f}$ 
and a set of input-outputs, the input-outputs can be propogated to the subexpression or establish that this line is not viable. Rules can inform the search if a candidate is not going to work e.g. map will always return a list of the same length so if the input length is different, map alone will not be viable. They can also provide information on how to propogate input-outputs to new expressions. It may not work when expressions involve functions e.g. if the same input value is mapped to multiple output values.

### Stochastic Search

#### Markov Chain

  A probabilistic process where there is a finite set of states 
  $ \chi $, and the probability of transitioning from a given state $x$ to a different state $y$ at each step of the process, is given by matrix 
  $ \bold{\textit K}(x,y): \chi \times \chi \to \reals $ where 
  $ \bold{\textit K}(x,y) \ge 0 $ and $ \sum_y \bold{\textit K}(x,y) = 1 $. Becuase the values of $\bold{\textit K}$ are probabilities, $\forall x,y. 0 \le \bold{\textit K}(x,y) < 1.0$
  and at every state there will be a transition (potentially to the same state) so  $\forall x.\sum_{y\in{\chi}} \bold{\textit K}(x,y) = 1.0$.  
  A markov chain is a sequence of states $\textit X_0, \textit X_1, \textit X_2,...$ in a markov process. The probability of the whole chain is the product of the probability of each transition:
  $$ (\textit X_1 = y|\textit X_0 = x) = \bold{\textit K} $$
  $$ \bold{\textit P}(\textit X_1 = y, \textit X_2 = z|\textit X_0 = x) = \bold{\textit K} $$
  $$ \bold{\textit P}(\textit X_2 = z|\textit X_0 = x) = \sum_y \bold{\textit K(x,y)} \times \bold{\textit K(y,z)} $$
  To obtain the probability that $X_2 = z$ given a starting point of $X_0 = x$, then we need to consider all the possible states of $X_1$ to get from $x$ to $z$. This is $ \sum_y \bold{\textit K(x,y)} \times \bold{\textit K(y,z)} $. $\bold{\textit K}$ is a matrix which gives the probability of transitioning from $x$ to $y$ in one step. $\bold{\textit K}^2$ is the probability of transitioning in 2 steps, and $\bold{\textit K}^n (x,y)$ is the probability of transitioning from $x$ to $y$ in exactly $n$ steps.

#### Stationary Distributions



# References

[^1] A. Solar-Lezama, MIT 6.S981 <a href="https://people.csail.mit.edu/asolar/SynthesisCourse/index.htm">Introduction to Program Synthesis</a>
  

