public class CajeroAutomatico {
    private CuentaBancaria cuenta; //Creación de atributo privado de la cuenta

    // Constructor de la clase de cajero
    public CajeroAutomatico(double saldoInicial) {
        this.cuenta = new CuentaBancaria(saldoInicial);
    }

    // Método público para retirar dinero
    public boolean retirarDinero(double cantidad) {
        return cuenta.retirar(cantidad);
    }

    // Método público para depositar dinero
    public void depositarDinero(double cantidad) {
        cuenta.depositar(cantidad);
    }

    // Método público para consultar saldo
    public double consultarSaldo() {
        return cuenta.getSaldo();
    }
}
