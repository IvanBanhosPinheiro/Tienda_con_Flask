from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
import mysql.connector

app = Flask(__name__)
csrf = CSRFProtect()

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DATABASE'] = 'tiendaflask'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abc123.'

db = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    database=app.config['MYSQL_DATABASE'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD']
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    # print(request.method)
    # print(request.form['usuario'])
    # print(request.form['password'])
    #CSRF (Cross.site Request Forgery): solicitud de falsificacion entre sitios.
    if request.method == 'POST':
        if request.form['usuario'] == "admin" and request.form['password'] == "1234":
            return redirect(url_for('index'))
        else:
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")

def paginaNoEncontrada(error):
    return render_template("errores/404.html"), 404


@app.route("/libros")
def listarLibros():
    try:
        cursor = db.cursor()
        sql="""select lib.isbn, lib.titulo, lib.anoedicion , lib.precio, a.nombres, a.apellidos
        from libro as lib  join autor as a on lib.autor = a.id
        order by titulo asc"""
        cursor.execute(sql)
        data = cursor.fetchall()
        data = {
            "libros":data
        }
        return render_template('listadoLibros.html', data=data)
    except Exception as ex:
        raise Exception(ex)

def inicializarApp(config):
    app.config.from_object(config)
    #Iniciar la proteccion contra logs de otros lados
    csrf.init_app(app)
    #Cuando salte el error 404 nos mandara a esta pagina 
    app.register_error_handler(404, paginaNoEncontrada)
    return app