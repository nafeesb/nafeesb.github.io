---
layout: publication
title: Blobtacular&#58; Surfacing Particle Systems in "Pirates of the Caribbean 3"
authors: Ken Museth, Michael Clive, Nafees Bin Zafar
journal: ACM SIGGRAPH 2007 Sketches
pdfurl: http://www.nafees.net/siggraph/museth-blobtacular-07.pdf
acmdl: 1278804
---
The core of this sketch was about generating smooth surfaces from low density
particle based fluid simulation.  The algorithm looked at the neighborhood of
particles around each particle to compute an ellipsoid.  Enough overlapping
ellipsoids leads to a smoother surface.  Prior methods involved stamping the
particles as spheres, which produced a "cottage cheese" appearance.  The method
was used heavily on "Pirates of the Carribbean 3".

{% include youtube.html id="ZtHQO5Rq2Pg" %}
