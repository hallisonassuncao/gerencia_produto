class ProdutoView:
    @staticmethod
    def menu():
        print("\n=====MENU DE PRODUTOS=====\n")
        print("1 - Listar produtos")
        print("2 - Cadastrar produto")
        print("3 - Atualizar produto")
        print("4 - Excluir produto")
        print("0 - Sair")
        
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("\nEntrada inválida. Digite um número.\n")
            return -1
        
    @staticmethod
    def listar(produtos):
        if not produtos:
            print("\nNenhum produto cadastrado.\n")
        else:
            print("\n=== Lista de Produtos ===\n")
            for p in produtos:
                print(f"ID: {p[0]} | Nome: {p[1]} | Preço: {p[2]:.2f}")

    
    @staticmethod
    def cadastrar():
        nome = input("Nome do produto: ")
        try:
            preco = float(input("Preço: "))
            return nome, preco
        except Exception as e:
            print("\nValor inválido para preço.\n")
            return None, None

    @staticmethod
    def atualizar():
        try:
            id_produto = int(input("ID do produto a atualizar: "))
            nome = input("Novo nome: ")
            preco = float(input("Novo preço: "))
            return id_produto, nome, preco
        except ValueError:
            print("\nEntrada inválida.\n")
            return None, None, None
        
    @staticmethod
    def excluir():
        try:
            id_produto = int(input("ID do produto a excluir: "))
            return id_produto
        except ValueError:
            print("\nEntrada inválida.\n")
            return None
    
    @staticmethod
    def mensagem(msg):
        print(msg)