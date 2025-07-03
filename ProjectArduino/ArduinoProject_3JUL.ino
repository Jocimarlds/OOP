/*
  PROYECTO DE ARDUINO POO
  Realizado por: Jocimar David Gutiérrez Ladeut
  Universidad Distrital Francisco José de Caldas | Ing. Electrónica
*/

// Clase Led
class Led {
  private:
    int pin;

  public:
    Led(int p) {
      pin = p;
      pinMode(pin, OUTPUT);
      apagar();
    }

    void encender() {
      digitalWrite(pin, HIGH);
    }

    void apagar() {
      digitalWrite(pin, LOW);
    }
};

// Clase Button con detección de flanco y debounce
class Button {
  private:
    int pin;
    bool ultimoEstado;
    unsigned long ultimoTiempo;
    const unsigned long debounceDelay = 50; // 50 ms para antirrebote

  public:
    Button(int p) {
      pin = p;
      pinMode(pin, INPUT_PULLUP);
      ultimoEstado = estaPresionado();
      ultimoTiempo = 0;
    }

    bool estaPresionado() {
      return digitalRead(pin) == LOW;
    }

    // Detectar pulsación nueva con debounce
    bool fuePresionado() {
      bool estadoActual = estaPresionado();
      unsigned long tiempoAhora = millis();
      bool presionado = false;

      if (estadoActual && !ultimoEstado && (tiempoAhora - ultimoTiempo > debounceDelay)) {
        presionado = true;
        ultimoTiempo = tiempoAhora;
      }

      ultimoEstado = estadoActual;
      return presionado;
    }
};

// Crear LEDs y botón
Led leds[4] = { Led(2), Led(3), Led(4), Led(5) };
Button boton(6);

// Variables de control
int indice = 0;
int direccion = 1;

void setup() {
  // Nada extra
}

void loop() {
  if (boton.fuePresionado()) {
    // Apagar todos los LEDs
    for (int i = 0; i < 4; i++) {
      leds[i].apagar();
    }

    // Encender LED actual
    leds[indice].encender();

    // Calcular siguiente índice
    indice += direccion;

    // Cambiar dirección si llega a un extremo
    if (indice >= 4) {
      indice = 2; // Regresa al tercero
      direccion = -1;
    } else if (indice < 0) {
      indice = 1; // Avanza al segundo
      direccion = 1;
    }
  }
}
