---
layout: post
title:  "Apunte de prueba"
date:   2018-08-01 23:51:22 -0500
categories: apunte prueba
asciimath: true
---
Este es un apunte de prueba para una clase ejemplo en la que se requiera de notación matemática.

Para ejemplificar, con MathJax - ASCIIMath, mostramos una demostración del teorema de diferenciación de Leibniz.

**Teorema**.

<div>
Para `U` es un abierto de `RR^n` y `f: U xx [a, b] -> RR` continua con derivadas parciales continuas:
</div>
<div>
`phi(x) = int_a^b f(x, t) dt`
</div>
es continuamente diferenciable y
<div>
`del_i phi(x) = int_a^b del_i f(x, t) dt`
</div>
Por el teorema fundamental del cálculo:
<div>
`int_a^b int_0^x {del f(y, t)}/{del y} dy dt = phi(x) - phi(0)`
</div>
Por Fubini: 
<div>
`int_0^x int_a^b {del f(y, t)}/{del y} dt dy = phi(x) - phi(0)`
</div>
<div>Derivando con respecto a `x` y por el primer teorema fundamental del cálculo:</div>
<div>
`int_a^b {del f(y, t)}/{del y} dt = phi'(x)`
</div>
