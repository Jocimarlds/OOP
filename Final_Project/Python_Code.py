import serial
import time

class ComunicadorSerial:
    """
    Clase encargada de manejar la comunicación serial con Arduino.
    Aplica encapsulamiento y abstracción.
    """
    def __init__(self, puerto: str, baudios: int = 9600):
        self.puerto = puerto
        self.baudios = baudios
        try:
            self.serial = serial.Serial(self.puerto, self.baudios, timeout=1)
            time.sleep(2)  # Esperar a que Arduino se reinicie al abrir puerto
            print(f"[✓] Conectado a {self.puerto} exitosamente.")
        except serial.SerialException as e:
            print(f"[X] Error al conectar con {self.puerto}: {e}")
            self.serial = None

    def enviar_hex(self, dato: str):
        """
        Envía un carácter hexadecimal (0-F) al Arduino
        """
        if self.serial and self.serial.is_open:
            dato = dato.upper()
            if len(dato) == 1 and dato in "0123456789ABCDEF":
                self.serial.write(dato.encode())
                print(f"[→] Enviado: {dato}")
            else:
                print("[!] Entrada inválida. Ingresa un valor hexadecimal (0-F).")
        else:
            print("[X] Puerto no disponible.")

    def cerrar(self):
        """
        Cierra el puerto serial correctamente
        """
        if self.serial and self.serial.is_open:
            self.serial.close()
            print(f"[✓] Puerto {self.puerto} cerrado.")


class InterfazUsuario:
    """
    Clase que representa la interfaz del usuario (separación de responsabilidades).
    """
    def __init__(self, comunicador: ComunicadorSerial):
        self.comunicador = comunicador

    def iniciar(self):
        """
        Bucle principal de interacción con el usuario
        """
        print("╭─────────────────────────────╮")
        print("│ Control de LEDs en Arduino │")
        print("╰─────────────────────────────╯")
        print("Ingresa un valor hexadecimal (0–F) o 'Q' para salir.")
        while True:
            entrada = input("Hex > ").strip().upper()
            if entrada == 'Q':
                print("Saliendo del programa...")
                break
            self.comunicador.enviar_hex(entrada)
        self.comunicador.cerrar()


if __name__ == "__main__":
    comunicador = ComunicadorSerial(puerto="COM60")
    interfaz = InterfazUsuario(comunicador)
    interfaz.iniciar()
