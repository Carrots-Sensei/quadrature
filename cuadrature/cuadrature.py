import numpy as np

def gaussxw(N):

    """
    Obtiene los pesos y puntos de muestreo para aproximar una integral por el método de cuadratura gaussiana.
    
    Args:
    	N (integer): número de particiones del dominio

    Returns:
    	x (list): vector de puntos de muestreo
    	w (list): vector de peso de los puntos de muestreo
    	
    Example:
    	- gaussxw(4)
    	- x = [ 0.86113631  0.33998104 -0.86113631 -0.33998104]
    	- w = [0.34785485 0.65214515 0.34785485 0.65214515]
    
    """

    # Aproximación inicial
    a = np.linspace(3, 4 * (N - 1), N) / ((4 * N) + 2)
    # Note código vectorial aquí
    x = np.cos(np.pi * a + 1 / (8 * N * N * np.tan(a)))

    # Ahora calculamos las raíces de los polinomios utilizando el método de Newton
    # Este es un tema que veremos la próxima semana!
    # De momento, puede ignorar el siguiente flujo de control con el "while" y saber que esto 
    # devuelve los puntos de muestreo obtenidos con los polinomios de Legendre
    epsilon = 1e-15
    delta = 1.0
    while delta > epsilon:
        p0 = np.ones(N, dtype = float)
        # Deep copy
        p1 = np.copy(x)
        for k in range(1, N):
            p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
        dp = (N + 1) * (p0 - x * p1) / (1 - x * x)
        dx = p1 / dp
        x -= dx
        delta = np.max(np.abs(dx))

    # Ahora calculamos los pesos
    w = 2 * (N + 1) * (N + 1)/(N * N * (1 - x * x) * dp * dp)

    # Note que la función devuelve un tuple
    return x,w

def gaussxwab(a, b, x, w):

    """
    Escala los pesos y puntos de muestreo para aproximar una integral por el método de cuadratura gaussiana fuera del intervalo [-1,1].

    Args:
    	a (float): límite inferior del nuevo dominio
    	b (float): límite superior del nuevo dominio
    	x (list): vector de puntos de muestreo
    	w (list): vector de peso de los puntos de muestre

    Returns:
    	x (list): vector escalado de puntos de muestreo
    	w (list): vector escalado de peso de los puntos de muestreo
    	
    Example:
    	- gaussxwab(1, 3, x, w)
    	- x = [2.86113631 2.33998104 1.13886369 1.66001896]
    	- w = [0.34785485 0.65214515 0.34785485 0.65214515]
    
    """
    
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def func(varInd):

    """
    Retorna el criterio de una función

    Args:
    	varInd (list): variable independiente de la función

    Returns:
    	output (list): una expresión matemática
    	
    Example:
    	- se toma varInd como la salida de la función gaussxwab para éste ejemplo
    	- func(varInd) = [552.92371418 169.63516215   1.19568479  21.41474705]
    
    """
    
    return varInd**6 - (varInd**2) * np.sin(2*varInd)
    
# Se obtienen los puntos y pesos
puntos, pesos = gaussxw(4)

# Se escala para el nuevo intervalo
puntos, pesos = gaussxwab(1, 3, puntos, pesos)

# Se calcula la integral
integral = np.sum(pesos * func(puntos))
integral # 317.3453903341579

# El resultado analítico es aprox. 317.34

