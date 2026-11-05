"""Módulo de análisis de error y solución de referencia analítica."""
import numpy as np

def desplazamiento_referencia(x, L, E, A, P, q):
    """u(0)=0, EA*u'(L)=P, q uniforme. Devuelve la solución exacta en mm."""
    x = np.asarray(x, dtype=float)
    return ((P + q * L) * x - 0.5 * q * x**2) / (E * A)

def error_puntos_medios(resultado, L, E, A, P, q):
    """Devuelve el máximo error absoluto de u_h frente a u_ref en puntos medios [mm]."""
    x_nodos = resultado.x
    u_nodos = resultado.u
    n_elem = len(x_nodos) - 1
    
    max_error = 0.0
    for e in range(n_elem):
        # Coordenada del punto medio del elemento e
        x_mid = 0.5 * (x_nodos[e] + x_nodos[e+1])
        # Interpolación lineal MEF dentro del elemento
        u_h_mid = 0.5 * (u_nodos[e] + u_nodos[e+1])
        # Solución exacta en el punto medio
        u_ref_mid = desplazamiento_referencia(x_mid, L, E, A, P, q)
        
        err = abs(u_h_mid - u_ref_mid)
        if err > max_error:
            max_error = err
            
    return float(max_error)
