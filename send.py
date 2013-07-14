import socket
import traceback


def send(ip, port, path,headers,status):
 try:
  MESSAGE = "POST "+ path+" HTTP/1.1\n"
  if(headers is not None):
    for k, v in headers.iteritems():
	MESSAGE = MESSAGE + k + ":" + v + "\n"
  MESSAGE = MESSAGE + "\n"
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((ip, port))
  s.send(MESSAGE+status)
  data=s.recv(10)
  #print "data: %s" %data
  s.close()
 except Exception, e:
  print e
  traceback.print_exc()

status = "hello"
headers= { "Content-Type" : "application/x-www-form-urlencoded", "Content-Length" : "5" }
send("localhost",9000,"/",headers,status)
