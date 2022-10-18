
from flask import Flask,render_template

app=Flask(__name__)

#Creamos el index de la app, utilizando templates, en html desde la carpteta templates
@app.route("/", methods=["POST"])
def index():
    nombreUsuario="Invitado"

    

        #validamos
        
   

    return render_template("index.html",,year=2022,turno="C",colores="green",nombre="invitado")
# fin iniciar sesion
if __name__=="__main__":
    app.run(debug=True)





    


