import network
from time import sleep
sta_if = network.wlan(network.STA_IF); sta_if.active(True)
ap_name = "Suza_4G"
password = "licet@123"
while not sta_if.isconnected():
    sta_if.connect(ap_name, password ) # Connect to an AP

if sta_if.isconnected():
    println("Connected")
import webrepl
webrepl.start()
