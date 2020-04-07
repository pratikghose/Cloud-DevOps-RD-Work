def update_vm(compute_client,RG_NAME,VM_NAME):
    vm = compute_client.virtual_machines.get(RG_NAME,VM_NAME)
    vm.hardware_profile.vm.size = 'Standard_DS3'
    update_result = compute_client.virtual_machines.create_or_update(
        RG_NAME,
        VM_NAME,
        vm
    )
    return update_result.result();