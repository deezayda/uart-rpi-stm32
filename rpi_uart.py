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

# Poll Rx and if signal then send data to STM32
while True: 
    received = uart.read() # Default Size 1 byte
    if received: # Check if anything was received
        received_data = int.from_bytes(received, byteorder="big")
        print(f"RPi received {received_data}")

        # Check for ready signal from STM32
        if received_data == 1: 
            # Send data to the STM32
            data_to_send = "[GRN, 10001, 3]"
            encoded_data = data_to_send.encode('utf-8') # Encode as bytes
            uart.write(encoded_data)  # Send data as bytes using utf-8 
            print("Data sent to STM32: ", data_to_send)
            time.sleep(2)
