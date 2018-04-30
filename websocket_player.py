#import vlc
import mplayer
import subprocess
# websocket-client package
import websocket

ws_url="192.168.2.132"
ws_port=9080

websocket.enableTrace(True)
ws_resource="ws://"+ws_url+ ":" + str(ws_port)
print ("Connecting websocket server: "+ ws_resource)
ws = websocket.create_connection(ws_resource) #, subprotocols=["binary", "base64"])

print ("Creating and opening audio.webm file...")
f = open('audio.webm', 'ab')

#cmdline = ['cvlc',   '--demux', 'h264', '-'] #pick a media player
#cmdline = ['mplayer', '-noconsolecontrols',  '-fps', '25', '-cache', '1024', '-']
cmdline = ['mplayer', '-noconsolecontrols',  '-fps', '25', '-']
print (cmdline)

player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
print ("Player was opened in subprocess...")
print ("Receiving data via websocket...")
while True:
    data = ws.recv()
    #print ("in loop")
    if data:
       f.write(data)

    player.stdin.write(data)

ws.close()

f.close()