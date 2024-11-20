from app import inicializarApp
from config import config

configuracion = config["development"]
app = inicializarApp(configuracion)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)  # O quita debug si no quieres el modo depuración
    
#Se llama con python manage.py run