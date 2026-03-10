# Proyecto-parcial-IA

## Nombre
Rayner Alexander Mora Poueriet
## Matrícula
24-EISN-2-004
## Proyecto

# SHOOT — Top-Down Shooter/ Inpirado en Gaunlet

Un videojuego de acción en vista superior (top-down) desarrollado en Python con Pygame, donde el jugador debe sobrevivir eliminando enemigos mientras recolecta recursos en un entorno de salas.

---

## Descripción

SHOOT es un juego 2D de disparos en perspectiva top-down. El jugador controla a un personaje armado que se mueve libremente por el escenario, apunta con el ratón y dispara balas en tiempo real. El objetivo es eliminar a los enemigos que habitan el mapa antes de que agoten la vida del jugador, recolectando monedas y pociones para sobrevivir.

---

## Características

- **Movimiento libre** en 4 direcciones con detección de colisiones contra obstáculos del mapa
- **Sistema de disparo** apuntado con el mouse, con cooldown entre disparos
- **Dos tipos de enemigos** con distintos niveles de vida y animaciones propias
- **Sistema de vida** visual con corazones (lleno, mitad, vacío)
- **Items recogibles:** monedas animadas y pociones de vida
- **Texto de daño flotante** al impactar enemigos
- **Sistema de cámara** que sigue al jugador por el mapa

---

## Controles

| Tecla / Input | Acción |
|---|---|
| `W` | Mover hacia arriba |
| `A` | Mover hacia la izquierda |
| `S` | Mover hacia abajo |
| `D` | Mover hacia la derecha |
| `Click izquierdo` | Disparar |

---

## Estructura del proyecto

```
├── main.py               # Loop principal del juego
├── personaje.py          # Clase jugador y enemigos
├── arma.py               # Clase arma y balas
├── mundo.py              # Carga y gestión del mapa
├── items.py              # Monedas y pociones
├── text_daño.py          # Texto flotante de daño
├── constantes.py         # Configuración global del juego
├── dividir_imagen.py     # Utilidad para cortar tilesets
└── assets/
    ├── imagenes/
    │   ├── characters/   # Sprites del jugador y enemigos
    │   ├── Armas/        # Sprite del arma y balas
    │   ├── tiles/        # Tiles del mapa
    │   └── items/        # Monedas, pociones, vida
    └── fonts/            # Fuente del juego
```

---

## Requisitos

- Python 3.x
- Pygame
- Pillow (para `dividir_imagen.py`)

Instalación de dependencias:

```bash
pip install pygame pillow
```

---

## Cómo ejecutar

```bash
python main.py
```

---

## Tecnologías utilizadas

- **Python 3**
- **Pygame** — motor gráfico, manejo de eventos, sprites y colisiones
- **Pillow** — procesamiento de imágenes para dividir tilesets

---

## Estado del proyecto

En desarrollo — proyecto parcial.