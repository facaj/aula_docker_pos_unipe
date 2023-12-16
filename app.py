from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', professor='Aécio Pires', curso='Desenvolvimento Full Stack', instituicao='Unipê', aluno='Francisco Albuquerque')

if __name__ == '__main__':
    app.run(debug=True)
