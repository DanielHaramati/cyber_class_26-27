packets = [
    ("BIN", "01001110"),
    ("HEX", "45"),
    ("DEC", "84"),
    ("BIN", "00111010")
]

def convert_to_decimal(packet):

    if packet[0] == "DEC":
        return int(packet[1])

    elif packet[0] == "BIN":
        return int(packet[1], 2)

    elif packet[0] == "HEX":
       return int(packet[1], 16)
    return ValueError("Not a valid base")


def convert_to_bin(packet):

    if packet[0] == "DEC":
        return bin(int(packet[1]))[2:]


    elif packet[0] == "BIN":
        return packet[1]


    elif packet[0] == "HEX":
        return bin(int(packet[1], 16))[2:]
    return ValueError("Not a valid base")


def convert_to_hex(packet):

    if packet[0] == "DEC":
        return hex(int(packet[1]))[2:]


    elif packet[0] == "BIN":
        return hex(int(packet[1], 2))[2:]


    elif packet[0] == "HEX":
        return packet[1]

    return ValueError("Not a valid base")

def convert_to_ascii(packet):
    if packet[0] == "DEC":
        return chr(int(packet[1]))


    elif packet[0] == "BIN":
        return chr(int(packet[1], 2))


    elif packet[0] == "HEX":
        return chr(int(packet[1], 16))

    return ValueError("Not a valid base")

convert_to_ascii(("HEX", "4e"))
def show_details_of_packet(packets_list):
    for packet in packets_list:
        print(f"Packet: {packet[0] +" " + packet[1]} / Decimal: {convert_to_decimal(packet)} / Binary: {convert_to_bin(packet)} / Hex: {convert_to_hex(packet)} / Ascii: {convert_to_ascii(packet)}")
show_details_of_packet(packets)

#Output: Packet: BIN 01001110 / Decimal: 78 / Binary: 01001110 / Hex: 4e / Ascii: N
#Packet: HEX 45 / Decimal: 69 / Binary: 1000101 / Hex: 45 / Ascii: E
#Packet: DEC 84 / Decimal: 84 / Binary: 1010100 / Hex: 54 / Ascii: T
#Packet: BIN 00111010 / Decimal: 58 / Binary: 00111010 / Hex: 3a / Ascii: :