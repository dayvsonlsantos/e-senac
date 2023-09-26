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
        print(f"|{'CADASTRAR CLIENTE':^{tam}}|")
        print(f"+{'-' * tam}+")

        # Inserindo dados do cliente
        nome_cliente = input('|Informe o nome do Cliente: ')
        saldo_conta_cliente = input(f'|Informe o saldo da conta do cliente {nome_cliente}: ')

        # Chamando o método para cadastrar um Cliente
        db.cadastrar_cliente(f'{nome_cliente}', float(saldo_conta_cliente))

        print(f"+{'-' * tam}+")
        print(f"|{'CADASTRO REALIZADO COM SUCESSO':^{tam}}|")
        print(f"+{'-' * tam}+\n")
    except:
        print(f"+{'-' * tam}+")
        print(f"|{'ERRO NO CADASTRO':^{tam}}|")
        print(f"+{'-' * tam}+\n")
        
def consultar_conta():
    try:
        # Limpar Tela
        os.system('clear')
        
        while True:
            
            print(f"+{'-' * tam}+")
            print(f"|{'CONSULTAR CONTA':^{tam}}|")
            print(f"+{'-' * tam}+")
            
            # Inserir número da conta
            print(f"|{' ' * tam}|")
            print(f"|{'Informe o código da conta do cliente':^{tam}}|")
            print(f"|{'(Não sabe o código ? Digite 0)':^{tam}}|")
            print(f"|{' ' * tam}|")
            codigo_conta_cliente = input('| Resposta: ')
            
            if codigo_conta_cliente == '0':
                exibir_contas()
                continue
            
            if codigo_conta_cliente != '0':
                break
        
        # Convertendo em inteiro
        int_codigo_conta_cliente = int(codigo_conta_cliente)
        
        # Enviando o código do cliente como argumento
        dados_cliente = db.buscar_clientes_por_codigo(int_codigo_conta_cliente)
        
        # Separando os resultados obtidos da busca
        (codigo_cliente, nome_cliente, saldo_cliente) = dados_cliente[0]
        
        # Limpar Tela
        os.system('clear')
        
        print(f"+{'-' * tam}+")
        print(f"|{'Dados do Cliente':^{tam}}|")
        print(f"+{'-' * tam}+")
        print(f"|{' ' * tam}|")
        print(f"|{'Cliente: {}'.format(nome_cliente):^{tam}}|")
        print(f"|{'Código: {}'.format(codigo_cliente):^{tam}}|")
        print(f"|{'Saldo: {}'.format(saldo_cliente ):^{tam}}|")
        print(f"+{'-' * tam}+\n")
        
    except:
        os.system('clear')
        print(f"+{'-' * tam}+")
        print(f"|{'NENHUMA CONTA ENCONTRADA':^{tam}}|")
        print(f"+{'-' * tam}+\n")

def alterar_conta():
    try:
        # Limpar Tela
        os.system('clear')
        
        while True:
            
            print(f"+{'-' * tam}+")
            print(f"|{'Alterar Conta':^{tam}}|")
            print(f"+{'-' * tam}+")
            print(f"|{' ' * tam}|")
            
            # Inserir número da conta
            print(f"|{'Informe o código da conta do cliente':^{tam}}|")
            print(f"|{'Não sabe o código ? Digite 0)':^{tam}}|")
            print(f"|{' ' * tam}|")
            codigo_conta_cliente = input('| Resposta: ')
            print(f"+{'-' * tam}+\n")
            
            if codigo_conta_cliente == '0':
                exibir_contas()
                
            if codigo_conta_cliente != '0':
                break;
        
        # Convertendo em inteiro
        int_codigo_conta_cliente = int(codigo_conta_cliente)
        
        # Enviando o código do cliente como argumento
        dados_cliente = db.buscar_clientes_por_codigo(int_codigo_conta_cliente)
        
        # Separando os resultados obtidos da busca
        (codigo_cliente, nome_cliente, saldo_cliente) = dados_cliente[0]
        
        # Limpar Tela
        os.system('clear')
        
        
        # Imprimindo os dados do cliente
        print(f"+{'-' * tam}+")
        print(f"|{'Dados do Cliente':^{tam}}|")
        print(f"+{'-' * tam}+")
        print(f"|{' ' * tam}|")
        print(f"|{'Cliente: {}'.format(nome_cliente):^{tam}}|")
        print(f"|{'Código: {}'.format(codigo_cliente):^{tam}}|")
        print(f"|{'Saldo: {}'.format(saldo_cliente ):^{tam}}|")
        print(f"+{'-' * tam}+")
        print(f"|{' ' * tam}|")
        
        # Limpar Tela
        while True:
            os.system('clear')
            
            print(f"+{'-' * tam}+")
            print(f"|{'O que deseja alterar ?':^{tam}}|")
            print(f"|{' ' * tam}|")
            print(f"|{'1 - Nome':^{tam}}|")
            print(f"|{'2 - Saldo':^{tam}}|")
            print(f"|{' ' * tam}|")
            print(f"+{'-' * tam}+")
            print(f"|{' ' * tam}|")
            qual_coluna_alterar = input('| Resposta: ')
            print(f"|{' ' * tam}|")
            
            # Escolhendo a coluna que deseja alterar
            if qual_coluna_alterar == '1':
                # Enviando os dados do cliente como argumento
                nome_coluna = 'nome'
                valor_nome_novo = input('| Informe o nome correto para o usuário: ')
    
                dados_cliente = db.atualizar_nome_cliente(nome_coluna, f"{valor_nome_novo}", int_codigo_conta_cliente)
                break
            elif qual_coluna_alterar == '2':
                # Enviando os dados do cliente como argumento
                nome_coluna = 'saldo'
                novo_valor = input('| Informe o valor correto para o usuário: ')
                
                dados_cliente = db.atualizar_saldo_cliente(nome_coluna, novo_valor, int_codigo_conta_cliente)
                break
            else:
                print(f"|{'Informe uma coluna válida':^{tam}}|")
        
        # Enviando o código do cliente como argumento
        dados_cliente = db.buscar_clientes_por_codigo(int_codigo_conta_cliente)
        
        # Separando os resultados obtidos da busca
        (codigo_cliente, nome_cliente, saldo_cliente) = dados_cliente[0]
        
        # Limpar Tela
        os.system('clear')
        
        # Imprimindo os dados do cliente
        print(f"+{'-' * tam}+")
        print(f"|{'Dados do Cliente':^{tam}}|")
        print(f"+{'-' * tam}+")
        print(f"|{' ' * tam}|")
        print(f"|{'Cliente: {}'.format(nome_cliente):^{tam}}|")
        print(f"|{'Código: {}'.format(codigo_cliente):^{tam}}|")
        print(f"|{'Saldo: {}'.format(saldo_cliente ):^{tam}}|")
        print(f"+{'-' * tam}+\n")    
        
    except:
        os.system('clear')
        print(f"+{'-' * tam}+")
        print(f"|{'NENHUMA CONTA ENCONTRADA':^{tam}}|")
        print(f"+{'-' * tam}+\n")

def remover_conta():
    try:
        # Limpar Tela
        os.system('clear')
        
        while True:
        
            # Mensagem
            print(f"+{'-' * tam}+")
            print(f"|{'Apagar Conta':^{tam}}|")
            print(f"+{'-' * tam}+")
            print(f"|{' ' * tam}|")
            print(f"|{'Informe o código da conta do cliente':^{tam}}|")
            print(f"|{'(Não sabe o código ? Digite 0)':^{tam}}|")
            print(f"|{' ' * tam}|")
            codigo_conta_cliente = input('| Resposta: ')
            
            if codigo_conta_cliente == '0':
                exibir_contas()
                
            if codigo_conta_cliente != '0':
                break
                    
        # Limpar Tela
        os.system('clear')
        
        # Chamando o método para cadastrar um Cliente
        foi_possivel_apagar = db.apagar_cliente(codigo_conta_cliente)
        if foi_possivel_apagar == None:
            print(f"+{'-' * tam}+")
            print(f"|{'ESSA CONTA NÃO EXISTE':^{tam}}|")
            print(f"+{'-' * tam}+\n")
        else:
            print(f"+{'-' * tam}+")
            print(f"|{'CONTA APAGADA COM SUCESSO':^{tam}}|")
            print(f"+{'-' * tam}+\n")
    except:
        os.system('clear')
        print(f"+{'-' * tam}+")
        print(f"|{'ERRO AO APAGAR A CONTA':^{tam}}|")
        print(f"+{'-' * tam}+\n")

def exibir_contas():
    # Abre a Conexão
    db = Conexao()
    dados_cliente = ""
    
    try:
        # Limpar Tela
        os.system('clear')
        
        # Mensagem
        print(f"+{'-' * tam}+")
        print(f"|{'EXIBIR TODAS AS CONTAS':^{tam}}|")
        print(f"+{'-' * tam}+\n")
        
        # Enviando o código do cliente como argumento
        dados_cliente = db.buscar_clientes()
        
        # Limpar Tela
        os.system('clear')
        
        for codigo_cliente, nome_cliente, saldo_cliente in dados_cliente:
            
            # Imprimindo os dados do cliente
            print(f"+{'-' * tam}+")
            print(f"|{'Dados do Cliente':^{tam}}|")
            print(f"+{'-' * tam}+")
            print(f"|{' ' * tam}|")
            print(f"|{'Cliente: {}'.format(nome_cliente):^{tam}}|")
            print(f"|{'Código: {}'.format(codigo_cliente):^{tam}}|")
            print(f"|{'Saldo: {}'.format(saldo_cliente ):^{tam}}|")
            print(f"+{'-' * tam}+\n")     

    except:
        os.system('clear')
        print(f"+{'-' * tam}+")
        print(f"|{'ERRO AO EXIBIR AS CONTAS':^{tam}}|")
        print(f"+{'-' * tam}+\n")