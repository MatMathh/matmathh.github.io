---
layout: single
title: Algunas ecuaciones diofanticas 2
excerpt: "Esta ecuación diofantica no tiene soluciones no triviales y veremos que probar esto es equivalente a probar que la ecuación $$x^4+y^4=z^4$$ no tiene soluciones no triviales también. Además que $$x^n+y^n=z^n$$ no tiene soluciones no triviales si $$n$$ es una potencia de $$2$$ mayor que $$2$$."
date: 2023-01-04
classes: wide
header:
  teaser: /assets/images/algunas-ecuaciones-diofanticas-2/LInternaute.jpg  
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Números
tags:  
  - Teoría de Números
  - Ecuaciones diofánticas
---

## La ecuación $$x^4+y^4=z^2$$

Esta ecuación diofantica no tiene soluciones no triviales y veremos que probar esto es equivalente a probar que la ecuación $$x^4+y^4=z^4$$ no tiene soluciones no triviales también.
Además que $$x^n+y^n=z^n$$ no tiene soluciones no triviales si $$n$$ es una potencia de $$2$$ mayor que $$2$$.

Veamos entonces este primer resultado.

## Demostración:(esto va a estar feo)

Es suficiente probar que la ecuación no tiene soluciones primitivas, es decir donde $$m.c.d(x,y,z)=1$$.
Supongamos entonces que la tripla $$(x,y,z)$$ es una solución primitiva tal que $$x>0,y>0,z>0$$ y $$z$$ es mínimo. Además, sin perder generalidad, podemos suponer que $$x$$ es impar y $$y$$ es par. Escribiendo $$x^4+y^4=z^2$$ de la forma:

$$
\begin{align*}
(x^2)^2+(y^2)^2=z^2
\end{align*}
$$

Sabemos que:

$$
\begin{align*}
x^2=a^2-b^2, y^2=2ab,z=a^2+b^2
\end{align*}
$$

Donde $$a>b>0$$, $$a$$ y $$b$$ de paridad opuesta y $$m.c.d(a,b)=1$$.

Ya que si $$a$$ fuese par y $$b$$ impar, el número $$x^2=a^2-b^2$$ seria de la forma $$4k-1=4(k-1)+3$$ con $$k>0$$, lo que es imposible ($$x^2$$ es un cuadrado perfecto). Luego $$a$$ es impar y $$b$$ es par.

Aplicando nuevamente el análisis anterior a la ecuación $$x^2+b^2=a^2$$ tenemos que:

$$
\begin{align*}
x=u^2-v^2, b=2uv,a=a^2+v^2
\end{align*}
$$

Donde $$u>v>0$$, $$m.c.d(u,v)=1$$ con $$u,v$$ de distinta paridad y como $$y^2=2ab$$ entonces $$y^2=4uv(u^2+v^2)$$ puesto que $$u,v$$ y $$(u^2+v^2)$$ son primos relativos dos a dos, entonces cada uno dde estos números debe ser un cuadrado perfecto; sea por ejemplo

$$
\begin{align*}
u=r^2, v=s^2, u^2+v^2=t^2
\end{align*}
$$

Donde podemos asumir que $$r,s$$ y $$t$$ son positivos. Además tenemos $$m.c.d(r,s,t)=1,t>1$$ y:

$$
\begin{align*}
r^4+s^4=t^2
\end{align*}
$$

Y como $$z=a^2+b^2=t^4+b^2>t^4$$, entonces $$z>t$$.

De esta forma hemos encontrado una solución primitiva y positiva de $$x^4+y^4=z^2$$, es decir $$(r,s,t)$$ donde $$t<z$$ lo que contradice la minimalidad de $$z$$, con lo cual queda demostrado el teorema.

$$\tag*{$\blacksquare$}$$

Note que esta prueba es por descenso infinito ya que si no suponemos $$z$$ mínimo podemos seguir aplicando este proceso y eso contradice el principio del buen orden.
Y es que al estudiar el trabajo de *Fermat* es muy común encontrarnos con pruebas de este estilo.

## La ecuación $$x^4+y^4=z^4$$

Veamo que esta ecuación diofantica tampoco tiene soluciones triviales.

## Demostración

Es suficiente observar que la ecuación puede escribirse en la forma:

$$
\begin{align*}
x^4+y^4=(z^2)^2
\end{align*}
$$

Y por el teorema anterior sigue que esta ecuación no tiene solución.

$$\tag*{$\blacksquare$}$$

Finalmente veamos que si $$n$$ es una potencia de $$2$$ mayor que $$2$$, entonces la ecuación $$x^n+y^n=z^n$$ no tiene soluciones no triviales.

## Demostración

Si $$n$$ es una potencia mayor que 2 , entonces $$n=2^{\ell}$$, con $$\ell \geq 2$$. Supongamos que la ecuación $$x^n+y^n=z^n$$ tiene solución, entonces $$x^{2^{\ell}}+y^{2^{\ell}}=z^{2^{\ell}}$$ tiene solución, luego

$$
\left(x^{2^{l-2}}\right)^4+\left(y^{2^{l-2}}\right)^4=\left(z^{2^{l-2}}\right)^4
$$

tiene solución entera, lo cual contradice el teorema anterior.

Es sorprendente ver lo lejos que podemos llegar a veces en matemáticas con tan pocas herramientas.


