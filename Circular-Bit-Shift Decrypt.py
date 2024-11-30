def circular_right_shift(bits, shift_count):
    """Effectue un décalage circulaire à droite sur la chaîne binaire donnée"""
    shift_count = shift_count % len(bits)  # Éviter les décalages supérieurs à la longueur des bits
    return bits[-shift_count:] + bits[:-shift_count]

def binary_to_string(binary):
    """Convertit une chaîne binaire en une chaîne de caractères"""
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

def string_to_binary(text):
    """Convertit une chaîne de caractères en binaire"""
    return ''.join(format(ord(c), '08b') for c in text)




binary_input = ['00001010', '01000011', '00101011', '01100011', '01100011', '01111001', '01100001', '00000011', '10100011', '01110011', '00100001', '00000011', '00110011', '01001011', '10010011', '10011011', '00000001', '00000011', '01111011', '00110001', '00000011', '00001011', '01100011', '01100001', '01110011', '10111011', '00101011', '01100011', '01100001', '00000011', '00100011', '01111011', '00000011', '00101001', '00001001', '00000010', '01000011', '00101011', '10010011', '00101001', '00000011', '01001011', '10011001', '00000011', '11001011', '01111011', '10101011', '10010001', '00000011', '00110011', '01100011', '00001011', '00111001', '00000011', '00001011', '10011001', '00100011', '00001001', '00000011', '10010011', '00101011', '10111011', '00001011', '10010011', '01100001', '11010001', '00000010', '00011001', '10001011', '10010011', '00011011', '10101011', '10011001', '10100011', '10010010', '11111011', '00010001', '10001011', '10100010', '11111011', '11111011', '01000001', '10001011', '00110011', '10100010', '11111010', '01001001', '10101010', '10011010', '01110001', '10000010', '10100010', '11111010', '10011010', '10101010', '10010001']

for shift_count in range(60):
    for binary in binary_input:
        result = circular_shift(binary, shift_count)

        if result:
            print(binary_to_string(result), end="")
    print()
