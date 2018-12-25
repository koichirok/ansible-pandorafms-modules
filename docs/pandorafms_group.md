# pandorafms\_group - Manage Pandora FMS groups

## Synopsis

Ansible module to manage Pandora FMS groups


## Parameters

| Parameter     | Choices/Defaults | Comments |
| ------------- |------------------| ---------|
| contact\_info| | contact information of the group. |
| custom\_id| | custom id of the group. |
| description| | description of the group. |
| disable\_alerts| | Wheter to disable or enable alerts in group. |
| force| | If set to True, group always updated even if it already present. |
| icon<br>required| | name of the group icon. |
| name<br>required| | name of the group. |
| other\_info| | other information of the group. |
| parent\_group| | name of the parent group. |
| propagate\_acl| | Wheter to enable or disable ACL propagation. |
| state| **Choices:**<ul><li>present ←</li><li>absent</li></ul>| Whether to create (`present'), or delete (`absent') module group. |


## Examples

```
---
- name: Example to create/update group
  pandoramfs_group:
    name: Test Group
    icon: applications
    description: description of Test Group
    console_url: http://example.com/pandora_console/
    login_user: admin
    login_password: pandora
    api_password: 1234

- name: Example to delete group
  pandorafms_group:
    name: Test Group
    state: absent
    console_url: http://example.com/pandora_console/
    login_user: admin
    login_password: pandora
    api_password: 1234

```

## Return Values
## Notes

- Due to the Pandora FMS API limitations, diff mode is not supported.

## License

GPLv3
