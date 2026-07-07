# app.py
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def dashboard():
    # Simulación de datos provenientes de una base de datos (Python SSR)
    # Cambia el valor a True o False para probar cómo responde Jinja2 dinámicamente
    mostrar_datos = True

    transacciones_mock = [
        {"id": "TX-1004", "cliente": "Taller Mecánico Automotriz Alfa", "monto": "$4,500.00"},
        {"id": "TX-1005", "cliente": "Distribuidora de Muelles del Sureste", "monto": "$12,850.00"},
        {"id": "TX-1006", "cliente": "Servicios Logísticos Monterrey", "monto": "$8,200.00"},
        {"id": "TX-1007", "cliente": "Refaccionaria El Camión", "monto": "$1,950.00"}
    ]

    # Si pones ?vacio=true en la URL (http://127.0.0.1:5000/?vacio=true), simulará un estado sin datos
    if request.args.get('vacio') == 'true':
        transacciones = []
    else:
        transacciones = transacciones_mock if mostrar_datos else []

    return render_template('dashboard_fixed.html', transacciones=transacciones)


if __name__ == '__main__':
    print("🚀 Servidor corriendo en http://127.0.0.1:5000")
    print("💡 Para probar el estado vacío entra a: http://127.0.0.1:5000/?vacio=true")
    app.run(debug=True)