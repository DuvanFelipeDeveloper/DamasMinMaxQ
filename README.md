Readme para el Proyecto de Damas con IA
Descripción
Este proyecto consta de un juego de Damas implementado en Python que utiliza la técnica de Inteligencia Artificial conocida como Minimax con poda Alfa-Beta para determinar las mejores movidas. Además, utiliza el método de Aprendizaje por Refuerzo para mejorar el desempeño de la IA a lo largo del tiempo.

Este juego también incluye una API multijugador basada en sockets y una API basada en Flask para interacción con el backend. Todo el código está disponible en este repositorio de GitHub.

Requisitos
Python 3.x
Flask
matplotlib
pickle
Instalación

Para instalar y ejecutar el juego, sigue los siguientes pasos:

Clona el repositorio en tu máquina local utilizando git clone.

Instala las dependencias del proyecto. Desde la raíz del proyecto, ejecuta el siguiente comando en la terminal:

Copy code

pip install -r requirements.txt

Ejecuta el juego utilizando Python:

css

Copy code

python app.py

tambien puede realizar el consumo del api y asi mismo tiene un componente de tablero por consola que puede utilizar 
en el archivo mimmax y minmaxultimate estan comentadas las lienas de pruebas y de entrenamiento tambien te recomiento revisar el repositorio del forntend en vue.js

Cómo Jugar
Una vez que el juego se está ejecutando, puedes interactuar con él a través de la API de Flask. Las instrucciones específicas para la interacción con la API se encuentran en la documentación de la API.

Descripción del Código
El juego consta de varios componentes, incluyendo el algoritmo Minimax, el aprendizaje por refuerzo, y las APIs de Flask y de sockets.

Minimax y Aprendizaje por Refuerzo
El algoritmo Minimax se implementa en la función minmax. Esta función toma un tablero de juego, una profundidad de búsqueda, y dos valores alfa y beta, y devuelve la mejor jugada para el jugador actual.

La función q_learning implementa el algoritmo de aprendizaje por refuerzo. Esta función toma un tablero de juego, un jugador, una tasa de aprendizaje, un factor de descuento, un valor de epsilon, y un número de episodios, y entrena la IA para mejorar su desempeño.

La función choose_move se usa para seleccionar la mejor jugada para un jugador dado. Esta función combina el algoritmo Minimax con el aprendizaje por refuerzo para tomar una decisión.

API de Flask
La API de Flask se utiliza para interactuar con el juego. Puedes hacer movimientos y obtener el estado actual del juego a través de esta API.

API de Sockets
La API de sockets se utiliza para la funcionalidad multijugador del juego. Con esta API, dos jugadores pueden jugar uno contra el otro en tiempo real.

Contribución
Las contribuciones a este proyecto son bienvenidas. Si encuentras un bug o tienes una idea para una nueva característica, por favor abre un issue o haz un pull request.

Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT. Para más detalles, ver el archivo LICENSE en el repositorio.
