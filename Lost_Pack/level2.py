secret_packets = [
    "4E4554574F524B",
    "2053414645",
    "205A4F4E45"
]



def convert_hex_string_to_bytes(hex_str):
    return bytes.fromhex(hex_str)

def convert_bin_to_str(bin_str):
    return bin_str.decode()

tot = ""
for packet in secret_packets:
    tot += convert_bin_to_str(convert_hex_string_to_bytes(packet))

print(tot)
print(b'\x41'.decode())