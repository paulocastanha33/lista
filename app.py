import os
from colorama import Fore, Back, Style, init

# INICIA O COLORAMA 
init(autoreset=True)

# FUNCAO PARA LIMPAR A TELA
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# FUNÇÃO PARA CARREGAR O ARQUIVO tarefas.txt
def carregar_tarefas(arquivo):
    try:
        with open(arquivo, 'r') as f:
            tarefas = []
            for linha in f:
                descricao, status = linha.strip().split('|')
                tarefa = {'descricao': descricao, 'concluida': status == 'Concluída'}
                tarefas.append(tarefa)
            return tarefas
    except FileNotFoundError:
        return []

# FUNÇÃO SALVAR NO ARQUIVO
def salvar_tarefas(tarefas, arquivo):
    with open(arquivo, 'w') as f:
        for tarefa in tarefas:
            status = "Concluída" if tarefa['concluida'] else "Pendente"
            f.write(f"{tarefa['descricao']}|{status}\n")

# FUNÇÃO LISTAR AS TAREFAS
def listar_tarefas(tarefas):
    #print("\n--- Lista de Tarefas ---")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"{i}. {tarefa['descricao']} ({status})")
   # print("-------------------------")

# FUNÇÃO PARA ADICIONAR TAREFAS
def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da nova tarefa: ")
    nova_tarefa = {'descricao': descricao, 'concluida': False}
    tarefas.append(nova_tarefa)

# FUNÇÃO PARA MARCAR COMO TAREFA CONCLUIDA
def marcar_como_concluida(tarefas):
    indice = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluida'] = True
    else:
        print("Índice inválido.")

# FUNÇÃO PARA DELETAR TAREFA
def remover_tarefa(tarefas):
    indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
    if 0 <= indice < len(tarefas):
        del tarefas[indice]
    else:
        print("Índice inválido.")

# FUNÇÃO MENU
def mostrar_menu():
    print(Fore.WHITE + Back.BLUE +" + --------------------------------+")
    print(Fore.WHITE + Back.BLUE +" |   Gerenciador de Tarefas        |")
    print(Fore.WHITE + Back.BLUE +" + --------------------------------+")
    print(Fore.WHITE + Back.BLUE +" |    [1] Listar tarefas           |")
    print(Fore.WHITE + Back.BLUE +" |    [2] Adicionar tarefa         |")
    print(Fore.WHITE + Back.BLUE +" |    [3] Marcar como concluída    |")
    print(Fore.WHITE + Back.BLUE +" |    [4] Remover tarefa           |")
    print(Fore.WHITE + Back.BLUE +" |    [5] Sair                     |")
    print(Fore.WHITE + Back.BLUE +" + --------------------------------+\n")

  
def main():
    arquivo = 'tarefas.txt'
    tarefas = carregar_tarefas(arquivo)

    while True:
        limpar_tela()
        mostrar_menu()
        listar_tarefas(tarefas)

        opcao = input(Fore.YELLOW +"  \nEscolha uma opção:  ")
       

        if opcao == '1':
            pass  
        elif opcao == '2':
            adicionar_tarefa(tarefas)
        elif opcao == '3':
            marcar_como_concluida(tarefas)
        elif opcao == '4':
            remover_tarefa(tarefas)
        elif opcao == '5':
            salvar_tarefas(tarefas, arquivo)
            break
        else:
            print("Opção inválida.")

        salvar_tarefas(tarefas, arquivo)

if __name__ == "__main__":
    main()
