import Hardware

import time
import sys






SECONDS_TO_WATER = 30
RELAY = Hardware.Relay(12, False)



def water_plant(relay=RELAY, seconds=SECONDS_TO_WATER):
    relay.on()
    print("Plant is being watered!")
    time.sleep(seconds)
    relay.off()



if __name__ == "__main__":
    water_plant()

