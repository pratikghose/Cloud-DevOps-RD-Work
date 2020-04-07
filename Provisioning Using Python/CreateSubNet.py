def create_subnet(network_client,RG_NAME,VNET_NAME,SUBNET_NAME):
    subnet_params={
        'address_prefix': '10.0.0.0/16'
    }
    subnet_results = network_client.subnets.create_or_update(
        RG_NAME,
        VNET_NAME,
        SUBNET_NAME,
        subnet_params
    )
    return subnet_results.result()