#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, KIKUCHI Koichiro <koichiro@hataki.jp>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: pandorafms_plugin_facts
short_description: Gather facts about Pandora FMS plugins
description:
    - Gather facts about plugins in Pandora FMS.
version_added: "2.7"
options:
    convert_macros:
        description:
            - If set to C(no), plugin macros not converted to json.
        type: bool
        default: yes
extends_documentation_fragment: pandorafms
author:
    - KIKUCHI Koichiro (@koichirok)
'''

EXAMPLES = '''
- name: Get plugin info
  pandoramfs_plugin_facts:
    console_url: http://example.com/pandora_console/
    login_user: admin
    login_password: pandora
    api_password: 1234
'''

RETURN = '''
---
pandora_plugin_facts:
  description: All plugins in Pandora FMS instance
  returned: success
  type: list
  sample:
    [
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
        },
    ]
'''

from ansible.module_utils.pandorafms import PandoraFMSAPI
from ansible.module_utils.pandorafms import PandoraFMSAPIModule


def main():

    module = PandoraFMSAPIModule(
        argument_spec = dict(
            convert_macros=dict(type='bool',default=True),
        ),
        supports_check_mode=True
    )
    api = PandoraFMSAPI(module)

    plugins = api.get_plugins(module.params['convert_macros'])

    module.exit_json(pandorafms_plugin_facts=plugins)


if __name__ == '__main__':
    main()
