#Atributos e Instaciación
class Speaker:
    brand = "Beatpill" # Atributo de clase

    def __init__(self, color, model):
        self.color = color # instance 
        self.model = model # model
speaker_one = Speaker("black", "85XB5")
speaker_two = Speaker("red", "Y8F33")

print(
    f"speaker one is {speaker_one.color} while speaker two is {speaker_two.color}",
    speaker_one.brand,
    speaker_two.brand,
    sep="\n",
)