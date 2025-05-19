```mermaid
graph TD
    UI[Interfaz de Usuario]
    UI --> A[Pantalla Principal]
    UI --> B[Marcador de Puntos]
    UI --> C[Indicador de Turno]
    UI --> D[Sección de Sensores]
    UI --> E[Botón Reiniciar]
    UI --> F[Mensajes / Alertas]

    A --> A1[Logo / Título]
    A --> A2[Instrucciones]
    B --> B1[Puntos Jugador 1]
    B --> B2[Puntos Jugador 2]
    C --> C1[Nombre Jugador Activo]
    D --> D1[Estado Sensor 1]
    D --> D2[Estado Sensor 2]
    D --> D3[Estado Sensor 3]
