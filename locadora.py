class Item:
    def __init__(self, codigo, titulo):
        self.codigo = codigo
        self.titulo = titulo
        self.disponivel = True

    def alugar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True


class Filme(Item):
    def __init__(self, codigo, titulo, genero, duracao):
        super().__init__(codigo, titulo)
        self.genero = genero
        self.duracao = duracao


class Jogo(Item):
    def __init__(self, codigo, titulo, plataforma, faixa_etaria):
        super().__init__(codigo, titulo)
        self.plataforma = plataforma
        self.faixa_etaria = faixa_etaria


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.itens = []

    def locar(self, item):
        if item.disponivel:
            item.alugar()
            self.itens.append(item)
            print(f"{self.nome} locou {item.titulo}")
        else:
            print(f"{item.titulo} não está disponível")

    def devolver(self, item):
        if item in self.itens:
            item.devolver()
            self.itens.remove(item)
            print(f"{self.nome} devolveu {item.titulo}")
        else:
            print(f"{self.nome} Não tem esse item")

    def listar_itens(self):
        if not self.itens:
            print(f"{self.nome} Não tem itens alugados")
        else:
            print(f"Itens alugados por {self.nome}:")
            for item in self.itens:
                print("-", item.titulo)


class Locadora:
    def __init__(self):
        self.clientes = []
        self.itens = []

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente cadastrado: {cliente.nome}")

    def cadastrar_item(self, item):
        self.itens.append(item)
        print(f"Item cadastrado: {item.titulo}")

    def listar_clientes(self):
        print("Clientes cadastrados:")
        for c in self.clientes:
            print("-", c.nome)

    def listar_itens(self):
        print("Itens cadastrados:")
        for i in self.itens:
            status = "Disponível" if i.disponivel else "Alugado"
            print(f"- {i.titulo} ({status})")
