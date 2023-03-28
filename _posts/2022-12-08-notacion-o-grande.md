---
layout: single
title: Notación O Grande
excerpt: "Encontrar algoritmos eficientes para hacer todo tipo de tareas es algo muy complicado y a esto se dedican muchos matemáticos. Así mismo es importante entender que tanto tiempo u operaciones deben realizar nuestros algoritmos para realizar distintas tareas, por consiguiente la notación O grande es importante de entender, ya que esta nos permitirá acotar el tiempo de ejecución de nuestro algoritmo para algún $$n$$ arbitrario." 
date: 2022-12-08
classes: wide
header:
  teaser: /assets/images/notacion-o-grande/portada.png 
  teaser_home_page: true
  icon: 
categories:
  - Álgebra Computacional
tags:  
  - Algoritmos
  - Notación O grande
---

Hoy veremos una forma de analizar nuestros algoritmos en cualquier lenguaje de programación:

## Notación O Grande:


<center><script type="text/tikz">



\tikzset{every picture/.style={line width=0.75pt}} %set default line width to 0.75pt        

\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
%uncomment if require: \path (0,472); %set diagram left start at 0, and has height of 472

%Shape: Axis 2D [id:dp11483536320529097] 
\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=1.5]  (13.57,234.56) -- (370.05,234.56)(49.22,16.29) -- (49.22,258.81) (363.05,229.56) -- (370.05,234.56) -- (363.05,239.56) (44.22,23.29) -- (49.22,16.29) -- (54.22,23.29)  ;
%Shape: Grid [id:dp5849393120179278] 
\draw  [draw opacity=0][dash pattern={on 1.69pt off 2.76pt}][line width=1.5]  (49.22,32.82) -- (360.52,32.82) -- (360.52,235.15) -- (49.22,235.15) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][dash pattern={on 1.69pt off 2.76pt}][line width=1.5]  (49.22,32.82) -- (49.22,235.15)(86.53,32.82) -- (86.53,235.15)(123.84,32.82) -- (123.84,235.15)(161.14,32.82) -- (161.14,235.15)(198.45,32.82) -- (198.45,235.15)(235.76,32.82) -- (235.76,235.15)(273.07,32.82) -- (273.07,235.15)(310.38,32.82) -- (310.38,235.15)(347.69,32.82) -- (347.69,235.15) ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][dash pattern={on 1.69pt off 2.76pt}][line width=1.5]  (49.22,32.82) -- (360.52,32.82)(49.22,70.13) -- (360.52,70.13)(49.22,107.44) -- (360.52,107.44)(49.22,144.75) -- (360.52,144.75)(49.22,182.06) -- (360.52,182.06)(49.22,219.37) -- (360.52,219.37) ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][dash pattern={on 1.69pt off 2.76pt}][line width=1.5]   ;
%Curve Lines [id:da31886486777884215] 
\draw [color={rgb, 255:red, 255; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]    (49.22,172.48) .. controls (63.42,161.81) and (73.24,89.19) .. (111.17,141.45) .. controls (149.1,193.71) and (150.57,189.06) .. (159.93,187.69) .. controls (169.29,186.33) and (178.6,160.31) .. (199.87,143.26) .. controls (221.13,126.2) and (230.98,82.8) .. (247.7,116.12) .. controls (264.41,149.44) and (285.44,90.03) .. (297.89,96.75) .. controls (310.33,103.47) and (346.23,95.81) .. (350.23,92.81) ;
%Curve Lines [id:da08176059116499501] 
\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=1.5]    (48.63,125.93) .. controls (62.83,115.26) and (72.66,42.64) .. (110.58,94.89) .. controls (148.51,147.15) and (161.93,121.29) .. (173.81,122.84) .. controls (185.68,124.39) and (190.61,200.21) .. (219,172.48) .. controls (247.39,144.76) and (228.56,107.81) .. (249.97,110.41) .. controls (271.38,113.01) and (283.65,144.94) .. (303.43,159.46) .. controls (323.21,173.99) and (353.94,182.07) .. (358.36,178.75) ;

% Text Node
\draw (265.95,235.24) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.3,yscale=1.3] [align=left] {$\displaystyle b$};
% Text Node
\draw (344.75,80.96) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.3,yscale=1.3] [align=left] {$\displaystyle c|g( x) |$};
% Text Node
\draw (357.05,179.14) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.3,yscale=1.3] [align=left] {$\displaystyle f( x)$};


\end{tikzpicture}

</script>
</center>

Comencemos con una definición

## Definición:

Sea $$g(x)$$ una función de variable real definida para todo real no negativo. Denotamos por $$O(g(x))$$, leído como O grande de $$g$$, el conjunto

$$\begin{aligned}
  O(g(x))& =\{f(n): \text{ existen reales} c>0 \text{ y } b \geq 0 \text{ tales que}\\
  & \quad |f(x)| \leq c|g(x)|, \text { para todo } x \geq b\}
\end{aligned}$$

## Pero, ¿y esto de qué nos sirve?

Básicamente podemos analizar nuestros algoritmos y contar las operaciones que hacen en cada una de las iteraciones, de esta forma obtener una función $$g(x)$$ y con $$O(g(x))$$ podemos ver el crecimiento de la misma comparado con otras funciones

## ¿Y esto qué nos dice de nuestro algoritmo?

Nos dice que qué tanto le tomará darnos un resultado dependiendo del tamaño de la tarea que le asignemos

No es lo mismo para un computador multiplicar 2 números de 100 dígitos que dos de 4 millones de dígitos, entonces la velocidad en la que nos entregue el resultado depende enteramente de nuestra capacidad de desarrollar algoritmos eficientes.

En la publicación de "División por tentativa" vimos como al implementar un pequeño teorema en teoría de números ahorramos mucho tiempo en factorizar un número por ejemplo.

## Ejemplo:

Si $$f(n)=n^2+10^{10} n$$, entonces $$f=O\left(n^2\right)$$. En efecto,

$$
\begin{aligned}
& |f(n)|=\left|n^2+10^{10} n\right| \\
& \leq n^2+10^{10} n \quad(n \geq 0) \\
& \leq n^2+10^{10} n^2 \quad(n \geq 1) \\
& =\left(10^{10}+1\right) n^2=c\left|n^2\right| \text {, } \\
\end{aligned}
$$

con $$c=10^{10}+1$$

Require: $$n \in \mathbb{Z}$$

$$\text{1: procedure ALGEJER2}$$

$$\begin{array}{lc}2: & \text { for } i:=1 \text { to } n \text { do } \\
 3: & \text { for } j:=1 \text { to } i \text { do } \\ 
 4: & \text { for } k:=1 \text { to } j \text { do } \\ 
 5: & x:=i \cdot j \cdot k \\ 
 6: & \text { end for } \\ 
 7: & \text { end for } \\ 
 8: & \text { end for } \\ 
 9: & \text { end procedure }
 \end{array}$$

Este algoritmo por ejemplo hace dos multiplicaciones para calcular el producto de 3 enteros y tiene 3 for anidados.

Notemos que el primer for va acumulando las operaciones que se hacen en los 2 de adentro, el último for ejecuta las 2 operaciones, luego para el segundo sumamos estas operaciones que se van acumulando y obtenemos:

$$
\sum_{m=1}^i 2 m=i(i+1)
$$

Como dijimos el primer for suma estas operaciones luego el total de operaciones que hace el algoritmo es:

$$
\sum_{i=1}^n i(i+1)=\frac{n(n+1)(n+2)}{2}
$$

al multiplicar los términos nos damos cuenta que el algoritmo es $$O\left(n^3\right)$$ (o de orden cúbico)

Note que esto es un abuso de notación tremendo, pero lo importante es que sirve $x d$, ahora veamos el tiempo computacional.

Asumiendo que una operación toma un nanosegundo ( $$10^{-9}$$ segundo), comparamos el tiempo computacional para diferentes ordenes de una función $$f(n)$$ a continuación.

$$
\tiny{\begin{array}{|c||c|c|c|c|}
\hline f(n) & n=10 & n=10^3 & n=10^5 & n=10^7 \\
\hline \log _2(n) & 3,3 * 10^{-9} \mathrm{~s} & 10^{-8} \mathrm{~s} & 1,7 * 10^{-8} \mathrm{~s} & 2,3 * 10^{-8} \mathrm{~s} \\
n & 10^{-8} \mathrm{~s} & 10^{-6} \mathrm{~s} & 0,0001 \mathrm{~s} & 0,01 \mathrm{~s} \\
n \log _2(n) & 3,3 * 10^{-8} \mathrm{~s} & 0,000010 \mathrm{~s} & 0,0017 \mathrm{~s} & 0,23 \mathrm{~s} \\
n^2 & 10^{-7} \mathrm{~s} & 0,0010 \mathrm{~s} & 10 \mathrm{~s} & 27 \text { horas } \\
n^3 & 10^{-6} \mathrm{~s} & 1 \mathrm{~s} & 11,5 \text { días } & 31709 \text { años } \\
2^n & 10^{-6} \mathrm{~s} & - & - & - \\
\hline
\end{array}}
$$

Luego el orden logaritmico sería lo más ideal si queremos que nuestros programas compilen rápido y el exponencial el peor, para tareas pesadas nos podemos morir sin conocer el resultado.