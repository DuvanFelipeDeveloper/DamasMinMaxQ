# 🎲 Juego de Damas con Algoritmo Minimax y Aprendizaje por Refuerzo 🎲

Este proyecto es una implementación de un juego de damas que utiliza el algoritmo Minimax para tomar decisiones. Adicionalmente, el programa utiliza técnicas de aprendizaje por refuerzo para mejorar el rendimiento del agente. El proyecto también incluye una API multijugador que utiliza sockets y Flask.

## 📖 Índice

1. [Instalación](#instalación)
2. [Uso](#uso)
3. [Descripción del código](#descripción-del-código)
4. [Contribuciones](#contribuciones)
5. [Contacto](#contacto)

## 💻 Instalación

Para instalar y ejecutar este proyecto, sigue los siguientes pasos:

1. Clona el repositorio:

```bash
https://github.com/DuvanFelipeDeveloper/DamasMinMaxQ.git
```

2. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

3. Ejecuta el archivo principal del programa

```bash
python MinMaxUltimate.py
flask run
```
ten en cuenta que al final del codigo de MinMaxUltimate estan las lineas de codigo de entrenamiento y pruebas comentadas

## 🕹️ Uso
Puedes jugar contra la IA ejecutando el archivo principal del programa. Utiliza las coordenadas del tablero para indicar tus movimientos.

## 📜 Descripción del código

El código principal del juego de damas se encuentra en el archivo main.py. Este archivo contiene las implementaciones del algoritmo Minimax y del aprendizaje por refuerzo. Los movimientos del jugador y de la IA se gestionan a través de este archivo.

La IA utiliza el algoritmo Minimax para tomar decisiones, considerando los posibles movimientos del adversario. Este algoritmo está optimizado con la técnica de poda alfa-beta, lo que mejora la eficiencia del algoritmo al evitar el análisis de movimientos que no van a ser seleccionados.

El aprendizaje por refuerzo se realiza mediante la técnica de Q-Learning. La IA almacena y actualiza los valores Q de cada estado y acción posible, lo que le permite aprender y mejorar sus decisiones con el tiempo.

El juego también incluye una API para partidas multijugador, utilizando sockets para la comunicación en tiempo real entre los clientes. Además, se utiliza Flask para gestionar las peticiones HTTP y proporcionar una interfaz web para el juego.

## 💡 Contribuciones

1. Realiza un Fork del proyecto
2. Crea tu Feature Branch (git checkout -b feature/AmazingFeature)
3. Realiza tus cambios (git commit -m 'Add some AmazingFeature')
4. Sube tus cambios (git push origin feature/AmazingFeature)
5. Abre una Pull Request
