public class Main {
    public static void main(String[] args) {
        Operations resultado = new Operations();

        resultado.sumar(3, 2); //  la suma
        System.out.println(resultado.getResultado()); // Obtener el resultado usando getResultado()

        resultado.restar(10, 5); //  la resta
        System.out.println(resultado.getResultado());

        resultado.multiplicar(2, 2); // la multiplicacion
        System.out.println(resultado.getResultado());

        //resultado.potencia(2, 4); //  la potencia
        //System.out.println(resultado.getResultado());
    }
}
