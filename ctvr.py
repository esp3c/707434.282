import socket

# Configure the receiver
RECEIVER_HOST = '172.22.144.1'  # IP address of the receiver
RECEIVER_PORT = 8080             # Port for connection

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

def text_to_morse(text):
    morse_code = ""
    for char in text:
        if char.upper() in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char.upper()] + " "
    return morse_code

def transmit_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((RECEIVER_HOST, RECEIVER_PORT))
        s.sendall(message.encode())

if __name__ == "__main__":
    print("Transmitter is online.")
    while True:
        message_to_send = input("Enter message to send (or type 'exit' to quit): ")
        if message_to_send.lower() == 'exit':
            break
        morse_message = text_to_morse(message_to_send)
        print("Message in Morse Code:", morse_message)
        transmit_message(morse_message)
