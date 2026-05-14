Interface Reconstruction
========================


In VOF/PLIC methods the interface is approximated in each cut cell by a portion of a straight line defined by the equation

.. math::
    :label: eq:line-equation

   \mathbf{n}\cdot\mathbf{x}=\alpha

where :math:`\mathbf{n}` is the normal vector of the interface and :math:`\alpha` is a constant. The area of the portion of the line that lies within the cell is equal to the volume fraction of the cell. 

The determination of :eq:`eq:line-equation` is basically a two step procedure:

1. Determine the normal vector :math:`\mathbf{n}`. 
2. Determine the constant :math:`\alpha` such that the area of the portion of the line that lies within the cell is equal to the volume fraction (C) of the cell.