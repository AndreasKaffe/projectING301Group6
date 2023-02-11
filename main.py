from smarthouse import SmartHouse, Room, Floor
from devices import *


def build_demo_house() -> SmartHouse:
    house = SmartHouse()

    #making rooms
    floor1 = house.create_floor()
    house.create_room(1, 39.75,"Living Room / Kitchen")
    house.create_room(1, 6.35,"Bathroom")
    house.create_room(1, 13.5,"Entrance")
    house.create_room(1, 8, "Guest Room 1")
    house.create_room(1, 19, "Garage")

    #registering devices
    house.register_device(Actuator(1,"Smart Lys",	"Fritsch Group",	"Tresom Bright 1.0",	"f11bb4fc-ba74-49cd","off","lys ved stuebord venstre"),"Living Room / Kitchen")
    house.register_device(Actuator(2,"Smart Lys",	"Fritsch Group",	"Alphazap 2",	"480dbae8-cce7-46d7","off","lys ved stue høyre"),"Living Room / Kitchen")
    house.register_device(Sensor(3,"Fuktighetssensor",	"Bernhard-Roberts",	"Andalax",	"4cb686fe-6448-4cf6", "68%","fuktighetssensor bad"),"Bathroom")
    house.register_device(Actuator(4,"Smart Lys",	"Fritsch Group",	"Alphazap 2",	"6a36c71d-4f48-4eb4","off","leselys i gjesterom"),"Guest Room 1")
    house.register_device(Actuator(5,"Smart Lys",	"Larkin-Nitzsche",	"Quo Lux",	"d01130c9-a368-42c6","off","garagelys"),"Garage")
    house.register_device(Actuator(6,"Billader",	"Jast, Hansen and Halvorson",	"Charge It 9000",	"0cae4f01-4ad9-47aa","off","billader"),"Garage")
    house.register_device(Actuator(7,"Paneloven",	"Hauck-DuBuque",	"Voyatouch 42",	"d16d84de-79f1-4f9a","off","ovn gjesterom 1"),"Guest Room 1")
    house.register_device(Sensor(8,"Temperatursensor",	"Moen Inc",	"Prodder Ute 1.22","e237beec-2675-4cb0", "1.3 °C","temperaturmåler ute"), None)
    house.register_device(Actuator(9,"Smart Lys",	"Fritsch Group",	"Alphazap 2","f4db4e54-cebe-428d","off","første lys i entre"),"Entrance")
    house.register_device(Actuator(10,"Smart Lys",	"Larkin-Nitzsche",	"Quo Vadis Lux",	"8d09aa92-fc58-4c6", "off", "utelys"),None)
    house.register_device(Sensor(11,"Strømmåler",	"Kilback LLC",	"Transcof Current",	"c8bb5601-e850-4a80", "0kWh","strømmåler kjøkken"),"Living Room / Kitchen")
    house.register_device(Sensor(12,"Temperatursensor",	"Moen Inc",	"Prodder Inne 2.3",	"d16d84de-79f1-4f9a", "18.1 °C", "temperaturmåler stue/kjøkken"),"Living Room / Kitchen")
    house.register_device(Actuator(13,"Smart Lys",	"Fritsch Group",	"Alphazap 2",	"390ae474-21fb-4e06", "off","andre lys i entre" ),"Entrance")
    house.register_device(Sensor(14,"Strømmåler",	"Ward-Schaefer",	"Zaam-Dox NetConnect",	"3b06cf0f-8494-458b","1.5 kWh","strømmåler i entre"),"Entrance")
    house.register_device(Actuator(15,"Smart Stikkontakt",	"Kilback LLC",	"Konklab 3",	"c28b6e75-d565-4678", "off","stikkontakt kjøkken"),"Living Room / Kitchen")
    house.register_device(Actuator(16,"Varmepumpe",	"Osinski Inc",	"Fintone XCX4AB",	"4eca6387-0767-4e4e","off","varmepumpe stue"),"Living Room / Kitchen")
    house.register_device(Sensor(17,"Luftkvalitetssensor",	"Hauck-DuBuque",	"Sonair Pro",	"c76688cc-3692-4aa3","0.08 g/m^2","luftkvalitetssensor stue"),"Living Room / Kitchen")
    house.register_device(Actuator(18,"Smart Stikkontakt",	"Kilback LLC",	"Konklab 3",	"4b9050f3-0ef0-4914","off","stikkontakt TV"),"Living Room / Kitchen")

    house.create_floor()
    house.create_room(2, 10,"Gang")
    house.create_room(2, 10,"Guest Room 3")
    house.create_room(2, 4,"Dressing Room")
    house.create_room(2, 17,"Master Bedroom")

    # #add devices
    # floor1.get_room("LivingRoom").add_device(SmartLight("Smart Lys","Fritsch Group","Tresom Bright 1.0","f11bb4fc-ba74-49cd",False))
    # floor1.get_room("LivingRoom").add_device(SmartThermostat("Smart Lys","Fritsch Group","Alphazap 2","480dbae8-cce7-46d7",False))
    # floor1.get_room("LivingRoom").add_device(SmartLight("Smart Lys","Fritsch Group","Tresom Bright 1.0","f11bb4fc-ba74-49cd",False))
    # floor1.get_room("Bathroom").add_device(SmartLight("Fuktighetssensor",	"Bernhard-Roberts","Andalax","4cb686fe-6448-4cf6",False))
    print(house)
    return house



def do_device_list(smart_house: SmartHouse):
    print("Listing Devices...")
    idx = 0
    for d in smart_house.get_all_devices():
        print(f"{idx}: {d}")
        idx += 1


def do_room_list(smart_house: SmartHouse):
    print("Listing Rooms...")
    idx = 0
    for r in smart_house.get_all_rooms():
        print(f"{idx}: {r}")
        idx += 1


def do_find(smart_house: SmartHouse):
    print("Please enter serial no: ")
    serial_no = input()
    device = smart_house.find_device_by_serial_no(serial_no)
    if device:
        devices = smart_house.get_all_devices()
        rooms = smart_house.get_all_rooms()
        room = smart_house.get_room_with_device(device)
        device_idx = devices.index(device)
        room_idx = rooms.index(room)
        print(f"Device No {device_idx}:")
        print(device)
        print(f"is located in room No {room_idx}:")
        print(room)
    else:
        print(f"Could not locate device with serial no {serial_no}")


def do_move(smart_house):
    devices = smart_house.get_all_devices()
    rooms = smart_house.get_all_rooms()
    print("Please choose device:")
    device_id = input()
    device = None
    if device_id.isdigit():
        device = devices[int(device_id)]
    else:
        device = smart_house.find_device_by_serial_no(device_id)
    if device:
        print("Please choose target room")
        room_id = input()
        if room_id.isdigit() and rooms[int(room_id)]:
            to_room = rooms[int(room_id)]
            from_room = smart_house.get_room_with_device(device)
            smart_house.move_device(device, from_room, to_room)
        else:
            print(f"Room with no {room_id} does not exist!")
    else:
        print(f"Device wit id '{device_id}' does not exist")


def main(smart_house: SmartHouse):
    print("************ Smart House Control *****************")
    print(f"No of Rooms:       {smart_house.get_no_of_rooms()}")
    print(f"Total Area:        {smart_house.get_total_area()}")
    print(f"Connected Devices: {smart_house.get_no_of_devices()} ({smart_house.get_no_of_sensors()} Sensors | {smart_house.get_no_of_actuators()} Actuators)")
    print("**************************************************")
    print()
    print("Management Interface v.0.1")
    while (True):
        print()
        print("Please select one of the following options:")
        print("- List all devices in the house (l)")
        print("- List all rooms in the house (r) ")
        print("- Find a device via its serial number (f)")
        print("- Move a device from one room to another (m)")
        print("- Quit (q)")
        char = input()
        if char == "l":
            do_device_list(smart_house)
        elif char == "r":
            do_room_list(smart_house)
        elif char == "f":
            do_find(smart_house)
        elif char == "m":
            do_move(smart_house)
        elif char == "q":
            break
        else:
            print(f"Error! Could not interpret input '{char}'!")


if __name__ == '__main__':
    house = build_demo_house()
    main(house)

