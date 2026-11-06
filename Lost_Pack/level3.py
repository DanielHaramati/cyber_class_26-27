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

def check_keys(packet):
    #There are 3 keys for each packet: id, payload, checksum

        # for each packet list(packet.keys()) should be ["id" , "payload" , "checksum"]
        if list(packet.keys()) != ["id", "payload", "checksum"]:
                return False

        return True





def check_types_of_values(packet):
    #id field - hex, payload field - binary, checksum field - hex

    if not is_hex(packet["id"]):
            return False

    elif not is_bin(packet["payload"]):
            return False

    elif not is_hex(packet["checksum"]):
            return False

    return True


def validate_packet(packet):
    #merge both conditions
    if check_keys(packet):
        return check_types_of_values(packet)
    return False



def check_protocol_for_each_packet(packet):

    id_value = int(packet["id"], 16)

    payload_value = int(packet["payload"], 2)

    checksum_value = int(packet["checksum"], 16)

    if (id_value + payload_value) % 256 != checksum_value:
        return False

    return True


def check_protocol_for_packets(packets_list):

    for packet in packets_list:

        if not validate_packet(packet):

            raise ValueError("Invalid Packet")

    for packet in packets_list:

        print(check_protocol_for_each_packet(packet))
#משתמשים במודולו 256 בשביל לשמור על הסכום שבודקים מול checksum בפרוטוקול שיהיה קטן מ256
#