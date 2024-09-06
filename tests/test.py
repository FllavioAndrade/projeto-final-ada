import pytest
from app.info_pet import app, calcular_imc_do_animal, salvar_informacoes_do_animal
import os
import unittest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestInfoPet(unittest.TestCase):

    def test_calcular_imc_do_animal(self):
        """Testa a função de cálculo do IMC"""
        peso = 10.0  # kg
        altura = 50.0  # cm
        imc = calcular_imc_do_animal(peso, altura)
        self.assertAlmostEqual(imc, 4.0, places=2)

    def test_salvar_informacoes_do_animal(self):
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
            self.assertIn("Nome: Rex", conteudo)
            self.assertIn("Idade: 5 anos", conteudo)
            self.assertIn("Peso: 10.0 kg", conteudo)
            self.assertIn("Altura: 50.0 cm", conteudo)
            self.assertIn("IMC: 4.00", conteudo)

    def test_coletar_informacoes_pet_get(self):
        """Testa a rota GET /"""
        with app.test_client() as client:
            rv = client.get('/')
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'Insira as informa\xc3\xa7\xc3\xb5es do seu pet', rv.data)

    def test_coletar_informacoes_pet_post(self):
        """Testa a rota POST /"""
        with app.test_client() as client:
            rv = client.post('/', data={
                'nome': 'Rex',
                'idade': '5',
                'peso': '10.0',
                'altura': '50.0'
            })
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'Nome: Rex', rv.data)
            self.assertIn(b'Idade: 5 anos', rv.data)
            self.assertIn(b'Peso: 10.0 kg', rv.data)
            self.assertIn(b'Altura: 50.0 cm', rv.data)
            self.assertIn(b'IMC do pet: 4.00', rv.data)

if __name__ == '__main__':
    unittest.main()