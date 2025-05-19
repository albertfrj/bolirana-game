```mermaid
flowchart TD
    A["Inicio del turno"] --> B["¿Turno de jugador 1?"]
    B -->|Sí| C["Jugador 1 realiza acción"]
    B -->|No| D["Jugador 2 realiza acción"]
    C --> E["Finalizar turno Jugador 1"]
    D --> F["Finalizar turno Jugador 2"]
    E --> G["Cambiar turno a Jugador 2"]
    F --> H["Cambiar turno a Jugador 1"]
    G --> I["¿Fin del juego?"]
    H --> I
    I -->|No| B
    I -->|Sí| J["Terminar juego"]
