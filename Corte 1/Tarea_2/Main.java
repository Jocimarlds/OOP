public class Main {

    public static void main(String[] args) {
          
        Operations resultado = new Operations();
        
        resultado.sumar(3, 2);
        System.out.println("El resultado de la suma es: " + resultado.getR());
        
        resultado.restar(10, 5);
        System.out.println("La diferencia es igual a: " + resultado.getR());
        
        resultado.multiplicar(10, 100);
        System.out.println("El producto de la multiplicacion es: " + resultado.getR());
        
        resultado.potencia(10, 2);
        System.out.println("El resultado de la potencia es: " + resultado.getR());
    }  
}
