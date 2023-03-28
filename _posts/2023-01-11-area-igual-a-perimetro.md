---
layout: single
title: Area igual a perímetro
excerpt: "¿Cuántos triángulos cumplen que su perímetro sea igual a su área?, aquí veremos la respuesta y encontraremos todos los triángulos que cumplen la propiedad" 
date: 2023-01-11
classes: wide
header:
  teaser: /assets/images/lema-de-euclides/Euclides.jpg  
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Números
tags:  
  - Teoría de Números
  - Geometría
---




<center><script type="text/tikz">




\tikzset{every picture/.style={line width=0.75pt}} %set default line width to 0.75pt        

\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
%uncomment if require: \path (0,472); %set diagram left start at 0, and has height of 472

%Shape: Grid [id:dp9210298878677159] 
\draw  [draw opacity=0][dash pattern={on 0.84pt off 2.51pt}] (94.1,128.86) -- (400.99,128.86) -- (400.99,388.29) -- (94.1,388.29) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][dash pattern={on 0.84pt off 2.51pt}] (94.1,128.86) -- (94.1,388.29)(117.56,128.86) -- (117.56,388.29)(141.02,128.86) -- (141.02,388.29)(164.48,128.86) -- (164.48,388.29)(187.94,128.86) -- (187.94,388.29)(211.4,128.86) -- (211.4,388.29)(234.87,128.86) -- (234.87,388.29)(258.33,128.86) -- (258.33,388.29)(281.79,128.86) -- (281.79,388.29)(305.25,128.86) -- (305.25,388.29)(328.71,128.86) -- (328.71,388.29)(352.18,128.86) -- (352.18,388.29)(375.64,128.86) -- (375.64,388.29)(399.1,128.86) -- (399.1,388.29) ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][dash pattern={on 0.84pt off 2.51pt}] (94.1,128.86) -- (400.99,128.86)(94.1,152.32) -- (400.99,152.32)(94.1,175.78) -- (400.99,175.78)(94.1,199.24) -- (400.99,199.24)(94.1,222.7) -- (400.99,222.7)(94.1,246.17) -- (400.99,246.17)(94.1,269.63) -- (400.99,269.63)(94.1,293.09) -- (400.99,293.09)(94.1,316.55) -- (400.99,316.55)(94.1,340.01) -- (400.99,340.01)(94.1,363.48) -- (400.99,363.48)(94.1,386.94) -- (400.99,386.94) ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][dash pattern={on 0.84pt off 2.51pt}]  ;
%Shape: Right Triangle [id:dp2427837281444376] 
\draw  [color={rgb, 255:red, 255; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=0.51 ] (99.17,197.23) -- (276.48,326.38) -- (183.75,371.41) -- cycle ;
%Shape: Right Triangle [id:dp7742542755528874] 
\draw  [color={rgb, 255:red, 255; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=0.56 ] (395.5,330.3) -- (210.32,177.7) -- (291.3,136.06) -- cycle ;

% Text Node
\draw (240.85,144.05) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ] [align=left] {5};
% Text Node
\draw (342.65,213.36) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ] [align=left] {12};
% Text Node
\draw (263.37,237.63) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ] [align=left] {13};
% Text Node
\draw (180.85,246.26) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ] [align=left] {10};
% Text Node
\draw (125.42,275.65) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ] [align=left] {8};
% Text Node
\draw (224.13,350.35) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ] [align=left] {6};


\end{tikzpicture}

</script>
</center>



Sabemos que por el teorema de pitágoras al ser un triangulo rectángulo se tiene que $$a^2+b^2=c^2$$, entonces consideramos $$a$$ y $$b \neq 0$$ ya que ningún lado puede ser 0 Sabemos que el área de un triángulo es $$\frac{a b}{2}$$ y que el perímetro sería $$a+b+c$$, luego
 
$$
\frac{a b}{2}=a+b+c
$$

Luego como $$c^2=a^2+b^2$$

$$
\left(\frac{a b}{2}-a-b\right)^2=a^2+b^2
$$

Ahora expandiendo el cuadrado, tenemos que

$$
\left(\frac{a b}{2}-a-b\right)^2=\frac{a^2 b^2}{4}+a^2+b^2-a^2 b-a b^2+2 a b
$$

Y por tanto

$$
\frac{a^2 b^2}{4}-a^2 b-a b^2+2 a b=0
$$

Ahora factorizamos $a b$ y nos queda lo siguiente:

$$
a b\left(\frac{a b}{4}-a-b+2\right)=0
$$

Y como $$a$$ y $$b \neq 0$$, entonces $$a b \neq 0$$, de esto sigue que

$$
\frac{a b}{4}-a-b+2=0
$$

Luego $$a b-4 a-4 b+8=0$$, así $$a b-4 a-4 b+16=8$$ y factorizamos otra vez xd

$$
(a-4)(b-4)=8
$$

Y listo, resolvimos el problema, ¿por qué?, pues básicamente nos basta considerar las formas posibles de obtener 8 como producto de dos naturales y como conocemos la factorización de 8 , es fácil.

Podemos tener $$4 * 2$$ o $$8 * 1$$, esto ya que $$2 * 4$$ y $$1 * 8$$ nos darían el mismo triangulo.

Ahora, si $$(a-4)=4$$ entonces $$a=8$$ y si $$(b-4)=2$$ entonces $$b=6$$ y obtenemos por el teorema de pitágoras $$(8,10,6)$$

Para el segundo consideramos $$(a-4)=8$$, entonces $$a=12$$ y si $$(b-4)=1$$, entonces $$b=5$$, obteniendo entonces $$(12,13,5)$$

Y listo, concluimos que estos son los posibles casos.