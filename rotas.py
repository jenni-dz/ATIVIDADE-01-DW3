from flask import Flask, render_template

app_Jennifer = Flask(__name__ , template_folder='templates')

@app_Jennifer.route('/')
@app_Jennifer.route('/rota1') 
def rota1():
    return 'Olá, tudo bem? (ESSA É A ROTA 1!)'

@app_Jennifer.route('/rota2') 
def rota2():
    resposta = "<H3>OLÁ. Essa é outra página da rota 2 <H3>"
    return resposta

@app_Jennifer.route("/homepage")
def homepage():          
    return render_template ("homepage.html")

@app_Jennifer.route("/index")  
def indice():
    return render_template ("index.html") #optei por prefixar com t_ os nomes dos arquivos que usam template

@app_Jennifer.route("/contato")
def contato():
    return render_template("contato.html") 

@app_Jennifer.route("/usuario")
def dados_usuario():
    nome_usuario="Jennifer"
    dados_usu = {"profissao": "Estagiária", "graduacao":"Sistemas para Internet"}
    return render_template("usuario.html", nome = nome_usuario, dados = dados_usu)

@app_Jennifer.route("/usuario/<nome_usuario>;<nome_profissao>;<nome_graduacao>") 
def usuario (nome_usuario, nome_profissao, nome_graduacao):
    dados_usu = {"profissao": nome_profissao, "graduacao": nome_graduacao}
    return render_template ("usuario.html", nome=nome_usuario, dados = dados_usu)   

if __name__ == "__main__":
    app_Jennifer.run(port = 8000)
