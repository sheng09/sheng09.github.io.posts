---
title: Wave Modeling in Stratified Media
date: 2016-10-19 15:59:00
categories: [Receiver Function]
tags: [Receiver Function, Modeling, Digital Signal Processing]
---

<!--more-->

<!--toc-->

This post presents wave modeling techniques related to Prof. Kennett's method. Detailed derivation, and analysis are introduced in the book <<Seismic Wave Propagation in Stratified Media>>, and this post just pay attention to some key points.

# Green Function
When talking about modeling, what we really pay attention to is the system response of media, the Green Function. It is independent of the source, and only determined by the media.

In Kennett's method, the main target is to obtain the Green Function of stratified media with a free surface boundary condition. 

Kennett's method is widely used in receiver function research, in which the synthetic Green Function of layers are calculated, and compared with the "observed" Green Functions,the deconvolution of seismic records. Model is calibrated by some inversion techniques until synthetic data "matches" observed data, and finally, the most optimal and reasonable model is obtained, as well as error estimation.

# Media Constraint and Wave decoupling
What we pay attention to is horizontally stratified media composed of isotropic and elastic material. This simplification or assumption is reasonable for it approximates the real Earth's structure.

In isotropic media, the wave could be decoupled into SH wave, and P-SV wave. Moreover, if the media is homogeneous, the P-SV wave could be decoupled. Here comes the key point of wave modeling:

- When it is in layer, everything is uniform, so the wave could be decomposed into three independent types of waves, direction of which are pependicular to the others. So we can construct a coordinates system aligning these three direction, the wave propagation is just the changes of phase for each wave component. In equation derivation, the rotation from ordinary XYZ coordinate to wave vector directions is called diagonalization.
- When it is crossing layers (the interface), isotropic condition is satisfied but homogeneous condtion is not, so the wave could be decomposed into SH wave and P-SV wave. So we make two similar derivations, one is for SH wave, which is easier, relatively, and the other is for P-SV wave.

# Diagonalization
An interesting problem is what would happen if imaginary items appear in the diagonalized propagation matrix. In fact, imaginary items correspond to $e^{\alpha z + i \beta x}$, the evanescent wave.

# Time Domain or Frequency Domain
Frequency domain is choosed for derivation. In frequency domain, time axis is totally rotated by 90 degrees, then we don't need to care which wave happens firstly, and which happens after. In other words, when calculate the wave in one position, we don't need to struggle with all the wave field of the total space happened formly. We just derive the system response of one layer or one interface in frequency domain, and repeate this derivation one layer by one layer, one interface by
interface, from surface to bottom or in reverse.

However, wraparound problems happen for computation in frequency domain. Since the computation is based on discrete space/time, implicit periodic condition exist for discrete fourier transformation(DFT). To avoid this problem, padding zeros is a simple but inconvenient solution. Much better method is employing imaginery frequency, which corresponds to $e^{-\omega_i nT}$ taper to eliminate the fake signal, the effect of DFT. 


