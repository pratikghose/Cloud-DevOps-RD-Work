def create_nic(network_client,RG_NAME,VNET_NAME,SUBNET_NAME,LOCATION,NIC_NAME,PUB_IP_NAME):
    subnet_info = network_client.subnets.get(
        RG_NAME,
        VNET_NAME,
        SUBNET_NAME
    )
    publicIPAddress = network_client.public_ip_addresses.get(
        RG_NAME,
        PUB_IP_NAME
    )
    nic_params = {
        'location': LOCATION,
        'ip_configuration': [{
            'name': 'newIPConfig',
            'public_ip_addresses': publicIPAddress,
            'subnet': {
                'id': subnet_info.id
            }
        }]
    }

    nic_results = network_client.network_interfaces.create_or_update(
        RG_NAME,
        NIC_NAME,
        nic_params
    )
    return nic_results.results();