Ansible Modules for Pandora FMS
===============================

Ansible modules for [Pandora FMS](https://pandorafms.org)

Requirements
------------

* Ansible >= ...
* Python >= 2.7.x
* Pandora FMS >= ... (now only tested with 7.0NG 729)

Installation and use
--------------------

```
$ ansible-galaxy install koichirok.pandorafms_modules
```

Once installed, use the modules in playbook or role:

```
- name: Load modules
  roles:
    - koichirok.pandorafms_modules
  tasks:
    ...
```

Modules
-------

See [docs/list\_of\_all\_modules.md](docs/list_of_all_modules.md)
