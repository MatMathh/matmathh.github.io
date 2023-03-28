---
layout: single
title: Algoritmo de Eulcides
excerpt: "¿Como podemos calcular el máximo común divisor de 2 enteros si no conocemos su expresión en factores primos?" 
date: 2023-02-21
classes: wide
header:
  teaser: /assets/images/lema-de-euclides/Euclides.jpg  
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Números
tags:  
  - Teoría de Números
  - Algoritmo de Euclides
---

¿Como podemos calcular el máximo común divisor de 2 enteros si no conocemos su expresión en factores primos?

$$
m.c.d(a, b)=d
$$

Aquí veremos como y por qué funciona el algoritmo de Euclides a la hora de calcular el máximo común divisor de 2 enteros. Además extenderemos este y veremos el algoritmo extendido de Euclides para así mismo ver la relación que tiene con la identidad de Bézout.

## Definición (Algoritmo de la división)

Sean $$a, b, q$$ y $$r \in \mathbb{N}$$ distintos de 0 con $$b \geq r$$. Llamamos cociente a $$q$$ y residuo a $$r$$ si cumplen que:

$$
a=b q+r
$$

Además de esto la pareja $$(q, r)$$ siempre existe y también es única, veremos este resultado en post futuros.

## Definición

Sean $$a, b \in \mathbb{Z}$$ distintos de 0 tales que $$d$$ es el mayor entero divisor de a y $$b$$. Lo notaremos como m.c.d$$(a, b)=d$$ o simplemente como $$(a, b)=d$$ (así como lo hemos hecho en post anteriores).

Recordemos que si $$d \mid a$$, entonces $$d \mid-a$$, por ende podemos afirmar que:

$$
\begin{aligned}
  m.c.d(a, b)&=m.c.d(-a, b)\\
  &=m.c.d(a,-b)\\
  &=m.c.d(-a,-b)\\
  &=d
\end{aligned}
$$

Entonces a pesar de que $$a$$ y $$b$$ son enteros, los tomaremos como enteros positivos y de igual forma tomaremos $$a \geq b$$, sin perdida de generalidad.

## Lema (Algoritmo de Euclides)

Sean $$a, b, q$$ y $$r \in \mathbb{Z}-\{0\}$$ tales que $$a=b q+r$$, entonces m.c.d $$(a, b)=m . c . d(b, r)$$
Tomemos $$a, b>0$$ y $$a \geq b$$, luego por el algoritmo de la división tenemos que:

$$
\begin{aligned}
& a=b q_1+r_2 \\
& b=r_2 q_2+r_3 \cdots \\
& r_{n-2}=r_{n-1} q_{n-1}+r_n \\
& r_{n-1}=r_n q_n+r_{n+1}
\end{aligned}
$$

Debería ser claro que $$r_n=$$ m.c.d$$\left(r_n, r_{n-1}\right)$$, luego $$r_n=m.c.d\left(r_{n-1}, r_{n-2}\right)$$ y así es fácil ver que podemos concluir que m.c.d$$(a, b)=r_n$$.

## Teorema de Bézout

Sean $$a, b \in \mathbb{Z}$$ distintos de 0 , entonces se tiene que existen $$x, y \in \mathbb{Z}$$ tales que:

$$
a x+b y=m.c.d(a, b)
$$

(La demostración de este teorema la dejaremos para futuros post en los que estudiemos el comportamiento de algunos conjuntos y propiedades especiales en los números naturales).

## Ejemplo:

Calculemos el m.c.d$$(8,5)$$ usando el algoritmo de Euclides:

$$
\begin{aligned}
& 8=5 * 1+3 \\
& 5=3 * 1+2 \\
& 3=2 * 1+1 \\
& 2=1 * 2+0
\end{aligned}
$$

Luego m.c.d $$(8,5)=1$$, note que podemos hacer que:

$$
\begin{aligned}
& 1=3-2 * 1=1(3)-1(2) \\
& 1=1(3)-1(5-3 * 1)=-1(5)+2(3) \\
& 1=-1(5)+2(8-5 * 1)=-3(5)+2(8) \\ 
\end{aligned}
$$

luego m.c.d(8,5)=1=-3(5)+2(8)

Con esto logramos ver un ejemplo del como usar el algoritmo de Euclides para hallar el máximo común divisor entre 2 enteros distintos de 0 y como encontrar la combinación lineal que nos asegura el teorema de Bézout, no obstante puede notar que es un proceso bastante extenso y que nos obliga a no solo haber calculado ya el máximo común divisor, s! no tener guardado en la memoria los resultados del paso a paso elaborado en el algoritmo.

Afortunadamente existe un algoritmo que nos permite ir calculando los valores del $x$ y $y$ de la combinación lineal mientras elaboramos el paso a paso del algoritmo, a este proceso le llamaremos El Algoritmo Extendido de Euclides.

## Algoritmo Extendido de Euclides

Considere $$a, b \in \mathbb{Z}$$ tales que $$0<b<a$$, luego definamos $$r_0=a, r_1=b, x_0=1, x_1=0, y_0=0 \mathrm{y}$$ $$y_1=1$$, luego fijemos las siguientes fórmulas de recurrencia:

$$
\begin{aligned}
& x_i=x_{i-2}-x_{i-1} q_{i-1} \\
& y_i=y_{i-2}-y_{i-1} q_{i-1}
\end{aligned}
$$

Analizando esto con cuidado se puede ver que:

$$
a x_i+b y_i=r_i
$$

## Por Inducción Fuerte

Veamos que para $$i=0$$ e $$i=1$$ se cumple, pues:

$$
\begin{aligned}
& a x_0+b y_0=a(1)+b(0)=a=r_0 \\
& a x_1+b y_1=a(0)+b(1)=b=r_1
\end{aligned}
$$

Luego, si asumimos que se cumple para todo $$j=$$ $$0,1, \cdots, n-1$$, veamos que se cumple para $$n$$ :

Del algoritmo de la división tenemos que $$r_n=r_{n-2}-$$ $$r_{n-1} q_{n-1}$$, así tenemos que:

$$
\begin{aligned}
r_n & =r_{n-2}-r_{n-1} q_{n-1} \\
& =a\left(x_{n-2}-x_{n-1} q_{n-1}\right)+b\left(y_{n-2}-y_{n-1} q_{n-1}\right) \\
& =a x_n+b y_n
\end{aligned}
$$

Por lo tanto se tiene para todo $$n \in \mathbb{N}$$

Note que esté algoritmo nos permite olvidarnos de guardar el paso a paso del algoritmo de Euclides, esto, para números muy grandes es buenísimo, pues no llenamos de datos la memoria, si no que nos concentramos en solo guardar lo necesario sin necesidad de regresar por los datos en un futuro. Por otro lado, el algoritmo extendido tiene muchísimas más implicaciones, datos curiosos y usos en la actualidad, de los cuales algunos de ellos serán vistos en futuros post como lo será el de encriptación por RSA.
