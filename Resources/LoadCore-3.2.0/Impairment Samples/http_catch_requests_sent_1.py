import PyLizard, json, copy

def Vector(data):
    vector = PyLizard.Uint8Vector()
    vector.extend(data)
    return vector


def Callback(*args):
    '''This will change the path of a /nausf-auth/v1/ue-authentications message sent from AMF to AUSF'''
    if args[0] == "HTTP::SendRequest":
        request = args[1]
        localEndpoint = args[2]
        remoteEndpoint = args[3]
        cb = args[4]
        url = request.GetHeaders().get(':path')
        print('LocalEndpoint: %s' % localEndpoint)
        print('RemoteEndpoint: %s' % remoteEndpoint)
        print('Method: %s' % request.method)
        print('URL: %s' % url)
        if "/nausf-auth/v1/ue-authentications" in url:
            bodyString = request.body
            headersDict = request.GetHeaders()
            
            try:
                contentType = headersDict['Content-Type']
            except KeyError:
                contentType = ''
            if contentType == 'application/json':
                bodyDict = json.loads(request.body)
                print(bodyDict.keys())
            
            newHeaders = copy.deepcopy(request.GetHeaders())
            # print('oldpath', newHeaders[':path'])
            newHeaders[':path'] = '/nausf-auth/v1/ue-aaaaaaaa'
            request.SetHeaders(newHeaders)
            cb(request)
    
PyLizard.SetCallback(Callback)
