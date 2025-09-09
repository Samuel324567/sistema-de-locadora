🎬 Sistema de Locadora em Python
Este projeto simula uma locadora de filmes e jogos utilizando os princípios da Programação Orientada a Objetos (POO) em Python.

O sistema permite:
✅ Cadastro de clientes
✅ Cadastro de itens (filmes e jogos)
✅ Aluguel de itens
✅ Devolução de itens
✅ Listagem de clientes e itens cadastrados

📂 Estrutura de Classes
🔹 Classe Item (Base)
class Item:
    def __init__(self, codigo, titulo):
        self.codigo = codigo
        self.titulo = titulo
        self.disponivel = True

    def alugar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True
Atributos:

codigo: Código identificador do item

titulo: Título do item

disponivel: Booleano que indica se o item está disponível

Métodos:

alugar(): Define disponivel = False

devolver(): Define disponivel = True

🎥 Classe Filme (Herda de Item)
class Filme(Item):
    def __init__(self, codigo, titulo, genero, duracao):
        super().__init__(codigo, titulo)
        self.genero = genero
        self.duracao = duracao
Atributos adicionais:

genero: Gênero do filme (ex: Ação, Comédia)

duracao: Duração em minutos

🎮 Classe Jogo (Herda de Item)
class Jogo(Item):
    def __init__(self, codigo, titulo, plataforma, faixaEtaria):
        super().__init__(codigo, titulo)
        self.plataforma = plataforma
        self.faixaEtaria = faixaEtaria
Atributos adicionais:

plataforma: Plataforma (ex: PS5, Xbox)

faixaEtaria: Idade mínima recomendada

👤 Classe Cliente
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.itensLocados = []

    def locar(self, item):
        if item.disponivel:
            item.alugar()
            self.itensLocados.append(item)
            print(self.nome, "locou", item.titulo)
        else:
            print(item.titulo, "não está disponível")

    def devolver(self, item):
        if item in self.itensLocados:
            item.devolver()
            self.itensLocados.remove(item)
            print(self.nome, "devolveu", item.titulo)
        else:
            print(self.nome, "não tem esse item alugado")

    def listarItens(self):
        if len(self.itensLocados) == 0:
            print(self.nome, "não tem itens alugados")
        else:
            print("Itens alugados por", self.nome + ":")
            for item in self.itensLocados:
                print("-", item.titulo)
Atributos:

nome: Nome do cliente

cpf: CPF do cliente

itensLocados: Lista dos itens alugados

Métodos:

locar(item): Aluga um item se disponível

devolver(item): Devolve um item alugado

listarItens(): Mostra todos os itens alugados

🏢 Classe Locadora
class Locadora:
    def __init__(self):
        self.clientes = []
        self.itens = []

    def cadastrarCliente(self, cliente):
        self.clientes.append(cliente)
        print("Cliente cadastrado:", cliente.nome)

    def cadastrarItem(self, item):
        self.itens.append(item)
        print("Item cadastrado:", item.titulo)

    def listarClientes(self):
        print("Clientes cadastrados:")
        for c in self.clientes:
            print("-", c.nome)

    def listarItens(self):
        print("Itens cadastrados:")
        for i in self.itens:
            status = "Disponível" if i.disponivel else "Alugado"
            print("-", i.titulo, "(", status, ")")
Atributos:

clientes: Lista de clientes cadastrados

itens: Lista de itens cadastrados (filmes e jogos)

Métodos:

cadastrarCliente(cliente): Adiciona um cliente

cadastrarItem(item): Adiciona um item

listarClientes(): Lista os clientes

listarItens(): Lista os itens e mostra se estão disponíveis ou alugados

