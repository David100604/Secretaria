from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__, static_url_path='/src/css', static_folder='css')

# Configurações do MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Omen157@1013",
    database="db_secretaria"
)

@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/cadastro-aluno', methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        idade = request.form['idade']
        matricula = request.form['matricula']
        turma = request.form['turma']
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO alunos (nome, cpf, idade, matricula, turma) VALUES (%s, %s, %s, %s, %s)", (nome, cpf, idade, matricula, turma))
        db.commit()
        cursor.close()
        
        return redirect(url_for('index'))  # Redireciona para a página inicial após o cadastro

    return render_template('cadastrar-aluno.html')

@app.route('/cadastro-professor', methods=['GET', 'POST'])
def cadastrar_professor():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        matricula = request.form['matricula']
        unidade = request.form['unidade']
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO professores (nome, cpf, matricula, unidadeCurricular) VALUES (%s, %s, %s, %s)", (nome, cpf, matricula, unidade))
        db.commit()
        cursor.close()
        
        return redirect(url_for('index'))  # Redireciona para a página inicial após o cadastro

    return render_template('cadastrar-professor.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/cadastro-turma', methods=['GET', 'POST'])
def cadastrar_turma():
    if request.method == 'POST':
        sala = request.form['sala']
        uc = request.form['uc']
        horario = request.form['horario']
      
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO turmas (sala, unidadeCurricular, horario) VALUES (%s, %s, %s)", (sala, uc, horario))
        db.commit()
        cursor.close()
        
        return redirect(url_for('index'))  # Redireciona para a página inicial após o cadastro

    return render_template('cadastrar-turma.html')




if __name__ == '__main__':
    app.run(debug=True)
