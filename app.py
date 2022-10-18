
from flask import Flask, render_template, request, redirect, session, url_for,flash

from datetime import date


import calendarioReal
import Usuarios
import gestionBD
import time

import formularios


usuario=Usuarios.Usuario()


turno=""





year=date.today().year

colores={"A":"bg-success", "B":"bg-primary", "C":"bg-danger" ,"D":"bg-warning" ,"E":"bg-warning bg-opacity-50" }
coloresdias={"N": "bg-secondary","T":"bg-warning" ,"M":"bg-info" } #Mañana tarde noche
nombreUsuarioActivo="Invitado"


# Con esta linea creamos la instancia de la clase Flask a nuestro objeto llamado app que será
#la aplicación en si.
app=Flask(__name__)

#Creamos el index de la app, utilizando templates, en html desde la carpteta templates
@app.route("/", methods=["POST","GET"])
def index():




    
    nombreUsuario="Invitado"

    datosCalendario=formularios.Datos(request.form)

    if request.method=='POST': #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        print("Soy index y llega por post")
    else:
        print("llega por otra cosa",year,turno,nombreUsuarioActivo)
        #validamos
        
   

    return render_template("index.html",formulario=datosCalendario,year=year,turno=turno,colores=colores,nombre=nombreUsuario)














# fin iniciar sesion
if __name__=="__main__":
    app.run(debug=False)





    


