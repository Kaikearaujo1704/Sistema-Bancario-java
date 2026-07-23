import random

print("=" * 35)
print("     JOGO DA ADIVINHAÇÃO")
print("=" * 35)

while True:
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("\nPensei em um número entre 1 e 100.")
    print("Tente adivinhar!")

    while True:
        try:
            chute = int(input("\nDigite seu palpite: "))
            tentativas += 1

            if chute < 1 or chute > 100:
                print("Digite um número entre 1 e 100.")
                continue

            if chute < numero_secreto:
                print("O número é MAIOR.")

            elif chute > numero_secreto:
                print("O número é MENOR.")

            else:
                print(f"\n🎉 Parabéns! Você acertou!")
                print(f"Número secreto: {numero_secreto}")
                print(f"Tentativas: {tentativas}")
                break

        except ValueError:
            print("Digite apenas números inteiros.")

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()

    if jogar_novamente != "s":
        print("Obrigado por jogar!")
        break