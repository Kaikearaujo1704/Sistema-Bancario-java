import random

opcoes = ["pedra", "papel", "tesoura"]

print("=" * 35)
print("     PEDRA, PAPEL E TESOURA")
print("=" * 35)

while True:
    print("\nEscolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("4 - Sair")

    escolha = input("\nDigite a opção: ")

    if escolha == "4":
        print("Até a próxima!")
        break

    if escolha not in ["1", "2", "3"]:
        print("Opção inválida!")
        continue

    jogador = opcoes[int(escolha) - 1]
    computador = random.choice(opcoes)

    print(f"\nVocê escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Resultado: Empate!")

    elif (
        (jogador == "pedra" and computador == "tesoura") or
        (jogador == "papel" and computador == "pedra") or
        (jogador == "tesoura" and computador == "papel")
    ):
        print("Resultado: Você venceu!")

    else:
        print("Resultado: Você perdeu!")

    novamente = input("\nJogar novamente? (s/n): ").lower()

    if novamente != "s":
        print("Obrigado por jogar!")
        break