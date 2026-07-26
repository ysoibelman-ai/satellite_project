from space_network_lib import *
from time import sleep

class Satellite (SpaceEntity):
    def __int__(self,name: str, distance_from_earth: int | float):
        super().__init__(self,name,distance_from_earth)

    def receive_signal(self, packet):
        print (f"{self.name} Received: {packet}")

class BrokenConnectionError (CommsError):
    pass

def attempt_transmission(packet: Packet):

    while True:

        try:
            israel_space_network.send(packet)
            break

        except TemporalInterferenceError:
            print ("Interference, waiting...")
            sleep (2)
            
        except DataCorruptedError:
            print ("Data corrupted. retrying...")

        except LinkTerminatedError:
            print ("Link Lost")
            raise BrokenConnectionError

        except OutOfRangeError:
            print ("Out of range")
            raise BrokenConnectionError

            
israel_space_network = SpaceNetwork(level = 3)
Sat1 = Satellite("Sat1", 100)
Sat2 = Satellite("Sat2", 200)
packet_1 = Packet ("this is an important secret message",Sat1,Sat2,)
try:
    attempt_transmission(packet_1)
except BrokenConnectionError:
    print ("Transmission failed")
