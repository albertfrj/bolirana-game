```mermaid
flowchart TD
    A["Inicio: Evento que otorga puntos"] --> B["Obtener valor base de puntos"]
    B --> C{"¿Multiplicador activo?"}
    C -- "Sí" --> D["Aplicar multiplicador al valor base"]
    C -- "No" --> E["Usar valor base sin modificar"]
    D --> F["Sumar puntos al total"]
    E --> F
    F --> G["Actualizar marcador en pantalla"]
    G --> H["Fin del proceso"]
