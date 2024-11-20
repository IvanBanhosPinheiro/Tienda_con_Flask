from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


def paginaNoEncontrada(error):
    return render_template("errores/404.html"), 404

def inicializarApp(config):
    app.config.from_object(config)
    #Cuando salte el error 404 nos mandara a esta pagina 
    app.register_error_handler(404, paginaNoEncontrada)
    return app