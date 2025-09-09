# 🎬 Sistema de Locadora 

## ✅ Funcionalidades

- Cadastro de clientes
- Cadastro de filmes e jogos
- Aluguel e devolução de itens
- Listagem de itens e clientes
- Verificação de disponibilidade

---

## 🧱 Estrutura de Classes

### 🔹 Classe `Item`

Classe base que representa qualquer item da locadora (filme ou jogo).

class Item:
    def __init__(codigo, titulo)
    def alugar()
    def devolver()
Atributos:

codigo: Código único do item

titulo: Nome do item

disponivel: Booleano que indica se o item está disponível

Métodos:

alugar(): Marca o item como alugado (disponivel = False)

devolver(): Marca o item como disponível (disponivel = True)

🎥 Classe Filme (herda de Item)
python
Copiar código
class Filme(Item):
    def __init__(codigo, titulo, genero, duracao)
Atributos adicionais:

genero: Gênero do filme (Ex: Ação, Comédia)

duracao: Duração em minutos

🎮 Classe Jogo (herda de Item)
python
Copiar código
class Jogo(Item):
    def __init__(codigo, titulo, plataforma, faixaEtaria)
Atributos adicionais:

plataforma: Ex: PS5, Xbox

faixaEtaria: Classificação etária (Ex: Livre, 18+)

👤 Classe Cliente
Representa um cliente da locadora.
class Cliente:
    def __init__(nome, cpf)
    def locar(item)
    def devolver(item)
    def listarItens()
Atributos:

nome: Nome do cliente

cpf: CPF do cliente

itensLocados: Lista de itens alugados

Métodos:

locar(item): Aluga um item se estiver disponível

devolver(item): Devolve um item se estiver alugado pelo cliente

listarItens(): Lista os itens atualmente alugados

🏪 Classe Locadora
Gerencia os clientes e itens.
