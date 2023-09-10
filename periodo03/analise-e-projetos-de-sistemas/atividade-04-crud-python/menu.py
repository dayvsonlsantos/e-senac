import os

from banco import Conexao

# Criando instância da classe Conexão
db = Conexao()

escolha_usuario = '0'
possiveis_escolhas = '123459'

while escolha_usuario not in possiveis_escolhas:

    escolha_usuario = input('Sistema Bancário Tabajara\n\n\
    Digite a sua opção: \n\
        1 - Cadastrar Conta \n\
        2 - Consultar Conta \n\
        3 - Alterar Conta \n\
        4 - Remover Conta \n\
        5 - Exibe todas as contas \n\
        9 - Sair do sistema \n\n\
    Sua opção: ') or '0'

    match escolha_usuario:
        case '1':   
            try:
                # Limpar Tela
                os.system('clear')
                
                # Mensagem
                print(20*'-', '\n')
                print('Cadastrar Novo Cliente:\n')
                
                # Inserindo dados do cliente
                nome_cliente = input('Informe o nome do Cliente: ')
                saldo_conta_cliente = input(f'Informe o saldo da conta do cliente {nome_cliente}: ')
                
                # Chamando o método para cadastrar um Cliente
                db.cadastrar_cliente(f'{nome_cliente}', float(saldo_conta_cliente))
                
                # Fecha a conexão
                db.close()
                
                # Encerrar Menu
                escolha_usuario = '1'
                
                print('\nCliente cadastrado com Sucesso\n')
                print(20*'-')
            except:
                print(f'\nErro ao cadastrar o cliente {nome_cliente}.')
                print(20*'-')
            
        case '2':
            try:
                
                # Limpar Tela
                os.system('clear')
                
                codigo_conta_cliente = '0'
                
                while codigo_conta_cliente == '0':
                    
                    # Mensagem
                    print(20*'-', '\n')
                    print('Consultar Conta:\n')
                    
                    # Inserir número da conta
                    print('Informe o código da conta do cliente:')
                    print('(Não sabe o código ? Digite 0)')
                    codigo_conta_cliente = input('\nResposta: ')
                    
                    if codigo_conta_cliente == '0':
                        # Limpar Tela
                        os.system('clear')
                        
                        # Mensagem
                        print('Exibir todas as Contas:')
                        
                        # Enviando o código do cliente como argumento
                        dados_cliente = db.buscar_clientes()
                        
                        for codigo_cliente, nome_cliente, saldo_cliente in dados_cliente:
                            
                            # Mensagem
                            print('\n', 20*'-', '\n')
                            
                            # Imprimindo os dados do cliente
                            print(f'Dados do Cliente {codigo_cliente}: \n\n')
                            print(f'Cliente: {nome_cliente}')
                            print(f'Código: {codigo_cliente}')
                            print(f'Saldo: {saldo_cliente}\n')
                
                # Convertendo em inteiro
                int_codigo_conta_cliente = int(codigo_conta_cliente)
                
                # Enviando o código do cliente como argumento
                dados_cliente = db.buscar_clientes_por_codigo(int_codigo_conta_cliente)
                
                # Separando os resultados obtidos da busca
                (codigo_cliente, nome_cliente, saldo_cliente) = dados_cliente[0]
                
                # Limpar Tela
                os.system('clear')
                
                # Mensagem
                print(20*'-', '\n')
                
                # Imprimindo os dados do cliente
                print('Dados do Cliente: \n\n')
                print(f'Cliente: {nome_cliente}')
                print(f'Código: {codigo_cliente}')
                print(f'Saldo: {saldo_cliente}\n')
                
                print(20*'-')
                
                # Fecha a conexão
                db.close()
                
                # Encerrar Menu
                escolha_usuario = '2'
            except:
                print('\nNenhuma conta encontrada\n')
                print(20*'-')
            
        case '3':
            try:
                # Limpar Tela
                os.system('clear')
                
                codigo_conta_cliente = '0'
                
                while codigo_conta_cliente == '0':
                
                    # Mensagem
                    print(20*'-', '\n')
                    print('Alterar Conta:\n')
                    
                    # Inserir número da conta
                    print('Informe o código da conta do cliente:')
                    print('(Não sabe o código ? Digite 0)')
                    codigo_conta_cliente = input('\nResposta: ')
                    
                    if codigo_conta_cliente == '0':
                        # Limpar Tela
                        os.system('clear')
                        
                        # Mensagem
                        print('Exibir todas as Contas:')
                        
                        # Enviando o código do cliente como argumento
                        dados_cliente = db.buscar_clientes()
                        
                        for codigo_cliente, nome_cliente, saldo_cliente in dados_cliente:
                            
                            # Mensagem
                            print('\n', 20*'-', '\n')
                            
                            # Imprimindo os dados do cliente
                            print(f'Dados do Cliente {codigo_cliente}: \n\n')
                            print(f'Cliente: {nome_cliente}')
                            print(f'Código: {codigo_cliente}')
                            print(f'Saldo: {saldo_cliente}\n')
                
                # Limpar Tela
                os.system('clear')
                
                print('\nEscolha a coluna que seja alterar:')
                print('1 - Nome \n2 - Saldo')
                qual_coluna_alterar = input('\n\nResposta: ')
                
                # Convertendo em inteiro
                int_codigo_conta_cliente = int(codigo_conta_cliente)
                
                # Enviando o código do cliente como argumento
                dados_cliente = db.buscar_clientes_por_codigo(int_codigo_conta_cliente)
                
                # Separando os resultados obtidos da busca
                (codigo_cliente, nome_cliente, saldo_cliente) = dados_cliente[0]
                
                # Limpar Tela
                os.system('clear')
                
                # Mensagem
                print(20*'-', '\n')
                
                # Imprimindo os dados do cliente
                print('Dados antigos do Cliente: \n\n')
                print(f'Cliente: {nome_cliente}')
                print(f'Código: {codigo_cliente}')
                print(f'Saldo: {saldo_cliente}\n')
                
                print(20*'-')
                
                # Escolhendo a coluna que deseja alterar
                if qual_coluna_alterar == '1':
                    # Enviando os dados do cliente como argumento
                    nome_coluna = 'nome'
                    valor_nome_novo = input('Informe o nome correto para o usuário: ')
                    
                    dados_cliente = db.atualizar_nome_cliente(nome_coluna, f"{valor_nome_novo}", int_codigo_conta_cliente)
                elif qual_coluna_alterar == '2':
                    # Enviando os dados do cliente como argumento
                    nome_coluna = 'saldo'
                    novo_valor = input('Informe o valor correto para o usuário: ')
                    
                    dados_cliente = db.atualizar_saldo_cliente(nome_coluna, novo_valor, int_codigo_conta_cliente)
                else:
                    print('\nInforme uma coluna válida\n')
                
                # Enviando o código do cliente como argumento
                dados_cliente = db.buscar_clientes_por_codigo(int_codigo_conta_cliente)
                
                # Separando os resultados obtidos da busca
                (codigo_cliente, nome_cliente, saldo_cliente) = dados_cliente[0]
                
                # Limpar Tela
                os.system('clear')
                
                # Mensagem
                print(20*'-', '\n')
                
                # Imprimindo os dados do cliente
                print('Dados atualizados do Cliente: \n\n')
                print(f'Cliente: {nome_cliente}')
                print(f'Código: {codigo_cliente}')
                print(f'Saldo: {saldo_cliente}\n')
                
                print(20*'-')
                
                # Fecha a conexão
                db.close()
                
                # Encerrar Menu
                escolha_usuario = '3'
            except:
                print('\nErro ao alterar a conta\n')
                print(20*'-')
        
        case '4':
            try:
                # Limpar Tela
                os.system('clear')
                
                while codigo_conta_cliente == '0':
                
                    # Mensagem
                    print(20*'-', '\n')
                    print('Apagar Cliente:\n')
                    
                    # Inserir número da conta
                    print('Informe o código da conta do cliente:')
                    print('(Não sabe o código ? Digite 0)')
                    codigo_conta_cliente = input('\nResposta: ')
                    
                    if codigo_conta_cliente == '0':
                        # Limpar Tela
                        os.system('clear')
                        
                        # Mensagem
                        print('Exibir todas as Contas:')
                        
                        # Enviando o código do cliente como argumento
                        dados_cliente = db.buscar_clientes()
                        
                        for codigo_cliente, nome_cliente, saldo_cliente in dados_cliente:
                            
                            # Mensagem
                            print('\n', 20*'-', '\n')
                            
                            # Imprimindo os dados do cliente
                            print(f'Dados do Cliente {codigo_cliente}: \n\n')
                            print(f'Cliente: {nome_cliente}')
                            print(f'Código: {codigo_cliente}')
                            print(f'Saldo: {saldo_cliente}\n')
                            
                # Limpar Tela
                os.system('clear')
                
                # Chamando o método para cadastrar um Cliente
                db.apagar_cliente(codigo_conta_cliente)
                
                # Fecha a conexão
                db.close()
                
                # Encerrar Menu
                escolha_usuario = '4'
                
                print(20*'-')
                print('\nCliente apagado com Sucesso\n')
                print(20*'-')
            except:
                print(f'\nErro ao apagar o cliente {nome_cliente}.')
                print(20*'-')
        
        case '5':
            try:
                # Limpar Tela
                os.system('clear')
                
                # Mensagem
                print(20*'-', '\n')
                print('Exibir todas as Contas:\n')
                
                # Enviando o código do cliente como argumento
                dados_cliente = db.buscar_clientes()
                
                # Limpar Tela
                os.system('clear')
                
                for codigo_cliente, nome_cliente, saldo_cliente in dados_cliente:
                    
                    # Mensagem
                    print(20*'-', '\n')
                    
                    # Imprimindo os dados do cliente
                    print(f'Dados do Cliente {codigo_cliente}: \n\n')
                    print(f'Cliente: {nome_cliente}')
                    print(f'Código: {codigo_cliente}')
                    print(f'Saldo: {saldo_cliente}\n')
                
                # Fecha a conexão
                db.close()
                
                print(20*'-')
                
                # Encerrar Menu
                escolha_usuario = '5'
            except:
                print('\nErro ao alterar a conta\n')
                print(20*'-')
                
        case '9':
            os.system('clear')
            print(20*'-', '\n')
            print('Saindo do Sistema...')
            print('Obrigado por utilizar nosso programa\n')
            print(20*'-')
            # Fecha a conexão
            db.close()
            escolha_usuario = '9'
            break
    
    if escolha_usuario not in possiveis_escolhas:
        os.system('clear')
        print('Essa opção não existe, favor escolher outra...\n')
        
    if len(escolha_usuario) > 1:
        os.system('clear')
        escolha_usuario = '0'

    # Limpar Tela
    print(20*'-', '\n')
    print('Você deseja voltar ao Menu ?')
    print('\nVoltar -> Digite 0')
    print('Sair -> Pressione qualquer tecla')
    voltar_ou_sair = input('\n\nResposta: ')

    if voltar_ou_sair == '0':
        os.system('clear')
        escolha_usuario = '0'
        codigo_conta_cliente = '0'
        # Criando instância da classe Conexão
        db = Conexao()
    else:
        os.system('clear')
        print(20*'-', '\n')
        print('Obrigado por utilizar nosso programa')
        print('\n', 20*'-')
        # Fecha a conexão
        db.close()

# Fecha a conexão
db.close()