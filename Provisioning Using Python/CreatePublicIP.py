def create_public_ip_address(network_client,LOCATION,PUB_IP_NAME,RG_NAME):
    pip_params={
        'location': LOCATION,
        'public_ip_allocation_method': 'Dynamic'
    }
    pip_result = network_client.public_ip_addresses.create_or_update(
        RG_NAME,
        PUB_IP_NAME,
        pip_params
    )
    return pip_result.result()