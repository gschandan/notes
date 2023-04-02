---
title: "Introduction to Program Synthesis"
categories:
- programming
- introduction
- program-synthesis
date: '2023-04-01'
description: Notes about basic terms and concepts
layout: post
toc: true
format:
  html:
    html-math-method: katex
---

# Program Synthesis

## Compilation vs Synthesis
  Generally, compilers transform source code from the source language to the target language, usually to create an executable program, whereas program synthesisers *search* for a program that will satisfy some stated requirements. They both take high-level specifications to generate software, but synthesisers can search over a solution space to discover how to generate a program to satisfy the requirements (some compiler optimisations also do this e.g. autotuning).
  A program in this context, is a description of how to perform a computation. It is useful to constrain the solution to narrower notation than programming languages such as Domain Specific Languages (DSL) to avoid using specific constructs, rather build using a limited set of functions. Functional programming notation is useful for synthesis as we avoid side effects which can simplify the reasoning process, and can be expressed concisely.
## Synthesis
  Program synthesis will generate a program that will solve the stated problem, within a specified program solution space i.e. with control over the space of programs, not just the intended behaviour. An example is flash fill (Excel) which derives and applies a small program to the rest of the data.
  The order can also be rveersed e.g. start with a program and search for the specification i.e. reverse engineering e.g. Verified Lifting - discovering a high level representation that is provably equivalent to an implementation which can then be uo generate a more efficient version of the program.
  There are 3 major challenges; intention, invention and adaptation to consider.  
 ### Intention
  - Semantic and syntactic constraints: form of user input will influence the synthesis system e.g. input-output examples like flash fill may not be suitable. May need a multimodal approach with some examples or abstract examples combined with logical specifications, to provide enough data about intended behaviour. 
  - Under specification: if there are multiple solutions that satisfy requirements, which one should be chosen?
### Invention
  - Discovering the code to satisfy the requirements
### Adaptation
  - The application of synthesis to broader software development e.g. bug fixing, optimisation and other maintenance or existing codebase tasks.

## Inductive Synthesis
  Inductive synthesis generates a function that matches provided input-output examples.
### Programming by example (PBE) and Programming by demonstration (PBD)
  In PBE, just the input-output is provided, which can leave a large potential solution space e.g. $f(1) = 1$ which could be addition, division, multiplication etc.   
  In PBD, a trace of the computation performed is also provided to provide additional specification which makes it easier to infer the intended program, e.g. $f(1) = 1 \times 1 = 1$  
  PBD and PBE can still be under-specificed with a large solution program space; need to address how to find the program that matches the observations, and how to know that the program that the user required is the one that was found. 
  Arbritrary spaces can also be searched e.g. a large but highly constrained space, allowing exclusion of undesirable solutions, but would still likely require ranking of solutions.

## Programming
  Need to represent code as a data structure - Abstrac Syntax Trees (AST) are commonly used for this as they usually follow the same structure of the parse tree of the program, whilst ignoring additional characters e.g. parentheses, hence abstract. Context free grammar notation is often used to describe ASTs, to represent the structure of DSLs.

## Search Techniques
### Explicit Enumeration
    Explicitly construct programs until one satisfies the observations, ideally avoiding the generation of programs that are not viable e.g. cannot satisfy the observations or can be proven redundant from existing found solutions.
    - Bottom-Up: discover low level components then ho to assemble them into programs i.e. leaf nodes up.
    - Top-Down: discover the high level structure first, then enumerate to the low level components i.e. root down.
    The synthesiser will maintain a partial or completely constructed program that is being evaluated e.g. would evaluate potential solutions until success.
### Symbolic Search
    In symbolic searching, the synthesiser will maintain a symbolic representation of the space of all programs that are considered valid e.g. Version Space Algebras and Constraint Systems.
    A symbolic search may perform some algebraeic manipulation to deduce results which may perform better in some cases, but not all e.g. binary search being effective in finding solutions where algebraeic manipulation may be too costly.
## Program Solution Space
### Small DSL
  One way to simplify the solution space is to define or use a small DSL, then consider all possible valid programs within this language, using context free grammar to describe the ASTs. This makes it simple to enumerate all (or randomly sample) programs in a small DSL. If the DSL has a type system, this can help eliminate solutions which violate type rules.
### Constraint Based
  Constraint based approaches utilise parametric representations of the space - different choices of paramters correspond to different forms of the program. Paramtetric representations can be more general than grammars - grammars can be encoded in paramteric representation provided a boundary on the length of the program. 
  Paramteric programs can also be referred to as generative models, particularly when the free parameter choice is associated with probabilities.
### Symmetry
  If there are many ways to represent the same program, the program space has lots of symmetry. Symmetry can be reduced with reduction of cummtativity e.g. forcing right or left associativity. Constraint and enumeration based strategies can benefit from symmetry reduction, though there are additional techniques that are mostly removed from this issue.

# References

[^1] 

- A. Solar-Lezama, MIT 6.S981 <a href="https://people.csail.mit.edu/asolar/SynthesisCourse/index.htm">Introduction to Program Synthesis</a>
  

