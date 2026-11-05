message = "ACK"


data_bytes = message.encode('ascii')

# 2. בניית החבילה: Length + Data + Checksum
length = len(data_bytes)                      # בית 1: אורך המידע (3)

checksum = sum(data_bytes) % 256              # בית 1: סכום בתי המידע מודולו 256 (65+67+75 = 207)

packet = bytes([length]) + data_bytes + bytes([checksum])

packet_in_hex = packet.hex()

def decode_packet(packet):

    length = packet[0]#is int

    checksum = packet[-1]

    data = packet[1: 1+length]

    if len(packet) != length + 2:

        print("Invalid first(length) byte")
        return None

    elif sum(data) % 256 != checksum:
        print("sum of ascii values of data is not equal to checksum")
        return None


    return data.decode('ascii')

