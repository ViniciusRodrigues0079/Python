class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

class Carro (Veiculo):
    def ligar (self):
        print (f"{self.modelo} agora está ligado.")

    def desligar (self):
        print (f"{self.modelo} agora está desligado.")

    def buzinar (self):
        print (f"{self.modelo}: BEEP BEEP!")

    def status (self):
        print (f"""
        Modelo do carro: {self.modelo}.
        Ano do carro: {self.ano}.
               """)

class Moto (Veiculo):
    def ligar (self):
        print (f"{self.modelo} agora está ligado.")

    def desligar (self):
        print (f"{self.modelo} agora está desligado.")

    def buzinar (self):
        print (f"{self.modelo}: BEEP BEEP!")

    def status (self):
        print (f"""
        Modelo da moto: {self.modelo}.
        Ano da moto: {self.ano}.
               """)