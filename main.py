class AnimalEstimacao:
    def __init__(self, nome, raca, idade, responsavel, telefone):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.responsavel = responsavel
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}\nRaça: {self.raca}\nIdade: {self.idade}\nResponsável: {self.responsavel}\nTelefone: {self.telefone}"

def cadastrar_animal():
    nome = input("Digite o nome do animal: ")
    raca = input("Digite a raça do animal: ")
    idade = input("Digite a idade do animal: ")
    responsavel = input("Digite o nome do responsável: ")
    telefone = input("Digite o telefone do responsável: ")

    # Criando um objeto AnimalEstimacao com os dados inseridos
    animal = AnimalEstimacao(nome, raca, idade, responsavel, telefone)

    return animal

# Exemplo de uso:
animal_cadastrado = cadastrar_animal()
print("\nCadastro do Animal de Estimação:")
print(animal_cadastrado)
