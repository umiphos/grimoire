import socket
try:
    raise socket.error(104, 'Connection reset by peer')
except socket.error:
    print "cachao"


