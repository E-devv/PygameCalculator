# Calculadora Neon

¡Una calculadora con un estilo visual llamativo de luces de neón!

## Sobre el Proyecto

Este proyecto es una calculadora de escritorio creada con Python y la librería Pygame. No solo realiza las operaciones aritméticas básicas, sino que también presenta una interfaz gráfica con un diseño "retro" inspirado en el neón, con efectos visuales que responden a la interacción del usuario.

## Cómo Funciona

La aplicación se estructura de la siguiente manera:

*   **`main.py`**: Es el núcleo del programa. Se encarga de inicializar Pygame, crear la ventana, gestionar el bucle de eventos, y dibujar todos los elementos en pantalla, como los botones y el display de resultados.
*   **`logic.py`**: Contiene la clase `CalculatorLogic`, que maneja toda la lógica detrás de las operaciones. Procesa las teclas presionadas, actualiza el estado interno de la calculadora y devuelve el texto que debe mostrarse.
*   **`button.py`**: Define la clase `Button`, que se ocupa de la apariencia y el comportamiento de cada botón. Esto incluye su color, tamaño, y cómo reacciona cuando el ratón pasa por encima o hace clic.
*   **`config.py`**: Almacena todas las constantes del proyecto, como los colores de neón, las dimensiones de la pantalla y la configuración de la fuente, facilitando la personalización del diseño.

## Construido Con

*   **Python**: El lenguaje de programación principal.
*   **Pygame**: Una librería de Python para crear videojuegos y aplicaciones multimedia, utilizada aquí para toda la representación gráfica y la gestión de eventos.

## Desarrolladora

Este proyecto fue desarrollado por **Elizabeth**.