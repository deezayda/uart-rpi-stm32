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

while True: 
    data_to_send = "[GRN, 10001, 3]"
    uart.write(data_to_send.encode())  # Send data as bytes
    print("Data sent to STM32: ", data_to_send)
    time.sleep(2)