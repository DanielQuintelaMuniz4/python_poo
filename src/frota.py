class Carro:
    modelo : str
    marca : str
    cor : str
    __odometro : 0.0
    __motor_on : False
    __tanque = 0.0
    consumo_medio : float

    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool, tanque : float, consumo_medio : float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = odometro
        self.motor_on = motor
        self.__tanque = tanque
        self.consumo_medio = consumo_medio

    def ligar(self):
        if not self.motor_on and self.__tanque > 0:
            self.motor_on = True
        else:
            raise Exception("Erro: Motor já ligado ou tanque vazio!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.motor_on and self.__tanque > 0:
            km = velocidade * tempo
            litros = km / self.consumo_medio

            if self.__tanque >= litros:
                self.__tanque -= litros
            else:
                km = litros * self.consumo_medio
                self.__tanque = 0
                self.desligar()
                self.__odometro += km
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado ou sem combustível!")

    def desligar(self):
        if self.motor_on:
            self.motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.motor_on}')
        return info
    
    def get_odometro(self):
        return self.__odometro

    def get_tanque(self):
        return self.__tanque





