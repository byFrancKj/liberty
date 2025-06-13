# Proyecto final — **Diseño con Python para un contexto visual**

## Descripción
**Liberty** es una pieza de arte generativo que produce composiciones abstractas sobre una cuadrícula.  
Usando *Processing.py* (modo Python de Processing), el programa crea círculos y polígonos con variaciones aleatorias de tamaño, color y posición.  
Cada ejecución genera una obra irrepetible, fusionando patrones orgánicos y geométricos inspirados en el arte abstracto.

## Historia
La idea surgió de un recuerdo de secundaria: mi profesor de matemáticas enseñó que si marcas *n* puntos equidistantes sobre una circunferencia (*n > 2*) y unes cada punto con sus dos vecinos inmediatos, se forma un polígono regular de *n* lados.

Partí de ese concepto para programar la generación automática de polígonos regulares con *n* entre 3 y 11. Luego introduje aleatoriedad en color, tamaño y rotación, y deformé sutilmente las figuras hasta obtener composiciones que evocaban las canicas de mi infancia y, al mismo tiempo, siluetas de aves en vuelo.  
Esa doble asociación inspiró el nombre **Liberty**, que refleja la libertad de la niñez y la de las aves, símbolo universal de independencia.

## Funcionalidades principales
- Cuadrícula de **20 × 20** celdas con figuras generadas al azar.  
- **Tres paletas cromáticas** cuidadosamente seleccionadas:  
  - *Círculos* → azules y grises.  
  - *Polígonos* → verdes y azules.  
  - *Bordes y fondo* → tonos neutros claros.  
- Curvas para números impares y polígonos rectos para números pares.  
- Variaciones aleatorias de tamaño y rotación.  
- Márgenes proporcionales que conservan el equilibrio visual.

## Tecnología
| Herramienta | Descripción |
|-------------|-------------|
| **Python** | Lógica y control del flujo de generación. |
| **Processing.py** | Motor gráfico que permite dibujar de forma sencilla en el lienzo. |

## Inspiración
El nombre **Liberty** captura la libertad creativa del arte generativo: dentro de parámetros definidos, cada renderizado explora caminos únicos e impredecibles.

---



