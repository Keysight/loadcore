import PyLizard

def Vector(data):
    vector = PyLizard.Uint8Vector()
    vector.extend(data)
    return vector

pathSwitchRequestsSent = 0

def Callback(*args):
    '''This will modify the NGAP PATH Switch Request Message'''
    global pathSwitchRequestsReceived

    if args[0] == 'Transport::SCTP::Send':
        data = args[1]
        localEndpoint = str(args[2])
        cb = args[3]

        # Replace with RAN N2 Address
        if localEndpoint.startswith('127.0.100.2'): # RAN
            if data[0] == 0x00 and data[1] == 0x19 and pathSwitchRequestsSent == 0: # First PathSwitchRequest
                # print('Found the PathSwitchRequest sent by RAN ')
                dataList = list(data)
                ie = bytearray.fromhex('0039000900000205000f400148') #IE to add.
                packetToSend        = dataList[0:-15] # slice the original message up to the last item in NGAP sessions to be switched
                packetToSend[3]    -= 15 # decreased the NGAP message length
                packetToSend[-17]  -= 15 # decreased the len of the sessions to be switched
                packetToSend[-16]   = 0 # decreased the item count in list of sessions to be switched to 1
                packetToSend[6]    += 1 # added one ie to ngap ie list
                packetToSend       += ie # adding the new IE
                packetToSend[3]    += len(ie) # increase the NGAP message length
                # print('Sending the modified message')
                pathSwitchRequestsSent += 1
                cb(Vector(packetToSend))

PyLizard.SetCallback(Callback)
