---
title: PML边界-一阶声波方程有线差分模拟在二维下的实现
date: 2016-09-17 01:54:33
categories: [PDE]
tags: [FD, modeling, wave equation]
---
本文介绍了二维下声波方程PML吸收边界的有限差分实现。
<img src="/fd-2d-PML/wave_field.jpg" width=600px >
<!-- more -->
<!-- toc -->

## PML区域控制方程
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

针对PML区域：
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

## $d(x)$的选择

$$
d(x) = log(\frac{1}{R}) \frac{3v}{2\delta}(\frac{x}{\delta})^2
$$

$R$推荐取0.001，$\delta$为PML层厚[[Collino and Tsogka 2001](http://library.seg.org/doi/abs/10.1190/1.1444908)]。

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
        D_t p_x + d(x)p_x & = & -\rho v^2 D_x q_x \\
        D_t p_z + d(z)p_z & = & -\rho v^2 D_z q_z \\
        D_t q_x + d(x)q_x & = & - \frac{1}{\rho}  D_x (p_x+p_z)\\
        D_t q_z + d(z)q_z & = & - \frac{1}{\rho}  D_z (p_x+p_z)
    \end{cases}
\end{eqnarray}
$$

### $q_x$递推
<img src="/fd-2d-PML/q_x1.jpg" width=200>
$$
\begin{eqnarray}
    D_t q_x(A) + d(A) q_x(A) & = & - \frac{1}{\rho}  D_x p(A)
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \frac{1}{\Delta t}[q_x(D) - q_x(C)] + \frac{d(A)}{2} [q_x(D) + q_x(C)] & = & - \frac{1}{\rho \Delta x} [p(F) - p(E)]
\end{eqnarray}
$$

$$
\begin{eqnarray}
\begin{aligned}
    \frac{1}{\Delta t}[q_x(x_{i+1/2},z_{j},t_{m+1} )  - & q_x(x_{i+1/2},z_j,t_{m})] + \\
    \frac{d(x_{i+1/2},z_j,t_{m+1/2})}{2}    [q_x(x_{i+1/2},z_{j},t_{m+1} )  + & q_x(x_{i+1/2},z_j,t_{m})] \\
    = - \frac{1}{\rho \Delta x} [ p(&x_{i+1},z_j,t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ]
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \begin{aligned}
    q_x(x_{i+1/2},z_{j},t_{m+1} )  = & c_{qx1} q_x(x_{i+1/2},z_j,t_{m}) \\ &+ c_{qx2} [ p(x_{i+1},z_j,t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ] \\
    \end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \begin{aligned}
      \begin{cases}
        c_{qx1}  =  \frac{ 2- \Delta t d(x_{i+1/2},z_j,t_{m+1/2})  }{2 + \Delta t d(x_{i+1/2},z_j,t_{m+1/2}) } \\
        c_{qx2}  =  -\frac{2 \Delta t}{\rho \Delta x [2 + \Delta t d(x_{i+1/2},z_j,t_{m+1/2})]}
      \end{cases}
    \end{aligned}
\end{eqnarray}
$$


### $q_z$递推
<img src="/fd-2d-PML/q_z1.jpg" width=200>
$$
\begin{eqnarray}
    D_t q_z(B) + d(B)q_z(B) & = & - \frac{1}{\rho}  D_z p(B)
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \frac{1}{\Delta t}[q_z(J) - q_z(H)] + \frac{d(B)}{2}[q_z(J) + q_z(H)] & = & - \frac{1}{\rho \Delta z} [p(G) - p(E)]
\end{eqnarray}
$$
$$
\begin{eqnarray}
\begin{aligned}
    \frac{1}{\Delta t}[q_z(x_{i},z_{j+1/2},t_{m+1} ) - & q_z(x_{i},z_{j+1/2},t_{m})]\\ +
    \frac{d(x_{i},z_{j+1/2},t_{m+1/2} )}{2}[q_z(x_{i},z_{j+1/2},t_{m+1} ) + & q_z(x_{i},z_{j+1/2},t_{m})] \\
    = - \frac{1}{\rho \Delta z} [ p(&x_i,z_{j+1},t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ]
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
\begin{aligned}
    q_z(x_{i},z_{j+1/2},t_{m+1} ) = & c_{qz1} q_z(x_{i},z_{j+1/2},t_{m}) \\
    &+c_{qz2} [ p(x_i,z_{j+1},t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ]
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \begin{aligned}
      \begin{cases}
        c_{qz1}  =  \frac{ 2- \Delta t d(x_{i},z_{j+1/2},t_{m+1/2})  }{2 + \Delta t d(x_{i},z_{j+1/2},t_{m+1/2}) } \\
        c_{qz2}  =  -\frac{2 \Delta t}{\rho \Delta z [2 + \Delta t d(x_{i},z_{j+1/2},t_{m+1/2})]}
      \end{cases}
    \end{aligned}
\end{eqnarray}
$$
### $p_x$递推
<img src="/fd-2d-PML/p1.jpg" width=400>
$$
\begin{eqnarray}
    D_t p_x + d(x)p_x & = & -\rho v^2 D_x q_x
\end{eqnarray}
$$

$$
\begin{eqnarray}
\begin{aligned}
    \frac{1}{\Delta t} [p_x(x_i,z_j,t_{m+1/2}) - & p_x(x_i,z_j,t_{m-1/2})]  \\
    +\frac{d(x_i,z_j,t_m)}{2} [p_x(x_i,z_j,t_{m+1/2}) + & p_x(x_i,z_j,t_{m-1/2})] \\
    = - &\frac{\rho v^2}{\Delta x} [ q_x(x_{i+1/2},z_j,t_m) - q_x(x_{i-1/2,z_j,t_m}) ]\\
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
\begin{aligned}
    p_x(x_i,z_j,t_{m+1/2}) = & c_{px1} p_x(x_i,z_j,t_{m-1/2})\\
    &  +c_{px2} [ q_x(x_{i+1/2},z_j,t_m) - q_x(x_{i-1/2,z_j,t_m}) ]\\
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \begin{aligned}
      \begin{cases}
        c_{px1}  =  \frac{ 2- \Delta t d(x_i,z_j,t_m)  }
                         {2 + \Delta t d(x_i,z_j,t_m) } \\
        c_{px2}  =  -\frac{2 \rho v^2 \Delta t}{\Delta x [2 + \Delta t d(x_i,z_j,t_m)]}
      \end{cases}
    \end{aligned}
\end{eqnarray}
$$

### $p_z$递推
<img src="/fd-2d-PML/p1.jpg" width=400>
$$
\begin{eqnarray}
    D_t p_z + d(z)p_z & = & -\rho v^2 D_z q_z
\end{eqnarray}
$$

$$
\begin{eqnarray}
\begin{aligned}
    \frac{1}{\Delta t}      [p_z(x_i,z_j,t_{m+1/2}) - & p_z(x_i,z_j,t_{m-1/2})] \\
    \frac{d(x_i,z_j,t_m)}{2}[p_z(x_i,z_j,t_{m+1/2}) + & p_z(x_i,z_j,t_{m-1/2})] \\
    = -&\frac{\rho v^2}{\Delta x} [ q_z(x_i,z_{j+1/2},t_m) - q_z(x_i,z_{j-1/2},t_m) ]\\
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
\begin{aligned}
    p_z(x_i,z_j,t_{m+1/2}) = & c_{pz1} p_z(x_i,z_j,t_{m-1/2}) \\
    &  +c_{pz2} [ q_z(x_i,z_{j+1/2},t_m) - q_z(x_i,z_{j-1/2},t_m) ]\\
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \begin{aligned}
      \begin{cases}
        c_{pz1}  =  \frac{ 2- \Delta t d(x_i,z_j,t_m)  }
                         {2 + \Delta t d(x_i,z_j,t_m) } \\
        c_{pz2}  =  -\frac{2 \rho v^2 \Delta t}{\Delta z [2 + \Delta t d(x_i,z_j,t_m)]}
      \end{cases}
    \end{aligned}
\end{eqnarray}
$$

## 递推汇总
$$
\begin{eqnarray}
    \begin{aligned}
        \begin{cases}
            q_x(x_{i+1/2},z_{j},t_{m+1} ) & = & c_{qx1} q_x(x_{i+1/2},z_j,t_{m}) \\
            &&+ c_{qx2} [ p(x_{i+1},z_j,t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ] \\

            q_z(x_{i},z_{j+1/2},t_{m+1} )& = & c_{qz1} q_z(x_{i},z_{j+1/2},t_{m}) \\
            &&+c_{qz2} [ p(x_i,z_{j+1},t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ] \\

            p_x(x_i,z_j,t_{m+1/2}) & = & c_{px1} p_x(x_i,z_j,t_{m-1/2})\\
            &&+c_{px2} [ q_x(x_{i+1/2},z_j,t_m) - q_x(x_{i-1/2,z_j,t_m}) ]\\

            p_z(x_i,z_j,t_{m+1/2}) & = & c_{pz1} p_z(x_i,z_j,t_{m-1/2}) \\
            &&+c_{pz2} [ q_z(x_i,z_{j+1/2},t_m) - q_z(x_i,z_{j-1/2},t_m) ]\\
        \end{cases}
    \end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \begin{aligned}
      \begin{cases}
        c_{qx1}  &= &  \frac{ 2- \Delta t d(x_{i+1/2},z_j,t_{m+1/2})  }{2 + \Delta t d(x_{i+1/2},z_j,t_{m+1/2}) } \\
        c_{qx2}  &= &  -\frac{2 \Delta t}{\rho \Delta x [2 + \Delta t d(x_{i+1/2},z_j,t_{m+1/2})]}\\
        c_{qz1}  &= &  \frac{ 2- \Delta t d(x_{i},z_{j+1/2},t_{m+1/2})  }{2 + \Delta t d(x_{i},z_{j+1/2},t_{m+1/2}) } \\
        c_{qz2}  &= &  -\frac{2 \Delta t}{\rho \Delta z [2 + \Delta t d(x_{i},z_{j+1/2},t_{m+1/2})]}\\
        c_{px1}  &= &  \frac{ 2- \Delta t d(x_i,z_j,t_m)  } {2 + \Delta t d(x_i,z_j,t_m) } \\
        c_{px2}  &= &  -\frac{2 \rho v^2 \Delta t}{\Delta x [2 + \Delta t d(x_i,z_j,t_m)]}\\
        c_{pz1}  &= &  \frac{ 2- \Delta t d(x_i,z_j,t_m)  } {2 + \Delta t d(x_i,z_j,t_m) } \\
        c_{pz2}  &= &  -\frac{2 \rho v^2 \Delta t}{\Delta z [2 + \Delta t d(x_i,z_j,t_m)]}\\
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


## Implementation


``` Matlab
%Matlab
    close all;clear;clc;
    %Parameters
    n_pml = 10;
    nx = 320; nz = 320; dx = 5.0; dz = 5.0;
    x  = (-n_pml:nx-1-n_pml) *dx; %(1:11) and (310:320) are PML zone
    z  = (-n_pml:nx-1-n_pml) *dz;
    dt = 1.0e-3; nt = 2000; t  = (0:nt-1)*dt;
    v = zeros(nx,nz) + 800.0; rho = 1000.0;
    R = 0.001; delta = n_pml * dx; d_const = (3.0/2.0/delta)*log(1.0/R) /(delta*    delta);

    %d(x) and d(z)
    d_pxLeft  = ( (-n_pml:0)*dx ).^2 * d_const;
    d_pxRight = ( (0:n_pml)*dx  ).^2 * d_const;
    d_qxLeft  = ( (-n_pml:-1)*dx +dx/2 ).^2 * d_const;
    d_qxRight = ( (1:n_pml)*dx   -dx/2 ).^2 * d_const;
    d_px      = [d_pxLeft zeros(1,nx-2*n_pml-2) d_pxRight];
    d_qx      = [d_qxLeft zeros(1,nx-2*n_pml-1) d_qxRight];
    d_pzLeft  = ( (-n_pml:0)*dz ) .^2 * d_const;
    d_pzRight = ( (0:n_pml)*dz  ) .^2 * d_const;
    d_qzLeft  = ( (-n_pml:-1)*dz +dz/2 ) .^2 *  d_const;
    d_qzRight = ( (1:n_pml)*dz   -dz/2 ) .^2 *  d_const;
    d_pz      = [d_pzLeft zeros(1,nx-2*n_pml-2) d_pzRight];
    d_qz      = [d_qzLeft zeros(1,nx-2*n_pml-1) d_qzRight];
    p   = zeros(nx,nz); p_x = zeros(nx,nz); p_z = zeros(nx,nz);
    q_x = zeros(nx-1,nz); q_z = zeros(nx,nz-1);

    $Source
    src = [ 2.0*mexihat(-5,5,200) zeros(1,nt)];
    ix_src = 161; iz_src = 161;

    %Main loop
    figure
    for it = 1:nt
        %
        %     1   2   3   4   5
        %   --q---q---q---q---q--...
        %   p---p---p---p---p---p...
        %   1   2   3   4   5   6
        %

        p_x(ix_src, iz_src) = p_x(ix_src,iz_src) + src(it)/2.0;
        p_z(ix_src, iz_src) = p_z(ix_src,iz_src) + src(it)/2.0;
        p(  ix_src, iz_src) = p(  ix_src,iz_src) + src(it)/2.0;
        %q_x
        for ix = 1:nx-1
            for iz = 1:nz
                deno  = (2.0 + dt * d_qx(ix)*v(ix,iz));
                c_qx1 = (2.0 - dt * d_qx(ix)*v(ix,iz) ) / deno;
                c_qx2 = -2.0*dt / rho / dx / deno;
                q_x(ix,iz) = c_qx1 * q_x(ix,iz) + c_qx2 *( p(ix+1,iz) - p(ix,iz) );
            end
        end
        %q_z
        for iz = 1:nz-1
            for ix = 1:nx
                deno  = (2.0 + dt * d_qz(iz)*v(ix,iz) );
                c_qz1 = (2.0 - dt * d_qz(iz)*v(ix,iz) )/ deno;
                c_qz2 = -2.0*dt/rho/ dz / deno;
                q_z(ix,iz) = c_qz1 * q_z(ix,iz) + c_qz2 *( p(ix,iz+1) - p(ix,iz) );
            end
        end

        %p_x
        for ix = 2:nx-1
            for iz = 2:nz-1
                deno  =  (2.0 + dt * d_px(ix)*v(ix,iz) );
                c_px1 =  (2.0 - dt * d_px(ix)*v(ix,iz) ) / deno;
                c_px2 = -2.0*rho*v2(ix,iz)*dt/dx / deno;
                deno  =  (2.0 + dt * d_pz(iz)*v(ix,iz) );
                c_pz1 =  (2.0 - dt * d_pz(iz)*v(ix,iz) ) / deno;
                c_pz2 = -2.0*rho*v2(ix,iz)*dt/dz /deno;
                p_x(ix,iz) = c_px1 * p_x(ix,iz) + c_px2 * ( q_x(ix,iz) - q_x(ix-    1,iz) );
                p_z(ix,iz) = c_pz1 * p_z(ix,iz) + c_pz2 * ( q_z(ix,iz) - q_z(ix,iz- 1) );
                p(ix,iz)   = p_x(ix,iz) + p_z(ix,iz);
            end
        end

        pmax = max(max( abs(p) ));
        imagesc(x, z, p/pmax );
        colormap('gray');
        axis square;
        pause(0.001);
    end
```
