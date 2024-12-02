from flask import Flask

app_Jennifer = Flask(__name__ , template_folder='templates')

@app_Jennifer.route('/')
@app_Jennifer.route('/rota1') 
def rota1():
    return 'Olá, tudo bem? (ESSA É A ROTA 1!)'

@app_Jennifer.route('/rota2') 
def rota2():
    resposta = "<H3>OLÁ. Essa é outra página da rota 2 <H3>"
    return resposta

if __name__ == "__main__":
    app_Jennifer.run(port = 8000)