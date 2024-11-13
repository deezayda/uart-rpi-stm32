import serial
import time

# Configure the UART for RPi and Match with STM32-NUCLEOG071RB
uart = serial.Serial(
    port='/dev/serial0',   # Use '/dev/serial0' or '/dev/ttyS0' 
    baudrate=115200,  
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1              # Timeout for reading data
)

# while True: 
#     data_to_send = "Hello, STM32 Microcontroller"
#     uart.write(data_to_send.encode())  # Send data as bytes
#     print("Data sent to STM32: ", data_to_send)
#     time.sleep(2)

# Poll Rx and if signal then send data to STM32
while True: 
    received = uart.read() # Default Size 1 byte
    received_data = int.from_bytes(received, byteorder="big")
    print(f"RPi received {received_data}")
    if received_data == 1: 
        # Send data to the STM32
        data_to_send = "Hello, STM32 Microcontroller"
        uart.write(data_to_send.encode('utf-8'))  # Send data as bytes using utf-8 
        print("Data sent to STM32: ", data_to_send)
