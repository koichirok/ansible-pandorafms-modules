# pandorafms\_plugin\_facts - Gather facts about Pandora FMS plugins

## Synopsis

Gather facts about plugins in Pandora FMS.


## Parameters

| Parameter     | Choices/[Defaults](#) | Comments |
| ------------- |------------------| ---------|
| api\_password<br><h6>required</h6>| | api password for the Pandora FMS console. |
| console\_url<br><h6>required</h6>| | URL of the Pandora FMS Console, with protocol (http or https). |
| convert\_macros<br><h6>bool</h6>| **Default:**<br>[True](#)</div>| If set to `no`, plugin macros not converted to json. |
| login\_password<br><h6>required</h6>| | password for the 'login\_user'. |
| login\_user<br><h6>required</h6>| | user name to login to Pandora FMS Console. |
| timeout| **Default:**<br>[10](#)</div>| timeout of API request. |
| validate\_certs<br><h6>bool</h6>| **Default:**<br>[True](#)</div>| If set to `no`, SSL certificates will not be validated. |


## Examples

```yaml
- name: Get plugin info
  pandoramfs_plugin_facts:
    console_url: http://example.com/pandora_console/
    login_user: admin
    login_password: pandora
    api_password: 1234

```

## Return Values

Common return values are documented [here](https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values), the following are the fields unique to this module:

| Key | Returned | Description |
| --- |----------| ----------- |
| pandora\_plugin\_facts<br/><h6>list</h6>| success | All plugins in Pandora FMS instance<br><div style="font-size: smaller">**Sample:**</div><div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[[
    {
        "description": "Samples:     ./mysql_plugin.sh -u root -p none -s localhost -q Com_select     ./mysql_plugin.sh -u root -p none -s localhost -q Com_update     ./mysql_plugin.sh -u root -p none -s localhost -q Connections     ./mysql_plugin.sh -u root -p anypass -s 192.168.50.24 -q Innodb_rows_read  ",
        "execute": "/usr/share/pandora_server/util/plugin/mysql_plugin.sh",
        "id": "6",
        "macros": {
            "1": {
                "desc": "IP address",
                "help": "IP address",
                "macro": "_field1_",
                "value": ""
            },
            "2": {
                "desc": "Username",
                "help": "Username to access to database",
                "macro": "_field2_",
                "value": ""
            },
            "3": {
                "desc": "Password",
                "help": "Password to access to database",
                "macro": "_field3_",
                "value": ""
            },
            "4": {
                "desc": "Query string",
                "help": "Query string of global status. For example 'Aborted_connects' or 'Innodb_rows_read'",
                "macro": "_field4_",
                "value": ""
            }
        },
        "max_retries": "0",
        "max_timeout": "15",
        "name": "MySQL Plugin",
        "net_dst_opt": "",
        "net_port_opt": "",
        "parameters": "-s _field1_ -u _field2_ -p _field3_ -q _field4_",
        "pass_opt": "",
        "plugin_type": "0",
        "user_opt": ""
    }
]](#)</div> |

## Notes

- To use this module, you have to configure API access for your Pandora FMS console. see https://wiki.pandorafms.com/index.php?title=Pandora:Documentation\_en:Annex\_ExternalAPI for detail.

## License

GPLv3
