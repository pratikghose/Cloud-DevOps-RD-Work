def create_availability_set(compute_client,LOCATION,AVAILSETS_NAME,RG_NAME):
    avset_params={
        'location': LOCATION,
        'sku': {'name': 'Aligned'},
        'platform_fault_domain_count': 3
    }
    avset_results = compute_client.availability_sets.create_or_update(
        RG_NAME,
        AVAILSETS_NAME,
        avset_params
    )
    return avset_results