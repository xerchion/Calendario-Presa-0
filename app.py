
from flask import Flask,render_template

app=Flask(__name__)

#Creamos el index de la app, utilizando templates, en html desde la carpteta templates
@app.route("/")
def index():

    return "hola"
# fin iniciar sesion
if __name__=="__main__":
    app.run(debug=True)





    


