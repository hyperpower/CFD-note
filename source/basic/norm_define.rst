Definition of Norm 
==============================

Vector Norm
-------------------------------

Below are the definitions of the **L₁ norm** (1-norm), **L₂ norm** (2-norm), and **L∞ norm** (infinity norm) for an :math:`n`-dimensional vector :math:`x = (x_1, x_2, \dots, x_n)`.

1-Norm (Manhattan Norm)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Definition**:  
  The sum of the absolute values of the vector’s components:  

.. math::
   :label: eq:norm1_v
   \|x\|_1 = \sum_{i=1}^n |x_i|

- **Explanation**:  
  The L₁ norm represents the total “distance” traveled along the coordinate axes.



2-Norm (Euclidean Norm)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Definition**:  
  The square root of the sum of the squared components:  

.. math::
   :label: eq:norm2-v
   \|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2}

- **Explanation**:  
  The L₂ norm represents the straight-line distance from the origin to the vector’s endpoint in Euclidean space, 
  making it the most commonly used geometric distance measure.


Infinity Norm (Maximum Norm)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Definition**:  
  The maximum absolute value among the vector’s components:  

.. math::
   :label: eq:norminf-v
   \|x\|_\infty = \max_{i} |x_i|

- **Explanation**:  
  The L∞ norm reflects the “most extreme” component of the vector, indicating its maximum magnitude in any single direction.


Vector Norm Summary 
^^^^^^^^^^^^^^^^^^^^^^^

+------------+-----------------------------------+--------------------------+
| Norm       | Formula                           | Meaning                  | 
+============+===================================+==========================+
| L₁ Norm    | :math:`\sum_{i=1}^n |x_i|`        | Sum of absolute values   |                          
+------------+-----------------------------------+--------------------------+
| L₂ Norm    | :math:`\sqrt{\sum_{i=1}^n x_i^2}` | Euclidean distance       | 
+------------+-----------------------------------+--------------------------+
| L∞ Norm    | :math:`\max_i |x_i|`              | Maximum absolute value   | 
+------------+-----------------------------------+--------------------------+


Matrix Norm Definitions
-------------------------------

Below are the definitions of some commonly used matrix norms for an :math:`m \times n` matrix :math:`A = [a_{ij}]`.

1-Norm (Column Sum Norm)
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Definition**:  
  The maximum absolute column sum of the matrix:  
.. math::
   :label: eq:norm1-m

   \|A\|_1 = \max_{j} \sum_{i=1}^m |a_{ij}|

- **Explanation**:  
  This norm calculates the largest sum of absolute values across all columns, treating the matrix as a linear operator.


2-Norm (Spectral Norm)
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Definition**:  
  The largest singular value of the matrix:  
  
.. math::
   :label: eq:norm2-m

   \|A\|_2 = \sigma_{\max}(A)

where :math:`\sigma_{\max}(A)` is the maximum singular value from the SVD of :math:`A`.


- **Explanation**:  
  This norm measures the maximum “stretching” of a unit vector by the matrix, computed via singular value decomposition.


Infinity Norm (Row Sum Norm)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Definition**:  
  The maximum absolute row sum of the matrix:  

.. math::
   :label: eq:norminf-m

   \|A\|_\infty = \max_{i} \sum_{j=1}^n |a_{ij}|



- **Explanation**:  
  This norm calculates the largest sum of absolute values across all rows, dual to the 1-norm.



Frobenius Norm
^^^^^^^^^^^^^^^^^^

- **Definition**:  
  The square root of the sum of squared elements:  

.. math::
   :label: eq:norminf-f
  
   \|A\|_F = \sqrt{\sum_{i=1}^m \sum_{j=1}^n |a_{ij}|^2}



- **Explanation**:  
  This norm treats the matrix as a flattened vector and computes its Euclidean length.


Matrix Norm Summary Table
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------+-----------------------------------------+
| Norm          | Formula                                 | 
+===============+=========================================+
| 1-Norm        | :math:`\max_{j} \sum_{i=1}^m |a_{ij}|`  | 
+---------------+-----------------------------------------+
| 2-Norm        | :math:`\sigma_{\max}(A)`                | 
+---------------+-----------------------------------------+
| Infinity Norm | :math:`\max_{i} \sum_{j=1}^n |a_{ij}|`  |
+---------------+-----------------------------------------+
| Frobenius     | :math:`\sqrt{\sum_{i=1}^m \sum_{j=1}^n}`|
+---------------+-----------------------------------------+

Norm definitions in Finite Volume Mesh
----------------------------------------

Finite Volume Mesh definition can be found in :doc:`../structure/structure_fv`. 
The definitions can be found in [Devendran2017]_.

Given a computational domain :math:`\Omega` whose resolution is :math:`h`, 
:math:`V_i` is cell volume. 
:math:`V_{\Omega}` is the volume of the whole domain.


1-Norm
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Definition**:  
  The average absolute sum of the whole control volumes.

.. math::
   :label: norm1

   \|E\|_1=\frac{1}{V_{\Omega}} \int_{\Omega}\left|E_i\right| d V=\frac{1}{V_{\Omega}} \sum_{i \in \Omega}\left|E_i\right| V_i


2-Norm
^^^^^^^^^^^^^^^^^^^^^^^^^^
- **Definition**:  
  The square root of the average of the squared error in control volumes 

.. math::
   :label: eq:norm2

   \|E\|_2=\left(\frac{1}{V_{\Omega}} \int_{\Omega}\left|E_i\right|^2 d V\right)^{\frac{1}{2}}
   =\left(\frac{1}{V_{\Omega}} \sum_{i \in \Omega}\left|E_i\right|^2V_i\right)^{\frac{1}{2}}

Infinity Norm
^^^^^^^^^^^^^^^
- **Definition**:  
  The maximum absolute error in the domain  

.. math::
   :label: eq:norminf

   \|E\|_{\infty}=\max _{i \in \Omega}\left|E_i\right|


Norm definitions in Finite Deference Mesh
----------------------------------------

1-Norm
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Definition**:  
  The average absolute sum of the whole vertex.

.. math::
   :label: eq:fd_norm1

   \|E\|_1=\frac{1}{n} \sum_{i \in n}\left|E_i\right|




Reference
------------

.. [Devendran2017] Devendran, D., Graves, D. T., Johansen, H., & Ligocki, T. (2017). 
                   A fourth-order cartesian grid embedded boundary method for poisson’s equation. 
                   Communications in Applied Mathematics and Computational Science, 12(1), 51–79. 
                   https://doi.org/10.2140/camcos.2017.12.51