# T05_U3_Tejo

Este repositorio contiene el desarrollo del Test 5 - Unidad 3 del curso Herramientas computacionales II.

El objetivo es evaluar la sensibilidad numerica y fisica mediante el refinamiento de malla (n = 2, 4, 8) y alteraciones de condiciones de controno en un modelo de elementos finitos para una barra axial con Carga distribuida 

# Resumen del modelo

Geometria y material:
- L = 2000 mm
- E = 200000 MPa
- A = 1000 mm^2

Cargas:
- Carga puntual P = 20000 N
- Carga distribuida q = 10 N/mm

Caso Base:
- u(0) = 0 (Dirichlet)
- EA u'(L) = P (Neumann)

Caso Alterado:
-BC_ALTERADO donde se añade u(L) = 0 Simulando doble empotramiento y manteniendo cargas constantes.

# Estructura del Repositorio

```
├── datos/
│   └── barra.json           # Parámetros geométricos, de carga y mallas
├── src/
│   ├── barra_mef.py         # Solver 1D suministrado en NumPy
│   ├── analisis.py          # Solución analítica y cálculo de error inter-nodal
│   └── ejecutar.py          # Script principal de simulación y generación de salidas
├── informe/
│   ├── main.tex             # Informe en LaTeX (plantilla U1 USACH)
│   ├── referencias.bib      # Archivo de referencias BibTeX
│   └── main.pdf             # PDF compilado final
├── salidas/
│   ├── resultados.csv       # Tabla de resultados numéricos
│   └── convergencia.png     # Gráfico log-log de convergencia del error
├── BITACORA.md              # Registro de predicciones previas a la ejecución
├── USO_IA.md                # Declaración transparente del uso de IA
├── entrega.json             # Metadatos del repositorio y commit evaluado
└── README.md                # Resumen, cargas, casos, entornos y ejecucion del repositorio
```

## Entorno y ejecución
Abra la carpeta de la actividad en VS Code.
Para un entorno propio: `python -m venv .venv`, active ese entorno y ejecute `python -m pip install -r requirements.txt`.
En Windows puede ejecutar `.venv\Scripts\python.exe` sin cambiar la política de PowerShell. En Linux use `.venv/bin/python`.
Ejecute `python -m pytest -q` y `python src/ejecutar.py`. Mediante estos comandos se obtiene el grafico  y la tabla de datos para las diferentes mallas.
Contraste tres mallas y el caso BC_ALTERADO; interprete por qué puede cerrar equilibrio y representar otro problema.
