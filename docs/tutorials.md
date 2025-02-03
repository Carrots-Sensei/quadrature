Se recomienda analizar los siguientes casos de ejemplo
para familiarizarse con el código.

### 1. Integrando

Consíderese la función siguiente:

\[
f(x) = x^6 - \sin(2x) \cdot x^2
\]

entonces se define func() tal que:

```python
def func(varInd):
    return varInd**6 - (varInd**2) * np.sin(2*varInd)
```

### 2. Cálculo de la Integral


Se realiza el cálculo con 4 particiones, dado que es el número que mejor se aproxima al resultado analítico y porque funciona para polinomios de grado 2(4-1) = 7 o menor. Para ello se calculan los puntos de muestreo y sus pesos:

```python
puntos, pesos = gaussxw(4)
```

se escalan para el intervalo [1,3]:

```python
puntos, pesos = gaussxwab(1, 3, puntos, pesos)
```

y luego se calcula la integral

```python
integral = np.sum(pesos * func(puntos))
integral # 317.3453903341579
```

El resultado analítico es aprox. 317.34
