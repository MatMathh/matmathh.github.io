---
layout: single
title: Congruencias
excerpt: "Aquí veremos una introducción a la aritmética modular y su fundamentación con base a las congruencias, definiremos estos conceptos y veremos un par de resultados" 
date: 2022-09-11 
classes: wide
header:
  teaser: /assets/images/congruencias/clock.png
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

## Definición:

Sean $$a$$ y $$b$$ enteros cualesquiera y $$n$$ un entero positivo. Si $$n \mid(a-b)$$ (n divide a $$(a-b)$$ ), decimos que a y $$b$$ son congruentes módulo $$n$$ y lo denotamos por

$$
a \equiv b(\bmod n)
$$

Si a no es congruente con $$b$$ módulo $$n$$, escribimos $$ a \not \equiv b(\bmod n)$$

Denotaremos por $$\operatorname{Res}(a, b)$$ el residuo de dividir a entre b.

Note que dos enteros $$a$$ y $$b$$ son congruentes módulo $$n$$ si y solo si tienen el mismo residuo al ser divididos por $$n$$.

Algo a tener en cuenta es que la congruencia es una relación de equivalencia, es decir, es transitiva, simétrica y reflexiva, ahora veamos unos cuantos teoremas que no son difíciles de verificar usando la definición de congruencia.

## Teorema:

Si $$a \equiv b(\bmod n)$$ y $$c \equiv d(\bmod n)$$ entonces

* Para todo par de enteros $$r$$ y $$s, a r+c s \equiv b r+d s(\bmod$$
n).

* $$a+c \equiv b+d(\bmod n)$$.
  
* $$a-c \equiv b-d(\bmod n)$$.
  
* $$a c \equiv b d(\bmod n)$$.
  
* Para todo entero positivo $$k, a^k \equiv b^k(\bmod n)$$.

* Para todo entero $$r, a+r \equiv b+r(\bmod n)$$.
  
* Para todo entero $$r, a r \equiv b r(\bmod n)$$.
  
Veremos la demostración de una de estas afirmaciones, las demás se hacen de forma similar por lo cual puede ser un buen ejercicio hacerlas.

## Demostración:

Si $$a \equiv b(\bmod n)$$, entonces $$n \mid(a-b)$$, es decir, existe $$k \in \mathbb{Z} a-b=k \cdot n$$, además como $$c \equiv d(\bmod n)$$, existe $$f \in \mathbb{Z}$$ tal que $$c-d=n \cdot f$$

Luego sumando estas igualdades tenemos que

$$
\begin{aligned}
0 & =c-d-n \cdot f+a-b-k \cdot n \\
& =c-d+a-b-n \cdot(k+f)
\end{aligned}
$$

Por tanto $$(c+a)-(b+d)=n \cdot(k+f)$$, luego por la propiedad clausurativa de la suma en los enteros, $$k+f \in$$ $$\mathbb{Z}$$, luego $$a+c \equiv b+d(\bmod n)$$

$$\tag*{$\blacksquare$}$$

De manera similar se hacen las demás pruebas del teorema.

## Mínimo común múltiplo:

Denotaremos $$[a, b]$$ el mínimo común múltiplo de $$a$$ y $$b$$

Recordemos que el mínimo común múltiplo es el menor entero que es divisible entre a y b simultáneamente.

## Teorema:

Sean $$n_1, n_2$$ enteros positivos. Si para $$i=1,2$$ se tiene que $$a \equiv b\left(\bmod n_i\right)$$ entonces

$$
a \equiv b\left(\bmod \left[n_1, n_2\right]\right) \text {. }
$$

En particular, si $$\operatorname{mcd}\left(n_1, n_2\right)=1$$ entonces

$$
a \equiv b\left(\bmod n_1 n_2\right)
$$

## Demostración:

Demostración Supongamos que

$$
a \equiv b\left(\bmod n_1\right) \text { y } a \equiv b\left(\bmod n_2\right)
$$

Entonces $$n_1 \mid(a-b)$$ y $$n_2 \mid(a-b)$$, luego:

$$
\left[n_1, n_2\right] \mid(a-b) .
$$

Por tanto, $$a \equiv b\left(\bmod \left[n_1, n_2\right]\right)$$.

Ahora cuando $$\operatorname{mcd}\left(n_1, n_2\right)=1\left[n_1, n_2\right]=n_1 \cdot n_2$$

Ahora veremos un resultado importante de congruencias con el que finalizaremos el post

## Teorema pequeño de Fermat

Sea $$p$$ un número primo, y $$a>0$$ tal que $$\operatorname{mcd}(a, p)=1$$, entonces

$$
a^{p-1} \equiv 1(\text { mód } p)
$$

Este resultado es equivalente al siguiente:

$$
a^p \equiv a(\operatorname{mód} p)
$$

Pero en este caso no es necesaria la hipótesis de $$\operatorname{mcd}(a,p)=1$$

<a href="https://www.google.com/url?sa=t&source=web&rct=j&url=https://matcris5.files.wordpress.com/2011/08/teoria_de_los_numeros_para_principiantes1.pdf&ved=2ahUKEwiWm87mvY76AhUbomoFHXwZAfUQFnoECBQQAQ&usg=AOvVaw2Ba0ElvKPa_hrPttUvRwAX"> Link-a-la-demostración </a> página 118

## Ejercicio de aplicación:

Si $$p$$ y $$q$$ son primos diferentes, probar que

$$
p^q+q^p \equiv(p+q)(\text { mód } p q)
$$

## Demostración:

Por el teorema pequeño de Fermat se tiene que:

$$
p^q \equiv p(\operatorname{mód} q), \quad q^p \equiv q(\text { mód } p)
$$

$$
\operatorname{Como}(p, q)=1, \text { entonces } p^q+q^p \equiv p+q(\text { mód } p q)
$$

## Otro ejercicio:

Pruebe que $$n^3-n$$ es divisible por 6

## Demostración:

Note que $$n^3-n=n(n-1)(n+1)$$, luego $$n^3-n \equiv 0( \bmod 2)$$ ya que es producto de dos enteros consecutivos y por consecuente par.

Ahora por el teorema pequeño de Fermat $$n^3 \equiv n$$ (mód 3), entonces $$n^3-n \equiv 0$$ (mód 3 ), finalmente concluimos que $$n^3-n \equiv 0$$( mód 6)

## Comentarios:

* La razón por la que se le llama aritmética del reloj es porque sumar módulo 12 o 24 es lo mismo que sumar horas en un reloj y preguntarse qué hora será.

En este punto más allá de ver la hora en un reloj o resolver problemas en teoría de números puede que no veamos aplicaciones de esto, pero en los siguientes post veremos como podemos aplicar esto para construir matemáticas muy potentes que nos ayuden con problemas cotidianos.