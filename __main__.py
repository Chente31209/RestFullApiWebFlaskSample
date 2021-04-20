from flask import Flask 
from DataBaseService import Libros 

app = Flask(__name__)

@app.route("/")
def GetLibros():
    return {"api/Libros/get":"Para Obtener los una lista de Libros ",
    "api/Libros/get{ id}":"Para Obtener los un libro por su id ",
    "api/Libros/post":"Para Reguistar Un libro en la  Lista de Libros  "}

if (__name__=="__main__"):
    app.run(debug= True)