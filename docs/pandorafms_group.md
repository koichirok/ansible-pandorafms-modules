# pandorafms\_group - Manage Pandora FMS groups

## Synopsis

Ansible module to manage Pandora FMS groups


## Parameters

| Parameter     | Choices/[Defaults](#) | Comments |
| ------------- |------------------| ---------|
| api\_password<br><h6>required</h6>| | api password for the Pandora FMS console. |
| console\_url<br><h6>required</h6>| | URL of the Pandora FMS Console, with protocol (http or https). |
| contact\_info| | contact information of the group. |
| custom\_id| | custom id of the group. |
| description| | description of the group. |
| disable\_alerts<br><h6>bool</h6>| | Wheter to disable or enable alerts in group. |
| force<br><h6>bool</h6>| | If set to `yes`, group always updated even if it already present. |
| icon<br><h6>required</h6>| | name of the group icon. |
| login\_password<br><h6>required</h6>| | password for the 'login\_user'. |
| login\_user<br><h6>required</h6>| | user name to login to Pandora FMS Console. |
| name<br><h6>required</h6>| | name of the group. |
| other\_info| | other information of the group. |
| parent\_group| | name of the parent group. |
| propagate\_acl<br><h6>bool</h6>| | Wheter to enable or disable ACL propagation. |
| state| **Choices:**<ul><li>[**present** ←](#)</li><li>absent</li></ul>| Whether to create `present`, or delete `absent` module group. |
| timeout| **Default:**<br>[10](#)</div>| timeout of API request. |
| validate\_certs<br><h6>bool</h6>| **Default:**<br>[True](#)</div>| If set to `no`, SSL certificates will not be validated. |


## Examples

```yaml
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

Common return values are documented [here](https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values), the following are the fields unique to this module:

| Key | Returned | Description |
| --- |----------| ----------- |
| group.status<br/><h6>string</h6>| success | state of group<br><div style="font-size: smaller">**Sample:**</div><div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[not present](#)</div> |
| group.id<br/><h6>string</h6>| if group present | id of group<br><div style="font-size: smaller">**Sample:**</div><div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[15](#)</div> |
| group.name<br/><h6>string</h6>| success | name of group<br><div style="font-size: smaller">**Sample:**</div><div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[Servers](#)</div> |

## Notes

- Due to the Pandora FMS API limitations, diff mode is not supported.
- To use this module, you have to configure API access for your Pandora FMS console. see https://wiki.pandorafms.com/index.php?title=Pandora:Documentation\_en:Annex\_ExternalAPI for detail.

## License

GPLv3
