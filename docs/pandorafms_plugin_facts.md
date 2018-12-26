# pandorafms\_plugin\_facts - Gather facts about Pandora FMS plugins

## Synopsis

Gather facts about plugins in Pandora FMS.


## Parameters

| Parameter     | Choices/[Defaults](#) | Comments |
| ------------- |------------------| ---------|
| api\_password<br><h6>required</h6>| | api password for the Pandora FMS console. |
| console\_url<br><h6>required</h6>| | URL of the Pandora FMS Console, with protocol (http or https). |
| convert\_macros<br><h6>bool</h6>| **Default:**<br>[True](#)</div>| If set to `no`, plugin macros not converted to json. |
| login\_password<br><h6>required</h6>| | password for the *login\_user*. |
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
| pandora\_plugin\_facts<br/><h6>list</h6>| success | All plugins in Pandora FMS instance<br><div style="font-size: smaller">**Sample:**</div><div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[[<br>&nbsp;&nbsp;&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"description":&nbsp;"Samples:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;./mysql_plugin.sh&nbsp;-u&nbsp;root&nbsp;-p&nbsp;none&nbsp;-s&nbsp;localhost&nbsp;-q&nbsp;Com_select&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;./mysql_plugin.sh&nbsp;-u&nbsp;root&nbsp;-p&nbsp;none&nbsp;-s&nbsp;localhost&nbsp;-q&nbsp;Com_update&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;./mysql_plugin.sh&nbsp;-u&nbsp;root&nbsp;-p&nbsp;none&nbsp;-s&nbsp;localhost&nbsp;-q&nbsp;Connections&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;./mysql_plugin.sh&nbsp;-u&nbsp;root&nbsp;-p&nbsp;anypass&nbsp;-s&nbsp;192.168.50.24&nbsp;-q&nbsp;Innodb_rows_read&nbsp;&nbsp;",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"execute":&nbsp;"/usr/share/pandora_server/util/plugin/mysql_plugin.sh",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id":&nbsp;"6",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"macros":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"1":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"desc":&nbsp;"IP&nbsp;address",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"help":&nbsp;"IP&nbsp;address",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"macro":&nbsp;"_field1_",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"value":&nbsp;""<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"2":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"desc":&nbsp;"Username",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"help":&nbsp;"Username&nbsp;to&nbsp;access&nbsp;to&nbsp;database",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"macro":&nbsp;"_field2_",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"value":&nbsp;""<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"3":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"desc":&nbsp;"Password",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"help":&nbsp;"Password&nbsp;to&nbsp;access&nbsp;to&nbsp;database",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"macro":&nbsp;"_field3_",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"value":&nbsp;""<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"4":&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"desc":&nbsp;"Query&nbsp;string",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"help":&nbsp;"Query&nbsp;string&nbsp;of&nbsp;global&nbsp;status.&nbsp;For&nbsp;example&nbsp;'Aborted_connects'&nbsp;or&nbsp;'Innodb_rows_read'",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"macro":&nbsp;"_field4_",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"value":&nbsp;""<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"max_retries":&nbsp;"0",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"max_timeout":&nbsp;"15",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name":&nbsp;"MySQL&nbsp;Plugin",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"net_dst_opt":&nbsp;"",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"net_port_opt":&nbsp;"",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"parameters":&nbsp;"-s&nbsp;_field1_&nbsp;-u&nbsp;_field2_&nbsp;-p&nbsp;_field3_&nbsp;-q&nbsp;_field4_",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"pass_opt":&nbsp;"",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"plugin_type":&nbsp;"0",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"user_opt":&nbsp;""<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>]](#)</div> |

## Notes

- To use this module, you have to configure API access for your Pandora FMS console. see https://wiki.pandorafms.com/index.php?title=Pandora:Documentation_en:Annex_ExternalAPI for detail.

## License

GPLv3
