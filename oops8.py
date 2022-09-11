class mother_bord:
    processer = 0
    cores = 0
    ram = 0
    rom = 0
    speed = 0
class pocket_device(mother_bord):
    networking_bands = 0
    network_driver = 0
    bluetooth_version = 0
    wifi_gen = 0
class phone(pocket_device):
    screen = "not named"
    speker = "not mentiond"
    camra = 0
    usb = "not mentioned"
    def __init__(self,screen,speker,camra,usb):
        self.screen = screen
        self.speker = speker
        self.camra = camra
        self.usb = usb
    @classmethod
    def phon_details(clr,string):
        return clr(*string.split("-"))
    @classmethod
    def set_bord_data(clr,networking_bands,network_driver,bluetooth_version,wifi_gen):
        clr.networking_bands = networking_bands
        clr.network_driver =  network_driver 
        clr.bluetooth_version = bluetooth_version 
        clr.wifi_gen = wifi_gen
    @classmethod
    def set_device_data(clr,processer,cores,speed,ram,rom):
        clr.processer=processer
        clr.cores = cores
        clr.speed = speed
        clr.ram = ram
        clr.rom = rom
    
smart_phone = phone.phon_details("amoled-hi_res-48-C")
smart_phone.set_bord_data(6,5,5.4,10)
smart_phone.set_device_data(64,8,5.5,12,124)

def print_function(self):
    print(f"The device have a {self.processer} bit processor\n The speed of the processor is {self.speed} Hz \n The processor have {self.cores} cores \n It have {self.ram} Gb ram on bord \n It have {self.rom} Gb rom on bord \n")
    print(f"The device have {self.screen} Display\n The speker of the phone is {self.speker} certified \n The camra is {self.camra} MP \n It have USB type {self.usb} in it")
    print(f"The device have {self.networking_bands} network bands \n The speed phone is {self.network_driver} G \n It have bluetooth {self.bluetooth_version} \n It wifi {self.wifi_gen} Gen")
    
print_function(smart_phone)