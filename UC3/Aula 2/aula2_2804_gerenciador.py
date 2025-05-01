# Define a função principal do gerenciador de tarefas
def gerenciador_tarefas():
    # Lista onde as tarefas serão armazenadas. Cada tarefa será um dicionário.
    tarefas = []
    
    # Loop principal que mantém o menu funcionando até o usuário escolher sair
    while True:
        # Mostra o menu de opções
        print("\nGerenciador de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        
        # Solicita a escolha do usuário
        opcao = input("Escolha uma opção: ")
        
        # Opção 1: Adiciona uma nova tarefa
        if opcao == '1':
            tarefa = input("Digite a nova tarefa: ")
            # Adiciona a tarefa como um dicionário com chave "tarefa" e "concluida"
            tarefas.append({"tarefa": tarefa, "concluida": False})
            print("Tarefa adicionada!")
        
        # Opção 2: Lista todas as tarefas
        elif opcao == '2':
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")  # Caso não haja tarefas
            else:
                print("\nLista de Tarefas:")
                # Percorre a lista de tarefas com índice
                for i, item in enumerate(tarefas, 1):
                    # Mostra um ✓ se a tarefa estiver concluída
                    status = "✓" if item["concluida"] else " "
                    print(f"{i}. [{status}] {item['tarefa']}")
        
        # Opção 3: Marca uma tarefa como concluída
        elif opcao == '3':
            if not tarefas:
                print("Nenhuma tarefa para marcar.")  # Se a lista estiver vazia
            else:
                try:
                    num = int(input("Número da tarefa concluída: ")) - 1
                    # Verifica se o número está dentro da faixa válida
                    if 0 <= num < len(tarefas):
                        tarefas[num]["concluida"] = True
                        print("Tarefa marcada como concluída!")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Digite um número válido.")  # Caso o usuário digite algo não numérico
        
        # Opção 4: Remove uma tarefa da lista
        elif opcao == '4':
            if not tarefas:
                print("Nenhuma tarefa para remover.")  # Lista vazia
            else:
                try:
                    num = int(input("Número da tarefa a remover: ")) - 1
                    if 0 <= num < len(tarefas):
                        # Remove a tarefa e armazena temporariamente para exibir
                        removida = tarefas.pop(num)
                        print(f"Tarefa '{removida['tarefa']}' removida.")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Digite um número válido.")  # Entrada inválida
        
        # Opção 5: Encerra o programa
        elif opcao == '5':
            print("Saindo do gerenciador...")
            break
        
        # Qualquer outra entrada é considerada inválida
        else:
            print("Opção inválida!")

# Chamada da função para iniciar o programa
gerenciador_tarefas()