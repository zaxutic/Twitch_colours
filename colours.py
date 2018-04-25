import socket
from datetime import datetime
import itertools
import time

colours = [
    'Blue', 'BlueViolet', 'CadetBlue', 'Chocolate',
    'Coral', 'DodgerBlue', 'Firebrick', 'GoldenRod',
    'Green', 'HotPink', 'OrangeRed', 'Red', 'SeaGreen',
    'SpringGreen', 'YellowGreen'
]

def current_time():
    t = datetime.now()
    return t.strftime("%y-%m-%d %H:%M:%S ")

def connect():
    global s
    print(current_time(), "CONNECTING")
    s = socket.socket()
    s.connect((Host, Port))
    s.send(bytes("PASS " + Pass + "\r\n", "UTF-8"))
    s.send(bytes("NICK " + Nick + "\r\n", "UTF-8"))
    s.send(bytes("JOIN #" + Channel + " \r\n", "UTF-8"))
    print(current_time(), "CONNECTED")
    while True:
        line = str(s.recv(1024))
        if "End of /NAMES list" in line:
            print(current_time, f"Entered {Channel}'s chat")
            break

def send_message(msg):
    s.send(bytes("PRIVMSG #" + Channel + " :" + msg + "\r\n", "UTF-8"))
    print(current_time() + Nick + ": " + msg + '\n')

def auto_reconnect():
    if len(line) == 0:
        sec = 2
        for i in itertools.count():
            try:
                print("Reconnecting in " + str(sec) + " seconds...")
                s.close()
                time.sleep(sec)
                if sec != 16 and i % 2 == 1:
                    sec *= 2
                connect()
                break
            except:
                pass

def main():
    global x
    line = s.recv(1024).decode("utf-8")
    auto_reconnect()
    parts = line.split(':')
    if line.startswith('PING'):
        s.send(bytes("PONG\r\n", "UTF-8"))
    elif len(parts) > 2:
        username = parts[1].split("!")[0]
        if username == Nick:
            send_message(".color {}".format(colours[x]))
            if x == len(colours) - 1:
                x = 0
            else:
                x += 1

if __name__ == '__main__':
    Host = "irc.twitch.tv"
    Port = 6667
    Channel = ''
    x = 0

    with open("auth", "r", encoding='utf-8') as auth_file:
        line = auth_file.readline().split()
        Nick = line[0].lower()
        Pass = line[1]

    if not Channel:
        Channel = input("Channel: ")

    connect()

    while True:
        main()
