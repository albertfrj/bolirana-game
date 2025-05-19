```mermaid
flowchart TD
    A["Escanear sensores de colisión (loop)"] --> B{"¿Sensor activado?"}
    B -- "No" --> A
    B -- "Sí" --> C["Leer ID o ubicación del sensor"]
    C --> D["Actualizar puntuación según el tipo de colisión"]
    D --> E["Reproducir efecto visual/sonoro (opcional)"]
    E --> F["Registrar evento para estadísticas o historial"]
    F --> A
