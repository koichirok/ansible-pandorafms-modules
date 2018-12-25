# pandorafms\_plugin\_facts - Gather facts about Pandora FMS plugins

## Synopsis

Gather facts about plugins in Pandora FMS.


## Parameters

| Parameter     | Choices/Defaults | Comments |
| ------------- |------------------| ---------|
| convert\_macros| **Default:**<br>True| If set to False, plugin macros not converted to json. |


## Examples

```
- name: Get plugin info
  pandoramfs_plugin_facts:
    console_url: http://example.com/pandora_console/
    login_user: admin
    login_password: pandora
    api_password: 1234

```

## Return Values
## License

GPLv3
