import os
import funcionalidades
import users

from banco import Conexao

# Criando instância da classe Conexão
db = Conexao()

tam = 50

user = "admin"
password = "admin"

while True:
    print(f"+{'-' * tam}+")
    print(f"|{'ACESSAR O SISTEMA':^{tam}}|")
    print(f"+{'-' * tam}+")
    print(f"|{' ' * tam}|")
    print(f"|{'Informe o usuário':^{tam}}|")
    print(f"|{' ' * tam}|")
    user = input('| Resposta: ')
    print(f"|{' ' * tam}|")
    print(f"|{'Informe a senha':^{tam}}|")
    print(f"|{' ' * tam}|")
    password = input('| Resposta: ')
    print(f"+{'-' * tam}+\n")
    
    usuario_cadastrado = users.buscar_usuarios(user, password)
    
    if ((user == "admin") and (password == "admin")) or (usuario_cadastrado != 0):
        # Limpar Tela
        os.system('clear')
        break
    else:
        print(f"+{'-' * tam}+")
        print(f"|{'USUÁRIO OU SENHA INCORRETOS':^{tam}}|")
        print(f"+{'-' * tam}+\n")
        continue

opcoes = {
    "1": "Cadastrar Conta",
    "2": "Consultar Conta",
    "3": "Alterar Conta",
    "4": "Remover Conta",
    "5": "Exibe todas as contas",
    "6": "Cadastrar Usuário",
    "9": "Alterar Dados",
    "0": "Sair do sistema",
}

while True:
    print(f"+{'-' * tam}+")
    print(f"|{'MENU':^{tam}}|")
    print(f"+{'-' * tam}+")
    for k, v in opcoes.items():
        if (k == '6') and (user != "admin"):
            continue
        
        if (k == '9') and (user == "admin"):
            continue
        
        print(f"|{f' {k} - {v}':{tam}}|")
    print(f"+{'-' * tam}+")
    

    op = input("Resposta: ")
    
    if op not in opcoes:
        # Limpar Tela
        os.system('clear')
        print(f"+{'-' * tam}+")
        print(f"|{'OPÇÃO INVÁLIDA':^{tam}}|")
        continue
    
    if op == "0":
        # Fecha a conexão
        db.close()
        print(f"\n+{'-' * tam}+")
        print(f"|{'ENCERRANDO O SISTEMA':^{tam}}|")
        print(f"|{' ' * tam}|")
        print(f"|{'OBRIGADO :)':^{tam}}|")
        print(f"+{'-' * tam}+\n")
        break;
    
    # print(f"{opcoes.get(op)}")
    match opcoes.get(op):
        case "Cadastrar Conta":
            funcionalidades.cadastrar()
        case "Consultar Conta":
            funcionalidades.consultar_conta()
        case "Alterar Conta":
            funcionalidades.alterar_conta()
        case "Remover Conta":
            funcionalidades.remover_conta()
        case "Exibe todas as contas":
            funcionalidades.exibir_contas()
        case "Cadastrar Usuário":
            if user != "admin":
                # Limpar Tela
                os.system('clear')
                print(f"+{'-' * tam}+")
                print(f"|{'OPÇÃO INVÁLIDA':^{tam}}|")
                continue
            else:
                users.cadastrar()
        case "Alterar Dados":
            if user == "admin":
                # Limpar Tela
                os.system('clear')
                print(f"+{'-' * tam}+")
                print(f"|{'OPÇÃO INVÁLIDA':^{tam}}|")
                continue
            else:
                users.alterar_dados_usuario(usuario_cadastrado)