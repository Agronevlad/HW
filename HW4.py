import numpy as np
import paho.mqtt.client as mqtt
import time

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "/data/movement_simulation"

# Initialize data lists
data_lists = {'t': [], 'x': [], 'y': [], 'vx': [], 'vy': []}

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(TOPIC, qos=2)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        print("Receiving data")
        data = msg.payload.decode('utf-8').split('#')
        for key, value in zip(data_lists.keys(), data):
            data_lists[key].append(float(value))
    except Exception as e:
        print(f"Error parsing MQTT message: {e}")

def save_to_numpy():
    t_array = np.array(data_lists['t'])
    x_array = np.array(data_lists['x'])
    y_array = np.array(data_lists['y'])
    vx_array = np.array(data_lists['vx'])
    vy_array = np.array(data_lists['vy'])
    return t_array, x_array, y_array, vx_array, vy_array

def mqtt_subscribe(client):
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 10)
    client.loop_start() 

def main():
    client = mqtt.Client()
    mqtt_subscribe(client)
    
    try:
        while True:
            time.sleep(1) 
    except KeyboardInterrupt:
        print("Program interrupted by user")
    finally:
        t_array, x_array, y_array, vx_array, vy_array = save_to_numpy()
        print("Data saved to numpy arrays")

if __name__ == '__main__':
    main()
