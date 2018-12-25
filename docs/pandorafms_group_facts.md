# pandorafms\_group\_facts - Gather facts about Pandora FMS groups

## Synopsis

Gather facts about groups in Pandora FMS.


## Parameters



## Examples

```
- name: Get group info
  pandoramfs_group_facts:
    console_url: http://example.com/pandora_console/
    login_user: admin
    login_password: pandora
    api_password: 1234

```

## Return Values
## Notes

- Due to Pandora FMS API limitations, this module returns only the group's ID and name.

## License

GPLv3
