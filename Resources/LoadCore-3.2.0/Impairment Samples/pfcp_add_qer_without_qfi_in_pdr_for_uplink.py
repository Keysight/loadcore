import sys, warnings
sys.path.insert(0, './current-spec')
warnings.simplefilter("ignore")
import PyLizard
import PyPFCP
warnings.simplefilter("default")


messageCount = 0
modification = False

def Callback(*args):

    global messageCount, modification

    if args[0] == "PFCP::Client::SendPFCPMessage" or args[0] == "SMF::SendPFCPMessage": # covers both n4-smf and smf applications
        message = args[1]
        cb = args[2]
        if isinstance(message, PyPFCP.SessionEstablishmentRequest):
            # print('Found a Session Establishment Message' )
            messageCount +=1
            if message.OptIeCreateQERList.__len__() > 0:
                # print('There are some Create QER IEs in this message')
                for value in [123, 124]:
                    newqer = PyPFCP.CreateQER()
                    # print('Initialized a new Create QER IE')
                    # CreateQER Object available methods are [
                    #   'HasIeAveragingWindow', 
                    #   'HasIeDLFlowLevelMarking', 
                    #   'HasIeGuaranteedBitrate', 
                    #   'HasIeMaximumBitrate', 
                    #   'HasIePacketRate', 
                    #   'HasIePagingPolicyIndicator', 
                    #   'HasIeQERCorrelationID', 
                    #   'HasIeQoSFlowIdentifier', 
                    #   'HasIeReflectiveQoS', 
                    #   'IeGateStatus', 
                    #   'IeQERID', 
                    #   'OptIeAveragingWindow', 
                    #   'OptIeDLFlowLevelMarking', 
                    #   'OptIeGuaranteedBitrate', 
                    #   'OptIeMaximumBitrate', 
                    #   'OptIePacketRate', 
                    #   'OptIePagingPolicyIndicator', 
                    #   'OptIeQERCorrelationID', 
                    #   'OptIeQoSFlowIdentifier', 
                    #   'OptIeReflectiveQoS'
                    #   and more])
                    # Next Configure the CreateQER object
                    newqer.IeQERID = value
                    if value == 123:
                        # Adding optional IE QFI to Create QER
                        newqer.HasIeQoSFlowIdentifier = True
                        # QFI IE is a PyPFCP.QFI object
                        newqer.OptIeQoSFlowIdentifier = PyPFCP.QFI()
                        # Setting the valie for QFI IE
                        newqer.OptIeQoSFlowIdentifier.Value = 11
                    # Append the CreatedQER IE to the message
                    message.OptIeCreateQERList.append(newqer)
                    

            if message.IeCreatePDRList.__len__() > 0:
                # Initialize a QERID object to use as QER ID in Create PDR
                tmp = PyPFCP.QERID()
                tmp.Value = 124
                # Set the QER ID object in first Create PDR IE
                message.IeCreatePDRList[0].OptIeQERIDList[0] = tmp

            cb(message)

        elif isinstance(message, PyPFCP.SessionModificationRequest):
            # Found a Session Modification Request. That means the Session Establishment was succesfull
            modification = True
    # This is optional.
    elif args[0] == 'Finalize':
        # This line will be printed at test end, when deleting the impairment script from agent
        print('validation result: %s' % (messageCount > 0 and modification == True))
    return

PyLizard.SetCallback(Callback)
