/*
  PROYECTO DE ARDUINO POO (CON SENSOR)
  Realizado por: Jocimar David Gutiérrez Ladeut
  Universidad Distrital Francisco José de Caldas | Ing. Electrónica
*/

// Clase Led (igual)
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

// Clase SensorIR (como Button, pero más semántico)
class SensorIR {
  private:
    int pin;
    bool ultimoEstado;
    unsigned long ultimoTiempo;
    const unsigned long debounceDelay = 100; // 100 ms antirrebote

  public:
    SensorIR(int p) {
      pin = p;
      pinMode(pin, INPUT);
      ultimoEstado = detectaObjeto();
      ultimoTiempo = 0;
    }

    bool detectaObjeto() {
      return digitalRead(pin) == LOW; // LOW = objeto detectado (depende del sensor)
    }

    bool fueDetectado() {
      bool estadoActual = detectaObjeto();
      unsigned long tiempoAhora = millis();
      bool detectado = false;

      if (estadoActual && !ultimoEstado && (tiempoAhora - ultimoTiempo > debounceDelay)) {
        detectado = true;
        ultimoTiempo = tiempoAhora;
      }

      ultimoEstado = estadoActual;
      return detectado;
    }
};

// Crear LEDs y sensor IR
Led leds[4] = { Led(2), Led(3), Led(4), Led(5) };
SensorIR sensor(7);  // Pin del sensor IR

// Variables de control
int indice = 0;
int direccion = 1;

void setup() {
  // Nada extra
}

void loop() {
  if (sensor.fueDetectado()) {
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
      indice = 2;
      direccion = -1;
    } else if (indice < 0) {
      indice = 1;
      direccion = 1;
    }
  }
}
