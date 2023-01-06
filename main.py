class Tankas:
    def __init__(self):
        self.x = []
        self.y = []
        self.kryptis = ["siaure"]
        self.boom_kryptis = {"Issauta kartu i siaure: ": 0, "Issauta kartu i pietus: ": 0,
                              "Issauta kartu i rytus: ": 0, "Issauta kartu i vakarus: ": 0}
        sum(self.boom_kryptis.values())


    def position_coord(self):
        x_suma = sum(self.x)
        y_suma = sum(self.y)
        print("x: ", x_suma, "y: ", y_suma)


    def forward(self):
        self.y.append(1)
        self.kryptis[0] = "siaure"

    def backward(self):
        self.y.append(-1)
        self.kryptis[0] = "pietus"

    def left(self):
        self.x.append(-1)
        self.kryptis[0] = "vakarai"

    def right(self):
        self.x.append(1)
        self.kryptis[0] = "rytai"

    def shoot(self):
        if self.kryptis[0] == "siaure":
            self.boom_kryptis["Issauta kartu i siaure: "] += 1
            print("Issauta kartu i siaure: ", self.boom_kryptis["Issauta kartu i siaure: "])

        if self.kryptis[0] == "pietus":
            self.boom_kryptis["Issauta kartu i pietus: "] += 1
            print("Issauta kartu i pietus: ", self.boom_kryptis["Issauta kartu i pietus: "])

        if self.kryptis[0] == "vakarai":
            self.boom_kryptis["Issauta kartu i vakarus: "] += 1
            print("Issauta kartu i vakarus: ", self.boom_kryptis["Issauta kartu i vakarus: "])

        if self.kryptis[0] == "rytai":
            self.boom_kryptis["Issauta kartu i rytus: "] += 1
            print("Issauta kartu i rytus: ", self.boom_kryptis["Issauta kartu i rytus: "])

    def info(self):
        print("-------------------------------------------")
        print(f"x: {sum(self.x)}, y: {sum(self.y)}")
        print("Kryptis i kuria pasisukes: ", self.kryptis[0])
        print("Isviso issauta kartu: ", sum(self.boom_kryptis.values()))
        print("Issauta kartu i siaure: ", self.boom_kryptis["Issauta kartu i siaure: "])
        print("Isauta kartu i pietus: ", self.boom_kryptis["Issauta kartu i pietus: "])
        print("Issauta kartu i vakarus: ", self.boom_kryptis["Issauta kartu i vakarus: "])
        print("Issauta kartu i rytus: ", self.boom_kryptis["Issauta kartu i rytus: "])
        print("-------------------------------------------")
tankas = Tankas()

while True:
    veiksmas = input("""Pasirinkite veiksma:
w - Vaziuoti i prieki
s - Vaziuoti i gala
a - Vaziuoti i kaire
d - Vaziuoti i desine
e - Sauti
i - Parodyti statistika
q - Baigti zaidima
""")
    if veiksmas == "w":
        tankas.forward()
        tankas.position_coord()
    elif veiksmas == "s":
        tankas.backward()
        tankas.position_coord()
    elif veiksmas == "a":
        tankas.left()
        tankas.position_coord()
    elif veiksmas == "d":
        tankas.right()
        tankas.position_coord()
    elif veiksmas == "e":
        tankas.shoot()
        tankas.position_coord()
    elif veiksmas == "i":
        tankas.info()
    elif veiksmas == "q":
        print("Zaidimas baigtas")
        break





