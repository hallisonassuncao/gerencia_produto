from model.produto_model import ProdutoModel
from view.produto_view import ProdutoView

class ProdutoController:
    def __init__(self):
        self.model = ProdutoModel()
        self.view = ProdutoView()

    def executar(self):
        while True:
            opcao = self.view.menu()
            
            if opcao == 1:
                produtos = self.model.listar()
                self.view.listar(produtos)
            
            elif opcao == 2:
                nome, preco = self.view.cadastrar()
                if nome and preco:
                    self.model.inserir(nome, preco)
                    self.view.mensagem("\nProduto cadastrado com sucesso!\n")

            elif opcao == 3:
                id_produto, nome, preco = self.view.atualizar()
                if id_produto and nome and preco:
                    sucesso = self.model.atualizar(id_produto, nome, preco)
                    if sucesso:
                        self.view.mensagem("\nProduto atualizado com sucesso!\n")
                    else:
                        self.view.mensagem("\nFalha ao atualizar: ID não encontrado.\n")

            elif opcao == 4:
                id_produto = self.view.excluir()
                if id_produto:
                    sucesso = self.model.excluir(id_produto)
                    if sucesso:
                        self.view.mensagem("\nProduto excluído com sucesso!\n")
                    else:
                        self.view.mensagem("\nFalha ao excluir: ID não encontrado.\n")

            elif opcao == 0:
                self.view.mensagem("\nSaindo do sistema...\n")
                break

            else:
                self.view.mensagem("\nOpção inválida!\n")