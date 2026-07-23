import math

while True:
    print("\n" + "=" * 40)
    print("      CALCULADORA CIENTÍFICA")
    print("=" * 40)
    print("1  - Soma")
    print("2  - Subtração")
    print("3  - Multiplicação")
    print("4  - Divisão")
    print("5  - Potência")
    print("6  - Raiz Quadrada")
    print("7  - Seno")
    print("8  - Cosseno")
    print("9  - Tangente")
    print("10 - Logaritmo")
    print("11 - Fatorial")
    print("12 - Valor Absoluto")
    print("13 - Resto da Divisão")
    print("14 - Sair")

    opcao = input("\nEscolha uma opção: ")

    try:

        if opcao == "1":
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))
            print(f"Resultado: {num1 + num2}")

        elif opcao == "2":
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))
            print(f"Resultado: {num1 - num2}")

        elif opcao == "3":
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))
            print(f"Resultado: {num1 * num2}")

        elif opcao == "4":
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))

            if num2 == 0:
                print("Erro: não é possível dividir por zero.")
            else:
                print(f"Resultado: {num1 / num2}")

        elif opcao == "5":
            base = float(input("Base: "))
            expoente = float(input("Expoente: "))
            print(f"Resultado: {math.pow(base, expoente)}")

        elif opcao == "6":
            numero = float(input("Número: "))

            if numero < 0:
                print("Não existe raiz quadrada real para números negativos.")
            else:
                print(f"Resultado: {math.sqrt(numero)}")

        elif opcao == "7":
            angulo = float(input("Ângulo (graus): "))
            print(f"Resultado: {math.sin(math.radians(angulo))}")

        elif opcao == "8":
            angulo = float(input("Ângulo (graus): "))
            print(f"Resultado: {math.cos(math.radians(angulo))}")

        elif opcao == "9":
            angulo = float(input("Ângulo (graus): "))
            print(f"Resultado: {math.tan(math.radians(angulo))}")

        elif opcao == "10":
            numero = float(input("Número: "))

            if numero <= 0:
                print("O logaritmo só existe para números positivos.")
            else:
                print(f"Resultado: {math.log10(numero)}")

        elif opcao == "11":
            numero = int(input("Número inteiro: "))

            if numero < 0:
                print("Não existe fatorial de número negativo.")
            else:
                print(f"Resultado: {math.factorial(numero)}")

        elif opcao == "12":
            numero = float(input("Número: "))
            print(f"Resultado: {abs(numero)}")

        elif opcao == "13":
            num1 = int(input("Primeiro número: "))
            num2 = int(input("Segundo número: "))

            if num2 == 0:
                print("Erro: divisão por zero.")
            else:
                print(f"Resto da divisão: {num1 % num2}")

        elif opcao == "14":
            print("Calculadora encerrada.")
            break

        else:
            print("Opção inválida.")

    except ValueError:
        print("Digite um valor válido!")