---
layout: publication
title: Guiding of Smoke Animations Through Variational Coupling of Simulations at Different Resolutions
authors: Michael B. Nielsen, Brian B. Christensen, Nafees Bin Zafar, Doug Roble, Ken Museth
journal: Proceedings of the 2009 ACM SIGGRAPH/Eurographics Symposium on Computer Animation (SCA '09)
pdfurl: http://euler.nafees.net/siggraph/nielsen-variational_smoke-2009.pdf
acmdl: 1599499
---
We propose a novel approach to guiding of Eulerian-based smoke animations
through coupling of simulations at different grid resolutions. Specifically we
present a variational formulation that allows smoke animations to adopt the
low-frequency features from a lower resolution simulation (or non-physical
synthesis), while simultaneously developing higher frequencies. The overall
motivation for this work is to address the fact that art-direction of smoke
animations is notoriously tedious. Particularly a change in grid resolution can
result in dramatic changes in the behavior of smoke animations, and existing
methods for guiding either significantly lack high frequency detail or may
result in undesired features developing over time. Provided that the bulk
movement can be represented satisfactorily at low resolution, our technique
effectively allows artists to prototype simulations at low resolution (where
computations are fast) and subsequently add extra details without altering the
overall "look and feel". Our implementation is based on a customized multi-grid
solver with memory-efficient data structures.

