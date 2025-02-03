## Descripción del Método Numérico

La **cuadratura de Gauss** es un método numérico para aproximar integrales definidas. La fórmula general para la cuadratura es:

\[
\int_a^b \, \mathrm{d}x \, f(x) \approx \sum_{k=1}^{N+1} w_k f(x_k)
\]

donde:

  * \( w_k \) son los *pesos* de cada punto de muestra.

  * \( x_k \) son los *puntos de muestreo*, que son las raíces de los polinomios de Legendre \( P_N(x) \).


Para la **cuadratura Gaussiana**:

  * Los puntos de muestreo no son equidistantes, lo que permite más grados de libertad para la misma discretización en \( N \) subintervalos.
  * La cuadratura Gaussiana es exacta para un polinomio de orden \( (2N - 1) \).
  * Esto implica que la cuadratura Gaussiana tiene la misma precisión que un polinomio de orden \( (2N - 1) \), lo que es una mejora significativa en comparación con los métodos de Newton-Cotes.

### Elección de los Puntos de Muestreo y Pesos

Para la cuadratura Gaussiana, los puntos y los pesos se eligen de manera especial:

  * Los puntos de muestreo \( x_k \) corresponden a las \( N \) raíces de los polinomios de Legendre \( P_N(x) \) de orden \( N \).
  * Los pesos \( w_k \) se calculan usando la fórmula:
  
  $$
  w_k = \left[ \frac{2}{1 - x^2} \left( \frac{dP_N}{dx} \right)^{-2} \right]_{x = x_k}
  $$

  donde \( x_k \) es una raíz tal que \( P_N(x_k) = 0 \). Este es un aspecto crucial que hace que la cuadratura Gaussiana sea eficiente y precisa.

### Pros y Contras de la Cuadratura Gaussiana

**Pros:**

  - El error en la aproximación decrece rápidamente, con una tasa de convergencia de \( \frac{\text{const.}}{N^2} \), lo que significa que la precisión mejora significativamente con cada punto adicional.
  - Ejemplo: Al pasar de \( N = 10 \) a \( N = 11 \), la estimación mejora por un factor cercano a 100, lo que indica que la convergencia es muy eficiente.
  
**Contras:**

  - La cuadratura Gaussiana solo funciona bien si la función a integrar es relativamente bien comportada. Si no lo es, es posible que se necesiten más puntos de muestreo cerca de las regiones problemáticas.
  - Evaluar el error con precisión puede ser complicado y no siempre es posible obtener una estimación precisa del mismo.


## En el Código

La librería funciona de la siguiente forma:

  - Se ingresa el criterio de la expresión a integrar en la función 'func'.
  - Luego se calculan los puntos y pesos del método con la función 'gaussxw' para un número de particiones N.
  - Los vectores resultantes se escalan con la función 'gaussxwab' para un intervalo [a,b]. 
  - Finalmente, la integral se obtiene al realizar el siguiente cálculo 'integral = np.sum(pesos * func(puntos))'.
  - En caso de no aproximar de manera correcta, incrementar el número de particiones."
