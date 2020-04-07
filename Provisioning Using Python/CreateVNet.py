def create_vnet(network_client,LOCATION,RG_NAME,VNET_NAME):
    vnet_params={
        'location': LOCATION,
        'address_space': {
            'address_prefixes': ['10.0.0.0/16']
        }
    }
    vnet_results=network_client.virtual_networks.create_or_update(
        RG_NAME,
        VNET_NAME,
        vnet_params
    )
    return vnet_results.result()