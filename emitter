import socket
import time
from colorama import init, Fore, Style

# Configure the receiver
HOST = '127.0.0.1'  # Listen on all interfaces
PORT = 65432        # Port for connection
LOG_FILE = 'transmission_log.txt'

# Initialize colorama
init()

def print_message(message_top, message_bottom):
    border = Fore.RED + Style.BRIGHT + "+" + "-"*(max(len(message_top), len(message_bottom))+2) + "+"
    print(border)
    print("| " + message_top.ljust(max(len(message_top), len(message_bottom))) + " |")
    print("| " + message_bottom.ljust(max(len(message_top), len(message_bottom))) + " |")
    print(border)

def save_transmission(message):
    with open(LOG_FILE, 'a') as file:
        file.write(message + '\n')

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
                message = data.decode()
                print_message("Transmission received", "Message: " + message)
                save_transmission("Transmission received: " + message)
