import java.util.ArrayList;

public class Banco {

    ArrayList<Conta> contas = new ArrayList<>();

    public void criarConta(int numero, String nome) {

        contas.add(new Conta(numero, nome));

        System.out.println("Conta criada!");

    }

    public Conta procurarConta(int numero) {

        for (Conta c : contas) {

            if (c.getNumero() == numero) {

                return c;

            }

        }

        return null;

    }

    public void listarContas() {

        if (contas.isEmpty()) {

            System.out.println("Nenhuma conta cadastrada.");
            return;

        }

        for (Conta c : contas) {

            c.mostrarConta();

        }

    }

    public void removerConta(int numero) {

        Conta conta = procurarConta(numero);

        if (conta != null) {

            contas.remove(conta);

            System.out.println("Conta removida.");

        } else {

            System.out.println("Conta não encontrada.");

        }

    }

}
