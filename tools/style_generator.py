# tools/style_generator.py
import json
import os

# Configuración del sistema de diseño basado en la escala de 8px
CONFIG_SISTEMA = {
    "spacing": {
        "xs": "4px",
        "sm": "8px",
        "md": "16px",
        "lg": "24px",
        "xl": "32px",
        "xxl": "48px"
    }
}


def generar_utilerias_css():
    spacing = CONFIG_SISTEMA["spacing"]

    css_content = "/* =========================================================================\n"
    css_content += "   CLASES UTILLITARIAS ATÓMICAS - GENERADAS AUTOMÁTICAMENTE POR PYTHON\n"
    css_content += "   ========================================================================= */\n\n"

    # Generación iterativa de paddings y margins con !important para garantizar la atomicidad
    for clave, valor in spacing.items():
        css_content += f"/* Escala {clave} ({valor}) */\n"
        css_content += f".p-{clave} {{ padding: {valor} !important; }}\n"
        css_content += f".p-x-{clave} {{ padding-left: {valor} !important; padding-right: {valor} !important; }}\n"
        css_content += f".p-y-{clave} {{ padding-top: {valor} !important; padding-bottom: {valor} !important; }}\n"
        css_content += f".m-b-{clave} {{ margin-bottom: {valor} !important; }}\n\n"

    # Asegurar que la ruta exista antes de guardar
    ruta_destino = os.path.join("static", "css", "generated_utilities.css")
    os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)

    with open(ruta_destino, "w", encoding="utf-8") as archivo:
        archivo.write(css_content)

    print("🐍 [Python Style Generator]: 'generated_utilities.css' generado exitosamente en static/css/")


if __name__ == "__main__":
    generar_utilerias_css()