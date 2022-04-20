
import PyLizard
import PyPFCP

SERcount = 0
SMRcount = 0

def Callback(*args):
    global SERcount
    global SMRcount
    # Dropping some response messages from UPF to check the SMF retry mechanism
    # Notes: 
    # 1. in case this operation is performed on a request message, like Session Establishment Request, the SMF will not resend the message.
    # 2. a UDP transport inparment could be used in above case. The SMF application will know teh message was sent, UDP will drop it and SMF will retry

    if args[0] == "PFCP::Server::SendPFCPMessage":
        message = args[1]
        cb = args[2]
        if isinstance(message, PyPFCP.SessionEstablishmentResponse):
            # print('Found a Session Establishment Response message')
            SERcount += 1
            # Dropping the first message
            if SERcount == 1:
                cb(None)
            
        elif isinstance(message, PyPFCP.SessionModificationResponse):
            # print('Found a Session Modification Response message')
            SMRcount += 1
            # Dropping the first message
            if SMRcount == 1:
                cb(None)
    return

PyLizard.SetCallback(Callback)
