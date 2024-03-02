import socket
import time

# Definir el alfabeto Morse
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', ' ': ' '
}

def text_to_morse(text):
    morse = ''
    for char in text.upper():
        if char in morse_code:
            morse += morse_code[char] + ' '
    return morse

# Configurar el emisor
HOST = '127.0.0.1'  # IP del receptor
PORT = 65432        # Puerto para la conexión

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((127.0.0.1, 65432))
    while True:
        mensaje = input("Ingrese el mensaje a enviar: ")
        morse = text_to_morse(mensaje)
        print("Mensaje en Morse:", morse)
        s.sendall(morse.encode())
        time.sleep(0.5)  # Esperar antes de enviar el siguiente mensaje
