import serial
import time

# Clase para manejar la comunicación con Arduino
class ArduinoController:
    def __init__(self, port, baudrate=9600):
        self.serial_port = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Espera a que Arduino se reinicie

    def send_hex(self, hex_char):
        if hex_char.upper() in '0123456789ABCDEF':
            self.serial_port.write(hex_char.upper().encode())
            print(f"[✔] Enviado: {hex_char.upper()}")
        else:
            print("[✘] Entrada no válida. Usa caracteres hexadecimales (0-F).")

    def close(self):
        self.serial_port.close()

# Clase principal de la aplicación
class HexLedApp:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        print("Presiona una tecla hexadecimal (0-F), 'q' para salir.")
        while True:
            key = input(">> ").strip()
            if key.lower() == 'q':
                break
            self.controller.send_hex(key)

        self.controller.close()

# Uso del programa
if __name__ == "__main__":
    port = "COM3"  # Cambiar por el puerto de tu Arduino (ej. "/dev/ttyUSB0" en Linux)
    arduino = ArduinoController(port)
    app = HexLedApp(arduino)
    app.run()
