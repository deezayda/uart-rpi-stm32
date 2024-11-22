import serial
import time

# Configure the UART for RPi and match with STM32-NUCLEOG071RB
uart = serial.Serial(
    port='/dev/serial0',  
    baudrate=115200,  
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1              # Timeout for reading data
)

while True: 
    data_to_send = "(GRN, 8)"        # Example Data, Ideally 8 bytes
    uart.write(data_to_send.encode()) # Send data as bytes
    print("Data sent to STM32: ", data_to_send)
    time.sleep(2)