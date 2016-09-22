---
title: PML
date: 2016-09-16 01:54:33
categories:
tags: [FD]
---
本文介绍了一阶声波方程在二维下的有限差分模拟。

<!-- more -->
<!-- toc -->

## 控制方程
二维下不考虑输出源，二阶声波方程为：
$$
\begin{eqnarray}
    \frac{\partial^2 p}{\partial x^2} +
        \frac{\partial^2 p}{\partial z^2} & = &
        \frac{1}{v^2} \frac{\partial^2 p}{\partial t^2} \\
\end{eqnarray}
$$
对应的一阶压强-速度方程可以写成：
$$
\begin{eqnarray}
    \begin{cases}
        \frac{\partial p}{\partial t} & = & -\rho v^2(
            \frac{\partial q_x}{\partial x} +
            \frac{\partial q_z}{\partial z}
            )\\
        \frac{\partial q_x}{\partial t} & = &
            - \frac{1}{\rho} \frac{\partial p}{\partial x}\\
        \frac{\partial q_z}{\partial t} & = &
            - \frac{1}{\rho} \frac{\partial p}{\partial z}
    \end{cases}
\end{eqnarray}
$$

将压强$p$写作$p_x+p_y$，可以获得：
$$
\begin{eqnarray}
    \begin{cases}
        p & = & p_x + p_z\\
        \frac{\partial p_x}{\partial t} & = & -\rho v^2
            \frac{\partial q_x}{\partial x}\\
        \frac{\partial p_z}{\partial_t} & = & -\rho v^2
            \frac{\partial q_z}{\partial z}\\
        \frac{\partial q_x}{\partial t} & = &
            - \frac{1}{\rho} \frac{\partial (p_x+p_z)}{\partial x}\\
        \frac{\partial q_z}{\partial t} & = &
            - \frac{1}{\rho} \frac{\partial (p_x+p_z)}{\partial z}
    \end{cases}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \begin{cases}
        p & = & p_x + p_z \\
        \frac{\partial p_x}{\partial t} + d(x)p_x & = & -\rho v^2
            \frac{\partial q_x}{\partial x}\\
        \frac{\partial p_z}{\partial_t} + d(z)p_z & = & -\rho v^2
            \frac{\partial q_z}{\partial z}\\
        \frac{\partial q_x}{\partial t} + d(x)q_x & = &
            - \frac{1}{\rho} \frac{\partial (p_x+p_z)}{\partial x}\\
        \frac{\partial q_y}{\partial t} + d(z)q_z & = &
            - \frac{1}{\rho} \frac{\partial (p_x+p_z)}{\partial z}
    \end{cases}
\end{eqnarray}
$$

## 交错网格
构建二维下的交错网格。
<img src="/fd-2d-PML/grid1.jpg" width=400>

对于交错节点，$p$,$q_x$,$q_z$递推关系如下图：
<table>
    <tr>
      <td><img src="/fd-2d-PML/p1.jpg" width=200></td>
      <td><img src="/fd-2d-PML/q_x1.jpg" width=200></td>
      <td><img src="/fd-2d-PML/q_z1.jpg" width=200></td>
    </tr>
</table>

## 二阶精度有现差分实现
$$
\begin{eqnarray}
    \begin{cases}
        p & = & p_x + p_z \\

        \frac{\partial p_x}{\partial t} + d(x)p_x & = & -\rho v^2
            \frac{\partial q_x}{\partial x}\\

        \frac{\partial p_z}{\partial_t} + d(z)p_z & = & -\rho v^2
            \frac{\partial q_z}{\partial z}\\

        \frac{\partial q_x}{\partial t} + d(x)q_x & = &
            - \frac{1}{\rho} \frac{\partial (p_x+p_z)}{\partial x}\\

        \frac{\partial q_y}{\partial t} + d(z)q_z & = &
            - \frac{1}{\rho} \frac{\partial (p_x+p_z)}{\partial z}
    \end{cases}
    \Rightarrow
    \begin{cases}
        p & = & p_x + p_z \\
        D_t p_x & = & -\rho v^2 D_x q_x \\
        D_t p_z & = & -\rho v^2 D_z q_z \\
        D_t q_x & = & - \frac{1}{\rho}  D_x (p_x+p_z)\\
        D_t q_z & = & - \frac{1}{\rho}  D_z (p_x+p_z)
    \end{cases}
\end{eqnarray}
$$

### $q_x$递推
<img src="/fd-2d-PML/q_x1.jpg" width=200>
$$
\begin{eqnarray}
    D_t q_x(A) & = & - \frac{1}{\rho}  D_x p(A)
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \frac{1}{\Delta t}[q_x(D) - q_x(C)] & = & - \frac{1}{\rho \Delta x} [p(F) - p(E)]
\end{eqnarray}
$$

$$
\begin{eqnarray}
\begin{aligned}
    \frac{1}{\Delta t}[q_x(x_{i+1/2},z_{j},t_{m+1} )  - & q_x(x_{i+1/2},z_j,t_{m})] \\& =
    - \frac{1}{\rho \Delta x} [ p(x_{i+1},z_j,t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ]
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \begin{aligned}
        q_x(x_{i+1/2},z_{j},t_{m+1} ) = & q_x(x_{i+1/2},z_j,t_{m}) \\
        &- \frac{\Delta t}{\rho \Delta x} [ p(x_{i+1},z_j,t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ]
    \end{aligned}
\end{eqnarray}
$$


### $q_z$递推
<img src="/fd-2d-PML/q_z1.jpg" width=200>
$$
\begin{eqnarray}
    D_t q_z(B) & = & - \frac{1}{\rho}  D_z p(B)
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \frac{1}{\Delta t}[q_z(J) - q_z(H)] & = & - \frac{1}{\rho \Delta x} [p(G) - p(E)]
\end{eqnarray}
$$
$$
\begin{eqnarray}
\begin{aligned}
    \frac{1}{\Delta t}[q_z(x_{i},z_{j+1/2},t_{m+1} ) - & q_z(x_{i},z_{j+1/2},t_{m})] \\& =
    - \frac{1}{\rho \Delta x} [ p(x_i,z_{j+1},t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ]
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
\begin{aligned}
    q_z(x_{i},z_{j+1/2},t_{m+1} ) = & q_z(x_{i},z_{j+1/2},t_{m}) \\
    &- \frac{\Delta t}{\rho \Delta x} [ p(x_i,z_{j+1},t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ]
\end{aligned}
\end{eqnarray}
$$

### $p_x$递推
<img src="/fd-2d-PML/p1.jpg" width=400>
$$
\begin{eqnarray}
    D_t p_x & = & -\rho v^2 D_x q_x
\end{eqnarray}
$$

$$
\begin{eqnarray}
\begin{aligned}
    \frac{1}{\Delta t} [p_x(x_i,z_j,t_{m+1/2}) - & p_x(x_i,z_j,t_{m-1/2})] \\
    & = -\frac{\rho v^2}{\Delta x} [ q_x(x_{i+1/2},z_j,t_m) - q_x(x_{i-1/2,z_j,t_m}) ]\\
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
\begin{aligned}
    p_x(x_i,z_j,t_{m+1/2}) = & p_x(x_i,z_j,t_{m-1/2})\\
    &  -\frac{\rho v^2\Delta t}{\Delta x} [ q_x(x_{i+1/2},z_j,t_m) - q_x(x_{i-1/2,z_j,t_m}) ]\\
\end{aligned}
\end{eqnarray}
$$

### $p_z$递推
<img src="/fd-2d-PML/p1.jpg" width=400>
$$
\begin{eqnarray}
    D_t p_z & = & -\rho v^2 D_z q_z
\end{eqnarray}
$$

$$
\begin{eqnarray}
\begin{aligned}
    \frac{1}{\Delta t} [p_z(x_i,z_j,t_{m+1/2}) - & p_z(x_i,z_j,t_{m-1/2})] \\
    & = -\frac{\rho v^2}{\Delta x} [ q_z(x_i,z_{j+1/2},t_m) - q_z(x_i,z_{j-1/2},t_m) ]\\
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
\begin{aligned}
    p_z(x_i,z_j,t_{m+1/2}) = & p_z(x_i,z_j,t_{m-1/2}) \\
    &  -\frac{\rho v^2\Delta t}{\Delta x} [ q_z(x_i,z_{j+1/2},t_m) - q_z(x_i,z_{j-1/2},t_m) ]\\
\end{aligned}
\end{eqnarray}
$$


## 递推汇总
$$
\begin{eqnarray}
    \begin{aligned}
        \begin{cases}
            q_x(x_{i+1/2},z_{j},t_{m+1} ) = & q_x(x_{i+1/2},z_j,t_{m}) \\
                &- \frac{\Delta t}{\rho \Delta x} [ p(x_{i+1},z_j,t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ]
                \\
            q_z(x_{i},z_{j+1/2},t_{m+1} ) = & q_z(x_{i},z_{j+1/2},t_{m}) \\
                &- \frac{\Delta t}{\rho \Delta x} [ p(x_i,z_{j+1},t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ]
                \\
            p_x(x_i,z_j,t_{m+1/2}) = & p_x(x_i,z_j,t_{m-1/2})\\
                &-\frac{\rho v^2\Delta t}{\Delta x} [ q_x(x_{i+1/2},z_j,t_m) - q_x(x_{i-1/2,z_j,t_m}) ]
                \\
            p_z(x_i,z_j,t_{m+1/2}) = & p_z(x_i,z_j,t_{m-1/2}) \\
                &-\frac{\rho v^2\Delta t}{\Delta x} [ q_z(x_i,z_{j+1/2},t_m) - q_z(x_i,z_{j-1/2},t_m) ]
        \end{cases}
    \end{aligned}
\end{eqnarray}
$$

故而，波场递推关系为：
$$
\begin{equation}
    \begin{cases}
        q_x(t=0)\\
        q_z(t=0)\\
        p(t=\Delta /2)
    \end{cases}
    \Rightarrow
    \begin{cases}
        \color{red}{q_x(t=\Delta t)}\\
        \color{red}{q_z(t=\Delta t)}\\
    \end{cases}
    \\
    \Rightarrow
    \begin{cases}
        \color{red}{q_x(t=\Delta t)}\\
        \color{red}{q_z(t=\Delta t)}\\
        p(t=\Delta /2)
    \end{cases}
    \Rightarrow
        \color{blue}{p(t=3\Delta /2)}
    \\
    \Rightarrow
    \begin{cases}
        \color{red}{q_x(t=\Delta t)}\\
        \color{red}{q_z(t=\Delta t)}\\
        \color{blue}{p(t=3\Delta /2)}
    \end{cases}
    \Rightarrow
    \begin{cases}
        \color{green}{q_x(t=2\Delta t)}\\
        \color{green}{q_z(t=2\Delta t)}\\
    \end{cases}
    \\
    \Rightarrow
    \begin{cases}
        \color{green}{q_x(t=2\Delta t)}\\
        \color{green}{q_z(t=2\Delta t)}\\
        \color{blue}{p(t=3\Delta /2)}
    \end{cases}
    \Rightarrow
    ............
    \\ \\
    ... ...
\end{equation}
$$
