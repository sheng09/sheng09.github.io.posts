---
title: 一阶声波方程有线差分模拟在二维下的实现
date: 2016-09-15 01:54:33
categories: [PDE]
tags: [FD, modeling, wave equation]
---
本文介绍了一阶声波方程在二维下的有限差分模拟。
<img src="/fd-2d/wave_field.jpg" width=600px >
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

## 交错网格
构建二维下的交错网格。
<img src="/fd-2d/grid1.jpg" width=400>

对于交错节点，$p$,$q_x$,$q_z$递推关系如下图：
<table>
    <tr>
      <td><img src="/fd-2d/p1.jpg" width=200></td>
      <td><img src="/fd-2d/q_x1.jpg" width=200></td>
      <td><img src="/fd-2d/q_z1.jpg" width=200></td>
    </tr>
</table>

## 二阶精度有现差分实现
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
<img src="/fd-2d/q_x1.jpg" width=200>
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
<img src="/fd-2d/q_z1.jpg" width=200>
$$
\begin{eqnarray}
    D_t q_z(B) & = & - \frac{1}{\rho}  D_z p(B)
\end{eqnarray}
$$
$$
\begin{eqnarray}
    \frac{1}{\Delta t}[q_z(J) - q_z(H)] & = & - \frac{1}{\rho \Delta z} [p(G) - p(E)]
\end{eqnarray}
$$
$$
\begin{eqnarray}
\begin{aligned}
    \frac{1}{\Delta t}[q_z(x_{i},z_{j+1/2},t_{m+1} ) - & q_z(x_{i},z_{j+1/2},t_{m})] \\& =
    - \frac{1}{\rho \Delta z} [ p(x_i,z_{j+1},t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ]
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
\begin{aligned}
    q_z(x_{i},z_{j+1/2},t_{m+1} ) = & q_z(x_{i},z_{j+1/2},t_{m}) \\
    &- \frac{\Delta t}{\rho \Delta z} [ p(x_i,z_{j+1},t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ]
\end{aligned}
\end{eqnarray}
$$

### $p_x$递推
<img src="/fd-2d/p1.jpg" width=400>
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
<img src="/fd-2d/p1.jpg" width=400>
$$
\begin{eqnarray}
    D_t p_z & = & -\rho v^2 D_z q_z
\end{eqnarray}
$$

$$
\begin{eqnarray}
\begin{aligned}
    \frac{1}{\Delta t} [p_z(x_i,z_j,t_{m+1/2}) - & p_z(x_i,z_j,t_{m-1/2})] \\
    & = -\frac{\rho v^2}{\Delta z} [ q_z(x_i,z_{j+1/2},t_m) - q_z(x_i,z_{j-1/2},t_m) ]\\
\end{aligned}
\end{eqnarray}
$$
$$
\begin{eqnarray}
\begin{aligned}
    p_z(x_i,z_j,t_{m+1/2}) = & p_z(x_i,z_j,t_{m-1/2}) \\
    &  -\frac{\rho v^2\Delta t}{\Delta z} [ q_z(x_i,z_{j+1/2},t_m) - q_z(x_i,z_{j-1/2},t_m) ]\\
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
                &- \frac{\Delta t}{\rho \Delta z} [ p(x_i,z_{j+1},t_{m+1/2}) - p(x_{i},z_j,t_{m+1/2}) ]
                \\
            p_x(x_i,z_j,t_{m+1/2}) = & p_x(x_i,z_j,t_{m-1/2})\\
                &-\frac{\rho v^2\Delta t}{\Delta x} [ q_x(x_{i+1/2},z_j,t_m) - q_x(x_{i-1/2,z_j,t_m}) ]
                \\
            p_z(x_i,z_j,t_{m+1/2}) = & p_z(x_i,z_j,t_{m-1/2}) \\
                &-\frac{\rho v^2\Delta t}{\Delta z} [ q_z(x_i,z_{j+1/2},t_m) - q_z(x_i,z_{j-1/2},t_m) ]
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
![](/fd-2d/wave_field.jpg)

``` Matlab
%Matlab
    close all; clear; clc;
    %Parameters
    nx = 300; nz = 300; dx = 5.0; dz = 5.0;
    x  = (0:nx-1) *dx; z  = (0:nz-1) *dz;
    dt = 1.0e-3; nt = 2000; t  = (0:nt-1)*dt;
    v = zeros(300,300)+800.0;v(101:200,:) = 1500.0;v(201:300,:) = 2000.0;
    v2 =  v.^2; rho = 1000.0;

    %Coefficients
    a_qx= dt/dx/rho; a_qz= dt/dz/rho;
    a_px= dt*rho/dx; a_pz= dt*rho/dz;
    %Initial condition
    p   = zeros(nx,nz);
    p_x = zeros(nx,  nz); p_z = zeros(nx,  nz);
    q_x = zeros(nx-1,nz); q_z = zeros(nx,nz-1);

    %Receiver
    rec = zeros(nt,nx); trace=zeros(nt,9);
    trace(:,1) = -4; trace(:,2) = -3; trace(:,3) = -2; trace(:,4) = -1;
    trace(:,5) =  0; trace(:,6) =  1; trace(:,7) =  2; trace(:,8) =  3;
    trace(:,9) =  4; trace_fill = trace;
    %Source
    src = [ 2.0*mexihat(-5,5,200) zeros(1,nt)]; ix_src = 1; iz_src = 150;

    figure
    %Main loop
    for it = 1:nt

        %     1   2   3   4   5
        %   --q---q---q---q---q--...
        %   p---p---p---p---p---p...
        %   1   2   3   4   5   6
        p_x(ix_src, iz_src) = p_x(ix_src,iz_src) + src(it)/2.0;
        p_z(ix_src, iz_src) = p_z(ix_src,iz_src) + src(it)/2.0;
        p(  ix_src, iz_src) = p(  ix_src,iz_src) + src(it)/2.0;
        for ix = 1:nx-1 %q_x
            for iz = 1:nz
                q_x(ix,iz) = q_x(ix,iz) - a_qx *( p(ix+1,iz) - p(ix,iz) );
            end
        end
        for iz = 1:nz-1 %q_z
            for ix = 1:nx
                q_z(ix,iz) = q_z(ix,iz) - a_qz *( p(ix,iz+1) - p(ix,iz) );
            end
        end
        for ix = 2:nx-1 %p_x
            for iz = 2:nz-1
                p_x(ix,iz) = p_x(ix,iz) - a_px *v2(ix,iz)*( q_x(ix,iz) - q_x(ix-    1,iz) );
                p_z(ix,iz) = p_z(ix,iz) - a_pz *v2(ix,iz)*( q_z(ix,iz) - q_z(ix,iz- 1) );
                p(ix,iz)   = p_x(ix,iz) + p_z(ix,iz);
            end
        end
        %Free boundary at z = 0
        p(1,:)    = p(2,:); p_x(1,:)  = p_x(2,:); p_z(1,:)  = p_z(2,:);

        %Plot
        rec(it,:)   = p(1,:);
        p_trace = 20.0* [p(1,30) p(1,60) p(1,90) p(1,120) p(1,149) p(1,180) p(1,210 ) p(1,240) p(1,270)];
        trace(it,:) = trace(it,:) + p_trace;
        trace_fill(it,:) = trace_fill(it,:) + 0.5*(p_trace + abs(p_trace) );
        pmax = max(max( abs(p) ));

        subplot(221),imagesc(x, z, p/pmax );
        colormap('gray');
        axis square;

        w_max = max(max( abs(rec) ));
        subplot(122),imagesc(x,t,rec./w_max);
        colormap('gray');

        subplot(223),fill(t, trace_fill ,'r');
        hold on;
        subplot(223),plot(t,trace,'k');
        hold off;
        pause(0.001);
    end
```
