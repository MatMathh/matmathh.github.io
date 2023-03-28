---
layout: single
title: El producto de Euler.
excerpt: "Al estudiar la función zeta de Riemann es natural preguntarnos su relación con los números primos y esta es quizás unas de las primeras que podemos encontrar, el producto de Euler además es uno de los primeros teoremas que relacionan el análisis con la teoría de números."
date: 2022-04-11 
classes: wide
header:
  teaser: /assets/images/el-producto-de-euler/riemannzeta.png
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Números
  - Análisis
  - Teoría analítica de números
tags:  
  - Euler
  - Zeta de Riemman
  - Números Primos
---

<center><img src="/assets/images/el-producto-de-euler/riemann_anim.png" width="80%" heigth="80%"></center>

Este es quizás uno de los resultados más impresionantes de **Euler**, este teorema relaciona la teoría de números, que estudia los números enteros, con el análisis matemático, en su momento, mostró la relación entre estas dos ramas de la matemática y dio paso a que posteriormente matemáticos como **Dirichlet** abrieran puertas y dieran inicio a la teoría analítica de números.

$$
\begin{align*}
\zeta(s)&=\prod_{p} \dfrac{1}{1-p^{-s}} &&\text{ para todo $s$ tal que $Re(s)>1$}
\end{align*}
$$

Para entender este resultado primero debemos conocer la función $$\zeta$$.

$$
\begin{align*}
\zeta(s)&=1+\dfrac{1}{2^s}+\dfrac{1}{3^s}+\dfrac{1}{4^s}+\dfrac{1}{5^s}+\dfrac{1}{6^s}+\cdots
\end{align*}
$$

Donde $s$ es un número complejo.

**Euler** se dio cuenta que si multiplicaba a ambos lados de la igualdad por $$\dfrac{1}{2^s}$$ la función $$\zeta$$ tomaba la siguiente forma:

$$\dfrac{1}{2^s}\zeta(s)=\dfrac{1}{2^s}+\dfrac{1}{4^s}+\dfrac{1}{6^s}+\dfrac{1}{8^s}+\dfrac{1}{10^s}+\cdots$$

Y restando esta segunda serie a la primera, es decir a $$\zeta(s)$$, podemos quitar todos los términos que son múltiplos de $$2$$, luego factorizando $$\zeta(s)$$ obtenemos lo siguiente:

$$(1-\dfrac{1}{2^s}) \zeta(s)=1+\dfrac{1}{3^s}+\dfrac{1}{5^s}+\dfrac{1}{7^s}+\dfrac{1}{9^s}+\dfrac{1}{11^s}+\cdots$$

Al hacer esto **Euler** se da cuenta que si hace este proceso para $$3,5,7,11,\cdots$$ y en general para todos los números primos, puede eliminar todos sus múltiplos y obtiene la siguiente expresión:

$$\cdots(1-\dfrac{1}{7^s})(1-\dfrac{1}{5^s})(1-\dfrac{1}{3^s})(1-\dfrac{1}{2^s})\zeta(s)=1$$

Por lo tanto:

$$\zeta(s)=\dfrac{1}{(1-\dfrac{1}{7^s})(1-\dfrac{1}{5^s})(1-\dfrac{1}{3^s})(1-\dfrac{1}{2^s})\cdots}$$

Luego podemos simplificar esta expresión con un producto obteniendo lo siguiente:

$$
\begin{align*}
\zeta(s)&=\prod_{p}\dfrac{1}{1-p^{-s}} && \text{Donde $p$ es un número primo.}
\end{align*}
$$

Pero para que este resultado valga, es necesario que la parte real de $$s$$ sea mayor que $$1$$, esto se escribe como $$Re(s)>1$$.

Y esta fue la prueba que dio **Euler**, que durante su vida se encontró muchas veces con resultados de este estilo, a veces resolviendo problemas terminaba abriendo paso a nuevas ramas de las matemáticas sin siquiera darse cuenta, como por ejemplo la topología y la teoría de grafos en el problema de los puentes de **Königsberg**.

Sin lugar a dudas fue un matemático increible.
