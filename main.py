from flask import Flask, request, render_template
from rotas import obter_rota_acessivel

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    solution = None
    if request.method == 'POST':

      origem  = request.form.get('origem')
      destino  = request.form.get('destino')
       
      solution = obter_rota_acessivel(origem, destino)
      solution = [step["html_instructions"] for step in solution["legs"][0]["steps"]]

      return render_template('index.html', solution=solution)
    else:
        return render_template('index.html', solution=solution)
if __name__ == '__main__':
    app.run(debug=True)

# Exemplo de uso
# origem = "rua joão luis vives 42, São Paulo"
# destino = "Av. da Liberdade 532, São Paulo"