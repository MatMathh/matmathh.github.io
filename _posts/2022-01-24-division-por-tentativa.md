---
layout: single
title: División por tentativa
excerpt: "Leonhard Euler demostró aproximadamente en 1772 que 2.147.483.647 es un numero primo y le mando una carta a Daniel Bernoulli informandole de su prueba, ¿Cómo fue que lo hizo con las limitaciones de su epoca para realizar cálculos?"
date: 2022-01-24
classes: wide
header:
  teaser: /assets/images/division-por-tentativa/euler.jpg
  teaser_home_page: true
  icon: 
categories:
  - Teoría de Números
  - Álgebra Computacional
tags:  
  - Números de Mersenne
  - Números Primos
  - Euler
  - Test de primalidad
---

<center> <img src="/assets/images/division-por-tentativa/euler.jpg" width="45%" heigth="45%"> </center>
<br>

Un número primo $$n$$ es un entero que solo es divisible por $$2$$ números distintos, siendo estos $$1$$ y $$n$$, entonces, si queremos verificar si un número $$n$$ es primo, debemos comprobar que no tiene algún factor primo $$k$$ tal que $$1<k<n$$, lo cual puede ser una tarea tediosa y larga. Así, a continuación presentaremos un teorema que nos ayudará a ahorrar tiempo a la hora de verificar si un número $$n$$ es primo, siendo este el mismo que usó **Euler** en su demostración.

## Teorema
Sea $$n\in\mathbb{Z}$$, si $$n$$ es compuesto, entonces $$n$$ tiene un factor primo $$k$$ menor o igual a $$\sqrt{n}$$.

## Demostración

Sea $$n$$ un compuesto (positivo), entonces existen a y $$b \in \mathbb{Z}$$ tales que $$n=a b$$, con $$1<a, b<n$$. Por tricotomía podemos suponer que $$a \leq b$$, sin pérdida de generalidad.

Veamos que $$a \leq \sqrt{n}$$ (lo que queremos demostrar), de lo contrario $$\sqrt{n}<a \leq b$$ así $$n=a \cdot b \geq a \cdot a>\sqrt{n} \cdot \sqrt{n}=n$$, es decir que $$n>n$$, **CONTRADICCIÓN**, entonces queda demostrado que $$n$$ tiene un factor $$a \leq \sqrt{n}$$, pero aún tenemos que verificar si es primo.

Ahora si a es primo pues ya acabamos, así que consideremos el otro caso, si $$a$$ no es primo, como $$a>1$$, entonces por el Teorema Fundamental de la Aritmética a tiene un factor primo que lo divide y por transitividad también divide a $$n$$, que es justamente lo que se quería demostrar.

$$\tag*{$\blacksquare$}$$



Este teorema es muy utíl, ya que su contrarecíproco nos asegura que si $$n$$ no tiene un factor primo $$k$$ menor o igual a $$\sqrt{n}$$, entonces $$n$$ es un número primo.

Algo interesante que podemos hacer es construir un programa que verifique la primalidad de un número dividiendolo entre los $$n$$ números menores que él y verificando el resultado, claramente este algoritmo no será muy eficiente, pero lo bueno es que es sencillo de programar y nos puede arrojar una gran diferencia de tiempo empleado si usamos o no el teorema anterior.

## Códigos
  - Usando el teorema.

    ```python
    from math import *
    from timeit import default_timer

    def verificar_si_es_primo(numero: int)->str:
      inicio = default_timer()
      respuesta = "Es primo"
      if (numero == 0 or numero == 1 or numero == 4):
        respuesta = "No es primo"
      x = 2
      contador = 1
      while (x <= sqrt(numero)):
        if ((numero % x) == 0):
          respuesta = "No es primo"
          x = numero
        x = x + 1
        contador = contador + 1
      final = default_timer()
      return str(respuesta + " y se ha tardado " + str(final - inicio) + " segundos en verificar, habiendo realizado " + str(contador) + " divisiones.")

    print("Bienvenido a la verificadora de numeros primos")
    numero = int(input("Por favor digite el número al cuál quiere verificar si es primo: "))
    resultado = verificar_si_es_primo(numero)
    print(resultado)
    ```

  - Probando hasta que encuentre un divisor o $$n$$.

    ```python
    from math import *
    from timeit import default_timer

    def verificar_si_es_primo(numero: int)->str:
      inicio = default_timer()
      respuesta = "Es primo"
      if (numero == 0 or numero == 1 or numero == 4):
        respuesta = "No es primo"
      x = 2
      contador = 1
      while (x <= numero):
        if ((numero % x) == 0):
          respuesta = "No es primo"
          x = numero + 1
        x = x + 1
        contador = contador + 1
      if (x == (numero + 1)):
        respuesta = "Es primo"
      final = default_timer()
      return str(respuesta + " y se ha tardado " + str(final - inicio) + " segundos en verificar, habiendo realizado " + str(contador) + " divisiones.")

    print("Bienvenido a la verificadora de numeros primos")
    numero = int(input("Por favor digite el número al cuál quiere verificar si es primo: "))
    resultado = verificar_si_es_primo(numero)
    print(resultado)
    ```

## Resultados
  - Usando el teorema.
  <center> <img src="/assets/images/division-por-tentativa/resultado_raiz.png" weidth="100%" heigth="100%"> </center>
  - Probando hasta que encuentre un divisor o $$n$$.
  <center> <img src="/assets/images/division-por-tentativa/resultado_fuerza_bruta.png" weidth="100%" heigth="100%"> </center>  
  <br>

Note que claramente el método aquí se puede mejorar, pues conociendo todos los números primos menores a $$\sqrt{n}$$ se descartan muchos casos de división en ambos casos, no obstante esta condición es demasiado fuerte, pues listar todos los números primos menores que $$\sqrt{n}$$ o $$n$$ si nos concentramos en el segundo caso, implica que debimos de haber corrido algún algoritmo previo o tabla en la que se encuentren estos mismos, por lo cual en un principio nuestro programa directamente prueba con todos los números menores. Por otro lado, es claro que usando el teorema visto anteriormente logramos una complejidad de computo mucho menor que directamente probando con todos los números menores a $$n$$.


**Euler** Utilizó este resultado para verificar que el número $$2.147.483.647$$ es primo y mejoró el método de **Cataldi**, por lo que solo tuvo que verificar $$372$$ divisiones.

## Curiosidades

  - Note que $$2.147.483.647 = 2^{(2^{5}-1)}-1$$ lo que lo convierte en un primo doble de **Mersenne**.

  - Durante diciembre de **2014** cuando el vídeo que hizo famoso a **PSY, “Gangnam Style”**, llegó a las $$2.147.483.647$$ views y el sistema de $$32-bit$$ de la web de vídeos no pudo continuar contándolas porque simplemente había llegado a su máximo. 

  - El 4 de junio de **1996** despegó el primer vuelo del cohete **Ariane 5** manejado por la Agencia Espacial Europea. Dentro de él no había una tripulación pero sí estaba cargado con cuatro satélites científicos muy costosos. El vuelo explotó apenas 39 segundos después de despegar, perdiendo alrededor de **370 millones de dólares**. Después de un poco de investigación se dieron cuenta que el problema no era más que un bug de software que involucraba el número $$2.147.483.647$$. Aparentemente, Ariane 5 necesitaba una aceleración horizontal mayor que los modelos previos porque su trayecto era distinto, y esto hizo que todos los computadores que controlaban el auto-piloto se confundieran y que comenzara una secuencia para auto-destruirse. 
