import PyLizard

def Vector(data):
    vector = PyLizard.Uint8Vector()
    vector.extend(data)
    return vector

echoRequest = False
echoResponse = False
messages = 0

def Callback(*args):
    'This will insert a GTPu Echo Request Message from UPF and will check the response from RAN'
    global echoRequest, echoResponse, messages

    if args[0] == 'Transport::UDP::Send':
        data = args[1]
        localEndpoint = str(args[2])
        cb = args[3]
        # Replace with UPF N3 address
        if localEndpoint.startswith('197.0.0.10'): # packet sent by UPF.
            # Found a UPF message sent from UPF N3 IP address
            messages += 1
            if not echoRequest and messages > 2:
                # print('Injecting GTP echo request')
                message = [0x32, 0x01, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
                # sending crafted GTPu Echo Request
                cb(Vector(message))
                echoRequest = True
                # Send the actual message that was supposed to be sent by UPF
                cb(Vector(data))

    elif args[0] == 'Transport::UDP::Receive':
        data = args[1]
        localEndpoint = str(args[2])
        cb = args[3]
        # Replace with UPF N3 address
        if localEndpoint.startswith('197.0.0.10'): # packet received by UPF
            if echoRequest and not echoResponse:
                # print('Checking if received message is a GTPu echo response')
                # print('Hex of received message %s' % (' '.join(['%02x' % i for i in data])))
                # This is expected Echo Response message
                expected = [0x32, 0x02, 0x00, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0e, 0x00]
                # print('Expected %s' % (' '.join(['%02x' % i for i in expected])))
                # Test if received == expected
                if list(data) == expected:
                    echoResponse = True
    
    # This is optional
    elif args[0] == 'Finalize':
        # This line will be printed before test end in Load Core agent log.
        print('Final Result: %s' % (echoRequest and echoResponse))

PyLizard.SetCallback(Callback)
