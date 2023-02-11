class Device:
    def __init__(self, nr: int, type, producer, product_name, serial_number, status, name=None):
        self.nr = nr
        self.type = type
        self.producer = producer
        self.product_name = product_name
        self.status = status
        self.serial_number = serial_number
        self.name = name
    def __repr__(self):
       f"{self.__class__.__name__}({self.serial_number}) Nr:{self.nr} TYPE: {self.type} STATUS: {self.status} PRODUCT DETAILS: {self.product_name} NAME: {self.name}"

class Sensor(Device):
    def __init__(self,nr, type, producer, product_name, serial_number, status):
        super().__init__( nr,type, producer, product_name, serial_number, status, name=None)

class Actuator(Device):
    def __init__(self,nr, type, producer, product_name, serial_number, status):
        super().__init__(nr, type, producer, product_name, serial_number, status, name=None)