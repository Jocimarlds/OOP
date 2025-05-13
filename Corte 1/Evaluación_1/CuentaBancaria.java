public class CuentaBancaria {
    private double saldo; // Creación de atributo de saldo como privado

    // Constructor de la clase cuenta bancaria
    public CuentaBancaria(double saldoInicial) {
        this.saldo = saldoInicial;
    }

    // Getter para saldo (acceso público)
    public double getSaldo() {
        return saldo;
    }

    // Setter para saldo (acceso público), si es necesario cambiar el saldo directamente
    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    // Método para retirar dinero
    public boolean retirar(double cantidad) {
        if (cantidad > saldo) {
            return false; // No hay suficiente saldo
        }
        saldo -= cantidad;
        return true;
    }

    // Método para depositar dinero
    public void depositar(double cantidad) {
        saldo += cantidad;
    }
}
