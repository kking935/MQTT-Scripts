import random
from srs import SRS

# VT Settings               # VMI Settings
broker = 'iot.cs.vt.edu'    # '199.244.104.202'
port = 1883                 # 1883
username = 'icat'           # 'dave'
password = 'icat2GO'        # 'password'

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

srs = SRS()

# topic = "vmi/box1/plug1"

# Need to also define a heart beat
# Move the server to MQTT 5 With Certificate