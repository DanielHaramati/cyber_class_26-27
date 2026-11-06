secret_packets = [
    "4E4554574F524B",
    "2053414645",
    "205A4F4E45"
]


def convert_hex_string_to_bytes(hex_str):
    if not isinstance(hex_str, str):
        raise TypeError("hex_str must be a string")

    return bytes.fromhex(hex_str)

def convert_bin_to_str(bin_str):
    return bin_str.decode()

def main():
    tot = ""
    for packet in secret_packets:
        try:
            tot += convert_bin_to_str(convert_hex_string_to_bytes(packet))
        
        except Exception as e:
            print(f"there was a problem with the packet: {packet}")
            print(e)

    return tot

res = main()
print(res)
