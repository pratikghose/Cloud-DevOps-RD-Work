from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from CreateAvailabilitySets import *
from CreateNIC import *
from CreatePublicIP import *
from CreateResourceGroup import *
from CreateSubNet import *
from CreateVM import *
from CreateVNet import *
from UpdateVM import *
from AddDataDisk import *
RG_NAME = 'ResourceGroup'
LOCATION = 'for example - centralindia'
VM_NAME = 'newVM'
SUBSCRIPTION_ID = 'your_subscription-id'
AVAILSETS_NAME = 'newAvailabilitySet'
PUB_IP_NAME  = 'newPublicIP'
VNET_NAME = 'newVirtualNetwork'
SUBNET_NAME='newSubNet'
NIC_NAME='newNIC'
VM_NAME='newVM'
DATADISK_NAME='newDataDisk'
userid = 'your azure userid'
password = 'your azure password'
vmsize = 'Standard_F1'


def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id='your_application_id',
        secret='your_client_secret',
        tenant='your_tenant_id'
    )
    return credentials

if __name__=="__main__":
    credentials = get_credentials()
    rg_client = ResourceManagementClient(
        credentials,
        SUBSCRIPTION_ID
    )

    network_client = NetworkManagementClient(
        credentials,
        SUBSCRIPTION_ID
    )

    compute_client = ComputeManagementClient(
        credentials,
        SUBSCRIPTION_ID
    )
    print(create_resource_group(rg_client,LOCATION,RG_NAME))
    print(create_availability_set(compute_client,LOCATION,AVAILSETS_NAME,RG_NAME))
    print(create_public_ip_address(network_client,LOCATION,PUB_IP_NAME,RG_NAME))
    print(create_vnet(network_client,LOCATION,RG_NAME,VM_NAME))
    print(create_subnet(network_client,RG_NAME,VNET_NAME,SUBNET_NAME))
    print(create_nic(network_client,RG_NAME,VNET_NAME,SUBNET_NAME,LOCATION,NIC_NAME,PUB_IP_NAME))
    print(create_vm(network_client,compute_client,VM_NAME,RG_NAME,LOCATION,NIC_NAME,AVAILSETS_NAME,userid,password,vmsize))
    print('=====VM Set=====')
    print('=====Start-VM=====')
    print(compute_client.virtual_machines.start(RG_NAME,VM_NAME))
    print(update_vm(compute_client,RG_NAME,VM_NAME))
    print(add_datadisk(compute_client,RG_NAME,DATADISK_NAME,VM_NAME,LOCATION))
    print('=====Stop-VM=====')
    print(compute_client.virtual_machines.power_off(RG_NAME,VM_NAME))




