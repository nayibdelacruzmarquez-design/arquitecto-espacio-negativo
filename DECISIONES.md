# Registro de Decisiones de Diseño y Arquitectura de Layouts
**Especialista:** Nayib  
**Módulo:** Gestión de Geometría y Diseño de Layouts  

### 1. Justificación de la Escala Sistémica de Espaciado (Múltiplos de 8px)
Se implementó de manera estricta una escala basada en múltiplos de 8 píxeles (`4px`, `8px`, `16px`, `24px`, `32px`, `48px`). Esta decisión obedece a estándares universales de ergonomía digital e ingeniería de software:
* **Armonía Proporcional:** Garantiza un ritmo vertical predecible que guía de manera natural la vista del usuario a través del flujo de datos del servidor.
* **Mitigación de Errores de Renderizado:** La gran mayoría de las resoluciones de pantallas comerciales modernas son divisibles de forma exacta por 8. Al estructurar nuestros paddings y márgenes bajo esta escala, evitamos que el navegador compute valores fraccionales de subpíxeles, erradicando los bordes borrosos (*subpixel rendering artifacts*) y manteniendo una nitidez absoluta en la UI.

### 2. Adopción de CSS Grid Gaps vs Márgenes Tradicionales
Para la macroestructura (`.dashboard-container`) y el contenedor secundario (`.kpi-grid`), se sustituyeron los márgenes individuales por la propiedad `gap` nativa de CSS Grid. 
* **Impacto en la Mantenibilidad:** La propiedad `gap` define el espacio exacto *únicamente entre los elementos del contenedor*, eliminando la necesidad de aplicar márgenes laterales o inferiores que requieran ser cancelados con selectores complejos como `:last-child`.
* **Inmunidad al Colapso:** Las propiedades de separación en rejillas Grid/Flexbox no sufren de colapso de márgenes, asegurando que el espacio asignado permanezca intacto sin importar la mutabilidad de los datos enviados desde Python. Esto facilita una maquetación ágil y responsiva mediante Media Queries con solo redefinir el valor del `gap` en el elemento padre.

### 3. Alineación Contextual Fina y Accesibilidad (WCAG)
* **Alineación de Tablas:** Los identificadores de texto y nombres se alinearon a la izquierda para mantener la inercia natural de lectura occidental, mientras que los valores financieros se alinearon estrictamente a la derecha. Esto posiciona de manera vertical las unidades con unidades y centenas con centenas, permitiendo un escaneo analítico veloz y disminuyendo errores de interpretación contable.
* **Diseño Condicional SSR (Jinja2):** Se aprovechó la potencia del renderizado en el servidor para inyectar dinámicamente un padding maximizado (`p-xxl`) en el estado vacío. Cuando el backend no retorna transacciones, la interfaz se expande para ventilar la pantalla, reduciendo la frustración del usuario mediante un contenedor perfectamente centrado que respira.
* **Accesibilidad Táctil:** El botón de acción interactivo cuenta con una regla restrictiva de `min-height: 44px`. Esto cumple cabalmente con las pautas de accesibilidad **WCAG**, garantizando un área de activación segura para pulsaciones táctiles en entornos móviles.