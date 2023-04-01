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
## Synthesis
  Program synthesis will generate a program that will solve the stated problem, within a specified program solution space i.e. with control over the space of programs, not just the intended behaviour. An example is flash fill (Excel) which derives and applies a small program to the rest of the data.
  The order can also be rveersed e.g. start with a program and search for the specification i.e. reverse engineering e.g. Verified Lifting - discovering a high level representation that is provably equivalent to an implementation which can then be used to generate a more efficient version of the program.
  Three major challenges:
  ### Intention
  - Semantic and syntactic constraints: form of user input will influence the synthesis system e.g. input-output examples like flash fill may not be suitable. May need a multimodal approach with some examples or abstract examples combined with logical specifications, to provide enough data about intended behaviour. 
  - Under specification: if there are multiple solutions that satisfy requirements, which one should be chosen?
  ### Invention
  - Discovering the code to satisfy the requirements
  ### Adaptation
  - The application of synthesis to broader software development e.g. bug fixing, optimisation and other maintenance or non-greenfield tasks

# References

[^1] 

- A. Solar-Lezama, MIT 6.S981 <a href="https://people.csail.mit.edu/asolar/SynthesisCourse/index.htm">Introduction to Program Synthesis</a>
  

