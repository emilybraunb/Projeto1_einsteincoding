# importar flask 
from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para página inicial
@app.route('/')
def home():
    return render_template('home.html')

# Matéria 1 - Bioética
@app.route('/bioetica', methods=['POST', 'GET'])
def bioetica():
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
    return render_template('bioetica.html')

# Matéria 2 - Biomateriais
@app.route('/biomateriais', methods=['POST', 'GET'])
def biomateriais():
    if request.method == 'POST':  # Se o método da requisição for POST (formulário enviado)
        p1 = float(request.form['Prova 1'])  
        p2 = float(request.form['Prova 2'])  
        tbl1 = float(request.form['TBL 1']) 
        tbl2 = float(request.form['TBL 2'])
        lab = float(request.form['Apresentação'])
        eng = float(request.form['Engajamento'])

        media = (p1 * 0.25) +(p2 * 0.35)+ (((tbl1+tbl2)/2) * 0.15)+(lab*0.15)+(eng*0.1)

        return render_template('biomateriais.html', media=media)

    return render_template('biomateriais.html')

# Matéria 3 - Sistema Digestório 
@app.route('/digestorio', methods=['POST', 'GET'])
def digestorio():
    if request.method == 'POST':  # Se o método da requisição for POST (formulário enviado)
        p1 = float(request.form['Prova 1'])  
        p2 = float(request.form['Prova 2']) 
        p3 = float(request.form['Prova 3'])
        tbl1 = float(request.form['TBL 1']) 
        tbl2 = float(request.form['TBL 2'])
        tbl3 = float(request.form['TBL 3'])
        tbl4 = float(request.form['TBL 4'])
        tbl5 = float(request.form['TBL 5'])

        media = (((p1+p2+p3)/3) * 0.7) + (((tbl1+tbl2+tbl3+tbl4+tbl5)/5) * 0.3)

        return render_template('digestorio.html', media=media)

    return render_template('digestorio.html')

# Materia 4 - Física Médica
@app.route('/fisica', methods=['POST', 'GET'])
def fisica():
    if request.method == 'POST':  # Se o método da requisição for POST (formulário enviado)
        p1 = float(request.form['Prova 1'])  
        p2 = float(request.form['Prova 2']) 
        tbl1 = float(request.form['TBL 1']) 
        tbl2 = float(request.form['TBL 2'])
        seminario = float(request.form['Seminário'])
        aula = float(request.form['Atividade em aula'])

        media = (p1*0.3)+(p2*0.3) + (((tbl1+tbl2)/2) * 0.1) + (seminario * 0.25) + (aula * 0.05)

        return render_template('fisica.html', media=media)

    return render_template('fisica.html')

# Materia 5 - Modelagem
@app.route('/modelagem', methods=['POST', 'GET'])
def modelagem():
    if request.method == 'POST':  # Se o método da requisição for POST (formulário enviado)
        p1 = float(request.form['Prova 1'])  
        p2 = float(request.form['Prova 2']) 
        tbl1 = float(request.form['TBL 1']) 
        tbl2 = float(request.form['TBL 2'])
        tbl3 = float(request.form['TBL 3'])
        projeto = float(request.form['Projeto final'])

        media = (((p1+p2)/2)*0.6) + (((tbl1+tbl2+tbl3)/3) * 0.15) + (projeto * 0.25)

        return render_template('modelagem.html', media=media)

    return render_template('modelagem.html')

# Materia 6 - Sistemas Digitais
@app.route('/sistemas', methods=['POST', 'GET'])
def sistemas():
    if request.method == 'POST':  # Se o método da requisição for POST (formulário enviado)
        p1 = float(request.form['Prova 1'])  
        p2 = float(request.form['Prova 2']) 
        tbl1 = float(request.form['TBL 1']) 
        tbl2 = float(request.form['TBL 2'])
        tbl3 = float(request.form['TBL 3'])
        quiz = float(request.form['Quiz de abertura'])
        pbl = float(request.form['PBL'])

        media = (((p1+p2)/2)*0.5) + (((tbl1+tbl2+tbl3)/3) * 0.15) + (quiz * 0.1) + (pbl * 0.25)

        return render_template('sistemas.html', media=media)

    return render_template('sistemas.html')


if __name__ == '__main__':
    app.run(debug=True)