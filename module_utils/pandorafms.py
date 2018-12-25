# -*- coding: utf-8 -*-
# Copyright: (c) 2018, KIKUCHI Koichiro < koichiro () hataki.jp>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


import json

from ansible.module_utils._text import to_text
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.module_utils.urls import fetch_url
from ansible.module_utils.basic import AnsibleModule


class PandoraFMSAPIModule(AnsibleModule):
    """
    Ansible module which uses Pandora FMS API for operation.
    """
    def __init__(self, argument_spec, **kwargs):
        common_args_spec = dict(
            console_url=dict(required=True, type='str'),
            login_user=dict(required=True, type='str'),
            login_password=dict(required=True, no_log=True, type='str'),
            api_password=dict(required=True, no_log=True, aliases=['apipass'], type='str'),
            timeout=dict(default=10, type='int'),
            validate_certs=dict(default=True, type='bool'),
        )
        common_args_spec.update(argument_spec)
        super(PandoraFMSAPIModule, self).__init__(common_args_spec, **kwargs)


class PandoraFMSAPI:
    def __init__(self, module):
        self.module = module
        console_url = module.params['console_url']
        if not console_url.endswith('/'):
            console_url += '/'
        self.api_url = console_url + 'include/api.php'
        self.api_auth = {
            'user': to_text(module.params['login_user']),
            'pass': to_text(module.params['login_password']),
            'apipass': to_text(module.params['api_password']),
        }

    def fetch_api_url(self, params_get={}, params_post={}):
        data = self.api_auth.copy()
        data.update(params_post)
        url = self.api_url
        if params_get:
            url += '?' + urlencode(params_get)

        res, info = fetch_url(
            self.module,
            url,
            data=urlencode(data),
            headers={'Content-type': 'application/x-www-form-urlencoded'},
            method="POST",
            timeout=self.module.params['timeout']
        )
        result = '' if res is None else to_text(res.read())

        if info['status'] != 200:
            self.module.fail_json(msg='HTTP Error: ' + str(info['status']))
        if result.startswith('Error'):
            self.module.fail_json(msg=result)
        return result


    def get_plugins(self, convert_macros=False):
        sep = ';'
        result = self.fetch_api_url(dict(op='get',op2='plugins',other=sep))
        keys = ['id','name','description','max_timeout','max_retries','execute',
                'net_dst_opt','net_port_opt','user_opt','pass_opt','plugin_type',
                'macros','parameters']
        plugins = []

        for x in result.split("\n"):
            if x:
                d = dict(zip(keys,x.split(sep)))
                if convert_macros:
                    try:
                        d['macros'] = json.loads(d['macros'])
                    except Exception:
                        pass
                plugins.append(d)

        return plugins


    def get_groups(self, name=None):
        result = self.fetch_api_url(dict(op='get',op2='groups',return_type='json'))
        jsonresult = json.loads(result)

        groups = [ {'id':x[0],'name':x[1]} for x in jsonresult['data'] ]

        return groups


    def get_group_id_by_name(self, name):
        return self.fetch_api_url(dict(op='get',op2='group_id_by_name',other=name)).strip()


    def delete_group(self, group_id):
        result = self.fetch_api_url({'op':'set','op2':'delete_group','id':group_id}).strip()

        if 'Correct Delete' not in result:
            self.module.fail_json(msg="Failed to delete group `{}': {}".format(group_name,result))

        return result


    def create_group(self, group_name):
        other = self.make_group_other_params([self.module.params['icon']])
        result = self.fetch_api_url({'op':'set','op2':'create_group','id':group_name}, other).strip()
        if not result.isdigit():
            self.module.fail_json(msg="Failed to create group: {}: {}".format(group_name,result))

        return result


    def update_group(self, group_id, group_name):
        other = self.make_group_other_params([group_name, self.module.params['icon']])
        result = self.fetch_api_url({'op':'set','op2':'update','id':group_id}, other).strip()

        if not result.isdigit():
            self.module.fail_json(msg="Failed to update group: {}: {}".format(group_name,result))

        return result


    def make_group_other_params(self, initial=[]):
        return self.make_other_params(
            initial,
            [
                ('parent_group', ''),
                ('description', ''),
                ('propagate_acl', '0'),
                ('disable_alerts', '0'),
                ('custom_id', ''),
                ('contact_info', ''),
                ('other_info', '')
            ]
        )

    def make_other_params(self, initial=[], defaults=[]):
        # `other' params are fully ordered and could not omit when later params are specified.
        other = initial.copy()
        tmp = []
        for opt in defaults:
            value = self.module.params[opt[0]]
            # If option is omitted, put default to 'tmp' list
            if value is None:
                tmp.append(opt[1])
            else:
                other += tmp
                tmp = []
                if opt[0] == 'parent_group':
                    parent_id = self.get_group_id_by_name(value)
                    if not parent_id.isdigit():
                        self.module.fail_json(msg="An error occurred while creating request string: parent_group not present: " + value)
                    other.append(parent_id)
                elif type(value) is bool:
                    other.append(str(int(value)))
                else:
                    other.append(value)

        other_string = ''.join(other)

        for sep in '|;%$*#@!':
            if sep not in other_string:
                return dict(
                    other=sep.join(other),
                    other_mode='url_encode_separator_' + sep
                )
        self.module.fail_json(msg="An error occurred while creating request string: failed to determin separator character for `other'")


