def create_resource_group(rg_client,LOCATION,RG_NAME):
    rg_params = {'location': LOCATION}
    rg_results = rg_client.resource_groups.create_or_update(
        RG_NAME,
        rg_params
    )
    return rg_results
