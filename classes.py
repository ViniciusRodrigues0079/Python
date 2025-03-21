#class Cachorro:
#    def  __init__(self, nome, raça, comida, energia):
#        self.nome = nome
#        self.raça = raça
#        self.comida = comida
#        self.energia = energia
#        self.acordado = True
#        self.feliz = True
#    def comer (self):
#        self.comida -= 1
#        print (f"{self.nome} está comendo.")
#    def dormir (self):
#        self.energia = 100
#        self.acordado = False
#        print (f"{self.nome} está dormindo.")
#    def acordar (self):
#        self.acordado = True
#        print (f"{self.nome} está acordado.")
#    def brincar (self):
#        if self.energia <= 20:
#            print (f"{self.nome} está muito cansado para brincar.")
#        else:
#            self.energia -= 20
#            self.feliz = True
#            print (f"{self.nome} está feliz.")
#    def ignorar (self):
#        self.feliz = False
#        print (f"{self.nome} está triste.")
#    def latir (self):
#        if self.energia == 0:
#            print (f"{self.nome} não pode latir agora, ele precisa dormir.")
#        else:
#            if self.acordado:
#                print (f"{self.nome}: Au!")
#                self.energia -= 1
#            else:
#                print (f"{self.nome} não pode latir agora, {self.nome} está dormindo.")
#cachorro1 = Cachorro("Batata", "Bulldog", 22, 100)
#cachorro2 = Cachorro("Reed", "Pastor alemão", 5, 100)

#class Carro:
#    def  __init__(self, modelo, ano, cor, combustivel, velocidade):
#        self.modelo = modelo
#        self.ano = ano
#        self.cor = cor
#        self.combustivel = combustivel
#        self.velocidade = velocidade
#        self.ligado = False
#    
#    def ligar (self):
#        self.ligado = True
#        print (f"{self.modelo} agora está ligado.")
#    
#    def desligar (self):
#        self.ligado = False
#        print (f"{self.modelo} agora está desligado.")
#    
#    def acelerar (self):
#        if self.ligado:
#            if self.combustivel == 0:
#                print ("Seu tanque de combustível está vazio. Abasteça-o para andar.")
#            else:
#                self.velocidade += 10
#                self.combustivel -= 5
#                print (f"Acelerando {self.modelo} em 10 km/h.")
#        else:
#            print ("É preciso ligar seu carro antes de acelerar!")
#    
#    def frear (self):
#        if self.ligado:
#            print (f"reduzindo a velocidade de {self.modelo} em 10 km/h.")
#        else:
#            print (f"É necessário ligar seu carro para frear!")
#    
#    def abastecer(self):
#        self.combustivel = 100
#        print ("Tanque abastecido!")
#
#    def buzinar (self):
#        print ("BEEP BEEP!")
#    
#    def status (self):
#        print (f"""
#        Modelo do carro: {self.modelo}.
#        Ano do carro: {self.ano}.
#        Cor do carro: {self.cor}.
#        Combustível disponível: {self.combustivel} litros.
#        Velocidade atual: {self.velocidade} km/h.
#        """)
#        if self.ligado:
#            print ("Estado atual: Ligado.")
#        else:
#            print ("Estado atual: Desligado.")
#
#carro1 = Carro("BMW 320i", 2023, "Azul escuro", 70, 0)