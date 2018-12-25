#!/bin/sh

cd ${0%/*}

ansible-playbook -i 'localhost,' generate-documentation.yml
