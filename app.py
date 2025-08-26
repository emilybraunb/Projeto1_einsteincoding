# gerencia os routs (ou caminhos) do seu site
# Cada rota corresponde a uma página que você verá ao acessar seu site no navegador

# importar flask 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# rota para página inicial
@app.route('/')
def home():
    return render_template('home.html')

# materia 1 - BIOETICA
@app.route('/bioetica', methods=['POST', 'GET'])
def materia1():
    if request.method == 'POST':  # Se o método da requisição for POST (formulário enviado)
        p1 = float(request.form['Prova 1'])  
        p2 = float(request.form['Prova 2'])  
        p3 = float(request.form['Prova 3'])
        tbl1 = float(request.form['TBL 1']) 
        tbl2 = float(request.form['TBL 2'])
        tbl3 = float(request.form['TBL 3'])
        apres = float(request.form['Apresentação'])
        
        # Calcula a média ponderada das notas
        media = (((p1+p2+p3)/3) * 0.5) + (((tbl1+tbl2+tbl3)/3) * 0.2)+(apres*0.3)

        # Retorna a página HTML 'bioetica.html' com a média calculada
        return render_template('bioetica.html', media=media)

    # Se for um GET (página carregada pela primeira vez), apenas renderiza o formulário
    return render_template('materia1.html')

if __name__ == '__main__':
    app.run(debug=True)