# Desenvolva uma calculadora estilo HP.
# Irá solicitar para o usuário informar a opção
# 1 - Adição
# 2- Subtração
# 3 - Multiplicação
# 4 - Divisão
# X - Sair
# Quando escolher uma das opções, irá receber os valores numéricos até o usuário digitar a letra P, posterior a isso exibirá o resultado do calculo escolhido, e voltará para o menu.


opcao = ''
while opcao.upper() != 'X':
    # Exibe o menu de opções para o usuário
    print("Escolha a opção:")

     # O menu de opções
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    # Opição caso o usuario deseje sair 
    print("X - Sair")


    # Lê a opção do usuário e converte para maiúscula 
    opcao = input("Qualopção: ").strip().upper()

    # Verifica se a opção é para sair de fato 
    if opcao == 'X':
        print("Saindo...")
        break

    # Verifica se a opção é válida (1, 2, 3, 4) para realizar as operações, 
    #se der invalida solisitar outra resposta 
    elif opcao not in {'1', '2', '3', '4'}:
        print("Opção inválida! Tente novamente.")
        continue

    # Lista para armazenar os números inseridos pelo usuário para usar nas operações
    numeros = []
    print("Insira os numeros que deseja  (digite 'P' para processar):")
    

    while True:
        valor = input().strip().upper()
        if valor == 'P':
            break
        try:
            # Tenta converter o valor para float e adiciona à lista
            numero = float(valor)
            numeros.append(numero)
        except ValueError:
            print("Valor inválido! Insira um número ou 'P' para processar.")

    # Verificar se a lista de números está vazia para retornar ao usuario que nesecita de numerros 
    if not numeros:
        print("Nenhum número foi inserido. Voltando ao menu.")
        continue

    # Processa a operação escolhida pelo usuário usando match-case para ezecutar o cauculo 
    match opcao:
        case '1': #adição
            resultado = sum(numeros)
            operacao = "Adição"
        case '2': #subitração
            resultado = numeros[0]
            for num in numeros[1:]:
                resultado -= num
            operacao = "Subtração"
        case '3':# mutiplicação
            resultado = 1
            for num in numeros:
                resultado *= num
            operacao = "Multiplicação"
        case '4': #divisão
            resultado = numeros[0]
            for num in numeros[1:]:
                if num == 0:
                    # casso o numerro seja zero retorne ao usuario o erro
                    print("Erro: Divisão por zero!")
                    resultado = None
                    break
                resultado /= num
            operacao = "Divisão"

    # Exibe o resultado da operação ao osuarrio 
    if resultado is not None:
        print(f"Resultado da {operacao}: {resultado}")

