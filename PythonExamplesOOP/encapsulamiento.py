class Speaker:
    brand = "Beatpill"

    def __init__(self, color, model):
        self._color = color  # Private attribute
        self._model = model  # Private attribute

    def power_on(self):
        print(f"Powering on {self._color} {self._model} speaker.")

    def power_off(self):
        print(f"Powering off {self._color} {self._model} speaker.")

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        self._color = new_color


speaker_one = Speaker("black", "85XB5")
speaker_one.power_on()

# Accessing a private attribute directly (not recommended)
print(speaker_one._color)

# Accessing a private attribute using the getter method (recommended)
print(speaker_one.get_color())

# Modifying a private attribute using the setter method (recommended)
speaker_one.set_color("white")
print(speaker_one.get_color())