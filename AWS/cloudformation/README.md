# Keysight LoadCore AWS CloudFormation Templates

## Prerequisites
The prerequisites are:
- Key pair for accessing to LoadCore instances
- An existing VPC
- An existing management subnet with internet access for accessing the LoadCore UI
- For some of the templates, you will need an existing test subnet
- existing Security Groups that allows HTTP/HTTPs traffic on inbound (for accessing the LoadCore UI), allows the traffic between LoadCore and LoadCore agents for management purposes and allows the test traffic

## Description of Cloudformation Templates

### LoadCore, two LoadCore Agents and the License Server 
Name: loadcore_two_agents_and_license_server.json
The template deploys:
- One LoadCore in the management subnet
- Two LoadCore Agents with two interfaces each. The first interface will be used for mananagament and the second interface will be used for testing
- One LoadCode License Server in the management subnet

When deleting the stack, the License Server will be skipped and the user should first de-activate the licenses before manually terminating the instance. This will prevent the licenses to remain activated on a deleted instance.

### LoadCore and two LoadCore Agents
Name: loadcore_and_two_agents.json
The template deploys:
- One LoadCore in the management subnet
- Two LoadCore Agents with two interfaces each. The first interface will be used for mananagament and the second interface will be used for testing

### LoadCore, two LoadCore Agents, License Server 
Name: loadcore_two_agents_license_server_test_subnet.json
The template deploys:
- One LoadCore in the management subnet
- Two LoadCore Agents with two interfaces each. The first interface will be used for mananagament and the second interface will be used for testing
- It will create a new test subnet which will be used as test subnet for the two LoadCore Agents.

### LoadCore and three LoadCore Agents
Name: loadcore_three_agents_and_license_server.json
The template deploys:
- One LoadCore in the management subnet
- Three LoadCore Agents with two interfaces each. The first interface will be used for mananagament and the second interface will be used for testing
- This setup can be used when planning to run tests with Application traffic (Raw Sockets)
- One LoadCode License Server in the management subnet

## Troubleshooting and Limitations

- In case of DELETE_FAILED when trying to delete a stack created by using Cloudformation templates, you should start again the Delete stack process