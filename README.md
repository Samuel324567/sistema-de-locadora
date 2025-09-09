# 🎬 Sistema de Locadora

Sistema simples para gerenciamento de uma locadora de filmes e jogos.

## ✅ Funcionalidades

Cadastro de clientes

Cadastro de filmes e jogos

Aluguel e devolução de itens

Listagem de itens e clientes

Verificação de disponibilidade

🧱 Estrutura de Classes
🔹 Classe Item

Classe base que representa qualquer item da locadora (filme ou jogo).

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

codigo: Código único do item

titulo: Nome do item

disponivel: Booleano que indica se o item está disponível

Métodos:

alugar(): Marca o item como alugado (disponivel = False)

devolver(): Marca o item como disponível (disponivel = True)

## 🎥 Classe Filme (herda de Item)
class Filme(Item):
    def __init__(self, codigo, titulo, genero, duracao):
        super().__init__(codigo, titulo)
        self.genero = genero
        self.duracao = duracao


Atributos adicionais:

genero: Gênero do filme (Ex: Ação, Comédia)

duracao: Duração em minutos

## 🎮 Classe Jogo (herda de Item)
class Jogo(Item):
    def __init__(self, codigo, titulo, plataforma, faixaEtaria):
        super().__init__(codigo, titulo)
        self.plataforma = plataforma
        self.faixaEtaria = faixaEtaria


Atributos adicionais:

plataforma: Plataforma (Ex: PS5, Xbox)

faixaEtaria: Classificação etária (Ex: Livre, 18+)

## 👤 Classe Cliente

Representa um cliente da locadora.

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.itensLocados = []

    def locar(self, item):
        if item.disponivel:
            item.alugar()
            self.itensLocados.append(item)

    def devolver(self, item):
        if item in self.itensLocados:
            item.devolver()
            self.itensLocados.remove(item)

    def listarItens(self):
        return self.itensLocados


Atributos:

nome: Nome do cliente

cpf: CPF do cliente

itensLocados: Lista de itens atualmente alugados

Métodos:

locar(item): Aluga um item se estiver disponível

devolver(item): Devolve um item se estiver alugado pelo cliente

listarItens(): Lista os itens alugados pelo cliente

## 🏪 Classe Locadora

Gerencia os clientes e itens.

class Locadora:
    def __init__(self):
        self.clientes = []
        self.itens = []

    def adicionarCliente(self, cliente):
        self.clientes.append(cliente)

    def adicionarItem(self, item):
        self.itens.append(item)

    def listarClientes(self):
        return self.clientes

    def listarItens(self):
        return self.itens

    def verificarDisponibilidade(self, codigo):
        for item in self.itens:
            if item.codigo == codigo:
                return item.disponivel
        return None


Atributos:

clientes: Lista de clientes cadastrados

itens: Lista de itens cadastrados

Métodos:

adicionarCliente(cliente): Adiciona um novo cliente

adicionarItem(item): Adiciona um novo item (filme ou jogo)

listarClientes(): Retorna a lista de clientes

listarItens(): Retorna a lista de itens

verificarDisponibilidade(codigo): Verifica se um item está disponível a partir do seu código
