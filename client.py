import socket
import speechRec
import speech_recognition as sr

def launchClient():
    
    
        
    #establish connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.246',1234))

    #send text to voice message
    try :
        s.sendall(bytes(speechRec.speechInput(),"utf-8"))
        #s.sendall(bytes("testing.... ////","utf-8"))
    except socket.error:
        #Send failed
        print ('Send failed')
        sys.exit()
    print ('Message send successfully')
    
    #Now receive data
    reply = s.recv(4096)
    print (reply)
    s.close()
