# pandorafms\_group\_facts - Gather facts about Pandora FMS groups

## Synopsis

Gather facts about groups in Pandora FMS.


## Parameters

| Parameter     | Choices/[Defaults](#) | Comments |
| ------------- |------------------| ---------|
| api\_password<br><h6>required</h6>| | api password for the Pandora FMS console. |
| console\_url<br><h6>required</h6>| | URL of the Pandora FMS Console, with protocol (http or https). |
| login\_password<br><h6>required</h6>| | password for the 'login\_user'. |
| login\_user<br><h6>required</h6>| | user name to login to Pandora FMS Console. |
| timeout| **Default:**<br>[10](#)</div>| timeout of API request. |
| validate\_certs<br><h6>bool</h6>| **Default:**<br>[True](#)</div>| If set to `no`, SSL certificates will not be validated. |


## Examples

```yaml
- name: Get group info
  pandoramfs_group_facts:
    console_url: http://example.com/pandora_console/
    login_user: admin
    login_password: pandora
    api_password: 1234

```

## Return Values

Common return values are documented [here](https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values), the following are the fields unique to this module:

| Key | Returned | Description |
| --- |----------| ----------- |
| pandora\_group\_facts<br/><h6>list</h6>| success | All groups in Pandora FMS instance<br><div style="font-size: smaller">**Sample:**</div><div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[[
    {
        "id": 0,
        "name": "All"
    }
]](#)</div> |

## Notes

- Due to Pandora FMS API limitations, this module returns only the group's ID and name.
- To use this module, you have to configure API access for your Pandora FMS console. see https://wiki.pandorafms.com/index.php?title=Pandora:Documentation\_en:Annex\_ExternalAPI for detail.

## License

GPLv3
