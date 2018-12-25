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
module: pandorafms_group_facts
short_description: Gather facts about Pandora FMS groups
description:
    - Gather facts about groups in Pandora FMS.
version_added: "2.7"
notes:
    - Due to Pandora FMS API limitations, this module returns only the group's ID and name.
extends_documentation_fragment: pandorafms
author:
    - KIKUCHI Koichiro (@koichirok)
'''

EXAMPLES = '''
- name: Get group info
  pandoramfs_group_facts:
    console_url: http://example.com/pandora_console/
    login_user: admin
    login_password: pandora
    api_password: 1234
'''

RETURN = '''
---
pandora_group_facts:
  description: All groups in Pandora FMS instance
  returned: success
  type: list
  sample:
    [
        {
            "id": 0,
            "name": "All"
        },
    ]
'''

from ansible.module_utils.pandorafms import PandoraFMSAPIModule
from ansible.module_utils.pandorafms import PandoraFMSAPI


def main():
    module = PandoraFMSAPIModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    api = PandoraFMSAPI(module)

    groups = api.get_groups()

    module.exit_json(pandorafms_group_facts=groups)


if __name__ == '__main__':
    main()
