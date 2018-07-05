# GradientDescent

Project to learn about gradient descent.

Two different methods are implemented:

(1) Simple, unconstrained gradient descent
(2) Constrained gradient descent for equality constraints using penalty method

NOTES:

- Input start vector and function to be optimized into "optimizer" function

- Function to be optimized must take a vector "x" of parameters to be optimized

- Does not support step size computation. 

- The algorithm is not very stable with a large amount of variables and jumps around. It finds the optimium, and jumps away. May be circumvented by having a looser convergence criterion.
