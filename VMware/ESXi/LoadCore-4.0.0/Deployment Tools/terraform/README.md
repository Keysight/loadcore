### Keysight LoadCore terraform plans

These terraform plans and the updateLoadCore tool can be used together to managed LoadCore product across releases.


#### Example of usage:
Prerequisites in order to managed the LoadCore product across releases:

- deploy one LoadCore MDW using the terraform from **VMware\ESXi\terraform\one_loadcore_mdw**

- deploy the LoadCore Agents using the terraforms from **VMware\ESXi\terraform\multiple_agents**

The updateLoadCore tool can be also used on an existing LoadCore setup.


#### Some deployment scenarios:

##### 1. update LoadCore MDW and LoadCore Agents:

* use **updateLoadCore** tool to update both MDW and Agents.



##### 2. update LoadCore MDW and re-deploy LoadCore Agents:

* use **updateLoadCore** tool to update LoadCore MDW (make sure to use deleteAgents flag to clean MDW of old agents)

* re-deploy agents using terraform plans (make sure to keep the terraform .tfstate file in order to delete them from the infrastructure)



##### 3. Re-deploy both LoadCore MDW and LoadCore Agents:

* Both actions can be done using terraforms plans from **VMware\ESXi\terraform**


#### Prerequisites
The prerequisites are:
1.	Download terraform tool (for example https://releases.hashicorp.com/terraform/1.1.4/terraform_1.1.4_windows_386.zip). Add it in System Variables -> Path of the machine running the terraform.
- Latest version of Terraform installed. https://learn.hashicorp.com/tutorials/terraform/install-cli

2.	(If the machine has access to internet, this step can be skipped)
Download the josenk provider (for example https://github.com/josenk/terraform-provider-esxi/releases -> terraform-provider-esxi_1.10.2_windows_386.zip).
Place a copy of it in your path or current directory of your terraform project.
Note: The josenk provider is used because the hashicorp/terraform provider does not support ovf/ova deploy from vSphere without having vCenter. More about this limitation here:
https://registry.terraform.io/providers/hashicorp/vsphere/latest/docs/resources/virtual_machine (“ovf deployment requires vCenter and is not supported on direct ESXi connections.”)

3.	Download the ovf tool (for example https://developer.vmware.com/web/tool/4.4.0/ovf) and add it in System Variables -> Path of the machine running the terraform.

#### How to use:

You can start learning terraform from the official website: https://learn.hashicorp.com/collections/terraform/aws-get-started

When you create a new configuration — or check out an existing configuration from version control — you need to initialize the directory with **terraform init** command.
You can also make sure your configuration is syntactically valid and internally consistent by using the **terraform validate** command.

The  **terraform apply**  command executes the actions proposed in a terraform template. All the default deployment variables may be changed. The variables will be explained in each of the proposed templates.


#### Short description of Terraform plans
For full description, please check the README.md from each folder

##### One LoadCore MDW
Terraform will deploy one LoadCore MDW on the specified ESXi infrastructure


##### Two LoadCore Agents
Terraform will deploy two LoadCore Agents on the specified ESXi infrastructure


##### Multiple LoadCore Agents
Terraform will deploy multiple LoadCore Agents on the specified ESXi infrastructure


##### One LoadCore MDW and two LoadCore Agents
Terraform will deploy one LoadCore MDW and two LoadCore Agents on the specified ESXi infrastructure
