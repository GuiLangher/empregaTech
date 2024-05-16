import os


"""Biblioteca de restaurantes, onde as variaveis de restaurantes são guardadas"""

restaurantes = [{"nome":"LaCardapia", "categoria":"Churrascaria", "ativo":False}, 
                {"nome":"EntrecotDeParri", "categoria":"Massas", "ativo":True},
                {"nome":"Celeiro", "categoria":"Pizzaria", "ativo":False}]

def nome_programa():
    print("Sᴀʙᴏʀ Exᴘʀᴇss\n")

def lista_opcoes():
    print("1. Cadastrar restaurantes")
    print("2. Listar Restaurante")
    print("3. Alternar estado do Restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Saindo do sistema...")

def voltar_menu():
    """Fução para retornar ao menu principal"""

    input("\nDigite uma tecla para voltar ao menu principal ")
    main()

def opcao_invalida():
    print("Opção Inválida, tente novamente")
    voltar_menu()

def exibir_subtitulo(texto):
    """Função criada para exibir todo o subtitulo, economizando linhas nas outras funções"""

    os.system('cls')
    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """Função para cadastrar um novo restaurante"""

    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_do_restaurante = input("Digite o nome do Restaurante: ")
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False }
    restaurantes.append(dados_do_restaurante)# .append coloca a variavel dentro da lista

    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!")

    voltar_menu()

def lista_restaurantes():
    """Função para listar todos os restaurantes cadastrados"""

    exibir_subtitulo("Lista de restaurantes cadastrados")

    print(f"-> {"Nome do Restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Status"}")
    linha = "-" * 60
    print(linha)

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo = "Ativo" if restaurante["ativo"] else "Desativado"

        print(f"-> {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}")

    voltar_menu()

def ativar_restaurante():
    """Função para alterar o Status do Restaurante, para True ou False"""

    exibir_subtitulo("Ativando Restaurante")
    nome_restaurante = input("Digite o nome do restaurante para ativar o estado: ")

    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_menu()

def escolher_opcao():
    """Parte onde o usuario escolhe a ação"""

    try: #try para a variavel opcao_escolhida tentar ler o codigo mesmo assim, caso não consiga o codigo sai para o except
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            lista_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """Função criada para economizar linhas nas outras funções, emglobando varias funções"""

    nome_programa()
    lista_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    """Cria a main(), para poder ser chamada"""

    main()
