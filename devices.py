class Device:
    def __init__(self, identifier, type, status, product_name, name=None):
        self.identifier = identifier
        self.type = type
        self.status = status
        self.product_details = product_name
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.identifier}) TYPE: {self.type} STATUS: {self.status} PRODUCT DETAILS: {self.product_details} NAME: {self.name}"


class Sensor(Device):
    def __init__(self, identifier, type, status, product_name, name=None):
        super().__init__(identifier, type, status, product_name, name)


class Actuator(Device):
    def __init__(self, identifier, type, status, product_name, name=None):
        super().__init__(identifier, type, status, product_name, name)
