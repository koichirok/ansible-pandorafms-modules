# -*- coding: utf-8 -*-

class ModuleDocFragment(object):
    # Standard F5 documentation fragment
    DOCUMENTATION = '''
options:
    console_url:
        description:
            - URL of the Pandora FMS Console, with protocol (http or https).
        required: true
    login_user:
        description:
            - user name to login to Pandora FMS Console.
        required: true
    login_password:
        description:
            - password for the I(login_user).
        required: true
    api_password:
        description:
            - api password for the Pandora FMS console.
        required: true
    timeout:
        description:
            - timeout of API request.
        default: 10
    validate_certs:
        description:
            - If set to C(no), SSL certificates will not be validated.
        default: yes
        type: bool
notes:
    - To use this module, you have to configure API access for your Pandora FMS console. see U(https://wiki.pandorafms.com/index.php?title=Pandora:Documentation_en:Annex_ExternalAPI) for detail.
'''
