# Coffee Shops Tia Rosa

    produtos = []
    clientes = []
    pedidos = []

    #três listas vazias para armazenar produtos, clientes e pedidos enquanto o programa estiver rodando.

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
  
    #O menu indica as opções numeradas. input lê a escolha do usuário como texto (string)

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: R$ "))
        produtos.append({"nome": nome, "preco": preco})
        print("Produto cadastrado com sucesso!")

      #Solicita nome e preço do produto.
      #se o usuário digitar algo não numérico no preço, haverá erro

    elif opcao == "2":
        print("--- Lista de Produtos ---")
        for p in produtos:
            print(f"{p['nome']} - R$ {p['preco']:.2f}")

          #Percorre a lista produtos e imprime cada produto.

    elif opcao == "3":
        nome = input("Nome do cliente: ")
        telefone = input("Telefone: ")
        clientes.append({"nome": nome, "telefone": telefone})
        print("Cliente cadastrado com sucesso!")

      #Lê nome e telefone e adiciona um dicionário na lista

    elif opcao == "4":
        print("--- Lista de Clientes ---")
        for c in clientes:
            print(f"{c['nome']} - {c['telefone']}")

          #Imprime cada cliente cadastrado.

    elif opcao == "5":
        if not clientes or not produtos:
            print("Cadastre pelo menos 1 cliente e 1 produto antes de registrar pedidos.")
            continue
        nome_cliente = input("Nome do cliente: ")
        nome_produto = input("Nome do produto: ")
        qtd = int(input("Quantidade: "))
        pedidos.append({"cliente": nome_cliente, "produto": nome_produto, "quantidade": qtd})
        print("Pedido registrado com sucesso!")

      #verifica se existe pelo menos um cliente e um produto. Se não, avisa e volta ao menu (continue pula o restante do loop atual).
      #Lê o nome do cliente, nome do produto e a quantidade (int(...) converte para inteiro).
      #Armazena o pedido na lista pedidos como um dicionário simples.

    elif opcao == "6":
        print("--- Lista de Pedidos ---")
        for p in pedidos:
            print(f"Cliente: {p['cliente']}, Produto: {p['produto']}, Quantidade: {p['quantidade']}")

          #Percorre os pedidos e mostra cada um com cliente, produto e quantidade.

    elif opcao == "0":
        print("Saindo do sistema... Até logo!")
        break
      
      #break sai do laço while True e encerra o programa.

    else:
        print("Opção inválida, tente novamente!")

      #Se o usuário digitar algo que não está nas opções, o programa avisa e volta a mostrar o menu.
