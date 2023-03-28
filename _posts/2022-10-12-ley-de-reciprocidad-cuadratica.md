---
layout: single
title: Ley de reciprocidad cuadrática
excerpt: "'La teoría de números moderna comenzó con el descubrimiento de la ley de reciprocidad cuadrática'- Hecke
  'Ocupado con otro trabajo me encontré con una verdad aritmética extraordinaria. Como la consideré, muy bella en si misma, concentré en ella todos mis esfuerzos para entender los principios de los cuales dependía y para obtener una prueba rigurosa.' - Gauss" 
date: 2022-10-12
classes: wide
header:
  teaser: /assets/images/ley-de-reciprocidad-cuadratica/Gauss.jpg
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Números
tags:  
  - Residuos cuadráticos
  - Ley de reciprocidad cuadrática
  - Gauss
---

Al estudiar los residuos cuadráticos notamos que estos tienen la siguiente simetría.

## Residuos cuadráticos módulo 7919

<center> <img src="/assets/images/residuos-cuadraticos/Residuos.svg" width="65%" heigth="65%"> </center>
<br>

Aquí veremos la razón de la simetría e introduciremos el criterio de **Euler** y la ley de reciprocidad cuadrática.

## Teorema

Se $$p$$ un primo impar, entonces hay exactamente $$\frac{p-1}{2}$$ residuos cuadráticos módulo $$p$$ incongruentes.

## Demostración

Sea $$k$$ uno de los elementos del sistema de residuos. Entonces $$k^2 \equiv (p-k)^2 (mód p)$$. Esto ya que $$(p-k)^2=p^2-2kp+k^2$$. En otras palabras, hay $$\dfrac{p-1}{2}$$ pares con mismo residuo en $$1^2\cdots (p-1)^2$$.

Veamos si entre los primeros $$\dfrac{p-1}{2}$$ hay dos equiresiduales. Para ello supongamos que $$j^2$$ es equiresidual con $$k^2$$, con $$j,k$$ en $$1,2,\cdots, \dfrac{p-1}{2}$$.

En resumen, el número de residuos cuaráticos es a lo más $$\dfrac{p-1}{2}$$.

Por tanto $$k^2-j^2$$ es múltiplo de $$p$$. Y como $$k^2-j^2=(k-j)(k+j)$$, entonces $$p$$ divide a uno de los factores, pero $$k+j$$ es menor que $$p$$, lueg es primo relativo con $$p$$.

Finalmente, $$k-j$$ es múltiplo de $$p$$, así que $$j-k=0$$ ya que $$j-k<p$$. Se concluye que $$j=k$$, es decir, ningún par de cuadrados entre los primeros $$\dfrac{p-1}{2}$$ de $$1^2,2^2,\cdots,(p-1)^2$$ son congruentes entre sí.

Y como entre esos primeros $$\dfrac{p-1}{2}$$ residuos no hay dos equiresiduales, entonces el número de residuos cuadráticos en $$1,2,\cdots,(p-1)$$ es a menos $$\dfrac{p-1}{2}$$. Luego hay exactamente $$\dfrac{p-1}{2}$$ residuos incongruentes.

$$\tag*{$\blacksquare$}$$

El pequeño teorema de **Fermat** nos dice que si $$mcd(a,p)=1$$, entonces $$a^{p-1}-1\equiv 0 (mód p)$$, como:

$$a^{p-2}-1=(a^{\dfrac{p-1}{2}}-1)(a^{\dfrac{p-1}{2}}+1)$$

tenemos que:

$$a^{\dfrac{p-1}{2}}\equiv \pm 1 (mód p)$$

## Criterio de Euler

Si $$p$$ es un primo impar y $$mcd(a,p)=1$$, entonces:

$$a^{\dfrac{p-1}{2}}\equiv (a\mid p) (mód p)$$

## Demostración

Acabamos de ver que todo entero $$a$$ satisface alguna de las congruencias

$$
a^{\frac{p-1}{2}} \equiv 1(\bmod p) \quad \text { o, } \quad a^{\frac{p-1}{2}} \equiv-1(\bmod p) .
$$

Además no puede satisfacer simultáneamente las dos, pues en tal caso se tendría que $$p \mid 2$$, lo cual es imposible ya que $$p$$ es un primo impar.

Si $$(a \mid p)=1$$, entonces existe una $$x_0$$ tal que $$x_0^2 \equiv a(\bmod p)$$ y por lo tanto

$$
a^{\frac{p-1}{2}} \equiv\left(x_0^2\right)^{\frac{p-1}{2}}=x_0^{p-1} \equiv 1(\bmod p),
$$

luego en este caso tenemos que $$a^{\frac{p-1}{2}} \equiv(a \mid p)(\bmod p)$$. El razonamiento anterior también nos muestra que todo residuo cuadrático módulo $p$ es solución de la congruencia

$$
x^{\frac{p-1}{2}} \equiv 1(\bmod p),
$$

y por el Teorema de Lagrange, concluimos que los $$\frac{p-1}{2}$$ residuos cuadráticos son precisamente todas las soluciones de esta congruencia. Por lo tanto, si un número $$a$$ no es residuo cuadrático, es decir si $$(a \mid p)=-1$$, entonces $$a$$ satisface la congruencia

$$
a^{\frac{p-1}{2}} \equiv-1(\bmod p),
$$

y también en este caso tenemos que $$a^{\frac{p-1}{2}} \equiv(a \mid p)(\bmod p)$$

$$\tag*{$\blacksquare$}$$


## Teorema (Algunas propiedades)

Sea $$p$$ un primo impar y sean $$a$$ y $$b$$ enteros primos relativos con $$p$$. Entonces:

- Si $$a \equiv b(mód p)$$ entonces $$(a \mid p) = (b\mid p)$$.
- $$(a^2 \mid p)=1$$.
- $$(1 \mid p)=1$$.
- $$(a \mid p)\equiv a^{\dfrac{p-1}{2}}(mód p)$$.
- $$(a \mid p)(b \mid p)=(ab \mid p)$$.
- $$(-1 \mid p) = (-1)^{\dfrac{p-1}{2}}$$.

## Demostración

1) Tenemos que $$mcd(a,p)=mcd(b,p)=1$$ y $$a \equiv b (mód p)$$, ahora consideremos $$x^2 \equiv a (mód p)$$, por transtividad $$x^2 \equiv a \equiv b (mód p)$$, luegoo es claro que $$(a \mid p)=(b \mid p)$$.

5) Aplicando el teorema de Euler tenemos:

$$\begin{aligned}
  (a\mid p)(b \mid p) &\equiv a^{\dfrac{p-1}{2}}b^{\dfrac{p-1}{2}}\\
  &=(ab)^{\dfrac{p-1}{2}}\\
  &\equiv (ab \mid p) (mód p)
\end{aligned}$$

Y como $$(a \mid p)(b \mid p) = \pm 1, (ab \mid p)= \pm 1$$ y $$p>2$$ se sigue que $$(a \mid p)(b \mid p)=(ab \mid p)$$.

Para los demás resultados la prueba es inmediata.

$$\tag*{$\blacksquare$}$$

De este teorema se sigue que para calcular $$(a \mid p)$$, para cualquier entero $$a$$, basta conocer $$(1 \mid p),(-1 \mid p),(2 \mid p)$$ y $$(q \mid p)$$ para todos los primos $$q$$ impares, positivos y menores que $$p$$.

## La Ley de Reciprocidad Cuadrática

Cada uno de los primeros matemáticos que se ocuparon de este fenómeno formuló el restultado a su manera. Quizá la versión más difundida hoy sea la de **Legendre**. Sin embargo en ciertos contextos otras presentaciones pueden resultar más útiles.

## Legendre

Sea $$p$$ y $$q$$ primos impares. Entonces:

$$(p \mid q)(q \mid p)=(-1)^{\dfrac{p-1}{2}\dfrac{q-1}{2}}$$

## Euler

Si $$p$$ y $$q$$ son primos impares distintos, entonces $$(q \mid p)=1$$ si y sólo si $$p \equiv \pm b^2 (mód 4q)$$ para algún entero impar $$b$$.

## Gauss

Sea $$p$$ y $$q$$ primos impares. Entonces:
- Si $$p$$ es de la forma $$4n+1$$, entonces $$q$$ es un residuo cuadrático módulo $$p$$ si y sólo si $$p$$ es un residuo cuadrático módulo $$q$$.
- Si $$p$$ es de la forma $$4n+3$$, entonces $$q$$ es un residuo cuadrático módulo $$p$$ si y sólo si $$-p$$ es un residuo cuadrático módulo $$q$$.

**Ejemplo:** Determinar si $$60$$ es un residuo cuadrático módulo $$239$$. Como $$60 = 2^2*3*5$$, entonces:

$$\begin{aligned}
  (60 \mid 239) &= (2 \mid 239)^2(3 \mid 239)(5 \mid 239)\\
  &=(3 \mid 239)(5 \mid 239)
\end{aligned}$$

Pero:

$$
\begin{align*}
(3 \mid 239)&=(239 \mid 3)(-1)^{\dfrac{238}{2}\dfrac{2}{2}}=-(239 \mid 3) \\
&= -(2 \mid 3) = -(-1) = 1
\end{align*}
$$

y

$$
\begin{align*}
(5 \mid 239)&=(239 \mid 5)(-1)^{\dfrac{238}{2}\dfrac{4}{2}}=(239 \mid 5) \\
&=(4 \mid 5)=(2 \mid 5)^2 = 1
\end{align*}
$$

Por lo tanto, $$(60 \mid 239)=1$$ y así, $$60$$ es un residuo cuadrático módulo $$239$$.

---

La idea de este post es introducir la ley de reciprocidad cuadrática, luego veremos cómo aplicarla para deducir criterios cuadráticos y en general reducir cuentas en muchos problemas en teoría de números.

Las preguntas más interesantes a las que nos enfrentamos al estudiar la ley de reciprocidad cuadrática parten también de intentar generalizarla, vimos 3 presentaciones de la misma y hay más, la pregunta de cómo lograr atrapar con una sola ley todas las demás es parte del trabajo del programa Langlands, trabajarla y aplicarla sobre extensiones de Galois sobre campos de números algebraicos... hacer que la teoría de números baile con el álgebra moderna, la belleza intensa que podemos encontrar, es simplemente fantástico.

## Links de interés

  - <a href="https://matcris5.files.wordpress.com/2011/08/teoria_de_los_numeros_para_principiantes1.pdf"> Teoría de números para principiantes </a>
  - <a href="https://es.m.wikipedia.org/wiki/Programa_de_Langlands"> https://es.m.wikipedia.org/wiki/Programa_de_Langlands </a>
  - <a href="https://www.famaf.unc.edu.ar/documents/942/CMat31-3.pdf"> https://www.famaf.unc.edu.ar/documents/942/CMat31-3.pdf </a>
