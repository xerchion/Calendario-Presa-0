
from flask import Flask, render_template, request

from datetime import date
import formularios
turno=""
year=date.today().year

app=Flask(__name__)

#Creamos el index de la app, utilizando templates, en html desde la carpteta templates
@app.route("/", methods=["POST","GET"])
def index():
    nombreUsuario="Invitado"

    datosCalendario=formularios.Datos(request.form)

    if request.method=='POST': #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        print("Soy index y llega por post")
    else:
        print("llega por otra cosa",year,turno)
        #validamos
        
   

    return render_template("index.html",formulario=datosCalendario,year=year,turno=turno,colores="green",nombre=nombreUsuario)

# fin iniciar sesion
if __name__=="__main__":
    app.run(debug=True)





    


