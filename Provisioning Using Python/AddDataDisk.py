from azure.mgmt.compute.models import DiskCreateOption
def add_datadisk(compute_client,RG_GROUP,DATADISK_NAME,VM_NAME,LOCATION):
    disk_creation = compute_client.disks.create_or_update(
        RG_GROUP,
        DATADISK_NAME,
        {
            'location': LOCATION,
            'disk_size_gb': 1,
            'creation_data': {
                'creation_option': DiskCreateOption.empty
            }
        }
    )
    data_disk = disk_creation.result()
    vm = compute_client.virtual_machine.get(RG_GROUP,VM_NAME)
    add_result = vm.storage_profile.data_disks.append({
        'lun': 1,
        'name': DATADISK_NAME,
        'create_option': DiskCreateOption.attach,
        'managed_disk': {
            'id': data_disk.id
        }
    })
    add_result = compute_client.virtual_machines.create_or_update(
        RG_GROUP,
        VM_NAME,
        vm
    )
    return add_result.result()