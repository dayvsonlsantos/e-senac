import os

from banco import Conexao

db = Conexao()

tam = 50

def cadastrar():
    try:
        # Criando instância da classe Conexão
        db = Conexao()

        # Limpar Tela
        os.system('clear')

        # Mensagem
        print(f"+{'-' * tam}+")
        print(f"|{'CADASTRAR USUÁRIO':^{tam}}|")
        print(f"+{'-' * tam}+")

        # Inserindo dados do cliente
        nome_usuario = input('|Informe o nome do Usuário: ')
        senha_usuario = input(f'|Informe a senha do usuário {nome_usuario}: ')

        # Chamando o método para cadastrar um Cliente
        db.cadastrar_usuário(f'{nome_usuario}', f'{senha_usuario}')

        print(f"+{'-' * tam}+")
        print(f"|{'CADASTRO REALIZADO COM SUCESSO':^{tam}}|")
        print(f"+{'-' * tam}+\n")
    except:
        print(f"+{'-' * tam}+")
        print(f"|{'ERRO AO CADASTRAR USUÁRIO':^{tam}}|")
        print(f"+{'-' * tam}+\n")
        
def buscar_usuarios(user, password):
    
    dados_usuarios = ""
    
    try:
        dados_usuarios = db.buscar_usuarios(user, password)
    
        # Separando os resultados obtidos da busca
        (codigo_usuario, nome_usuario, senha_usuario) = dados_usuarios[0]
        
        if (nome_usuario is not None) and (senha_usuario is not None):
            return int(codigo_usuario)
        else:
            return 0
        
    except:
        return False
    
def alterar_dados_usuario(usuario_cadastrado):
    # try:
        
        dados_usuario = ""
        
        # Limpar Tela
        while True:
            os.system('clear')
            
            print(f"+{'-' * tam}+")
            print(f"|{'O que deseja alterar ?':^{tam}}|")
            print(f"|{' ' * tam}|")
            print(f"|{'1 - Nome':^{tam}}|")
            print(f"|{'2 - Senha':^{tam}}|")
            print(f"|{' ' * tam}|")
            print(f"+{'-' * tam}+")
            print(f"|{' ' * tam}|")
            qual_coluna_alterar = input('| Resposta: ')
            print(f"|{' ' * tam}|")
            
            int_usuario_cadastrado = int(usuario_cadastrado)
            
            dados_usuario = db.buscar_usuarios_por_codigo(int_usuario_cadastrado)

            # # Separando os resultados obtidos da busca
            (codigo_usuario, nome_usuario, senha_usuario) = dados_usuario[0]
            
            # Escolhendo a coluna que deseja alterar
            if qual_coluna_alterar == '1':
                # Enviando os dados do cliente como argumento
                nome_coluna = 'nome'
                valor_nome_novo = input('| Informe o nome correto para o usuário: ')
    
                dados_usuario = db.alterar_nome_usuario(nome_coluna, f"{valor_nome_novo}", codigo_usuario)
                break
            elif qual_coluna_alterar == '2':
                # Enviando os dados do cliente como argumento
                nome_coluna = 'senha'
                antiga_senha = input('| Informe a senha antiga: ')
                print(f"|{' ' * tam}|")
                nova_senha = input('| Informe a nova senha: ')
                print(f"|{' ' * tam}|")
                conf_nova_senha = input('| Confirme a nova senha: ')
                print(f"+{'-' * tam}+")
                
                if (antiga_senha == senha_usuario) and (nova_senha == conf_nova_senha):
                    dados_usuario = db.alterar_senha_usuario(nome_coluna, f"{nova_senha}", codigo_usuario)
                break
            else:
                print(f"|{'Informe uma coluna válida':^{tam}}|")
        
        dados_usuario = db.buscar_usuarios_por_codigo(int_usuario_cadastrado)

        # # Separando os resultados obtidos da busca
        (codigo_usuario, nome_usuario, senha_usuario) = dados_usuario[0]
        
        # Limpar Tela
        os.system('clear')
        
        # Imprimindo os dados do cliente
        print(f"+{'-' * tam}+")
        print(f"|{'Dados do Cliente':^{tam}}|")
        print(f"+{'-' * tam}+")
        print(f"|{' ' * tam}|")
        print(f"|{'Usuário: {}'.format(nome_usuario):^{tam}}|")
        print(f"|{'Senha: {}'.format(senha_usuario ):^{tam}}|")
        print(f"+{'-' * tam}+\n")
        
    # except:
    #     os.system('clear')
    #     print(f"+{'-' * tam}+")
    #     print(f"|{'NENHUMA CONTA ENCONTRADA':^{tam}}|")
    #     print(f"+{'-' * tam}+\n")