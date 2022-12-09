from flask import Flask,render_template,url_for,redirect,request,jsonify,Response
from config import config
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from cliente import Cliente
from gevent.pywsgi import WSGIServer




app=Flask(__name__)



client = MongoClient("mongodb+srv://SantiagoVela:millos2011@cluster0.y1njt.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('avanzo')

records=db.db_ava







usuario_ingresado=[]



@app.route('/' )
def index():
    return redirect(url_for('login'))



@app.route("/login", methods=["GET", 'POST'])
def login():

    centinela=False
    if request.method == 'POST':

        if len(usuario_ingresado)>0:
            for i in range(len(usuario_ingresado)):
                usuario_ingresado.pop()

        user=request.form['username']
        passs =request.form['password']

        user_log=records.find_one({'name': user})


        contra=user_log["contrasena"]


        if   check_password_hash( contra,passs) :

            print("perrrrrrrrraaaaaaaaa")
            
            usuario_ingresado.append(user_log["name"])

            return agregarusuario(user_log["name"])




        elif check_password_hash(contra, passs):

            usuario_ingresado.append(user_log["nombre"])

            return agregarusuario(user_log["nombre"])

    else:
        return render_template("signup_form.html")



@app.route('/creacion',methods=['POST'] )
def prueba() :

    nombre=request.form['nombre']
    apellido = request.form['apellido']
    contrasena=request.form['contrasena']
    empresa=request.form['empresa']
    deuda="$0"


    if  nombre and apellido  and empresa and contrasena :

        contra=generate_password_hash(contrasena)
        product = Cliente(nombre, apellido,empresa,contra,deuda )
        records.insert_one(product.toDBCollection())
       
    
        return redirect(url_for('crudUsuarios')) 
    else:
        return NOT_FOUND()





@app.route('/agregar', methods=["GET", 'POST'])
def agregarusuario(nombre):


    return render_template('main.html',data=nombre)





@app.route('/reporte' ,methods=["GET", 'POST'])
def report() :
    listain=list(records.find())
    return render_template('listametas.html',listaa=listain)








@app.route('/creacion-usuarios')
def crudUsuarios():

    return render_template('prueba2.html')



@app.route('/crud-lista')
def crudInactivos():
    listain=list(records.find())
    return render_template('usuarioin.html',listaa=listain)




@app.route('/fix')
def crudInat():
    return render_template('calendario.html')






if __name__=='__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
