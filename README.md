# El Arquitecto del Espacio Negativo - Dashboard Analítico

Este proyecto forma parte de la fase final del módulo **"Gestión de geometría y diseño de layouts"** dentro de la certificación en Desarrollo de Software. Consiste en la reestructuración y optimización de una interfaz analítica utilizando renderizado en el servidor (Python SSR) con un enfoque sistémico del espacio, alineación y accesibilidad.

## Características del Proyecto
- **Sistema de Diseño Basado en Múltiplos de 8px:** Escalabilidad tipográfica y espacial armónica.
- **Reset Universal Box Model:** Migración de `content-box` a `border-box` para eliminar desbordamientos horizontales.
- **Estructura Avanzada Grid & Flexbox:** Uso estratégico de `gap` para erradicar el colapso de márgenes verticales.
- **Automatización de Estilos:** Script en Python que autogenera clases utilitarias CSS mediante la lectura de un archivo de configuración JSON.
- **Control Lógico-Visual SSR (Jinja2):** Lógica condicional en plantillas para renderizar estados vacíos con paddings maximizados y componentes de interacción accesibles (WCAG target de 44px).

## Estructura del Repositorio
- `/static/css/`: Hojas de estilos del sistema, componentes y utilerías generadas.
- `/templates/`: Vistas dinámicas del servidor (diseño corregido y respaldo del diseño legacy).
- `/tools/`: Script automatizador de estilos `style_generator.py`.
- `/evidencias/`: Capturas de pantalla técnicas con auditorías de DevTools.
- `DIAGNOSTICO.md`: Informe técnico detallado sobre la autopsia visual del layout original.
- `DECISIONES.md`: Registro formal y justificación UX/Gestalt del sistema de espaciado.

## Instalación y Ejecución

1. Asegúrate de tener un entorno virtual activo y las dependencias instaladas:
   ```bash
   pip install -r requirements.txt