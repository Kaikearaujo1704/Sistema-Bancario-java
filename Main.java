import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Banco banco = new Banco();

        int opcao;

        do {

            System.out.println("\nBANCO");
            System.out.println("1 - Criar Conta");
            System.out.println("2 - Depositar");
            System.out.println("3 - Sacar");
            System.out.println("4 - Consultar Saldo");
            System.out.println("5 - Listar Contas");
            System.out.println("6 - Remover Conta");
            System.out.println("0 - Sair");

            opcao = sc.nextInt();

            switch (opcao) {

                case 1:

                    System.out.print("Número da conta: ");
                    int numero = sc.nextInt();

                    sc.nextLine();

                    System.out.print("Nome: ");
                    String nome = sc.nextLine();

                    banco.criarConta(numero, nome);

                    break;

                case 2:

                    System.out.print("Conta: ");
                    numero = sc.nextInt();

                    Conta conta = banco.procurarConta(numero);

                    if (conta != null) {

                        System.out.print("Valor: ");

                        double valor = sc.nextDouble();

                        conta.depositar(valor);

                    } else {

                        System.out.println("Conta não encontrada.");

                    }

                    break;

                case 3:

                    System.out.print("Conta: ");

                    numero = sc.nextInt();

                    conta = banco.procurarConta(numero);

                    if (conta != null) {

                        System.out.print("Valor: ");

                        double valor = sc.nextDouble();

                        conta.sacar(valor);

                    } else {

                        System.out.println("Conta não encontrada.");

                    }

                    break;

                case 4:

                    System.out.print("Conta: ");

                    numero = sc.nextInt();

                    conta = banco.procurarConta(numero);

                    if (conta != null) {

                        System.out.println("Saldo: R$ " + conta.getSaldo());

                    } else {

                        System.out.println("Conta não encontrada.");

                    }

                    break;

                case 5:

                    banco.listarContas();

                    break;

                case 6:

                    System.out.print("Conta: ");

                    numero = sc.nextInt();

                    banco.removerConta(numero);

                    break;

                case 0:

                    System.out.println("Até logo!");

                    break;

                default:

                    System.out.println("Opção inválida.");

            }

        } while (opcao != 0);

    }

}
