---
title: Boundary Conditions for Differential Equations
date: 2016-09-01 03:34:51
categories: [PDE]
tags: [PDE]
---

There are different types of boundary conditions for ODE(Oridinary Differential Equation) and PDE(Partial Differential Equation). This post present all collections of these boundary conditions and associated equations.
Besides, this post also present the combination of Dirichlet and Neumann boundary conditions in construct absorbing boundary for solving wave eqution.
<!-- more -->
<!-- toc -->

## Dirichlet Boundary Condition
Given ODE or PDE, conditions that specify values of the solution along the boundary of the domain is Dirichlet boundary condition. [Wiki](https://en.wikipedia.org/wiki/Dirichlet_boundary_condition)

{% math %}
\begin{equation}
  \begin{cases}
    f(y'',y) & = & 0 \\
    y(\alpha) & = & 0 \\
    y(\beta) & = & 0
  \end{cases}
\end{equation}
{% endmath %}

{% math %}
\begin{equation}
  \begin{cases}
    f(\nabla^{2}G,G) & = & 0 \\
    G|_{boundary} & = & g(x,y,z)
  \end{cases}
\end{equation}
{% endmath %}

## Neumann Boundary Condition
Being different to Dirichlet boundary condition, Neumann boundary condition specify the values of the derivative of the solution along the boundary. [Wiki](https://en.wikipedia.org/wiki/Neumann_boundary_condition)
{% math %}
\begin{equation}
  \begin{cases}
    f(y'',y) & = & 0 \\
    y'|_{x=\alpha} & = & 0 \\
    y'|_{x=\beta} & = & 0
  \end{cases}
\end{equation}
{% endmath %}
{% math %}
\begin{equation}
  \begin{cases}
    f(G'',G) & = & 0 \\
    G'|_{boundary} & = & g(x,y,z) \\
  \end{cases}
\end{equation}
{% endmath %}

## Robin Boundary Condition
Robin boundary condition is the combination of Dirichlet and Neumann boundary conditions.[Wiki](https://en.wikipedia.org/wiki/Robin_boundary_condition)

{% math %}
\begin{equation}
  \begin{cases}
    f(G'',G) & = & 0 \\
    G+G'|_{boundary} & = & g(x)
  \end{cases}
\end{equation}
{% endmath %}

## Mixed Boundary Condition
Being different from Robin condition, Mixed condition means different types of condition along different subset of the boundary. It is much more complex than Robin condition.[Wiki](https://en.wikipedia.org/wiki/Mixed_boundary_condition)

{% math %}
\begin{equation}
  \begin{cases}
    f(G'',G) & = & 0 \\
    G|_{1st\ boundary\ subset} & = & g_1(x) \\
    G'|_{2nd\ boundary\ subset} & = & g_2(x)
  \end{cases}
\end{equation}
{% endmath %}

## Cauchy Boundary Condition
In Cauchy boundary condition, Dirichlet and Neumann conditions are declared along the boundary to ensure the unique solution. [Wiki](https://en.wikipedia.org/wiki/Cauchy_boundary_condition)

{% math %}
\begin{equation}
  \begin{cases}
    f(G'',G) & = & 0 \\
    G|_{boundary} & = & g_1(x) \\
    G'|_{ boundary} & = & g_2(x)
  \end{cases}
\end{equation}
{% endmath %}


## Associated Problems for PDE of Wave Equation
Considering boundary conditions for wave equation, Dirichlet and Neumann conditions produce reflection that are opposite in sign. Thus, the summation of these two cases will cancel the reflection.[[Smith 1974](http://www.sciencedirect.com/science/article/pii/0021999174900758)]

## Reference
[1] [Smith W D. A nonreflecting plane boundary for wave propagation problems[J]. Journal of Computational Physics, 1974, 15(4): 492-503.](http://www.sciencedirect.com/science/article/pii/0021999174900758)
