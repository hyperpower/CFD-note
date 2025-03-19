List of Maclaurin series of some common functions
===================================================

Exponential function
----------------------

.. math::
    e^x&=\sum_{n=0}^\infty\frac{x^n}{n!} \\
       &=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots.

Natural logarithm
------------------

.. math::
    \ln(1-x)&=-\sum_{n=1}^\infty\frac{x^n}{n} \\
            &=-x-\frac{x^2}{2}-\frac{x^3}{3}-\cdots,
    
.. math::    
    \ln(1+x)&=\sum_{n=1}^\infty(-1)^{n+1}\frac{x^n}{n} \\
            &=x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots.

Geometric series
------------------

.. math::
    \frac{1}{1-x}=\sum_{n=0}^\infty x^n


.. math::
    \frac{1}{(1-x)^2}=\sum_{n=1}^\infty nx^{n-1}


.. math::
    \frac{1}{(1-x)^3}=\sum_{n=2}^\infty\frac{(n-1)n}{2}x^{n-2}.

Binomial series
----------------

Definition of binomial coefficients

.. math::
    \binom{\alpha}{n}=\prod_{k=1}^n\frac{\alpha-k+1}{k}=\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}

.. math::
    (1+x)^\alpha=\sum_{n=0}^\infty\binom{\alpha}{n}x^n

Trigonometric functions
------------------------

.. math::
    \sin x=\sum_{n=0}^\infty\frac{(-1)^n}{(2n+1)!}x^{2n+1}=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots\text{for all }x


.. math::
    \cos x=\sum_{n=0}^\infty\frac{(-1)^n}{(2n)!}x^{2n} ==1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots\text{for all }x 


.. math::
    \tan x&=\sum_{n=1}^\infty\frac{B_{2n}(-4)^n\left.(1-4^n)\right.}{(2n)!}x^{2n-1} \\
          &=x+\frac{x^3}{3}+\frac{2x^5}{15}+\cdots && \text{for} |x|<\frac{\pi}{2}


















