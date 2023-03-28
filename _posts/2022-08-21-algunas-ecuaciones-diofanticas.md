---
layout: single
title: Algunas ecuaciones diofanticas
excerpt: "En álgebra es usual preguntarse por soluciones a ciertos problemas restringiendo el conjunto de salida de las mismas, las ecuaciones diofánticas son un caso más en el que esto ocurre y veremos como estas engloban varios de los problemas más complejos de la teoría de números " 
date: 2022-08-21 
classes: wide
header:
  teaser: /assets/images/algunas-ecuaciones-diofanticas/LInternaute.jpg
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Números
  - Álgebra
tags:  
  - Ecuaciones diofánticas
  - Teoría de Números
---

Una ecuación de la forma $$p\left(x_1, x_2, \ldots, x_n\right)=0$$ donde $$p\left(x_1, x_2, \ldots, x_n\right)$$ es un polinomio con coeficientes enteros y con sus variables restringidas a tomar solo valores enteros se denomina una Ecuación Diofántica en honor al matemático griego Diofanto de Alejandría quien las estudió primera vez en su libro Arithmetica.

Hoy veremos una ecuación diofántica muy famosa propuesta por Fermat y estudiaremos cómo se comporta el caso particular en el que esta tiene solución (el teorema de pitágoras).

## Introducción:

Fermat afirmaba haber demostrado que la ecuación $$x^n+y^n=z^n$$ no tiene solución en $$\mathbb{Z} \backslash 0$$ para todo $$n \geq 3$$, como podemos observar, se trata de una ecuación diofántica, esta demostración no es sencilla y nuestro objetivo va a ser demostrar todos los casos en los que $$n$$ es una potencia de 2 mayor que 2.

Para esto primero debemos entender muy bien exactamente cómo se comportan las soluciones de $$x^2+y^2=$$ $$z^2$$

## Ternas pitagóricas:

Lo primero que tenemos es que si $$(x, y, z)$$ es una solución de $$x^n+y^n=z^n$$, entonces $$(k x, k y, k z)$$ también lo es para todo $$k \in \mathbb{Z}$$, esto se puede comprobar fácilmente haciendo cálculos, por tanto podemos siempre restringirnos a buscar soluciones donde $$(x, y, z)=$$ 1 , es decir donde $$x, y, z$$ son coprimos, estas soluciones se llamas primitivas, más aún, solo es necesario encontrar soluciones primitivas positivas.

## Observaciones: 
Note que si $$(x, y)=d>1$$ y $$p$$ es un primo tal que $$p|d, p| x$$ y $$p \mid y$$, entonces $$p\left|x^2, p\right| y^2$$, luego tenemos que $$p \mid\left(x^2+y^2\right)=z^2$$

Y como $$p$$ es primo entonces $$p \mid z$$ y esto contradice que $$(x, y, z)=1$$, luego $$(x, z)=1$$, análogamente se verifica que $$(y, z)=1$$.

Ahora observe que exactamente uno de los números $$x$$ o $$y$$ debe ser impar ya que si ambos son impares entonces $$x^2+y^2=z^2$$ es de la forma $$4 k+2$$ y ningún cuadrado perfecto es de la forma $$4 k+2$$.

Finalmente en la siguiente presentación veremos cómo se comportan las ternas pitagóricas.

## Teorema:

Los enteros $$x, y, z$$ con $$x$$ impar son una solución primitiva y positiva de la ecuación $$x^2+y^2=z^2$$ si y solamente si existen enteros positivos a y b tales que,

$$
x=a^2-b^2, \quad y=2 a b, \quad z=a^2+b^2
$$

donde $$a>b,(a, b)=1$$ con a y $$b$$ de distinta paridad.

## Demostración:

Note que tomando los anteriores valores para $$x,y,z$$, tenemos que:

$$
x^2+y^2=\left(a^2-b^2\right)^2+(2 a b)^2=a^4+2 a^2 b^2+b^4=z^2
$$

Por tanto este cálculo directo nos permite verificar esta dirección del teorema, veamos la otra que no es tan evidente.

$$\Rightarrow$$ Supongamos que $$(x, y, z)$$ es una solución primitiva y positiva, donde $$x$$ es impar. Como $$(y, z)=1$$ entonces $$(z-y, z+y)=1$$ o 2 , es decir el máximo común divisor es 1 o 2 .

Esto se tiene ya que si $$d=(z-y, z+y)$$, entonces $$d \mid(-z+y+z+y)=2 y$$ y $$d \mid(z-y+z+y)=2 z$$, luego $$d \mid(2 z, 2 y)=2(z, y)=2(1)$$, ya que se tiene que $$(y, z)=1$$

Y puesto que $$y$$ es par y $$z$$ es impar $$(z-y, z+y)=$$ 1 , por lo tanto $$(x, y, z)$$ también es solución de la ecuación

$$
x^2=z^2-y^2=(z-y)(z+y)
$$

Luego $$(z-y)$$ y $$(z+y)$$ deben ser números impares y cuadrados perfectos, ya que son positivos

Supongamos entonces $$(z-y)=r^2 y(z+y)=s^2$$ donde $$r$$ y s son impares y positivos y definamos

$$
a=\frac{s+r}{2}, \quad b=\frac{s-r}{2}
$$

Se puede verificar con cuenticas que $$r=a-b$$ y $$s=a+b$$. Por lo tanto,

$$
z-y=(a-b)^2, \quad z+y=(a+b)^2
$$

Luego:

$$
\begin{aligned}
& z=\frac{\left((a-b)^2+(a+b)^2\right)}{2}=a^2+b^2 \\
& y=\frac{\left((a+b)^2-(a-b)^2\right)}{2}=2 a b \\
& x=(a-b)(a+b)=a^2-b^2
\end{aligned}
$$

Puesto que $$y>0, a$$ y $$b$$ tienen el mismo signo y como $$s=a+b$$ entonces $$a$$ y $$b$$ resultan positivos. Como $$r=a-b>0$$ entonces $$a>b$$ y como $$s=a+b$$ es impar entonces a y $$b$$ tienen distinta paridad

Finalmente $$(a, b)=1$$ pues si $$p$$ es un primo tal que $$p \mid a$$ y $$p \mid b$$ entonces $$p\mid x, p \mid y, p \mid z$$ lo que contradice que $$(x, y, z)=1$$


$$\tag*{$\blacksquare$}$$

Y estas ecuaciones diofanticas tienen muchas conexiones con el álgebra, de hecho la prueba de Andrew Wiles del último teorema de Fermat se basa en curvas elípticas, dejaremos un enlace a la parte 2 de este post aquí para quien le interese ver la continuación.