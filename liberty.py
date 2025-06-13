from math import cos, sin

# Paletas
paleta_circulos = [
    color(34, 48, 63),
    color(231, 232, 231),
    color(143, 191, 218),
    color(44, 100, 133),
    color(57, 74, 86)
]

paleta_poligonos = [
    color(46, 61, 22),
    color(70, 89, 2),
    color(70, 115, 2),
    color(52, 126, 191),
    color(176, 198, 217)
]

paleta_borde = [
    color(245, 241, 235),
    color(217, 213, 206),
    color(182, 173, 163)
]

# Configuración
num = 20

def setup():
    size(1080, 1000)
    noLoop()
    dibujar_figuras()

def dibujar_figuras():
    background(255)
    canvas_width = width
    canvas_height = height

    # Calcular el margen como el 20% del tamaño del canvas
    margin_width = canvas_width * 0.04
    margin_height = canvas_height * 0.04

    # Calcular el ancho y alto disponibles para dibujar
    available_width = canvas_width - (2 * margin_width)
    available_height = canvas_height - (2 * margin_height)

    # Calcular el tamaño de la celda basado en el ancho disponible
    celda_width = available_width / num
    celda_height = available_height / num # Considerar si quieres celdas cuadradas o rectangulares

    for i in range(num):
        for j in range(num):
            # Calcular las coordenadas del centro de la celda con el nuevo margen
            cx = margin_width + (i * celda_width + celda_width / 2)
            cy = margin_height + (j * celda_height + celda_height / 2)

            # Usar el menor valor entre celda_width y celda_height para el radio si quieres círculos/polígonos contenidos
            radio = min(celda_width, celda_height) / 2
            n = int(random(3, 20))

            # Si es impar, dibuja el círculo
            if n % 2 != 0:
                color_circulo = paleta_circulos[int(random(len(paleta_circulos)))]
                fill(color_circulo)
                stroke(0)
                ellipse(cx, cy, celda_width, celda_height) # Usar celda_width y celda_height para que el círculo ocupe la celda

            # Color según si está en el borde
            es_borde = i == 0 or j == 0 or i == num - 1 or j == num - 1
            if es_borde:
                color_figura = paleta_borde[int(random(len(paleta_borde)))]
            else:
                color_figura = paleta_poligonos[int(random(len(paleta_poligonos)))]

            fill(color_figura)
            stroke(0)

            rotacion = (PI)

            # 🌀 Figuras curvas si n es impar, rectas si es par
            if n % 2 != 0:
                beginShape()
                for k in range(n + 0):  
                    angle = TWO_PI * (k % n) / n + rotacion
                    r_var = radio * random(0, 1.0)
                    x = cx + r_var * cos(angle)
                    y = cy + r_var * sin(angle)
                    curveVertex(x, y)
                endShape(CLOSE)
            else:
                beginShape()
                for k in range(n):
                    angle = TWO_PI * k / n + rotacion
                    r_var = radio * random(0, 1.0)
                    x = cx + r_var * cos(angle)
                    y = cy + r_var * sin(angle)
                    vertex(x, y)
                endShape(CLOSE)
