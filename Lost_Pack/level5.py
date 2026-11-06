
def build_package(data_bytes): # 2
    if len(data_bytes) > 255:
        raise ValueError("Data cannot exceed 255 bytes")

    length = len(data_bytes) 
    
    checksum = sum(data_bytes) % 256   
    packet = bytes([length]) + data_bytes + bytes([checksum])
    return packet

def decode_packet(packet):
    if len(packet) < 2:
        return None

    length = packet[0]
    checksum = packet[-1]
    data = packet[1: 1+length] # 1 is the length byte. it checks from first byte of the msg till the last byte of the msg

    if len(packet) != length + 2: # if it doesnt equal the bytes length + length byte + checksunm byte 

        print("Invalid first(length) byte")
        return None

    elif sum(data) % 256 != checksum:
        print("sum of ascii values of data is not equal to checksum")
        return None

    try:
        return data.decode('ascii')
    except UnicodeDecodeError as e:
        print("unicode error. Invalid ascii.")
        return None






MSG = "ACK"
data_bytes = MSG.encode("ascii")

packet = build_package(data_bytes)

print("Hex:", packet.hex().upper())
print("Decoded:", decode_packet(packet))
