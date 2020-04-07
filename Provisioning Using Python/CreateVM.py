def create_vm(network_client,compute_client,VM_NAME,RG_NAME,LOCATION,NIC_NAME,AVAILSETS_NAME,userid,password,vmsize):
    nic = network_client.network_interfaces.get(
        RG_NAME,
        NIC_NAME
    )
    avset = compute_client.availability_sets.get(
        RG_NAME,
        AVAILSETS_NAME
    )
    vm_params = {
        'location': LOCATION,
        'os_profile': {
            'computer_name': VM_NAME,
            'admin_username': userid,
            'admin_password': password
        },
        'hardware_profile': {
            'vm_size': vmsize
        },
        'storage_profile': {
            'image_reference': {
                'publisher': 'MicrosoftWindowsServer',
                'offer': 'WindowsServer',
                'sku': '2012-R2-Datacenter',
                'version': 'latest'
            }
        },
        'network_profile':{
            'network_interfaces': [{
                'id': nic.id
            }]
        },
        'availability_set': {
            'id': avset.id
        }
    }

    vm_results = compute_client.virtual_machines.create_or_update(
        RG_NAME,
        VM_NAME,
        vm_params
    )

    return  vm_results.result()