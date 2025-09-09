class Item:
    def __init__(self, codigo, titulo):
        self.codigo = codigo
        self.titulo = titulo
        self.disponivel = True

    def alugar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

#-----------------------------------------------------------------------------------------
class Filme(Item):
    def __init__(self, codigo, titulo, genero, duracao):
        super().__init__(codigo, titulo)
        self.genero = genero
        self.duracao = duracao

#--------------------------------------------------------------------------------------------
class Jogo(Item):
    def __init__(self, codigo, titulo, plataforma, faixaEtaria):
        super().__init__(codigo, titulo)
        self.plataforma = plataforma
        self.faixaEtaria = faixaEtaria

#-------------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------------------
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
