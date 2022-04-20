import PyLizard

def Vector(data):
    vector = PyLizard.Uint8Vector()
    vector.extend(data)
    return vector

deregistrationSent = False

deregistrationMessage = [
    0x00, 0x0f, 0x40, 0x49, 0x00, 0x00, 0x05, 0x00, 0x55,
    0x00, 0x02, 0x00, 0x00, 0x00, 0x26, 0x00, 0x19, 0x18,
    0x7e, 0x01, 0x00, 0x00, 0x00, 0x00, 0x02, 0x7e, 0x00,
    0x45, 0x01, 0x00, 0x0b, 0xf2, 0x22, 0xf6, 0x01, 0x01,
    0x00, 0x83, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79, 0x00,
    0x0f, 0x40, 0x62, 0xf2, 0x08, 0x07, 0x55, 0x48, 0x00,
    0x20, 0x62, 0xf2, 0x08, 0x00, 0x14, 0x39, 0x00, 0x5a,
    0x40, 0x01, 0x18, 0x00, 0x1a, 0x00, 0x07, 0x00, 0x20,
    0xc0, 0x00, 0x00, 0x00, 0x00
]

def Callback(*args):
    '''This is used to send a full Deregistration Request NAS message in a Initial UE Message after the RAN performed a AN Release Procedure'''
    global deregistrationSent
    global deregistrationMessage
    
    if args[0] == 'Transport::SCTP::Send':
        # Data is the payload for SCTP protocol, in this case the whole NGAP message
        data = args[1]
        localEndpoint = str(args[2])
        cb = args[3]
        # Replace with RAN N2 IP address
        if localEndpoint.startswith('127.0.10.2'): # RAN
            if deregistrationSent == False:
                if data[0] == 0x20 and data[1] == 0x29:
                    # print('Found the UE Context Release Complete Message')
                    # print('Sending the UE Context Release Complete Message on the wire')
                    cb(Vector(data))
                    # print('Sending Deregistration in InitialUeMessage on the wire')
                    cb(Vector(deregistrationMessage))
                    deregistrationSent = True
            
PyLizard.SetCallback(Callback)
