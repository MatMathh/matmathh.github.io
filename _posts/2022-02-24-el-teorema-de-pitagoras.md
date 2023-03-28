---
layout: single
title: El teorema de pitágoras.
excerpt: "El teorema de pitágoras es uno de los más conocidos de toda la matemática, además tiene una gran cantidad de pruebas, hoy veremos dos de ellas, una de ellas propuesta por un presidente de los EE.UU."
date: 2022-02-24 
classes: wide
header:
  teaser: /assets/images/el-teorema-de-pitagoras/portada.jpg
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Números
  - Geometría
tags:  
  - Pitágoras
---

<center> <img src="/assets/images/el-teorema-de-pitagoras/portada.jpg" width="30%" heigth="30%"> </center>

La mayor parte de las demostraciones conocidas de este teorema consisten en calcular un área de dos maneras diferentes para posteriormente igualarlas y manipular la expresión resultante, como ocurre en el siguiente caso:

## Demostración usual:


<center> <script type="text/tikz">
 

\tikzset{every picture/.style={line width=0.75pt}} %set default line width to 0.75pt        

\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
%uncomment if require: \path (0,221); %set diagram left start at 0, and has height of 221

%Shape: Rectangle [id:dp8670474238257233] 
\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (218.7,33.88) -- (389.99,33.88) -- (389.99,193.52) -- (218.7,193.52) -- cycle ;
%Shape: Rectangle [id:dp08207234382767448] 
\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (292.58,34.38) -- (389.45,102.71) -- (316.11,193.02) -- (219.25,124.69) -- cycle ;

% Text Node
\draw (248.22,12.32) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.5,yscale=1.5] [align=left] {a};
% Text Node
\draw (200.65,147.93) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.5,yscale=1.5] [align=left] {a};
% Text Node
\draw (349.52,196.43) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.5,yscale=1.5] [align=left] {a};
% Text Node
\draw (395.97,55.61) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.5,yscale=1.5] [align=left] {a};
% Text Node
\draw (340.56,11.8) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.5,yscale=1.5] [align=left] {b};
% Text Node
\draw (200.09,60.83) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.5,yscale=1.5] [align=left] {b};
% Text Node
\draw (397.65,145.32) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.5,yscale=1.5] [align=left] {b};
% Text Node
\draw (257.17,198) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.5,yscale=1.5] [align=left] {b};
% Text Node
\draw (261.09,76.47) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.5,yscale=1.5] [align=left] {c};
% Text Node
\draw (331.61,69.17) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.5,yscale=1.5] [align=left] {c};
% Text Node
\draw (270.05,140.63) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.5,yscale=1.5] [align=left] {c};
% Text Node
\draw (343.36,128.11) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.5,yscale=1.5] [align=left] {c};


\end{tikzpicture}
</script> </center>

En este caso lo que queremos es calcular el área del cuadrado grande de dos maneras diferentes, una de ellas es ver que es un cuadrado de lado $$(a+b)$$ y por lo tanto su area es $$(a+b)^2=a^2+2 a b+b^2$$.

La otra manera es calcular el área del cuadrado interior, la cual es $$c^2$$ y sumarle el área de los 4 triángulos interiores, cuya área es $$\frac{a b}{2}$$, por tanto el área total sería $$c^2+4\left(\frac{a b}{2}\right)=c^2+2 a b$$.

Luego, como estas son dos formas de calcular la misma área, podemos igualarlas de la siguiente manera

$$
c^2+2 a b=a^2+2 a b+b^2
$$

Luego podemos restar $2 a b$ ambos lados de la igualdad y nos queda finalmente que

$$
c^2=a^2+b^2
$$

Y este es justamente el teorema de pitágoras que conocemos y usamos tantas veces en geometría para medir distancias.

$$\tag*{$\blacksquare$}$$

## Demostración del presidente

Ahora veamos la demostración que dió a este teorema el presidente de los EE.UU James Abram Garfield, nuevamente consiste en calcular el área del siguiente trapecio de dos maneras diferentes.


<center><script type="text/tikz">

\tikzset{every picture/.style={line width=0.75pt}} %set default line width to 0.75pt        

\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
%uncomment if require: \path (0,423); %set diagram left start at 0, and has height of 423

%Shape: Right Triangle [id:dp7177952443822921] 
\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (156.43,93.29) -- (271.53,270.73) -- (156.43,270.73) -- cycle ;
%Shape: Right Triangle [id:dp3425406003573437] 
\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (458.79,149.14) -- (459.42,270.74) -- (271.55,270.74) -- cycle ;
%Straight Lines [id:da9979673577761621] 
\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (156.43,93.29) -- (458.77,149.13) ;
%Shape: Rectangle [id:dp4714976041799841] 
\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (267.64,264.15) -- (273.88,260.1) -- (277.77,266.69) -- (271.53,270.74) -- cycle ;

% Text Node
\draw (142.22,177.52) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.3,yscale=1.3] [align=left] {a};
% Text Node
\draw (381.64,270.96) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.3,yscale=1.3] [align=left] {a};
% Text Node
\draw (200.55,272.85) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.3,yscale=1.3] [align=left] {b};
% Text Node
\draw (464.35,203) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.3,yscale=1.3] [align=left] {b};
% Text Node
\draw (222.32,180.35) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.3,yscale=1.3] [align=left] {c};
% Text Node
\draw (356.39,188.84) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ,xscale=1.3,yscale=1.3] [align=left] {c};


\end{tikzpicture}

</script>
</center>

Usando la fórmula para calcular el área de un trapecio podemos ver que el área del mismo es $$\frac{(a+b)^2}{2}$$.

Otra forma de calcular esta área es calcular el área de los 3 triángulos y sumarla, el área de cada uno de los triángulos grises es justamente $$\frac{a b}{2}$$, y la del triángulo blanco es $$\frac{c^2}{2}$$ luego el área del trapecio sería:

$$
\frac{a b}{2}+\frac{a b}{2}+\frac{c^2}{2}=a b+\frac{c^2}{2}
$$

Al igualar estas dos formar de calcular el área nos queda lo siguiente:

$$
\frac{(a+b)^2}{2}=a b+\frac{c^2}{2}
$$

Ahora podemos multiplicar por 2 a ambos lados y nos que:

$$
(a+b)^2=a^2+2 a b+b^2=2 a b+c^2
$$

Y restando $2 a b$ a ambos lados nos queda finalmente el teorema de pitágoras.

$$
a^2+b^2=c^2
$$

$$\tag*{$\blacksquare$}$$

La fama del teorema de pitágoras se debe a que tiene una gran importancia en la geometría y es de uso recurrente para medir distancias, pero su impacto va más allá, este teorema inspiró a Fermat a plantear varios problemas en teoría de números, tales como el último teorema de Fermat, que duró más de 300 años sin resolverse.