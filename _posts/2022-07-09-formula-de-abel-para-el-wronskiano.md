---
layout: single
title: Formula de Abel para el Wronskiano
excerpt: "Abel fue un matemático Noruego que ha inspirado a muchos matemáticos, sus aportes se centran principalmente en el álgebra, sin embargo hoy veremos uno de sus aportes a la rama del análisis.  " 
date: 2022-07-09 
classes: wide
header:
  teaser: /assets/images/formula-de-abel-para-el-wronskiano/niels.jpg
  teaser_home_page: true
  icon: 
categories:
  - Análisis
  - Ecuaciones Diferenciales
tags:  
  - Ecuaciones Diferenciales
---

Niels Hendrik Abel nació en noruega en 1802 y murió en 1829 a la edad de 26 años, a pesar de su corta vida se convirtió en un matemático muy conocido, en especial por haber demostrado en 1824 que la ecuación general de quinto grado no es resoluble por radicales, Abel sin duda fue un matemático increíble e hizo mucho en una vida muy corta, por eso hoy veremos un resultado que lleva su nombre.

## Wronskiano:

Dado un conjunto de funciones $$f_1, f_2, \cdots, f_n$$ que son $$n-1$$ derivables y definidas en un intervalo I, entonces definimos el Wronskiano como:

$$
W\left(f_1, \ldots, f_n\right)(x)=\left|\begin{array}{cccc}
f_1(x) & f_2(x) & \ldots & f_n(x) \\
f_1^{\prime}(x) & f_2^{\prime}(x) & \ldots & f_n^{\prime}(x) \\
\vdots & \vdots & \ddots & \vdots \\
f_1^{(n-1)}(x) & f_2^{(n-1)}(x) & \ldots & f_n^{(n-1)}(x)
\end{array}\right|, \quad x \in I
$$

Veremos a continuación un teorema que muestra la utilidad de Wronskiano a la hora de resolver una ecuación diferencial

## Teorema:

Sean $$f_1(t), \ldots, f_n(t)$$ funciones definidas y derivables hasta $$n-1$$ veces en un intervalo $$I$$. Si existe un $$t_0 \in I$$ tal que

$$
W\left[f_1(t), \ldots, f_n(t)\right]\left(t_0\right) \neq 0
$$

entonces $$f_1(t), \ldots, f_n(t)$$ son linealmente independientes en I.

Luego el Wronskiano es muy útil para determinar la independencia lineal de funciones, por tanto, nos ayuda a expresar la solución de una ecuación diferencial como combinación lineal de las funciones linealmente independientes que podemos encontrar con los diversos métodos conocidos.

De hecho el Wronskiano es usado en varios de estos métodos, por ejemplo en el método de variación de parámetros.

La fórmula de Abel para el Wronskiano, también conocida como identidad de Abel-Liouville facilita el cálculo del mismo ya que calcular un determinante no siempre es un proceso corto y fácil, para conocer su construcción es necesario observar primero lo siguiente:

## Observación:

Sea:

$$
D(t):=\left|\begin{array}{ll}
a(t) & b(t) \\
c(t) & d(t)
\end{array}\right| \text {, para } t \in I
$$

Entonces,

$$
\begin{aligned}
D^{\prime}(t) & =(a(t) d(t)-c(t) b(t))^{\prime} \\
& =(a(t) d(t))^{\prime}-(c(t) b(t))^{\prime} \\
& =\left(a^{\prime}(t) d(t)+a(t) d^{\prime}(t)\right)-\left(c^{\prime}(t) b(t)+c(t) b^{\prime}(t)\right) \\
& =a^{\prime}(t) d(t)-c(t) b^{\prime}(t)+a(t) d^{\prime}(t)-c^{\prime}(t) b(t) \\
& =\left|\begin{array}{cc}
a^{\prime}(t) & b^{\prime}(t) \\
c(t) & d(t)
\end{array}\right|+\left|\begin{array}{cc}
a(t) & b(t) \\
c^{\prime}(t) & d^{\prime}(t)
\end{array}\right|
\end{aligned}
$$


## Teorema de Abel para el Wronskiano:

Sea

$$
x^{\prime \prime}+a_1(t) x^{\prime}+a_2(t) x=0
$$

una ecuación diferencial lineal homogénea de segundo orden, donde $$a_1(t)$$ y $$a_2(t)$$ son funciones reales continuas en un intervalo $$I$$. Sean $$x_1(t), x_2(t)$$ dos soluciones de la ecuación diferencial y sea

$$
W(t)=W\left[x_1(t), x_2(t)\right]
$$

su Wronskiano. Entonces,

$$
\text { Para todo } t \in I, \quad W(t)=C e^{-\displaystyle \int a_1(t)  dt}
$$


## Demostración:

Como

$$
W(t)=\left|\begin{array}{cc}
x_1(t) & x_2(t) \\
x_1^{\prime}(t) & x_2^{\prime}(t)
\end{array}\right|,
$$

derivando obtenemos:

$$
\begin{aligned}
W^{\prime}(t) & =\left|\begin{array}{cc}
x_1^{\prime}(t) & x_2^{\prime}(t) \\
x_1^{\prime}(t) & x_2^{\prime}(t)
\end{array}\right|+\left|\begin{array}{cc}
x_1(t) & x_2(t) \\
x_1^{\prime \prime}(t) & x_2^{\prime \prime}(t)
\end{array}\right|\\
&=\left|\begin{array}{cc}
x_1(t) & x_2(t) \\
x_1^{\prime \prime}(t) & x_2^{\prime \prime}(t)
\end{array}\right| \\
& =x_1(t) x_2^{\prime \prime}(t)-x_1^{\prime \prime}(t) x_2(t)
\end{aligned}
$$

Y como $$x_1(t)$$ y $$x_2(t)$$ son soluciones de la ecuación diferencial, tenemos que:

$$
\begin{aligned}
& x_1^{\prime \prime}(t)=-a_1(t) x_1^{\prime}(t)-a_2(t) x_1(t) \\
& x_2^{\prime \prime}(t)=-a_1(t) x_2^{\prime}(t)-a_2(t) x_2(t)
\end{aligned}
$$

Por tanto reemplazando $$x_1^{\prime \prime}(t)$$ y $$x_2^{\prime \prime}(t)$$ :

$$
\begin{aligned}
W^{\prime}(t)= & x_1(t)\left[-a_1(t) x_2^{\prime}(t)-a_2(t) x_2(t)\right] \\
& -\left[-a_1(t) x_1^{\prime}(t)-a_2(t) x_1(t)\right] x_2(t) \\
= & -a_1(t) x_1(t) x_2^{\prime}(t)-a_2(t) x_1(t) x_2(t) \\
& +a_1(t) x_1^{\prime}(t) x_2(t)+a_2(t) x_1(t) x_2(t) \\
= & -a_1(t)\left[\begin{array}{ll}
\left.x_1(t) x_2(t)-x_1^{\prime}(t) x_2(t)\right]
\end{array}\right. \\
= & -a_1(t)\left|\begin{array}{ll}
x_1(t) & x_2(t) \\
x_1^{\prime}(t) & x_2^{\prime}(t)
\end{array}\right| \\
= & -a_1(t) W(t) .
\end{aligned}
$$

Luego para todo $$t \in 1, W^{\prime}(t)=-a_1(t) W(t)$$.

Luego como $$W^{\prime}(t)=-a_1(t) W(t)$$ es una ecuación diferencial lineal homogenea de primer orden, concluimos que:

$$
W(t)=C e^{-\displaystyle\int a_1(t) d t}
$$

Esto ya que la solución para la ecuación diferencial lineal $$\dfrac{d y}{d x}+y P(x)=Q(x)$$ es justamente:

$$\begin{aligned}
e^{-\displaystyle\int P(x) d x}\left(\displaystyle\int Q(x) \cdot e^{\displaystyle\int P(x) dx} dx+C\right)\end{aligned}
$$


$$\tag*{$\blacksquare$}$$


Este teorema es muy bonito y además se puede generalizar a ecuaciones de orden superior, cosa que no hacemos aquí porque se haría demasiado largo.

Los invito a ver la prueba de la solución general de la ecuación diferencial lineal que se usó para esta demostración, lo bello de estas pruebas es que son muy constructivas lo que nos permite en cada paso sentir como nos acercamos de forma directa a lo que queremos.