sensor_data = [
    "00010101",
    "11110110",
    "00000011",
    "10000000"
]

def is_bin(binary_value):
    try:
        int(binary_value, 2)
        return True
    except (ValueError, TypeError):
        return False


def decode_signed_byte(binary_value):
    if not is_bin(binary_value) or len(binary_value) != 8:
        return None

    val = int(binary_value, 2)

    # במידה והביט השמאלי ביותר (MSB) הוא 1, המספר שלילי בשיטת המשלים ל-2
    if val >= 128:
        return val - 256
    return val

for binary_str in sensor_data:
    decoded_val = decode_signed_byte(binary_str)
    print(f"binary : {binary_str} decimal: {decoded_val}")