from flask import Flask, render_template

app = Flask("Hello")

@app.route("/")
def usuario():
    usuario = [1, "Raiane Caroline ", "Aluna"]
    alunos = ["Emanoel", "Elvis", "Fernando", "Raiane"]
    return render_template("index.html", usuario=usuario, alunos=alunos)

@app.route("/contatos")
def contato():
    nomeAula = "Aula python para Web"
    return render_template("index.html", nome=nomeAula)
