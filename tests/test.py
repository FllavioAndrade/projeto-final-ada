import pytest
from app.info_pet import app, calcular_imc_do_animal, salvar_informacoes_do_animal
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calcular_imc_do_animal():
    """Testa a função de cálculo do IMC"""
    peso = 10.0  # kg
    altura = 50.0  # cm
    imc = calcular_imc_do_animal(peso, altura)
    assert imc == pytest.approx(4.0, 0.01)

def test_salvar_informacoes_do_animal():
    """Testa a função de salvamento das informações do animal"""
    nome = "Rex"
    idade = 5
    peso = 10.0
    altura = 50.0
    imc = calcular_imc_do_animal(peso, altura)
    
    # Remove o arquivo se ele já existir
    if os.path.exists("informacoes_do_animal.txt"):
        os.remove("informacoes_do_animal.txt")
    
    salvar_informacoes_do_animal(nome, idade, peso, altura, imc)
    
    # Verifica se o arquivo foi criado e contém as informações corretas
    with open("informacoes_do_animal.txt", "r") as arquivo:
        conteudo = arquivo.read()
        assert "Nome: Rex" in conteudo
        assert "Idade: 5 anos" in conteudo
        assert "Peso: 10.0 kg" in conteudo
        assert "Altura: 50.0 cm" in conteudo
        assert "IMC: 4.00" in conteudo

def test_coletar_informacoes_pet_get(client):
    """Testa a rota GET /"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Insira as informa\xc3\xa7\xc3\xb5es do seu pet' in rv.data

def test_coletar_informacoes_pet_post(client):
    """Testa a rota POST /"""
    rv = client.post('/', data={
        'nome': 'Rex',
        'idade': '5',
        'peso': '10.0',
        'altura': '50.0'
    })
    assert rv.status_code == 200
    assert b'Nome: Rex' in rv.data
    assert b'Idade: 5 anos' in rv.data
    assert b'Peso: 10.0 kg' in rv.data
    assert b'Altura: 50.0 cm' in rv.data
    assert b'IMC do pet: 4.00' in rv.data
