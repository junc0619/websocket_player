#import vlc
import mplayer
import subprocess
# websocket-client package
import websocket
import os
import logging


# create logger
logger = logging.getLogger('websocket_ffmpeg_pipe')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

#logger.debug('debug message')
#logger.info('info message')
#logger.warn('warn message')
#logger.error('error message')


ws_url="192.168.2.132"
#ws_url="10.16.37.97"
ws_port=9080

logger.info('Connecting websocket server...')
websocket.enableTrace(True)
ws_resource="ws://"+ws_url+ ":" + str(ws_port)
#print ("Connecting websocket server: "+ ws_resource)
ws = websocket.create_connection(ws_resource) #, subprotocols=["binary", "base64"])

logger.info('Creating and opening audio.webm file...')
#print ("Creating and opening audio.webm file...")
#f = open('audio.webm', 'ab')

#cmdline = ['cvlc',   '--demux', 'h264', '-'] #pick a media player
#cmdline = ['mplayer', '-noconsolecontrols',  '-fps', '25', '-cache', '1024', '-']
#cmdline = ['mplayer', '-noconsolecontrols',  '-fps', '25', '-']
#cmdline = ['mplayer', '-noconsolecontrols',  '-cache', '128', '-']
#cmdline = ['mplayer', '-noconsolecontrols', '-ac', 'fflibopus', '-nocache', '-']
#cmdline = ['mplayer', '-noconsolecontrols', '-nocache', '-']

logger.info('Creating a subprocess...')

cmdline = ['ffplay', 'mypipe']
print (cmdline)
player = subprocess.Popen(cmdline)
logger.info("Player was opened in subprocess...")

logger.info('Openning the pipe...')
fifo = open ('mypipe','wb')
logger.info('Receiving data via websocket...')

while True:
    data = ws.recv()
    #logger.debug('Receiving data via websocket...')
    #print ("in loop")
    if data:
    	fifo.write(data)

player.kill()
ws.close()
f.close()