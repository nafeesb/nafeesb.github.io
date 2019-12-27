---
layout: publication
title: Pyramid Coordinates for Deformation with Collision Handling
journal: ACM SIGGRAPH 2016 Talks
authors: Gene Lin, Nafees Bin Zafar, Junze Zhou, Edwin Ng
pdfurl: http://www.nafees.net/siggraph/lin-pyramid_coord-2016.pdf
acmdl: 2927400
---

We present an efficient implementation of the reconstruction of pyramid
coordinates which are used for the deformation of animated characters. By
reformulating the pyramid coordinates as an optimization problem with one-ring
neighborhood constraints, we can solve the problem using an efficient projective
solver. This greatly improves the overall performance, and makes it easier to
incorporate other geometric constraints. Collisions between the deformed and
kinematic geometries are handled using a two-pass methodology. By resolving
collisions before applying pyramid coordinate constraints, we obtain a
consistent result after the constraint projection. Dynamic simulation is also
possible by modeling proper constraints and projection operators under the same
framework.

{% include youtube.html id="nDHKl1pP-q8" %}