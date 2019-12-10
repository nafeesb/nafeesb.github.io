---
layout: publication
title: A Schur Complement Preconditioner for Scalable Parallel Fluid Simulation
date: 2017-10-01
journal: ACM Transactions on Graphics (TOG)
authors: Jieyu Chu, Nafees Bin Zafar, Xubo Yang
pdfurl: http://www.nafees.net/siggraph/chu-schur_complement-2017.pdf
acmdl: 3092818
---
We present an algorithmically efficient and parallelized domain decomposition
based approach to solving Poisson’s equation on irregular domains. Our technique
employs the Schur complement method, which permits a high degree of parallel
efficiency on multi-core systems. We create a novel Schur complement
preconditioner which achieves faster convergence, and requires less computation
time and memory. This domain decomposition method allows us to apply different
linear solvers for different regions of the flow. Subdomains with regular
boundaries can be solved with an FFT based Fast Poisson Solver. We can solve
systems with 10243 degrees of freedom, and demonstrate its use for the pressure
projection step of incompressible liquid and gas simulations. The results
demonstrate considerable speedup over preconditioned conjugate gradient methods
commonly employed to solve such problems, including a multigrid preconditioned
conjugate gradient method.
