def salvar_informacoes_do_animal(nome, idade, peso, altura, imc):
    with open("informacoes_do_animal.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Idade: {idade} anos\n")
        arquivo.write(f"Peso: {peso} kg\n")
        arquivo.write(f"Altura: {altura} cm\n")
        arquivo.write(f"IMC: {imc:.2f}\n")
        arquivo.write("-----------------------\n")
        arquivo.write("\n")

def calcular_imc_do_animal(peso, altura):

    """
    Calcula o IMC (índice de Massa Corporal) de um animal com base em seu peso e altura.

    :param peso: Peso do animal, em kg
    :param altura: Altura do animal, em cm
    :return: IMC do animal
    """

    imc = peso / (altura ** 2)
    return imc

# Função para coletar informações sobre o pet
def coletar_informacoes_pet():
    """
    Coleta informações sobre o pet do usuário, incluindo o nome, idade, peso e altura, e calcula o IMC do pet.

    :return: Nenhum valor é retornado. As informações do pet são exibidas na tela.
    """
    print("Por favor, insira as informações sobre seu pet.")

    # Coleta do nome do pet
    nome = input("Nome do pet: ")

    # Coleta da idade do pet, garantindo que seja um número inteiro
    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    # Coleta do peso do pet, garantindo que seja um número flutuante
    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

    # Coleta da altura do pet, garantindo que seja um número flutuante
    while True:
        try:
            altura = float(input("Altura do pet (em cm): "))
            if altura < 0:
                print("A altura não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a altura.")

    # Calcula o IMC do pet  
    imc = calcular_imc_do_animal(peso, altura)
    

    # Exibindo as informações coletadas
    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} cm")
    print(f"IMC do pet: {imc:.2f}")

    salvar_informacoes_do_animal(nome, idade, peso, altura, imc)

# Chama a função para coletar e exibir as informações do pet
def main():
    while True:
        coletar_informacoes_pet()
        resposta = input("\nDeseja continuar? (s/n): ")
        if resposta.lower() != "s":
            break

if __name__ == "__main__":
    main()
