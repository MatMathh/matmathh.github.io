---
layout: single
title: Residuos cuadráticos
excerpt: "En álgebra se estudian detalladamente las soluciones de ecuaciones polinómicas, de forma análoga aquí estudiaremos las congruencias polinómicas con coeficientes en los enteros" 
date: 2022-09-18
classes: wide
header:
  teaser: /assets/images/residuos-cuadraticos/legendre.jpg  
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Números
  - Álgebra
tags:  
  - Ecuaciones diofánticas
  - Congruencias
  - Teoría de números
---

En álgebra se estudian detalladamente las soluciones de ecuaciones polinómicas, de forma análoga aquí estudiaremos las congruencias polinómicas con coeficientes en $$\mathbb{Z}$$.

La congruencia $$f(x) \equiv 0$$ (mód $$n$$ ) se llama lineal cuando $$f(x)$$ es un polinomio de grado 1.

Consideraremos solo las soluciones de la ecuación que sean incongruentes, es decir que tengan un residuo distinto módulo $$n$$

Toda congruencia lineal se puede escribir de la forma $$a x \equiv b \pmod n$$

Tenemos el siguiente teorema que no es difícil de verificar

## Teorema:

La congruencia lineal $$a x \equiv b($$ mód $$n)$$ tiene solución si $$y$$ solo si $$d \mid b$$, donde $$d=(a, n)$$

## Congruencias cuadráticas módulo $$p$$:

Una congruencia cuadrática con módulo primo $$p$$ tiene la forma,

$$
a x^2+b x+c \equiv 0(\operatorname{mód} p), \text { con } \operatorname{mcd}(a, p)=1
$$

Note que $$\operatorname{mcd}(4 a, p)=1$$, luego la congruencia anterior es equivalente a:

$$
4 a^2 x^2+4 a b x+4 a c \equiv 0(\operatorname{mód} p)
$$

Y por tanto a la siguiente:

$$
(2 a x+b)^2 \equiv b^2-4 a c(\operatorname{mód} p)
$$

Note que esto no es más que una factorización, ahora sea $$X=2 a x+b$$ y $$d=b^2-4 a c$$, finalmente con este cambio nos queda la congruencia:

$$
X^2 \equiv d(\operatorname{mód} p)
$$

Por tanto solucionar congruencias cuadráticas es equivalente a buscar residuos cuadráticos.

Tenemos que si $$u$$ es una solución de la congruencia anterior, es decir si $$u^2 \equiv d$$ (mód $$p$$ ), entonces el entero $$x_0$$ es solución de la ecuación $$2 a x+b \equiv u(\operatorname{mód} p)$$.

## Definición

Sea $$p$$ un primo impar y a un entero tal que $$(a, p)=1$$, si la congruencia

$$
x^2 \equiv a(\operatorname{mód} p)
$$

tiene solución, decimos que a es un residuo cuadrático módulo $$p$$.

## Teorema de Lagrange

Si $$p$$ es un número primo y $$f(x)=a_0+a_1 x+\cdots+a_n x^n$$ es un polinomio de grado $$n \geq 1$$ con coeficientes enteros y tal que $$a_n \not \equiv 0(\operatorname{mód} p)$$, entonces la congruencia polinómica

$$
f(x) \equiv 0(\operatorname{mód} p)
$$

tiene a lo más $$n$$ soluciones incongruentes módulo p.

Luego la congruencia anterior tiene a lo más dos soluciones incongruentes módulo $$p$$.

Además, si $$x_0$$ es una solución de la congruencia, entonces la otra solución es $$p-x_0$$ ya que

$$
\left(p-x_0\right)^2 \equiv x_0^2(\operatorname{mód} p)
$$

Resolvamos la congruencia cuadrática

$$
5 x^2-6 x+2 \equiv 0(\text { mód } 13)
$$

La congruencia dada es equivalente a la congruencia

$$
100 x^2-120 x+40 \equiv 0(\text { mód } 13) \text {, }
$$

es decir a la congruencia

$$
(10 x-6)^2 \equiv-4(\operatorname{mód} 13)
$$

Si hacemos $$X=10 x-6$$, tenemos la congruencia

$$
X^2 \equiv-4(\operatorname{mód} 13)
$$

Por verificación directa, encontramos que 3 y $$13-3=10$$ son las soluciones de esta congruencia. Ahora, resolvemos las congruencias

$$
10 x-6 \equiv 3(\operatorname{mód} 13) \text { y } \quad 10 x-6 \equiv 10(\operatorname{mód} 13)
$$

Luego las soluciones están determinadas por las soluciones de estas congruencias lineales.

La siguiente gráfica muestra las soluciones de $$x^2 \equiv a$$ (mód 7919)

## Residuos cuadráticos módulo 7919

<center> <img src="/assets/images/residuos-cuadraticos/Residuos.svg" width="65%" heigth="65%"> </center>
<br>

Note que hay simetría con respecto a $$\frac{7919-1}{2}$$, la razón de esta simetría la veremos en otro post.

Finalizaremos introduciendo el símbolo de Legendre.

## Símbolo de Legendre

Si $$p$$ es un primo impar y $$(a, p)=1$$, definimos el símbolo de Legendre $$(a \mid p)$$ como sigue:

$$(a \mid p)= \begin{cases}1, & \text { si a es un residuo cuadrático módulo } p \\ -1, & \text { a no es un residuo cuadrático módulo } p\end{cases}$$

El símbolo de Legendre se representa con frecuencia porla notación $$\left(\frac{a}{p}\right)$$.
