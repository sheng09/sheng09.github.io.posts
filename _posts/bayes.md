---
title: What does Bayes' Theorem Tell?
date: 2016-10-15 11:14:01
categories:
tags:
---

# Tony's Problem
Tony is very sad and regretful today since a cancerous cell test presented positive result, which means the lung cancer.
"Don't worry. Be optimistic", doctor White said, "the test just give 95% true result."
"95%, it is approximate 100%", Tony roared, "how could I be optimistic for 100%!"
"I am serious, and *Tomas Bayes'* magic will save you!" doctor White said.

Who is *Tomas Bayes*, is he a MIRACLE? What is his magic?

*Tomas Bayes* is really a miracle, and his magic is called "Bayes' theorem"

# Bayes' Theorem
Yes, it is math formula:

$$
\begin{equation}
    P(A | B) = \frac{P(B | A) P(A)}{P(B)}
\end{equation}
$$

> $A$ and $B$ are events;
> $P(A)$ and $P(B)$ are the probabilities of observing $A$ and $B$ without regard to each other;
> $P(A | B)$, a conditional probability, is the probability of observing event $A$ given that $B$ is true;
> $P(B | A)$ is the probability of observing event $B$ given that $A$ is true.

# Save Tony Now
"The possibility of having the lung cancer is $0.001%$, and the cancerous cell test only present 95% true result", doctor White said, "so according to Baye's Theorem your possibility of having the lung cancer is:"

$$
\begin{eqnarray}
    P(cancer | positive test) & = & \frac{ P(positive test | cancer) P(cancer)} { P(positive test) }  \\
                            &= & \frac{ 95% \times 0.001% } { 95% \times 0.001% + (100%-95%) \times (100%-0.001%) } \\
                            &= & 0.018996 %
\end{eqnarray}
$$

"look, just 0.018996% !", doctor White said.
"WHAT?", Tony, "so this test is nonsense?"
"Don't worry, we offer more accurate tests. Options are: 98% correct test for $100, 99.9% correct test for $600, and 99.9999% correct test for $2000." doctor Whit said.
"Which option should I take?" Tony is confused.
"Let Bayes tell you!" mysterious smile appears in doctor's face.

# Smart Tony

Tony derived:
$$
\begin{equation}
P(cancer | positive test) & = & \frac{ P(positive test | cancer) P(cancer)} { P(positive test) }  \\
                        &= & \frac{ x \times 0.001% } { x \times 0.001% + (100%-x) \times (100%-0.001%) } \\
\end{equation}
$$
where $x$ means the possibility of the test to give correct result.

Tony plot:
![]()
