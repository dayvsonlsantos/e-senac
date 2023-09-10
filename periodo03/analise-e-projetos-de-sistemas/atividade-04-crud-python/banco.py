import mysql.connector
# CRUD

# comando = '' -> Comando escrito aqui
# cursor.execute(comando) -> Executa o comando
# conexao.commit() -> Executamos quando editamos o banco de dados (create, update e delete)
# resultado = cursor.fetchall() -> Executamos quando apenas lemos o banco de dados (read)

class Conexao:
    
    def __init__(self):
        
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'senha',
            database = 'dbtabajara',
        )

        self.cursor = self.conexao.cursor()
        
    def close(self):
        self.cursor.close()
        self.conexao.close()

    # CREATE

    def cadastrar_cliente(self, nome_cliente, saldo_cliente):
        # nome_cliente = 'João Ferreira'
        # saldo_cliente = 1200.59

        comando = f'INSERT INTO conta (nome, saldo) \
            VALUES ("{nome_cliente}", {saldo_cliente})'
        self.cursor.execute(comando)
        self.conexao.commit()

    # cadastrar_cliente('Jonas André', 600)


    # Read

    def buscar_clientes(self):
        comando = 'SELECT * FROM conta'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    # buscar_clientes()
    
    
    # Read ID

    def buscar_clientes_por_codigo(self, codigo):
        comando = f'SELECT * FROM conta WHERE codigo = {codigo}'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    # buscar_clientes_por_codigo(1)

    
    # Update Strings

    def atualizar_nome_cliente(self, nome_coluna, valor_nome_novo, valor_codigo):
        # nome_coluna = 'nome'
        # valor_nome_novo = 'Pedro Ribeiro'
        # valor_codigo = 9

        comando = f'UPDATE conta SET {nome_coluna} = "{valor_nome_novo}" WHERE codigo = {valor_codigo}'
        self.cursor.execute(comando)
        self.conexao.commit()

    # atualizar_nome_cliente('nome', 'Emanuel Junior', 9)

    # Update Numbers

    def atualizar_saldo_cliente(self, nome_coluna, novo_valor, valor_codigo):
        # nome_coluna = 'saldo'
        # novo_valor = 1800
        # valor_codigo = 9

        comando = f'UPDATE conta SET {nome_coluna} = {novo_valor} WHERE codigo = {valor_codigo}'
        self.cursor.execute(comando)
        self.conexao.commit()

    # atualizar_saldo_cliente('saldo', 1500, 9)


    # Delete

    def apagar_cliente(self, valor_codigo):
        # valor_codigo = 9

        comando = f'DELETE FROM conta WHERE codigo = {valor_codigo}'
        self.cursor.execute(comando)
        self.conexao.commit()
        
    # apagar_cliente(9)