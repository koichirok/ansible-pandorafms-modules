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
module: pandorafms_group
short_description: Manage Pandora FMS groups
description:
    - Ansible module to manage Pandora FMS groups
version_added: "2.7"
options:
    name:
        description:
            - name of the group.
        required: true
    icon:
        description:
            - name of the group icon.
        required: true
    parent_group:
        description:
            - name of the parent group.
    description:
        description:
            - description of the group.
    propagate_acl:
        description:
            - Wheter to enable or disable ACL propagation.
        type: bool
    disable_alerts:
        description:
            - Wheter to disable or enable alerts in group.
        type: bool
    custom_id:
        description:
            - custom id of the group.
    contact_info:
        description:
            - contact information of the group.
    other_info:
        description:
            - other information of the group.
    force:
        description:
            - If set to C(yes), group always updated even if it already present.
        type: bool
        default: no
    state:
        description:
            - Whether to create C(present), or delete C(absent) module group.
        default: present
        choices: [ "present", "absent" ]
notes:
    - Due to the Pandora FMS API limitations, diff mode is not supported.
extends_documentation_fragment: pandorafms
author:
    - KIKUCHI Koichiro (@koichirok)
'''

EXAMPLES = '''
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
'''

RETURN = '''
---
group.status:
    description: state of group
    returned: success
    type: string
    sample: not present
group.id:
    description: id of group
    returned: if group present
    type: string
    sample: 15
group.name:
    description: name of group
    returned: success
    type: string
    sample: Servers
'''

import json

from ansible.module_utils._text import to_text
from ansible.module_utils.pandorafms import PandoraFMSAPIModule
from ansible.module_utils.pandorafms import PandoraFMSAPI


def main():
    argument_spec = dict(
        name=dict(required=True, type='str'),
        icon=dict(type='str'),
        parent_group=dict(default=None, type='str'),
        description=dict(default=None, type='str'),
        propagate_acl=dict(default=None, type='bool'),
        disable_alerts=dict(default=None, type='bool'),
        custom_id=dict(default=None, type='str'),
        contact_info=dict(default=None, type='str'),
        other_info=dict(default=None, type='str'),
        force=dict(default=False, type='bool'),
        state=dict(default='present', choices=['absent', 'present']),
    )

    module = PandoraFMSAPIModule(
        argument_spec=argument_spec,
        required_if=[ ('state', 'present', ['icon']) ],
        supports_check_mode=True
    )

    api = PandoraFMSAPI(module)

    group_name = module.params['name']
    state = module.params['state']
    parent_group = module.params['parent_group']
    force = module.params['force']

    group_id = api.get_group_id_by_name(group_name)
    group = dict(name=group_name)

    if state == 'absent':
        if not group_id.isdigit():
            group['state'] = 'not present'
            module.exit_json(changed=False, group=group)

        group['id'] = group_id
        if module.check_mode:
            group['state'] = 'will be deleted'
            module.exit_json(changed=True, group=group)

        api.delete_group(group_id)
        group['state'] = 'deleted'

    elif state == 'present':
        if not group_id.isdigit():
            if module.check_mode:
                group['state'] = 'will be created'
                module.exit_json(changed=True, msg="group `{}' not present".format(group_name))

            result = api.create_group(group_name)
            group['id'] = result
            group['state'] = 'created'
        else:
            group['id'] = group_id
            if not force:
                group['state'] = 'present'
                module.exit_json(changed=False, group=group)
            elif module.check_mode:
                # always `changed' since we could not obtain group properties from API :(
                group['state'] = 'will be updated'
                module.exit_json(changed=True, group=group)

            result = api.update_group(group_id, group_name)
            group['state'] = 'updated'

    module.exit_json(changed=True, group=group)#, response=headers)

if __name__ == '__main__':
    main()
