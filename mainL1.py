from space_network_lib import *
from time import sleep

class Satellite (SpaceEntity):
    def __int__(self,name: str, distance_from_earth: int | float):
        super().__init__(self,name,distance_from_earth)

    def receive_signal(self, packet):
        print (f"{self.name} Received: {packet}")


israel_space_network = SpaceNetwork(level = 2)
Sat1 = Satellite("Sat1", 100)
Sat2 = Satellite("Sat2", 200)

valid = False
packet_1 = Packet ("this is an important secret message",Sat1,Sat2,)
 
while valid == False:

    try:
          israel_space_network.send(packet_1)
          valid = True
    
    except TemporalInterferenceError, DataCorruptedError:
        continue




