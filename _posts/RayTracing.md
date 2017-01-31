---
title: Ray Tracing (1) Derivation
date: 2015-10-26 16:46:59
categories: [Seismic Tomography]
tags:
---

Give acoustic wave equation $\eqref{acoustic_wave}$, consider the harmonic solution $\eqref{harmonic_sol}$, where $c(x_i)$ is the velocity, $T(x_i)$ the travel time. 

$$
\begin{eqnarray}
    \nabla^2\phi & = & \frac{1}{c^2(x_i)}\phi \label{acoustic_wave}
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \phi(x_i) & = & \Phi(x_i)exp[-i\omega(t-T(x_i))] \label{harmonic_sol}
\end{eqnarray}
$$

Applying the high frequency approximation, eikonal equation$\eqref{eikonal_eq}$ and transport equation $\eqref{transport_eq}$ are derived. $\textbf{p}$, the slowness vector, which is perpendicular to the wavefront, the contour of travel time $T$, declares the propagation direction of waves.
$$
\begin{cases}
\begin{eqnarray}
    & & p_ip_i  =  \frac{1}{c^2(x_i)} \label{eikonal_eq} \\
    & & p_i = (\nabla T)_i \\
    & & 2 \nabla \Phi \cdot \nabla T+ \Phi \nabla^2T = 0 \label{transport_eq}
\end{eqnarray}
\end{cases}
$$

Build Hamilton equation for eikonal equation, where $s$ declares the ray path.

$$
\begin{cases}
\begin{eqnarray}
    H(x_i, p_i) & = & (p_ip_i)^{1/2} - c^{-1}(x_i) \label{hamilton_eq} \\
    \frac{dx_i}{ds} & = & \frac{\partial H}{\partial p_i} \\
    \frac{dp_i}{ds} & = & \frac{\partial H}{\partial x_i} \\
    \frac{dT}{d} & = & p_i \frac{\partial H}{\partial p_i}
\end{eqnarray}
\end{cases}
$$

Derivation ends here. In the right side of $\eqref{rt1}$, $\frac{dc}{dx_i}$ is the velocity gradient, $\frac{dc}{ds}\frac{dx_i}{ds}$ the projection of velocity gradient along ray path. In the left side, $\frac{d^2x_i}{ds^2}$ declares the curvature direction of ray path. Thus, the direction change of ray path can be calculated given the velocity gradient and ray path direction. Or, given a initial ray path direction, we could derive each segments of ray path. 


$$
\begin{eqnarray}
    \frac{d^2x_i}{ds^2} = \frac{1}{c} ( -\frac{dc}{dx_i} + \frac{dc}{ds}\frac{dx_i}{ds} ) \label{rt1}\\
%    T = \int_s \frac{1}{c}ds \label{rt2}
\end{eqnarray}
$$

However, the **boundary condition problem**, the two-point ray tracing problem, but not **initial condition problem** is much more prevalent. It could be solved using iteration, and the ray path is calibrated in each step according to $\eqref{rt1}$. This is **bending method**.


**Reference**
Cerveny, V.,M.G. Brown, Seismic Ray Theory. Applied Mechanics Reviews, 2002. 55(6): p.14.






