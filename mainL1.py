from space_network_lib import *

class Satellite (SpaceEntity):
    def __int__(self,name: str, distance_from_earth: int | float):
        super().__init__(self,name,distance_from_earth)

    def receive_signal(self, packet):
        print (f"{self.name} Received: {packet}")


israel_space_network = SpaceNetwork(level = 1)
Sat1 = Satellite("Sat1", 100)
Sat2 = Satellite("Sat2", 200)

packet_1 = Packet ("this is an important secret message",Sat1,Sat2,)
israel_space_network.send(packet_1)







    
