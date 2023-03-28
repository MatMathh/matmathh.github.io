---
layout: single
title: Teorema chino del residuo
excerpt: "El teorema chino del Residuo y solución de sistemas de congruencias" 
date: 2022-12-31
classes: wide
header:
  teaser: /assets/images/teorema-chino-del-residuo/portada.jpg  
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Números
tags:  
  - Teorema chino del Residuo
  - Congruencias
---

## Teorema (Teorema chino del residuo)

Sean $$m_1,m_2,\cdots,m_r$$ enteros positivos primos relativos dos a dos y sean $$a_1,a_2,\cdots,a_r$$ enteros arbitratios. Entonces el sistema de congruencias lineales:

$$
\left\{\begin{array}{cc}
x \equiv a_1 & \left(\text { mód } m_1\right) \\
x \equiv a_2 & \left(\text { mód } m_2\right) \\
\vdots & \\
x \equiv a_r & \left(\text { mód } m_r\right)
\end{array}\right.
$$

Tiene solución única módulo $$m= \prod_{i=1}^{r} m_i$$.

Anteriormente vimos que hay ecuaciones que se plantean con congruencias, pero también podemos obtener sistemas de ecuaciones con congruencias (sistemas de congruencias, en este caso lineales.)

Y claro, lo que ocurre es que nuestra solución debe satisfacer cada una de las congruencias del sistema, el teorema chino del residuo nos garantiza la existencia y la unicidad de estas soluciones

Pero esta claro que no siempre, el teorema tiene condiciones suficientes para ser cierto (no condiciones necesarias).

Este es uno de esos teoremas cuya demostración nos sacaremos de lo más profundo del anuel, y ya veremos porqué, peeeero también es uno de esos teoremas cuya demostración nos aporta un montón, siendo en este caso la prueba la que nos proporciona la idea para un algoritmo más eficiente que puede resolver este tipo de problemas

## Teorema (Euler)

Si a y $$n$$ son enteros positivos tales que m.c.d. $$(a, n)=1$$, entonces $$a^{\Phi(n)} \equiv 1$$ (mód $$\left.n\right)$$.
donde $$\Phi(n)$$ es la función phi de Euler

## Lema

Si m.c.d. $$(a, n)=1$$, entonces la congruencia lineal $$a x \equiv b(\operatorname{mód} n)$$ tiene solución única módulo $$n$$ y está dada por $$x=a^{\Phi(n)-1} b($$ mód $$n)$$.

A este teorema de Euler le debemos un post completo después ya que implica el teorema pequeño de Fermat y un montón de cosas más, pero por ahora enfoquémonos en el lema.

## Demostración: 

Por el Teorema de Euler, tenemos que $$a^{\Phi(n)} \equiv 1$$ (mód $$\left.n\right)$$, así $$a^{\Phi(n)} b \equiv b \quad$$ (mód $$n$$ ) y luego por transitividad se tiene que $$a x \equiv a^{\Phi(n)} b$$ (mód $$n$$ ). Esto implica que $$x \equiv a^{\Phi(n)-1} b$$ (mód $$n$$ ) puesto que a y $$n$$ son primos relativos.

Y ahora la unicidad

Supongamos que $$a x_0 \equiv b$$ (mód $$\left.n\right)$$ y $$a x_1 \equiv b$$ (mód $$n$$ ), entonces $$a x_0 \equiv a x_1$$ (mód $$n$$ ), luego, $$n \mid a\left(x_0-x_1\right)$$.

Como m.c.d. $$(n, a)=1$$ entonces $$n \mid\left(x_0-x_1\right)$$ (lema de Euclides), es decir $$x_0 \equiv x_1$$ (mód $$\left.n\right)$$.

$$\tag*{$\blacksquare$}$$

Ahora sí podemos demostrar el teorema chino de residuo.

* Sacamos de nuestra bola de cristal por arte de magia la solución y demostramos que sirve

Sea

$$
M_i=\frac{m}{m_i}=\prod_{j \neq i} m_j, \quad i=1, \ldots, r .
$$

Es claro que m.c.d. $$\left(M_i, m_i\right)=1$$ para todo $$i$$ (si m.c.d. $$(a, b)=1=$$ m.c.d. $$(a, c)$$ entonces m.c.d. $$(a, b c)=1) . \mathrm{y}$$ por el lema se tiene que las ecuaciones

$$
M_i x \equiv 1 \quad\left(\text { mód } m_i\right), \quad i=1, \ldots, r
$$

Tienen solución única $$b_1, b_2, \ldots, b_r$$ tales que $$M_i b_i \equiv 1$$ (mód $$m_i$$ ).

Sea $$x_0=\sum_{i=1}^r M_i b_i a_i$$, entonces por la definición de $$M_i$$ se tiene que

$$
x_0 \equiv M_i b_i a_i \equiv a_i \quad\left(\text { mód } m_i\right)
$$

Luego $$x_0$$ es solución del sistema de congruencias lineales.

* Demostramos la unicidad

La unicidad se tiene módulo $$m=\prod_{i=1}^r m_i$$. En efecto, sean $$x_1$$ y $$x_0$$ dos soluciones del sistema de congruencias. Entonces $$x_1 \equiv a_i \equiv x_0\left(\right.$$ mód $$\left.m_i\right)$$ para $$i=1, \ldots, r$$. Así $$x_1 \equiv x_0$$ (mód $$m$$ ) (si $$a \equiv b$$ (mód $$m_1$$ ) y $$a \equiv b$$ (mód $$m_2$$ ) y además m.c.d. $$\left(m_1, m_2\right)=1$$, entonces $$a \equiv b$$ (mód $$\left.m_1 m_2\right)$$.

Note que al ser una prueba constructiva ahora sabemos como solucionar estos problemas, construimos el $$x_0$$ siguiendo los pasos como en la prueba y listo.
