---
layout: single
title: La divergencia de $$\sum_{p \in \mathcal{P}}\dfrac{1}{p}$$
excerpt: "Este es uno de los primeros resultados en teoría analítica de números, veremos una prueba sencilla de este y por qué implica que los primos son infinitos. " 
date: 2023-03-13
classes: wide
header:
  teaser: /assets/images/funcion-phi-de-euler/euler.jpg
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Números
tags:  
  - Teoría de Números
  - Teoría Analítica de Números
---

Hoy estudiaremos un resultado clásico de todo libro de introducción a la teoría analítica de números, la divergencia de la serie:

$$
\sum_{p \in \mathcal{P}} \frac{1}{p}
$$

con $$\mathcal{P}$$ denotaremos el conjunto de los números primos, con la prueba de la divergencia de esta serie nos encontramos con una prueba directa de que los números primos son infinitos.

La prueba que veremos hoy es muy similar a la que se encuentra en el libro de Introducción a la teoría de números moderna de Ireland y Rosen, sin embargo tiene un par de modificaciones y aclaraciones que se hacen necesarias para entender cada paso.

## Demostración:
Tenemos que si $$\operatorname{Re}(s)>1$$ :

$$
\sum_{n=1}^{\infty} \frac{1}{n^s}=\prod_{p \in \mathcal{P}} \frac{1}{1-p^{-s}}
$$

(Post del producto de Euler)

Luego aplicamos logaritmo natural a ambos lados de la igualdad:

$$
\begin{aligned}
\log \left(\sum_{n=1}^{\infty} \frac{1}{n^s}\right) & =\log \left(\prod_{p \in \mathcal{P}} \frac{1}{1-p^{-s}}\right) \\
& =\sum_{p \in \mathcal{P}} \log \left(\frac{1}{1-p^{-s}}\right)
\end{aligned}
$$

Ya que $$\log (m \cdot n)=\log (m)+\log (n)$$

y como $$\log \left(\frac{m}{n}\right)=\log (m)-\log (n)$ y $\log (1)=0$$

$$
\sum_{p \in \mathcal{P}} \log \left(\frac{1}{1-p^{-s}}\right)=-\sum_{p \in \mathcal{P}} \log \left(1-p^{-s}\right)
$$

Ahora consideremos:

$$
-\log (1-x)=\sum_{n=1}^{\infty} \frac{x^n}{n}
$$

Su serie de Taylo, así:

$$
\begin{aligned}
\omega & =\log \left(\sum_{n=1}^{\infty} \frac{1}{n^s}\right) \\
& =\sum_{p \in \mathcal{P}}-\log \left(1-p^{-s}\right) \\
& =\sum_{p \in \mathcal{P}}\left(\frac{1}{p^s}+\frac{1}{2 p^{2 s}}+\frac{1}{3 p^{3 s}}+\cdots\right)
\end{aligned}
$$

Por tanto

$$
\omega<\sum_{p \in \mathcal{P}} \frac{1}{p^s}+\sum_{p \in \mathcal{P}} \frac{1}{p^{2 s}}\left(1+\frac{1}{p^s}+\frac{1}{p^{2 s}}+\cdots\right)
$$

Luego:

$$
\omega<\sum_{p \in \mathcal{P}} \frac{1}{p^s}+\sum_{p \in \mathcal{P}}\left(\sum_{k \geq 2}\left(p^{-s}\right)^k\right)
$$

Ahora, los términos de la serie son geométricos pero comienzan desde $$k \geq 2$$, luego aplicamos la fórmula de la convergencia para series geométricas y quitamos los términos $$k=0$$ y $$k=1$$

$$
\omega<\sum_{p \in \mathcal{P}} \frac{1}{p^s}+\sum_{p \in \mathcal{P}} \frac{1}{1-p^{-s}}-\left(1+\frac{1}{p^s}\right)
$$

Ahora operando:

$$
\begin{aligned}
\omega-\sum_{p \in \mathcal{P}} \frac{1}{p^s} & <\sum_{p \in \mathcal{P}} \frac{p^s}{p^s-1}-1-\frac{1}{p^s} \\
& =\sum_{p \in \mathcal{P}} \frac{1}{p^s-1}-\frac{1}{p^s} \\
& =\sum_{p \in \mathcal{P}} \frac{1}{p^s\left(p^s-1\right)}
\end{aligned}
$$

Es decir:

$$
\omega=\log \left(\sum_{n=1}^{\infty} \frac{1}{n^s}\right)<\sum_{p \in \mathcal{P}} \frac{1}{p^s}+\sum_{p \in \mathcal{P}} \frac{1}{p^s\left(p^s-1\right)}
$$

Y como:

$$
\begin{aligned}
\sum_{p \in \mathcal{P}} \frac{1}{p^s\left(p^s-1\right)} & <\sum_{p \in \mathcal{P}} \frac{1}{p^{2 s}} \\
& <\sum_{n=1}^{\infty} \frac{1}{n^{2 s}}
\end{aligned}
$$

Entonces:

$$
\log \left(\sum_{n=1}^{\infty} \frac{1}{n^s}\right)<\sum_{p \in \mathcal{P}} \frac{1}{p^s}+\sum_{n=1}^{\infty} \frac{1}{n^{2 s}}
$$

Ahora note que cuando $$s \longrightarrow 1$$, de un lado tenemos el logaritmo de la serie armónica (divergente) y del otro lado:

$$
\sum_{p \in \mathcal{P}} \frac{1}{p}+\frac{\pi^2}{6}
$$

Y como $$\operatorname{lím}_{x \rightarrow \infty}(\log (x))=\infty$$, entonces $$\sum_{p \in \mathcal{P}} \frac{1}{p}$$ es divergente ya que $$\frac{\pi^2}{6}$$ no afecta en nada.

$$\tag*{$\blacksquare$}$$

Ahora, como $$\sum_{p \in \mathcal{P}}\dfrac{1}{p}$$ diverge, entonces los primos son infinitos
