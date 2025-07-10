// Clase para manejar los LEDs
class LedManager {
  private:
    int ledPins[4];  // Pines conectados a los LEDs

  public:
    // Constructor que recibe los pines
    LedManager(int pin0, int pin1, int pin2, int pin3) {
      ledPins[0] = pin0;
      ledPins[1] = pin1;
      ledPins[2] = pin2;
      ledPins[3] = pin3;
      for (int i = 0; i < 4; i++) {
        pinMode(ledPins[i], OUTPUT);
      }
    }

    // Método para mostrar número binario en LEDs
    void displayBinary(byte value) {
      for (int i = 0; i < 4; i++) {
        digitalWrite(ledPins[i], (value >> i) & 0x01);
      }
    }
};

LedManager leds(2, 3, 4, 5);  // Instancia de la clase con los pines

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char input = Serial.read();         // Leer carácter
    byte value = hexCharToByte(input);  // Convertir a valor binario
    leds.displayBinary(value);          // Mostrar en LEDs
  }
}

// Convierte carácter '0' - 'F' a número 0 - 15
byte hexCharToByte(char c) {
  if (c >= '0' && c <= '9') return c - '0';
  if (c >= 'A' && c <= 'F') return c - 'A' + 10;
  if (c >= 'a' && c <= 'f') return c - 'a' + 10;
  return 0;
}
