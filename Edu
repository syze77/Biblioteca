# Função para adicionar um novo produto ao estoque
def adicionar_produto(estoque, nome_produto, quantidade):
    if nome_produto in estoque:
        print(f"O produto '{nome_produto}' já existe no estoque. Use a função de atualização.")
    else:
        estoque[nome_produto] = quantidade
        print(f"Produto '{nome_produto}' adicionado com sucesso.")

# Função para atualizar a quantidade de um produto existente
def atualizar_produto(estoque, nome_produto, quantidade):
    if nome_produto in estoque:
        estoque[nome_produto] += quantidade
        print(f"Quantidade do produto '{nome_produto}' atualizada para {estoque[nome_produto]}.")
    else:
        print(f"O produto '{nome_produto}' não existe no estoque. Use a função de adicionar.")

# Função para remover um produto do estoque
def remover_produto(estoque, nome_produto):
    if nome_produto in estoque:
        del estoque[nome_produto]
        print(f"Produto '{nome_produto}' removido com sucesso.")
    else:
        print(f"O produto '{nome_produto}' não existe no estoque.")

# Função para visualizar o estoque atual
def visualizar_estoque(estoque):
    if not estoque:
        print("O estoque está vazio.")
    else:
        for produto, quantidade in estoque.items():
            print(f"Produto: {produto}, Quantidade: {quantidade}")

# Função principal para interação com o usuário
def menu():
    estoque = {}
    
    while True:
        print("\n1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Remover produto")
        print("4. Visualizar estoque")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome_produto = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade: "))
            adicionar_produto(estoque, nome_produto, quantidade)
        elif escolha == '2':
            nome_produto = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade a adicionar (use valores negativos para subtrair): "))
            atualizar_produto(estoque, nome_produto, quantidade)
        elif escolha == '3':
            nome_produto = input("Digite o nome do produto: ")
            remover_produto(estoque, nome_produto)
        elif escolha == '4':
            visualizar_estoque(estoque)
        elif escolha == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
