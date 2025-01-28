from flask import Flask
#flask associa funzioni ad URL in forma abbreviata

app = Flask(__name__) # web app

@app.route('/')
def index():
    return "Ciao!"

@app.route("/pagina/")
def index2():
    return "pagina!"


# vengono eseguite quando avviene una get sulla pagina
if __name__ == '__main__':
    app.run(debug=True, host="localhost") #debug = true per caricare in automatico le modifiche sul web server
    
# nomi cartelle obbligatori: 
# static <-- oggetti statici come css database o immagini
# templates <-- codici html

# app.render_template("index.html") <-- su quel url carica la pagina html

#URL dinamica
"""
@app.route("/hello/<name>")
def hello(name):
    return app.render_template("page.html", name=name)
"""