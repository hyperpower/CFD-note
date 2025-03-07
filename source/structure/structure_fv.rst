Cell-Centered Structure Grid
===========================================

Define a two-dimensional region in the real number space,
where the region is denoted by :math:`\mathbb{Z}` and 
its boundary is denoted by :math:`\Gamma`, see :numref:`fig-dd`.

.. _fig-dd:
.. figure:: fig/structure_domain.png
    
    Domain and boundary define 

Structure grid is defined as a grid with a regular topological structure, 
where the grid points are arranged in an orderly manner 
and can typically be uniquely identified 
using a logical two- or three-dimensional coordinate system 
(e.g., :math:`i,j,k`). 
In other words, the cells or control volumes
(such as quadrilaterals in 2D,  see :numref:`fig-cell`, or hexahedrons in 3D) 
in a structured grid are organized 
in a systematic row-and-column fashion, 
with well-defined geometric relationships between neighboring cells.

.. _fig-cell:
.. figure:: fig/structure_fv.png
    
    Structure Grid and cells definition 