---
title: Central Finite Difference of Derivatives(中心有限差分)
date: 2016-10-13 03:53:58
categories: [PDE]
tags:  [modeling, FD, error]
---

This post derived the method of central finite difference for calculating derivatives, especially for first and second order derivatives, and finally arrive at perfect results. Example are provided to verify the results.

<!-- more -->
<!-- toc -->


## Taylor expansion
According to Taylor expansion, we have:

$$
\begin{eqnarray}
    f(x+\delta ) & = & f(x) +  \delta  f'(x) +
                            \frac{\delta ^2}{2!}  f''(x)  +
                            \frac{\delta ^3}{3!}  f^{(3)} (x)  +
                            ... +
                            \frac{\delta ^i}{i!}  f^{(i)} (x)  +
                            \frac{\delta ^n}{n!}  f^{(n)} (x)  +
                            O(\delta^{n+1})\\
    f(x-\delta ) & = & f(x) -  \delta  f'(x) +
                        \frac{\delta ^2}{2!}  f''(x)  -
                        \frac{\delta ^3}{3!}  f^{(3)} (x)  +
                        ... +
                        \frac{(-\delta)^i}{i!}  f^{(i)} (x)  +
                        \frac{(-\delta)^n}{n!}  f^{(n)} (x)  +
                        O(\delta^{n+1})
\end{eqnarray}
$$


## Derivatives
In physical field, it is first and second order derivatives, as well as other boundary(initial) functions or constants, that compose the differential control equations. So we only pay attention to the first and second order derivatives.
Adding and subtraction of $f(x+\delta)$ and $f(x-\delta)$ lead to:
$$
\begin{eqnarray}
    \frac{f(x+\delta) + f(x-\delta)}{2} & = & f(x) +    \frac{\delta^2}{2!} f''(x) +
                                                        \frac{\delta^4}{4!} f^{(4)}(x) +
                                                        \frac{\delta^{2i}}{(2i)!} f^{(2i)}(x) +
                                                        O( \delta^{2i+2})
                                                        \label{second} \\
    \frac{f(x+\delta) - f(x-\delta)}{2} & = & \delta f'(x) +
                                            \frac{\delta^3}{3!} f^{(3)}(x) +
                                            \frac{\delta^5}{5!} f^{(5)}(x) +
                                            \frac{\delta^{2i-1}}{(2i-1)!} f^{(2i-1)}(x) +
                                            O(\delta^{2i+1})
                                            \label{first}

\end{eqnarray}
$$

#### (1) First order derivative
According to $\eqref{first}$, $f'(x)$ should be:
$$
\begin{eqnarray}
    f'(x;\delta) = \frac{f(x+\delta) - f(x-\delta)}{2\delta}
                                                        - \frac{\delta^2}{3!} f^{(3)}(x)
                                                        - \frac{\delta^4}{5!} f^{(5)}(x)
                                                        - \frac{\delta^{2i-2}}{(2i-1)!} f^{(2i-1)}(x)
                                                        + O(\delta^{2i})
\end{eqnarray}
$$
omitting tail items leads to $f'(x) = \frac{f(x+\delta) - f(x-\delta)}{2\delta}$. The accuracy is $O(\delta^2)$, known as second order accuracy.

#### (2) Second order derivative
In the same way, $f''(x)$ is derived from $\eqref{second}$
$$
\begin{eqnarray}
 f''(x;\delta)  = \frac{f(x+\delta) + f(x-\delta) - 2f(x)}{ \delta^2}
                                                    - \frac{2\delta^2}{4!} f^{(4)}(x)
                                                    - \frac{2\delta^4}{6!} f^{(6)}(x)
                                                    - \frac{2\delta^{2i-2}}{(2i)!} f^{(2i)}(x)
                                                    + O( \delta^{2i})
\end{eqnarray}
$$
omitting tail items leads to $f''(x) = \frac{f(x+\delta) + f(x-\delta) - 2f(x)}{ \delta^2}$. The accuracy is $O(\delta^2)$, also know as second order accuaray.


## Higher Order Accuracy
To increase the accuracy, $f'(x;\delta)$, $f'(x;2\delta)$, $f'(x;3\delta)$...etc are could be added together by appropriate ratios to counteract the items of $\delta^2$,$\delta^4$,$\delta^6$...etc. This method works for $f''(x)$ as well.
#### (1) $f'(x)$
For step of $\delta$, $2\delta$, $3\delta$...etc, we have:
$$
\begin{eqnarray}
    \begin{cases}
        f'(x; \delta) & = & \frac{f(x+\delta) - f(x-\delta)}{2\delta}
                                        - \frac{\delta^2}{3!} f^{(3)}(x)
                                        - \frac{\delta^4}{5!} f^{(5)}(x)
                                        - \frac{\delta^{2i-2}}{(2i-1)!}  f^{(2i-1)}(x)
                                        + O(\delta^{2i})\\
        f'(x;2\delta) & = & \frac{f(x+2\delta) - f(x-2\delta)}{2 (2\delta)}
                                        - \frac{2^2\delta^2}{3!}  f^{(3)}(x)
                                        - \frac{2^4\delta^4}{5!}  f^{(5)}(x)
                                        - \frac{2^{2i-2}\delta^{2i-2}}{(2i-1)!}  f^{(2i-1)}(x)
                                        + O(\delta^{2i}) \\
        f'(x;3\delta) & = & \frac{f(x+3\delta) - f(x-3\delta)}{2 (3\delta)}
                                        - \frac{3^2\delta^2}{3!}  f^{(3)}(x)
                                        - \frac{3^4\delta^4}{5!}  f^{(5)}(x)
                                        - \frac{3^{2i-2}\delta^{2i-2}}{(2i-1)!}  f^{(2i-1)}(x)
                                        + O(\delta^{2i}) \\
        ...\\
        f'(x;N\delta) & = & \frac{f(x+N\delta) - f(x-N\delta)}{2 (N\delta)}
                                        - \frac{N^2\delta^2}{3!}  f^{(3)}(x)
                                        - \frac{N^4\delta^4}{5!}  f^{(5)}(x)
                                        - \frac{N^{2i-2}\delta^{2i-2}}{(2i-1)!}  f^{(2i-1)}(x)
                                        + O(\delta^{2i}) \\
    \end{cases}
\end{eqnarray}
$$
summing all these items proportionally from $f'(x;\delta)$ to $f'(x;N\delta)$ leads to:
$$
\begin{equation}
\begin{aligned}
    f'(x) = &\sum \limits_{k=1}^N {C_k \frac{ f(x+k\delta) - f(x-k\delta) }{2k\delta} } + O(\delta^{2i}) \\
            & - \frac{\delta^2 f^{(3)}(x) }{3!} \sum \limits_{k=1}^N {C_k k^2}
              - \frac{\delta^4 f^{(5)}(x) }{5!} \sum \limits_{k=1}^N {C_k k^4}
              - ...
              - \frac{\delta^{2i-2} f^{(2i-1)}(x) }{5!} \sum \limits_{k=1}^N {C_k k^{2i-2}}
\end{aligned}
\end{equation}
$$
$$
\begin{equation}
C_1+C_2+C_3+...+C_N = 1
\end{equation}
$$

so, if we want to have 2ith order accuracy, all item coefficients of $\sum \limits_{k=1}^N {C_k k^{**}}$ must have value of zero. Besides, to determine the value of $C_1,C_2,...,C_N$, $i$ should equals to $N$. So we arrive at a linear equation of $C$:

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
    \label{M_C}
\end{equation}
$$

By calculation, $C_1,C_2,C_3,...,C_N$ have the value of:


#### (2) $f''(x)$
For step of $\delta$, $2\delta$, $3\delta$...etc, we have:
$$
\begin{eqnarray}
    \begin{cases}
        f''(x; \delta)  & = & \frac{f(x+\delta) + f(x-\delta) - 2f(x)}{ \delta^2}
                                                            - \frac{2\delta^2}{4!} f^{(4)}(x)
                                                            - \frac{2\delta^4}{6!} f^{(6)}(x)
                                                            - \frac{2\delta^{2i-2}}{(2i)!} f^{(2i)}(x)
                                                            + O( \delta^{2i}) \\
f''(x;2\delta)  & = & \frac{f(x+2\delta) + f(x-2\delta) - 2f(x)}{ 2^2\delta^2}
                                                    - 2^2     \frac{2 \delta^2}{4!} f^{(4)}(x)
                                                    - 2^4     \frac{2 \delta^4}{6!} f^{(6)}(x)
                                                    - 2^{2i-2}\frac{2 \delta^{2i-2}}{(2i)!} f^{(2i)}(x)
                                                    + O( \delta^{2i}) \\
f''(x;3\delta)  & = & \frac{f(x+3\delta) + f(x-3\delta) - 2f(x)}{3^2 \delta^2}
                                                    - 3^2     \frac{2 \delta^2}{4!} f^{(4)}(x)
                                                    - 3^4     \frac{2 \delta^4}{6!} f^{(6)}(x)
                                                    - 3^{2i-2}\frac{2 \delta^{2i-2}}{(2i)!} f^{(2i)}(x)
                                                    + O( \delta^{2i}) \\
f''(x;N\delta)  & = & \frac{f(x+N\delta) + f(x-N\delta) - 2f(x)}{N^2 \delta^2}
                                                    - N^2     \frac{2 \delta^2}{4!} f^{(4)}(x)
                                                    - N^4     \frac{2 \delta^4}{6!} f^{(6)}(x)
                                                    - N^{2i-2}\frac{2 \delta^{2i-2}}{(2i)!} f^{(2i)}(x)
                                                    + O( \delta^{2i})
    \end{cases}
\end{eqnarray}
$$
summing all these items proportionally from $f'(x;\delta)$ to $f'(x;N\delta)$ leads to:
$$
\begin{equation}
    \begin{aligned}
        f''(x) = & \sum \limits_{k=1}^N F_k \frac{ f(x+k\delta) - f(x-k\delta) -2f(x) }{k^2 \delta^2} +O( \delta^{2i}) \\
                & - \frac{2 \delta^2}{4!} f^{(4)}(x) \sum \limits_{k=1}^N F_k k^2
                  - \frac{2 \delta^4}{6!} f^{(6)}(x) \sum \limits_{k=1}^N F_k k^4
                  ...
                  - \frac{2 \delta^{2i-2}}{(2i)!} f^{(2i)}(x) \sum \limits_{k=1}^N F_k k^{2i-2}
    \end{aligned}
\end{equation}
$$
$$
\begin{equation}
F_1+F_2+F_3+...+F_N = 1
\end{equation}
$$

so, if we want to have 2ith order accuracy, all item coefficients of $\sum \limits_{k=1}^N {F_k k^{**}}$ must have value of zero. Besides, to determine the value of $F_1,F_2,...,F_N$, $i$ should equals to $N$. So we arrive at a linear equation of $F$, which is same as $\eqref{M_C}$.

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
        F_1 \\ F_2 \\ F_3 \\ F_4 \\ ... \\ F_N
    \end{bmatrix}
    =
    \begin{bmatrix}
        1 \\ 0 \\ 0 \\ 0 \\ ... \\ 0
    \end{bmatrix}
    \label{M_F}
\end{equation}
$$


## Conclusion
To sum up, finite difference of 2Nth order accuracy for first or second order derivative are:

$$
\begin{eqnarray}
D  [f(x)]   & = & \sum \limits_{k=1}^N {C_k \frac{ f(x+k\delta) - f(x-k\delta) }{2k\delta} } \\
D^2[f(x)]   & = & \sum \limits_{k=1}^N C_k \frac{ f(x+k\delta) - f(x-k\delta) -2f(x) }{k^2 \delta^2} \\
%C_k         & = &
\end{eqnarray}
$$

Values of $C_k$ are obtained by [solving vandermonde equation](http://sheng09.github.io/2016/10/15/vandermonde/).
$$
\begin{eqnarray}
    \begin{cases}
    C_i & = & \frac{ (-1)^{i-1}  (i-1)! i! } { (2i-1)! } - \sum \limits_{j=i+1}^N \frac  { i (j+i-1)! } { j(2i-1)!(j-i)! } C_i \\
    %\left[ i= 1,2,3...,N-1 \right]\\
    C_N & = & \frac  { (-1)^{N-1}  (N-1)! N! } { (2N-1)! } \\
    \end{cases}
\end{eqnarray}
$$

by simplifying:
$$
\begin{eqnarray}
D  [f(x)]   & = & \sum \limits_{k=1}^N  \frac{c_k}{\delta}   \left[f(x+k\delta) - f(x-k\delta)         \right] \\
D^2[f(x)]   & = & \sum \limits_{k=1}^N  \frac{f_k}{\delta^2} \left[f(x+k\delta) - f(x-l\delta) - 2f(x) \right]  \\
c_k         & = & \frac{C_k}{2k} \\
f_k         & = & \frac{C_k}{k^2}
\end{eqnarray}
$$
Values of $C_k$, $c_k$ and $f_k$ are:

|order|$C_{1}$ |$C_{2}$ |$C_{3}$ |$C_{4}$ |$C_{5}$ |$C_{6}$ |
|-|-|-|-|-|-|
|2| $1$ | | | | | |
|4| $4/3$ | $-1/3$ | | | | |
|6| $3/2$ | $-3/5$ | $1/10$ | | | |
|8| $8/5$ | $-4/5$ | $8/35$ | $-1/35$ | | |
|10| $5/3$ | $-20/21$ | $5/14$ | $-5/63$ | $1/126$ | |
|12| $12/7$ | $-15/14$ | $10/21$ | $-1/7$ | $2/77$ | $-1/462$ |

|order|$c_{1}$ |$c_{2}$ |$c_{3}$ |$c_{4}$ |$c_{5}$ |$c_{6}$ |
|-|-|-|-|-|-|
|2| $0.5$ | | | | | |
|4| $2/3$ | $-1/12$ | | | | |
|6| $3/4$ | $-3/20$ | $1/60$ | | | |
|8| $4/5$ | $-1/5$ | $4/105$ | $-1/280$ | | |
|10| $5/6$ | $-5/21$ | $5/84$ | $-5/504$ | $1/1260$ | |
|12| $6/7$ | $-15/56$ | $5/63$ | $-1/56$ | $1/385$ | $-1/5544$ |

|order|$f_{1}$ |$f_{2}$ |$f_{3}$ |$f_{4}$ |$f_{5}$ |$f_{6}$ |
|-|-|-|-|-|-|
|2| $1.0$ | | | | | |
|4| $4/3$ | $-1/12$ | | | | |
|6| $3/2$ | $-3/20$ | $1/90$ | | | |
|8| $8/5$ | $-1/5$ | $8/315$ | $-1/560$ | | |
|10| $5/3$ | $-5/21$ | $5/126$ | $-5/1008$ | $1/3150$ | |
|12| $12/7$ | $-15/56$ | $10/189$ | $-1/112$ | $2/1925$ | $-1/16632$ |

## Examples
Applying finite-difference method to calculate the first and second derivatives of $f(x)=sin(x)$, results of 2nd, 4th, 6th order accuracy are presented below, as well as their error.
[Codes](/exam/fd_eg.m)
![](/finite-difference/1st.jpg)
![](/finite-difference/2nd.jpg)

## What's more
Method presented above applies to collocated grid and symmetric points only. Find method for staggered grid, and [method for processing boundary points(asymmetric method)](http://sheng09.github.io/2016/10/17/finite-difference-asymmetric/).
