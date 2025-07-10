class LedBinario {
  private:
    // Orden de pines: [MSB, ..., LSB] → pin 2 (bit 3) hasta pin 5 (bit 0)
    const byte pines[4] = {2, 3, 4, 5};

  public:
    void iniciar() {
      for (int i = 0; i < 4; i++) {
        pinMode(pines[i], OUTPUT);
        digitalWrite(pines[i], LOW);
      }
      Serial.begin(9600);
    }

    void mostrar(byte valor) {
      for (int i = 0; i < 4; i++) {
        // Bit 0 controla pin 5, bit 1 pin 4, etc.
        digitalWrite(pines[3 - i], (valor >> i) & 1);
      }
    }
};

LedBinario leds;

void setup() {
  leds.iniciar();
}

void loop() {
  if (Serial.available()) {
    char recibido = Serial.read();
    byte valor = 0;

    if (recibido >= '0' && recibido <= '9') {
      valor = recibido - '0';
    } else if (recibido >= 'A' && recibido <= 'F') {
      valor = recibido - 'A' + 10;
    } else if (recibido >= 'a' && recibido <= 'f') {
      valor = recibido - 'a' + 10;
    }

    leds.mostrar(valor);
  }
}
