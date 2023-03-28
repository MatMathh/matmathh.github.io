---
layout: single
title: 1) Teoría de conjuntos (ZF)
excerpt: "Este será uno de nuestros primeros acercamientos a la teoría de conjuntos desde la axiomática de Zermelo-Frankel (ZF), en un principio veremos una pequeña motivación del por que esta misma ha sido tan importante y trabajada por grandes maestros de las matemáticas, así en esta serie de post comentaremos y compararemos ZF con otras axiomáticas y veremos el por qué esta parece ser una de las más estandares en el mundo de las matemáticas." 
date: 2023-03-14
classes: wide
header:
  teaser: /assets/images/1-la-teoria-de-conjuntos-zf/vacio.png
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Conjuntos
  - Axiomática
tags:  
  - Teoría de Conjuntos
  - Axiomas
  - Construcción
---

## TEORÍA DE CONJUNTOS (ZF)

<center><img src="/assets/images/1-la-teoria-de-conjuntos-zf/vacio.png" width="30%" heigth="30%"> </center>

A través de la historia de las matemáticas algunas mentes maestras han intentado fundamentar las bases de las mismas intentando reducir estas a problemas aparentemente "sencillos" de comprender. No obstante, a pesar de tener que reducir las matemáticas a sistemas axiomáticos, matemáticos cómo Cantor, Frege, Rusell, Zermelo, Fraenkel y otros muchos más se tomaron la tarea de comprimir el entendimiento de las matemáticas a modelos conjuntistas.

<center>
  <table>
    <tr>
      <td> <img src="/assets/images/1-la-teoria-de-conjuntos-zf/fraenkel.jpg" width="600px" heigth=auto> </td>
      <td> <img src="/assets/images/1-la-teoria-de-conjuntos-zf/skolem.jpg" width="600px" heigth=auto> </td>
      <td> <img src="/assets/images/1-la-teoria-de-conjuntos-zf/zermelo.jpg" width="600px" heigth=auto> </td>
    </tr>
  </table>
</center>

Siendo así, nos daremos la libertad de hablar un poco sobre la axiomatica de *Zermelo-Fraenkel* (*ZF*) (Aunque también parte del trabajo en construir esta axiomática se le debe a *Skolem*) e iremos comentando el por qué está misma se toma como una fundamentación fuerte y lógicamente sencilla de comprender, respecto a algunas otras que intentan lograr el mismo cometido.

## Notación

Estas serán algunas de las notaciones que usaremos durante los post:

  - La relación de pertenencia la notaremos como $$\in$$, esta la usaremos para referirnos a que un elemento $$a$$ hace parte de un conjunto $$A$$, lo escribiremos $$a\in A$$ y lo leeremos como $$a$$ que pertenece al conjunto $$A$$.
  - la relación de igualdad la notaremos como $$=$$, esta la usaremos para referirnos a que 2 conjuntos son el mismo, lo escribiremos como $$A=B$$ y lo leeremos como el conjunto $$A$$ es igual al conjunto $$B$$.
  - La relación de contenencia la notaremos como $$A \subseteq B$$ ($$A\subset B$$) si todos los elementos de $$A$$ son los elementos de $$B$$ con la posibilidad de que $$A=B$$ (Si todos los elementos de $$A$$ están en $$B$$ y $$A\neq B$$), esto lo leeremos como el conjunto $$A$$ está contenido en el conjunto $$B$$ (el conjunto $$A$$ está estrictamente contenido en el conjunto $$B$$).

Para comenzar tenemos que tratar de ser lo más claros e intuitivos posible, es por esto que para definir un conjunto nos es necesario aceptar que existe alguno, ya que tratar de definir conjunto de manera rigurosa solo nos lleva a algunos términos equivalentes, lo que nos vuelve a sentar en el mismo problema.

Así, nuestro primer axioma será adoptar la existencia del conjunto vacío.
  
## Axioma de existencia

Existe un conjunto sin elementos.
<center> $$\{  \}$$ </center>
Note que describir este conjunto es intuitivo y además evidente en muchas de las áreas del conocimiento.

## Ejemplo

  - $$A=\{$$los $$x\in\mathbb{R}$$ tales que $$x^2+1=0 \}$$
  - $$B=\{$$los $$x\in\mathbb{Z}$$ tales que $$x<10$$ y $$x>15$$ en el orden usual$$\}$$
  - $$C=\{$$los $$x$$ tales que $$x\in\mathbb{N}$$ tales que $$2<x<3$$ en el orden usual$$\}$$

Aquí podemos ver que los conjuntos $$A,B$$ y $$C$$ son iguales, aunque descritos de formas distintas, note que para poder realizar semejante afirmación necesitamos definir una forma de reconocer si $$2$$ conjuntos son el mismo.

## Axioma de Extensionalidad}

Todo elemento de $$X$$ es elemento de $$Y$$ y todo elemento de $$Y$$ es elemento de $$X$$ si y sólo si $$X=Y$$

Esto es lo mismo que decir que si $$2$$ conjuntos tienen los mismos elementos, entonces en realidad estamos hablando de un mismo y único conjunto.

## Lema 
Solamente existe un conjunto sin elementos.

## Demostración
*Por contradicción.*

Suponga $$A$$ y $$B$$ conjuntos, ambos sin elementos, luego supongamos que $$A \neq B$$, luego tendríamos que existe $$a\in A$$ tal que $$a \notin B$$ (o $$a\in B$$ tal que $$a\notin A$$), *CONTRADICCIÓN*, ya que $$A$$ (o $$B$$) es un conjunto sin elementos, luego por el axioma de Extensionalidad $$A=B$$.

## Definición
El único conjunto sin elementos es llamado *vacío* y se denota por $$\emptyset$$.

## Axioma del esquema de comprensión

Tome $$P(x)$$ como una propiedad aplicada a $$x$$. Para algún conjunto $$A$$ existe un conjunto $$B$$ tal que $$x\in B$$ si y sólo si $$x\in A$$ y $$P(x)$$ es verdadera.

Note que este axioma implica que $$B\subseteq A$$, ya que todos los elementos de $$B$$ pertenecen a $$A$$, incluso si tuviéramos una proposición como "$$x=x$$", tendríamos que $$B=A$$ (este hecho es muy importante, pues en otras axiomáticas de las cuales hablaremos luego veremos que si no tomamos a $x$ como un elemento de un conjunto ya antes construido nos puede generar problemas). 

Por otro lado, note que el hecho de que la proposición sea aplicada a $$x$$, no nos dice que no podamos usar más variables, conjuntos, etc. Siendo esta una banda libre que nos sirve para crear conjuntos mucho más allá de los que quizás solamente pertenecen a $$A$$, tome por ejemplo $$P(x):=$$ los $$x$$ tales que $$x\in C$$, luego por el axioma del esquema de comprensión tendríamos que $$B$$ es el conjunto de todos los $$x\in A$$ tales que $$P(x)$$ es verdadera, o sea, los $$x\in A$$ tales que $$x\in C$$, luego $$P(x)$$ en realidad podría escribirse como $$P(x,C)$$, así que podemos extender nuestro axioma a $$P(x,a,\cdots,n)$$.

## Lema

Para todo $$A$$, existe solamente un $$B$$ tal que $$x\in B$$ si y sólo si $$x\in A$$ y $$P(x)$$ es verdadera.

## Demostración

Suponga $$B$$ y $$C$$ conjuntos tales que $$x\in B$$ y $$x\in C$$ con $$P(x)$$ verdadera, luego todo $$x\in B$$ cumple $$P(X)$$ y $$x\in A$$, además todo $$x\in C$$ cumple $$P(x)$$ y $$x\in A$$, luego por el axioma de extensionalidad $$B=C$$.

## Definición

$$\{x\in A \mid P(x)\}$$ es el conjunto de todos los $$x\in A$$ tales que $$P(x)$$ es verdadera.

Note que aunque en el ejemplo hemos logrado realizar algunos conjuntos específicos, en la teoría no podemos hacer mucho aún, ya que nuestros axiomas solo nos permiten la existencia de un conjunto vacío que por más de que quisiéramos cambiar por el axioma del esquema de comprensión no lograremos, pues como mencionamos antes, este axioma solo asegura que existe un conjunto $$B\subseteq A$$, sobre un conjunto $$A$$ previamente construido, en nuestro caso si el único conjunto que podemos construir es $$\emptyset$$, solo lograremos obtener que $$B=\emptyset$$. Por consiguiente aún necesitamos robustecer nuestra axiomática antes de comenzar con la teoría de conjuntos, tarea a la que nos dedicaremos en un próximo post.
