from devices import Device, SmartLight, SmartThermostat
from typing import List, Optional

class Room:
    """Representerer et rom i en etasje i ett hus.
        Et rom har et areal og det kan gis et kort navn.
        På et romm kan også registreres smarte enheter."""

    def __init__(self, area: float, name: str = None):
        self.area = area
        self.name = name

    def __repr__(self):
        return f"{self.name} ({self.area} m^2)"


class Floor:
    """Representerer en etasje i ett hus.
        En etasje har et entydig nummer og består av flere rom."""

    def __init__(self, floor_no: int):
        self.floor_no = floor_no
        self.rooms = []


class SmartHouse:
    """Den sentrale klasse i et smart hus system.
        Den forvalter etasjer, rom og enheter.
        Også styres alle enheter sentralt herifra."""

    def __init__(self):
        self.floors = []

    def create_floor(self) -> Floor:
        """Legger til en etasje og gi den tilbake som objekt.
            Denne metoden ble kalt i initialiseringsfasen når
            strukturen av huset bygges opp-."""
        floor = Floor()
        self.floors.append(floor)

    def create_room(self, floor_no: int, area: float, name: str = None) -> Room:
        """Legger til et rom i en etasje og gi den tilbake som objekt.
            Denne metoden ble kalt i initialiseringsfasen når
            strukturen av huset bygges opp-."""
        floor = self.floors[floor_no]
        room = Room(floor_no, area, name)
        floor.rooms.append(room)


    def get_no_of_rooms(self) -> int:
        """Gir tilbake antall rom i huset som heltall"""
        return sum(len(floor.rooms) for floor in self.floors)

    def get_all_devices(self) -> List[Device]:
        """Gir tilbake en liste med alle enheter som er registrert i huset."""
        return self.devices

    def get_all_rooms(self) -> List[Room]:
        """Gir tilbake en liste med alle rom i huset."""
        return self.rooms

    def get_total_area(self) -> float:
        """Regner ut det totale arealet av huset."""
        return self.total_area

    def register_device(self, device: Device, room: Room):
        """Registrerer en enhet i et gitt rom."""
        room.devices.append(device)

    def get_no_of_devices(self) -> int:
        """Gir tilbake antall registrerte enheter i huset."""
        return len(self.devices)

    def get_no_of_sensors(self) -> int:
        """Git tilbake antall av registrerte sensorer i huset."""
        return len(self.sensors)

    def get_no_of_actuators(self) -> int:
        """Git tilbake antall av registrerte aktuatorer i huset."""
        return len(self.actuators)

    def move_device(self, device: Device, from_room: Room, to_room: Room):
        """Flytter en enhet fra et gitt romm til et annet."""
        device_moved = False
        for room in self.rooms:
            if room == from_room:
                room.devices.remove(device)
                device_moved = True
            if room == to_room and device_moved:
                room.devices.append(device)
            return True
        return False

    def find_device_by_serial_no(self, serial_no: str) -> Optional[Device]:
        """Prøver å finne en enhet blant de registrerte enhetene ved å
        søke opp dens serienummer."""
        for device in self.devices:
            if device.identifier == serial_no:
                return device
            else:
                return None

    def get_room_with_device(self, device: Device):
        """Gir tilbake rommet der en gitt enhet er resitrert."""
        for room in self.rooms:
            if device in room.devices:
                return room
            else:
                return None

    def get_all_devices_in_room(self, room: Room) -> List[Device]:
        """Gir tilbake en liste med alle enheter som er registrert på rommet."""
        for room in self.rooms:
            if room == room:
                return room.devices
            else:
                return None

    def turn_on_lights_in_room(self, room: Room):
        """Slår på alle enheter av type 'Smart Lys' i et gitt rom."""
        for device in room.devices:
            if device.type == "Smart Lys":
                return device.turn_on()
            else:
                return None

    def turn_off_lights_in_room(self, room: Room):
        """Slår av alle enheter av type 'Smart Lys' i et gitt rom."""
        for device in room.devices:
            if device.type == "Smart Lys":
                return device.turn_off()
            else:
                return None

    def get_temperature_in_room(self, room: Room) -> Optional[float]:
        """Prøver å finne ut temperaturen i et gitt rom ved å finne
        enheter av type 'Temperatursensor' der og gi tilake verdien som kommatall."""
        for device in room.devices:
            if device.type == "Temperatursensor":
                return device.get_value()
            else:
                return None
    def set_temperature_in_room(self, room: Room, temperature: float):
        """Prøver å sette temperaturen i et gitt rom ved å sette alle aktuatorer
        som kan påvirke temperatur ('Paneloven', 'Varmepumpe', ...) til ønsket
        temperatur."""
        for device in room.devices:
            if device.type == "Paneloven" or device.type == "Varmepumpe" or device.type == "Gulvvarmepanel":
                return device.set_value(temperature)
            else:
                return None
