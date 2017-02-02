---
title: Linear Deconvolution
date: 2016-06-09 20:27:50
categories: [Digital Signal Processing]
tags: [Digital Signal Processing, Inversion, Regularization, Receiver Function]
---
Deconvolution problem is a subset of inversion, in which observed data is deconvolved to reconstruct the model given the blurring function or source wavelet. Items of inversion including "resolution", "error", "regularization", et. al also apply to deconvolution. Besides, deconvolution always associates transformation between time domain and frequency domain. Thus, principles inherited from digital singal processing apply to deconvolution. In other words, deconvolution is very complex, though massive codes and programs could output a time series in a blink of eye given no matter what kind of data input. Without comprehension of deconvolution and inversion, programs could be misused to provide wrong results. This blog attempts to theories and implementations of deconvolution.

<!-- more -->
<!-- toc -->

## Convolution
Convolution in time domain corresponds to multiplication in frequency domain:

{% math %}
\begin{eqnarray}
r(t) & = & m(t) \otimes s(t) \label{convo_time}\\
R(\omega) & = & M(\omega) S(\omega) \label{convo_freq}
\end{eqnarray}
{% endmath %}

in $\eqref{convo_time}$, $s(t)$ is the source wavelet or blurring function, $r(t)$ is the observed data, and $m(t)$ is the impulse repsonse of the model. Theoretically, given $s(t)$ and $r(t)$, $m(t)$ could be calculated by division according to $\eqref{convo_freq}$

$$
\begin{equation}
m(t) = IFT \left\{\frac{R(\omega)}{S(\omega)}\right\} \label{decon_div}
\end{equation}
$$

However, $\eqref{decon_div}$ always present problematic results because observations $r(t)$ contain noise, and some values of $s(\omega)$ approach zero, which result in instablities in the division.

## Deconvolution in frequency domain
Considering noise $n(t)$, $\eqref{convo_time}$ should be:

$$
\begin{eqnarray}
r(t) & = & m(t) \otimes s(t) + n(t) \label{convo_time_real}\\
R(\omega) & = & M(\omega) S(\omega) + N(\omega) \label{convo_freq_real}
\end{eqnarray}
$$

In deconvolution, we aim to find a time series $s'(t)$, which acts like the inverse of the source wavelet or blurring function $s(t)$. So the convolution of $s'(t)$ and $s(t)$ will produces a desired resolution function $h(t)$, being impulse function theoretically.

$$
\begin{eqnarray}
r(t) \otimes s'(t) & = & m(t) \otimes s(t) \otimes s'(t) + n(t) \otimes s'(t) \label{conv_with_s_inv_time}\\
R(\omega) S'(\omega) & = & M(\omega) S(\omega) S'(\omega) + N(\omega) S'(\omega) \label{conv_with_s_inv_freq}
\end{eqnarray}
$$

Let us define:

$$
\begin{equation}
  \begin{cases}
    \hat{m}(t) & = & r(t) \otimes s'(t) \\
    res(t) & = & s(t) \otimes s'(t) \\
    err(t) & = & n(t) \otimes s'(t)
  \end{cases}
\end{equation}
$$

$\hat{m}(t)$ is the calculated model, $res(t)$ is the resolution function, and $err(t)$ is the model error:

$$
\begin{equation}
  \hat{m}(t) = m(t) \otimes res(t) + err(t)
\end{equation}
$$

In deconvolution, the real resolution function $res(t)$ should approximates desired one $h(t)$, and model error $err(t)$ should approximates zero. Trade-off exists for these two approaches. Thus, an objective function is built:

$$
\begin{equation}
  obj = \int_{-\infty}^{+\infty}\{a|res(t)-h(t)|^2+(1-a)|err(t)|^2\}dt \label{obj_func}
\end{equation}
$$

according to Parseval's theorem, in the frequency domain, $\eqref{obj_func}$ has the form of:

$$
\begin{equation}
  obj =  a|S(\omega)S'(\omega) - h(\omega)|^2 + (1-a) | N(\omega)S'(\omega) |^2 \label{obj_func_freq}
\end{equation}
$$

When objective function approach the minimal value, the derivative of $obj$ to $S'(\omega)$ should be zero. Corresponding $S'(\omega)$ is :

$$
\begin{eqnarray}
  S'(\omega) & = & \frac{S^*(\omega)h(\omega)}{S(\omega)S^*(\omega)+b|N(\omega)|^2} \\
  b & = & \frac{1-a}{a}
\end{eqnarray}
$$

Choose gaussian function as desired resolution function, and estimate the noise $|N(\omega)|^2$ on the basis of observation and signal to noise energy ratio $\nu$.
$$
\begin{equation}
  \hat{m}(t) = IFT\left\{\frac{R(\omega)S^*(\omega)}{S(\omega)S^*(\omega)+c\sigma_0^2}e^{-\frac{\omega^2}{4\alpha^2}} \right\} \label{mod}
\end{equation}
$$

$\sigma_0^2$ is the self-correlation of $S(t)$, and $c = b \nu$.

From the viewpoint to regularization, an item of $c\sigma_0^2$ is added to the denominator. So instablity result from the near-zero value of $S(\omega)S^*(\omega)$ is reduced.

Likewise, we could build the solver equation of:

$$
\begin{equation}
  \hat{m}(t) = IFT\left\{\frac{R(\omega)S^*(\omega)}{ max[S(\omega)S^*(\omega), c\sigma_0^2] }e^{-\frac{\omega^2}{4\alpha^2}} \right\} \label{mod_water_level}
\end{equation}
$$

which is the water-level regularization deconvolution.


## Iterative deconvolution in time domain

For time series, the model $m(t)$ is superposition of impulse functions:

$$
\begin{equation}
  \hat{m}(t) = \sum_{i} m_i h(t-t_i) \label{superposition}
\end{equation}
$$

To determine $m_1$ and $t_1$, the error $\eqref{err_iter}$ should approach its minimal value.

$$
\begin{equation}
  \Delta_1 = \int_{-\infty}^{+\infty}\{r(t) - m_1 h(t-t_1) \otimes s(t)\}^2dt \label{err_iter}
\end{equation}
$$

Corresponding $m_1$ and $\Delta_1$ could be calculated assuming $ \frac{\partial \Delta_1} {\partial m_1} = 0 $:

$$
\begin{eqnarray}
  m_1 & = & \frac { \int_{-\infty}^{+\infty} r(t)s(t-t_1)dt } { \int_{-\infty}^{+\infty} s^2(t)dt} \\
  \Delta_1 & = & \frac { \int_{-\infty}^{+\infty}r^2(t)dt -[\int_{-\infty}^{+\infty}r(t)s(t-t_1)dt ]^2} {\int_{-\infty}^{+\infty}s^2(t)dt}
\end{eqnarray}
$$

Obviously, $[\int_{-\infty}^{+\infty}r(t)s(t-t_1)dt ]^2 $ should approach its maximal value so that the error $\Delta_1 $ approach its minimum. Under this criterion, $t_1$ could be acquired by traversal.
After obtaining $m_1$ and $t_1$, we subtract $m_1h(t-t_1)$ from $r(t)$ and get residual time series:

$$
\begin{equation}
  r'(t) = r(t) - m_1h(t-t_1)
\end{equation}
$$

Likewise, $m_2$ and $t_2$ could be obtain by applying above procedure to $r'(t)$. This kind of procedure is iterated for N times until no more significant decrease in the residual time series occurs. The model could be applying a gausssian function to $\eqref{superposition}$ with $ m_i$ and $t_i(i=1,2,...N)$. Besides, synthetic observation and error are:

$$
\begin{eqnarray}
  \hat{r} & = & \sum_{i=1}^N m_i s(t-t_i) \\
  \Delta_N & = & \int_{-\infty}^{+\infty} [r(t) - \hat{r}(t)]^2 dt
\end{eqnarray}
$$

## Error and resolution estimation
It is important to evaluate the results of deconvolution, thus to choose the optimal regularization factor $c$ in $ \eqref{mod} $, $\eqref{mod_water_level}$, $N$ for iteration deconvolution, and gaussian factor.
First, to determine the error of our result, the calculated model $\hat{m}{t}$ is convolved with $s(t)$, and then compared with observation $r(t)$:

$$
\begin{equation}
  \Delta = \int_{-\infty}^{+\infty} r(t) - \hat(m)(t) \otimes s(t) dt
\end{equation}
$$

Second, for resolution estimation. A simply way to obtain resolution function is to deconvolve $s(t)$ from itself. Since we desire a gaussian shape resolution function in derivations, the calculated one will approximates gaussian function.
Resolution estimation for $eqref{mod}$ and $\eqref{mod_water_level}$:

$$
\begin{eqnarray}
  \widehat{res}(t) & = & IFT\left\{\frac{S(\omega)S^*(\omega)}{S(\omega)S^*(\omega)+c\sigma_0^2}e^{-\frac{\omega^2}{4\alpha^2}} \right\} \label{res} \\

  \widehat{res}(t) & = & IFT\left\{\frac{S(\omega)S^*(\omega)}{ max[S(\omega)S^*(\omega), c\sigma_0^2] }e^{-\frac{\omega^2}{4\alpha^2}} \right\} \label{res_water_level}
\end{eqnarray}
$$


## Implementations
You could design your codes according to deconvolution equtions. [CPS](http://www.eas.slu.edu/eqc/eqccps.html) provide programs of `sacdecon` for deconvolution in frequency domain, and `saciterd` for iteration deconvolution in time domain. Besides, package of [hk](http://www.eas.slu.edu/People/LZhu/downloads/hk1.3.tar) provides `decon` and `iter_decon` as well. These programs differs slighty in the output. To find their usages details, please vist package homepage or [XX]().
You could find examples of deconvolution for receiver functions at [XX]().

##Reference
