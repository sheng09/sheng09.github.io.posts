---
title: Solving Vandermonde Equation for FD
date: 2016-10-15 03:07:44
categories: [PDE]
tags:  [modeling, FD, error, Linear Equation]
---
This post presents how to solve vandermonde equation in finite-difference.　For 2N order accuracy [finite-difference of derivatives](http://sheng09.github.io/2016/10/13/finite-difference/#conclusion), $C_k(k=1,2,...,N)$ is the solution of a vandermonde equation:
$$
\begin{equation}
    \begin{bmatrix}
        1        & 1        & 1        & ... & 1        \\
        1^2      & 2^2      & 3^2      & ... & N^2      \\
        1^4      & 2^4      & 3^4      & ... & N^4      \\
        1^6      & 2^6      & 3^6      & ... & N^6      \\
        ... \\
        1^{2N-2} & 2^{2N-2} & 3^{2N-2} & ... & N^{2N-2}
    \end{bmatrix}
    \begin{bmatrix}
        C_1 \\ C_2 \\ C_3 \\ C_4 \\ ... \\ C_N
    \end{bmatrix}
    =
    \begin{bmatrix}
        1 \\ 0 \\ 0 \\ 0 \\ ... \\ 0
    \end{bmatrix}
    \label{equ}
\end{equation}
$$

<!-- more -->
<!-- toc -->

## Gaussian Elimination
This linear equation could be solved by gaussian elimination.
Augmented matrix of linear equation $\eqref{equ}$ is:

$$
\begin{equation}
    \begin{bmatrix}
        1^0 & 2^0 & 3^0 & 4^0 & 5^0 & 6^0 & ... & N^0 & 1\\
        1^2 & 2^2 & 3^2 & 4^2 & 5^2 & 6^2 & ... & N^2 & 0\\
        1^4 & 2^4 & 3^4 & 4^4 & 5^4 & 6^4 & ... & N^4 & 0\\
        1^6 & 2^6 & 3^6 & 4^6 & 5^6 & 6^6 & ... & N^6 & 0\\
        1^8 & 2^8 & 3^8 & 4^8 & 5^8 & 6^8 & ... & N^8 & 0\\
        ... \\
        1^{2N-2} & 2^{2N-2} & 3^{2N-2} & ... & ...& ...& ... & N^{2N-2} & 0 \\
    \end{bmatrix}
\end{equation}
$$

An upper triangular matrix could be obtained by subtracting the row $(i+1)$  from row $i$:

#### Step 1


$row(i+1) - row(i) [i=1,2,3,4,5,...,N-1] $

$$
\begin{equation}
    \begin{bmatrix}
        1^0 & 2^0              & 3^0                 & ... & N^0            & 1   \\
        0   & 2^2-1            & 3^2-1               & ... & N^2-1          &-1   \\
        0   & 2^2(2^2-1)       & 3^2(3^2-1)          & ... & N^2(N^2-1)     & 0   \\
        0   & 2^4(2^2-1)       & 3^4(3^2-1)          & ... & N^4(N^2-1)     & 0   \\
        0   & 2^6(2^2-1)       & 3^6(3^2-1)          & ... & N^6(N^2-1)     & 0   \\
        ... \\
        0   & 2^{2N-4}(2^2-1)  & 3^{2N-4}(3^2-1) 　& ... & N^{2N-4}(N^2-1)& 0   \\
    \end{bmatrix}
\end{equation}
$$

#### Step 2
$row(i+1) - 2^2row(i) [i=2,3,4,5,...,N-1] $
$$
\begin{equation}
    \begin{bmatrix}
        1 & 1     & 1                        & ... &  1                        & 1   \\
        0 & 2^2-1 &              3^2-1       & ... &               N^2-1       & -1  \\
        0 & 0     &    (3^2-2^2)(3^2-1)      & ... &     (N^2-2^2)(N^2-1)      & 2^2 \\
        0 & 0     & 3^2(3^2-2^2)(3^2-1)      & ... &  N^2(N^2-2^2)(N^2-1)      & 0   \\
        0 & 0     & 3^4(3^2-2^2)(3^2-1)      & ... &  N^4(N^2-2^2)(N^2-1)      & 0   \\
        ...\\
        0 & 0     & 3^{2N-6}(3^2-2^2)(3^2-1) & ... &  N^{2N-6}(N^2-2^2)(N^2-1) & 0   \\
    \end{bmatrix}
\end{equation}
$$

#### Step 3
$row(i+1) - 3^2row(i) [i=3,4,5,...,N-1] $

$$
\begin{equation}
    \begin{bmatrix}
        1 & 1     & 1                   & ... &   1                                & 1         \\
        0 & 2^2-1 &              3^2-1  & ... &                        N^2-1       & -1        \\
        0 & 0     &    (3^2-2^2)(3^2-1) & ... &              (N^2-2^2)(N^2-1)      & 2^2       \\
        0 & 0     & 0                   & ... &     (N^2-3^2)(N^2-2^2)(N^2-1)      & -2^23^2   \\
        0 & 0     & 0                   & ... &  N^2(N^2-3^2)(N^2-2^2)(N^2-1)      & 0         \\
        ...\\
        0 & 0     & 0                   & ... &  N^{2N-8}(N^2-3^2)(N^2-2^2)(N^2-1) & 0         \\
    \end{bmatrix}
\end{equation}
$$

#### Step k

$row(i+1) - k^2row(i) [i=k,k+1,...,N-1] $
...
#### Step N-1
$row(i+1) - k^2row(i) [i=N-1] $

Detail derivations are presented in [fd_coef_vandermonde.pdf](/exam/fd_coef_vandermonde.pdf).
## Result
Finally, the augmented matrix is:

$$
\begin{eqnarray}
    \begin{bmatrix}
        1 & a_{12} & a_{13} & a_{14}  & ... & a_{1N} 　　　　　& b_1  \\
        0 & 1      & a_{23} & a_{24}  & ... & a_{2N} 　　　　　& b_2  \\
        0 & 0      & 1      & a_{34}  & ... & a_{3N} 　　　　　& b_3  \\
        ...\\
        0 & 0      &0       & 0       & ... & 1      　　　　　& b_4  \\
    \end{bmatrix}\\

\end{eqnarray}
$$

$$
\begin{eqnarray}
    a_{ij} & = & \frac  { i (j+i-1)! } { j(2i-1)!(j-i)! } (j>i)\\
    b_i    & = & \frac  { (-1)^{i-1}  (i-1)! i! } { (2i-1)! } \\
\end{eqnarray}
$$


Thus:
$$
\begin{eqnarray}
    C_i & = & b_i - \sum \limits_{j=i+1}^N a_{ij}C_j = \frac{ (-1)^{i-1}  (i-1)! i! } { (2i-1)! }
                                                        - \sum \limits_{j=i+1}^N \frac  { i (j+i-1)! } { j(2i-1)!(j-i)! } C_i \\
    C_N & = & \frac  { (-1)^{N-1}  (N-1)! N! } { (2N-1)! } \\
        %& = &  \sum \limits_{i=k+1}^N \frac{1}{N-k} \frac { (-1)^{k-1}  (k-1)! k! (i-k)!i } { i(2k-1)! (i-k)! }
        %     - \sum \limits_{i=k+1}^N  \frac  { k (i+k-1)! } { i(2k-1)!(i-k)! } C_i \\
        %& = &  \sum \limits_{i=k+1}^N \frac{1}{ i(2k-1)!(i-k)! }
        %        \left[ \frac{ (-1)^{k-1}  (k-1)! k! (i-k)!i }{N-k} - { k (i+k-1)! } C_i \right]
\end{eqnarray}

$$

## Value and Program
Values of $C_i$ are calculated by [fd_coef.py](/exam/fd_coef.py).

|order|$C_{1}$ |$C_{2}$ |$C_{3}$ |$C_{4}$ |$C_{5}$ |$C_{6}$ |
|-|-|-|-|-|-|
|2| $1$ | | | | | |
|4| $4/3$ | $-1/3$ | | | | |
|6| $3/2$ | $-3/5$ | $1/10$ | | | |
|8| $8/5$ | $-4/5$ | $8/35$ | $-1/35$ | | |
|10| $5/3$ | $-20/21$ | $5/14$ | $-5/63$ | $1/126$ | |
|12| $12/7$ | $-15/14$ | $10/21$ | $-1/7$ | $2/77$ | $-1/462$ |
