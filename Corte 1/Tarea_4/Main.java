import javax.swing.JOptionPane;

public class Main {

    public static void main(String[] args) {
        // Crear una instancia de la clase Operations
        Operations resultado = new Operations();

        // Mostrar un cuadro de diálogo para pedir los números
        String num1Str = JOptionPane.showInputDialog("Introduce el primer número:");
        String num2Str = JOptionPane.showInputDialog("Introduce el segundo número:");

        // Parsear los valores string a enteros
        int num1 = parseInteger(num1Str);
        int num2 = parseInteger(num2Str);

        // Realizar operaciones
        resultado.sumar(num1, num2);
        JOptionPane.showMessageDialog(null, "El resultado de la suma es: " + resultado.getR());

        resultado.restar(num1, num2);
        JOptionPane.showMessageDialog(null, "La diferencia es igual a: " + resultado.getR());

        resultado.multiplicar(num1, num2);
        JOptionPane.showMessageDialog(null, "El producto de la multiplicación es: " + resultado.getR());

        resultado.potencia(num1, num2);
        JOptionPane.showMessageDialog(null, "El resultado de la potencia es: " + resultado.getR());
    }

    // Método para parsear enteros
    private static int parseInteger(String value) {
        try {
            return Integer.parseInt(value);
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Error: Por favor, ingrese un número válido.");
            return 0; // Retorna 0 si el parseo falla
        }
    }
}
