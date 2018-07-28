

def decimal_to_color_hex(number):
    return "#" + str(hex(int(number))).split("x")[1]
