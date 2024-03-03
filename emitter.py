import socket
import os

HOST = '172.22.144.1'  
PORT = 8080            

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def save_transmission(message):
    with open('transmission_log.txt', 'a') as file:
        file.write(message + '\n')

def morse_to_text(morse_code):
    text = ""
    morse_code = morse_code.split(" ")
    for code in morse_code:
        if code in REVERSE_MORSE_CODE_DICT:
            text += REVERSE_MORSE_CODE_DICT[code]
    return text

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Waiting for connection from the transmitter...')
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected to', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    morse_code = data.decode()
                    print("Received Morse Code:", morse_code)
                    decoded_message = morse_to_text(morse_code)
                    save_transmission("Transmission received: " + decoded_message)
