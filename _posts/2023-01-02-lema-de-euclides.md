---
layout: single
title: Lema de Euclides
excerpt: "Cuando queremos resolver problemas de teoría elemental de números nos encontramos demasiadas veces con la necesidad de usar este teorema, aquí veremos una prueba, que no es la que originalmente dio Euclides, pero que es más sencilla." 
date: 2023-01-02
classes: wide
header:
  teaser: /assets/images/lema-de-euclides/Euclides.jpg  
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Números
tags:  
  - Teorema chino del Residuo
  - Lema de Euclides
---

## Lema de Euclides

Si $$a \mid b c$$ y m.c.d. $$(a, b)=1$$, entonces $$a \mid c$$

## Identidad de Bezout

Sean a y $$b \in \mathbb{Z}$$, si $$d=$$ m.c. $$d(a, b)$$ entonces exiten $$x$$ y $$y \in \mathbb{Z}$$ tales que $$d=a x+b y$$

## Demostración:

Supongamos que $$d=(a, b)$$ y sea

$$
S=\left\{z \in \mathbb{Z}^{+} \mid z=a x+b y \text { con } x, y \in \mathbb{Z}\right\} .
$$

$$ S \neq \varnothing$$ puesto que $$z=a^2+b^2 \in S$$. Luego por el Principio del Buen Orden, $$S$$ posee un mínimo, llamémoslo $$g$$ que podemos escribir en la forma $$g=a x_0+b y_0$$. Probaremos que $$g=d=(a, b)$$. En efecto $$g$$ es divisor común de $$a$$ y $$b$$, pues si dividimos $$a$$ entre $$g$$ tenemos:

$$
a=q g+r \text { con } 0 \leq r<g
$$

luego,

$$
\begin{aligned}
r & =a-q g \\
& =a-q\left(a x_0+b y_0\right) \\
& =a\left(1-q x_0\right)+b\left(-q y_0\right) \\
& =a x^{\prime}+b y^{\prime} .
\end{aligned}
$$

Ahora, si $$r \neq 0$$ entonces $$r \in S$$ lo cual contradice la minimalidad de $$g$$, en consecuencia $$r=0$$ y así $$g \mid a$$. Análogamente se verifica que $$g \mid b$$.

Como $$d=(a, b)$$ y $$g$$ es un divisor común entonces $$g \leq d$$.

De otra parte $$g=a x_0+b y_0$$ y $$d \mid a$$ y $$d \mid b$$ luego $$d \mid g$$ y como ambos números son positivos $$d \leq g$$ y en consecuencia $$d=g$$.

$$\tag*{$\blacksquare$}$$

## Demostración (Lema de Euclides):

Tenemos que m.c.d. $$(a, b)=1$$, por la identidad de Bezout existen $$x$$ y $$y \in \mathbb{Z}$$ tal que $$1=a x+b y$$, luego $$c=c \cdot a x+$$ c. by, luego a $$\mid c \cdot a x$$ y como a $$\mid$$ bc entonces a $$\mid c \cdot b y)$$ por tanto a $$\mid c$$

$$\tag*{$\blacksquare$}$$

Veamos ahora un ejemplo de ejercicio clásico cuya prueba depende fuertemente del Lema de Euclides.

## Ejercicio:

Demuestre que si $$\frac{a}{b}+\frac{c}{d}=n$$ con $$n \in \mathbb{Z}$$ y m.c.d. $$(a, b)=$$ m.c.d. $$(c, d)=1$$, entonces $$ \mid b \mid = \mid d \mid $$

Es decir que si la suma de dos fracciones irreducibles es un número entero entonces el valor absoluto de sus denominadores es igual.

Los invito a pensar en la solución antes de leerla :v

## Solución:

Para la solución necesitaremos este teorema:

## Teorema:

Sean a y $$b \in \mathbb{Z}$$, si $$a \mid b$$ y $$b \mid a$$, entonces $$ \mid a \mid = \mid b \mid $$

Esto se puede probar fácilmente de la definición de divisibilidad y usando que si $$a \mid b$$ y $$b \neq 0$$ entonces $$ \mid a \mid  \leq \mid b \mid $$ .

$$2 \mid 4 $$ y $$4 \neq 0$$ entonces $$  \mid 2 \mid \leq  \mid 4 \mid $$

## Demostración:

Tenemos que $$\dfrac{a d+b c}{b d}=n$$, con $$n \in \mathbb{Z}$$, entonces b y d dividen a $$a d+b c$$, luego $$b \mid$$ ad y $$d \mid b c$$ y como m.c.d. $$(a, b)=m . c . d .(c, d)=1$$, por el lema de Euclides sigue que $$b \mid d$$ y $$d \mid b$$, así $$ \mid b \mid = \mid d \mid $$.

$$\tag*{$\blacksquare$}$$
