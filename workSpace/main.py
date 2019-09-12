import network
from mqtt import MQTTClient 
import machine 
import time 
  
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("cruzanet", "gyata786")
 
station.isconnected()
station.ifconfig()
 
client = MQTTClient("device_id", "mqtt.bikerhq.ml",user="biker", password="biker", port=8883) 
client.set_callback(sub_cb) 
client.connect()
client.subscribe(topic="123456/heat") 
while True: 
    print("Sending ON") 
    client.publish(topic="123456/heat", msg="ON")
    time.sleep(1) 
    print("Sending OFF") 
    client.publish(topic="123456/heat", msg="OFF")
    
    time.sleep(1) 
