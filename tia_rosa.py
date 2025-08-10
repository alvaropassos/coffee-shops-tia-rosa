# 3 listas vazias:
# - produtos: vai guardar os produtos cadastrados (nome e preço)
# - clientes: vai guardar os dados dos clientes (nome e telefone)
# - pedidos: vai guardar os pedidos feitos (quem comprou o quê e quanto)
produtos = []
clientes = []
pedidos = []

# Esse while True cria um menu que fica repetindo até a pessoa digitar "0" pra sair
while True:
    print("\n=== Coffee Shops Tia Rosa ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Cadastrar cliente")
    print("4 - Listar clientes")
    print("5 - Fazer pedido")
    print("6 - Listar pedidos")
    print("0 - Sair")
    opcao = input("Escolha: ")  

    # Se a pessoa escolheu a opção 1, vamos cadastrar um novo produto
    if opcao == "1":
        nome = input("Nome do produto: ")  
        try:
            preco = float(input("Preço: R$ "))  
            produtos.append({"nome": nome, "preco": preco})
            print("Produto cadastrado com sucesso!")
        except ValueError:
            print("Preço inválido. Use números.")

    # Se escolheu a opção 2, mostramos todos os produtos já cadastrados
    elif opcao == "2":
        print("--- Lista de Produtos ---")
        for p in produtos:
            print(f"{p['nome']} - R$ {p['preco']:.2f}")

    # Cadastrar cliente
    elif opcao == "3":
        nome = input("Nome do cliente: ")
        telefone = input("Telefone: ")
        clientes.append({"nome": nome, "telefone": telefone})
        print("Cliente cadastrado com sucesso!")

    # Listar os clientes cadastrados
    elif opcao == "4":
        print("--- Lista de Clientes ---")
        for c in clientes:
            print(f"{c['nome']} - {c['telefone']}") 

    # Fazer um pedido
    elif opcao == "5":
        # Antes de tudo, verifica se já tem cliente e produto cadastrado
        if not clientes or not produtos:
            print("Cadastre pelo menos 1 cliente e 1 produto antes de registrar pedidos.")
            continue  

        nome_cliente = input("Nome do cliente: ")
        nome_produto = input("Nome do produto: ")

        try:
            qtd = int(input("Quantidade: "))  
            pedidos.append({"cliente": nome_cliente, "produto": nome_produto, "quantidade": qtd})
            print("Pedido registrado com sucesso!")
        except ValueError:
            print("Quantidade inválida. Use um número inteiro.")

    # Mostrar os pedidos que foram feitos
    elif opcao == "6":
        print("--- Lista de Pedidos ---")
        for p in pedidos:
            print(f"Cliente: {p['cliente']}, Produto: {p['produto']}, Quantidade: {p['quantidade']}")

    # Opção 0: sair do programa
    elif opcao == "0":
        print("Saindo do sistema... Até logo!")
        break  

    # Qualquer outra coisa que o usuário digitar que não for de 0 a 6
    else:
        print("Opção inválida, tente novamente!")
