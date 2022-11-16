import abc
class otrosparqueaderos(abc.ABC):
    @abc.abstractmethod
    def informacion():
        ...
    @abc.abstractmethod
    def AcceptingCars():
        ...

class parqueadero():
    def __init__(self, spacescompac=int, spacesSUV = int, spacesvan = int) :
        self.spccompac = spacescompac
        self.spcSUV = spacesSUV
        self.spcvan = spacesvan
        

    def informacion(self):
        self.dinero = 0 
        print(f"Puestos:{self.spccompac}, {self.spcSUV}, {self.spcvan}") 
        print(f"Dinero obtenido: {self.dinero}")
    
    def entradaparqueadero(self, data):
        if (data.self.llegada > 6 and data.self.llegada < 18):
            self.AcceptingCars()
        else:
            print("Parqueadero cerrado")
    
    def AcceptingCars(self, data):               
            pass

class vehiculo(abc.ABC):
    @abc.abstractmethod
    def PayCharge():
        ...                   

class Vehiculo(vehiculo):
    def __init__(self, tipo, hours, llegada):
        self.tipo = tipo        
        self.hour = hours
        self.llegada = llegada
        if (not isinstance(self.tipo, str)):
            raise TypeError("Debe ser string, son tipos de carros")

    @property
    def pago(self):
        return ((self.hour*24)*2000*24) + ((self.hour)*2000) + ((self.hour)*2000/3600)
        
    def PayCharge(self):           
        if self.tipo == "van":
            self.pago *= 1
            

        

