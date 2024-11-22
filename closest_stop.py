from collections import deque

# input parameters - list of tuples [[orange, 1], [silver, 5]...]
# checks - less than or equal to 5, deal with repeats, logic with priority of lines
# output parameter - tuple - denotes closest stop

def calc_closest_stop(buses, recent_buses):
    color_codes = {"OR" : "ORN", "GRN" : "GRN", "GOLD" : "GLD", "SLV" : "SLV"}
    filtered_buses = {}

    for bus_id, bus_color, stops in buses: 
        if stops <= 25 and bus_id not in recent_buses:  # Only consider 5 stops or fewer
            # Store the closest stop 
            if(bus_id not in filtered_buses):
                filtered_buses[bus_id] = (bus_color, stops)
                print(f"filtered_buses {bus_id} and {bus_color} and stops {stops}")
    
    # print(filtered_buses.items())

    # No valid buses within 5 stops
    if not filtered_buses: 
        return None

    # Find the bus with the least stops away
    closest_bus = min(
        filtered_buses.items(), key=lambda x: (x[1][1])
    )
    # byte size = 8 - STM32 RX BUFFER LENGTH - COLORS GLD, GRN, ORG, SIL
    # print(f"Closest Bus: {closest_bus}")

    bus_id, (color, stops) = closest_bus
    color_code = color_codes[color]

    recent_buses.append(bus_id)
    if len(recent_buses) > 3:
        recent_buses.popleft()

    # Format as string and ensure length is exactly 8 bytes 
    # Options: "(ORN, #)", "(GRN, #)", "(GLD, #)", "(SLV, #)"

    closest_bus = f"({color_code}, {stops})"
    closest_bus = closest_bus.ljust(8) # Pad with spaces if less than 8 bytes

    print(f"Closest Bus: {closest_bus}")

    print(f"Number of bytes: {len(closest_bus.encode("utf-8"))}")

    return closest_bus

def main():
    queue = deque()
    sample_data = [
        ('4009271', 'GRN', 8), 
        ('4009275', 'OR', 25), 
        ('4014843', 'OR', 17), 
        ('4009271', 'GRN', 7), 
        ('4014851', 'GOLD', 26), 
        ('4016911', 'GOLD', 9), 
        ('4018257', 'GOLD', 16), 
        ('4018259', 'SLV', 4), 
        ('4018265', 'GOLD', 24), 
        ('4018951', 'OR', 15)
    ]
    for _ in range (3): 
        calc_closest_stop(sample_data, queue)

if __name__ == "__main__":
    main()
