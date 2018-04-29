#import vlc
import mplayer
import subprocess
from websocket import create_connection


ws = create_connection("ws://localhost:9080") #, subprotocols=["binary", "base64"])
f = open('audio.webm', 'ab')

#cmdline = ['cvlc',   '--demux', 'h264', '-'] #pick a media player
#cmdline = ['mplayer', '-noconsolecontrols',  '-fps', '25', '-cache', '1024', '-']
cmdline = ['mplayer', '-noconsolecontrols',  '-fps', '25', '-']

print (cmdline)
player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
print ("player opened")
while True:
    data = ws.recv()
    print ("in loop")
    if data:
       f.write(data)

    player.stdin.write(data)

ws.close()

f.close()