from flask import Flask, request, render_template_string

app = Flask(__name__)
##
# Função para salvar as informações do pet em um arquivo de texto
def salvar_informacoes_do_animal(nome, idade, peso, altura, imc):
    with open("informacoes_do_animal.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Idade: {idade} anos\n")
        arquivo.write(f"Peso: {peso} kg\n")
        arquivo.write(f"Altura: {altura} cm\n")
        arquivo.write(f"IMC: {imc:.2f}\n")
        arquivo.write("-----------------------\n")
        arquivo.write("\n")

# Função para calcular o IMC do animal
def calcular_imc_do_animal(peso, altura):
    imc = peso / ((altura/100) ** 2)
    return imc

# Página inicial para inserir informações do pet
@app.route('/', methods=['GET', 'POST'])
def coletar_informacoes_pet():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = int(request.form['idade'])
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        
        # Calcula o IMC do pet
        imc = calcular_imc_do_animal(peso, altura)

        # Salva as informações no arquivo
        salvar_informacoes_do_animal(nome, idade, peso, altura, imc)

        return f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: 'Arial', sans-serif; /* Define a fonte como Arial */
                }}
            </style>
        </head>
        <body>
            <h2>Informações do Pet:</h2>
            <p>Nome: {nome}</p>
            <p>Idade: {idade} anos</p>
            <p>Peso: {peso} kg</p>
            <p>Altura: {altura} cm</p>
            <p>IMC do pet: {imc:.2f}</p>
            <a href="/">Inserir outro pet</a>
        </body>
        </html>
        """

    # Exibe o formulário para inserir informações do pet
    formulario_html = """
    <html>
        <head>
            <style>
                body {
                    font-family: 'Arial', sans-serif
                    background-color: #6a5acd; /* Define a cor de fundo azul petróleo */
                }

                .center {
                    font-family: 'Verdana', sans-serif;
                    text-align: center;
                    font-size: 40px;
                    color: white; /* Define a cor do texto como branco */
                    margin-top: 10vh; /* Centraliza verticalmente usando margem superior */
                    transform: translateY(-10%); /* Ajusta a posição verticalmente */
                }

                h2 {
                font-family: 'Verdana', sans-serif; /* Diferente fonte para o título */
            }
                form {
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                input[type="text"], input[type="number"] {
                    width: 100%;
                    padding: 10px;
                    margin: 8px 0;
                    box-sizing: border-box;
                    border: 2px solid #ccc;
                    border-radius: 4px;
                }
                input[type="submit"] {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <h2>Insira as informações do seu pet</h2>
            <form method="POST">
                Nome: <input type="text" name="nome" required><br><br>
                Idade (em anos): <input type="number" name="idade" required><br><br>
                Peso (em kg): <input type="number" step="0.01" name="peso" required><br><br>
                Altura (em cm): <input type="number" step="0.01" name="altura" required><br><br>
                <input type="submit" value="Enviar">
            </form>
        </body>
    </html>
    """
    return render_template_string(formulario_html)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

