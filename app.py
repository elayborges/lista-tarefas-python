tarefas = []

def mostrar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nSuas tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1} - {tarefa}")

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def remover_tarefa():
    mostrar_tarefas()
    try:
        numero = int(input("Digite o número da tarefa que deseja remover: "))
        tarefa_removida = tarefas.pop(numero - 1)
        print(f"Tarefa '{tarefa_removida}' removida!")
    except:
        print("Erro ao remover tarefa.")

while True:
    print("\n--- MENU ---")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_tarefas()
    elif opcao == "2":
        adicionar_tarefa()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")