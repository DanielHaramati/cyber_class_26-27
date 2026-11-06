packets = [
    {"id": "0x2A", "payload": "01010110", "checksum": "0x80"},
    {"id": "0x10", "payload": "11110000", "checksum": "0x00"},
    {"id": "0x05", "payload": "00101010", "checksum": "0x30"}

]

def is_hex(val):
    #check if a value is hexadecimal
    try:

        int(val, 16) #trying to convert val to hex
        return True

    except (TypeError, ValueError):
    #ValueError - e.g. Letters outside A-F(the hex range)
    #TypeError - e.g. an int

        return False

def is_bin(val):
    # check if a value is binary
    try:

        int(val, 2) #trying to convert val to bin
        return True
    except (TypeError, ValueError):
    # ValueError - e.g. Invalid binary characters(such as 3 in a binary string)
    # TypeError - e.g. An int

        return False

"""
def check_keys(packet):
    if not isinstance(packet, dict):
        raise TypeError("packet must be a dict")

    
    #There are 3 keys for each packet: id, payload, checksum

        # for each packet list(packet.keys()) should be ["id" , "payload" , "checksum"]
        if list(packet.keys()) != ["id", "payload", "checksum"]:
                return False

        return True
"""



"""
def check_types_of_values(packet):
    if not isinstance(packet, dict):
        raise TypeError("packet must be a dict")

    if not is_hex(packet["id"]):
            return False

    elif not is_bin(packet["payload"]):
            return False

    elif not is_hex(packet["checksum"]):
            return False

    return True
"""

def validate_packet(packet):
    if not isinstance(packet, dict):
        raise TypeError("packet must be a dict")

    if not is_hex(packet["id"]) or not is_hex(packet["checksum"]):
        raise TypeError("need to be hex")

    if not is_bin(packet["payload"]):
        raise TypeError("binary needs to be binary")

    id_decimal = int(packet["id"], 16)
    payload_decimal = int(packet["payload"], 2)
    check_sum = int(packet["checksum"], 16)

    return (id_decimal + payload_decimal) % 256 == check_sum


"""
def check_protocol_for_each_packet(packet):
    if not isinstance(packet, dict):
        raise TypeError("packet must be a dict")

    id_value = int(packet["id"], 16)

    payload_value = int(packet["payload"], 2)

    checksum_value = int(packet["checksum"], 16)

    if (id_value + payload_value) % 256 != checksum_value:
        return False

    return True
"""

def check_protocol_for_packets(packets_list):
    if not isinstance(packets_list, list):
        raise TypeError("packet must be a dict")

    for packet in packets_list:
        try:
            if not validate_packet(packet):
                print("packet is not valid! :(")
            else:
                print("packet is valid !!!  :)")
        except Exception as e:
            print(e)

check_protocol_for_packets(packets)

#משתמשים במודולו 256 בשביל לשמור על הסכום שבודקים מול checksum בפרוטוקול שיהיה קטן מ256
#