import psycopg2

class ProdutoModel:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="loja",
                user="postgres",
                password="alunocceia",
                host="localhost",
                port="5432"
            )

            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"\nErro ao conectar ao banco de dados: {e}\n")

    def listar(self):
        try:
            self.cursor.execute("select * from produtos order by id;")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"\nErro ao listar produtos: {e}\n")
            return []
    
    def inserir(self, nome, preco):
        try:
            self.cursor.execute("insert into produtos (nome, preco) values (%s,%s);", (nome, preco))
            self.conn.commit()
        except Exception as e:
            print(f"\nErro ao inserir produto: {e}\n")
            self.conn.rollback()

    def existe_id(self, id_produto):
        try:
            self.cursor.execute("select 1 from produtos where id=%s;", (id_produto,))
            return self.cursor.fetchone is not None
        except Exception as e:
            print(f"\nErro ao verificar a existência do produto: {e}\n")
            return False
        
    def atualizar(self, id_produto, nome, preco):
        try:
            if not self.existe_id(id_produto):
                print("\nNenhum produto encontrado com esse ID.\n")
                return False
        
            self.cursor.execute("update produtos set nome= %s, preco= %s where id= %s;", (nome, preco, id_produto))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao atualizar produto: {e}\n")
            self.conn.rollback()
            return False
    
    def excluir(self, id_produto):
        try:
            if not self.existe_id(id_produto):
                print("\nNenhum produto encontrado com esse ID.\n")
                return False
        
            self.cursor.execute("delete from produtos where id= %s;", (id_produto,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"\nErro ao excluir produto: {e}\n")
            self.conn.rollback()
            return False
        
    def __del__(self):
        if hasattr(self, "cursor") and hasattr(self, "conn"):
            self.cursor.close()
            self.conn.close()
    
    