public class Operations {
    
    // Atributos privados
    private int a, b, r;

    // Getters
    public int getA() {
        return a;
    }

    public int getB() {
        return b;
    }

    public int getR() {
        return r;
    }

    // Setters
    public void setA(int a) {
        this.a = a;
    }

    public void setB(int b) {
        this.b = b;
    }

    public void setR(int r) {
        this.r = r;
    }

    // Métodos para operaciones matemáticas

    public int sumar(int a, int b) {
        r = a + b;
        return r;
    }

    public int restar(int a, int b) {
        r = a - b;
        return r;
    }

    public int multiplicar(int a, int b) {
        r = a * b;
        return r;
    }

    public int potencia(int base, int exponente) {
        r = (exponente == 0) ? 1 : base * potencia(base, exponente - 1);
        return r;
    }
}
