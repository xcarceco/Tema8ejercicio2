#En este segundo ejercicio, tendréis que crear un archivo py
# y dentro crearéis una clase Vehículo, haréis un objeto de ella,
# lo guardaréis en un archivo y luego lo cargamos.

class Vehiculo():
    def __init__(self, marca, color, placa, modelo):
        # Propiedades
        self.numero_llantas = 4
        self.marca = marca
        self.color = color
        self.placa = placa
        self.modelo = modelo
    def acelerar(self):
        print(f"Soy {self.marca}, estoy acelerando!!")
    def frenar(self):
        print(f"Soy {self.marca}, estoy frenando!!")
    def voltear(self, direccion):
        print(f"Soy {self.marca}, estoy volteando a la {direccion}")
    def __str__(self):

       return self.marca

obj_mazda = Vehiculo('Mazda 6', 'Rojo', 'RED126', '2020')
obj_renault =Vehiculo('Renault Clio', 'Negro', 'FRE009', '2021')
obj_audi =Vehiculo('Audi Q3', 'Blanco', 'DPK312', '2016')

