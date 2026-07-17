public class Conta {

    private int numero;
    private String titular;
    private double saldo;

    public Conta(int numero, String titular) {
        this.numero = numero;
        this.titular = titular;
        this.saldo = 0;
    }

    public int getNumero() {
        return numero;
    }

    public String getTitular() {
        return titular;
    }

    public double getSaldo() {
        return saldo;
    }

    public void depositar(double valor) {

        if (valor > 0) {
            saldo += valor;
            System.out.println("Depósito realizado.");
        } else {
            System.out.println("Valor inválido.");
        }

    }

    public void sacar(double valor) {

        if (valor <= saldo && valor > 0) {

            saldo -= valor;
            System.out.println("Saque realizado.");

        } else {

            System.out.println("Saldo insuficiente.");

        }

    }

    public void mostrarConta() {

        System.out.println("-----------------------");
        System.out.println("Conta: " + numero);
        System.out.println("Titular: " + titular);
        System.out.println("Saldo: R$ " + saldo);
        System.out.println("-----------------------");

    }

}
