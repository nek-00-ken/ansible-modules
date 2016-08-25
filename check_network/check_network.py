#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2015, Quentin Moulinier <quentin.moulinier@gmail.com>

DOCUMENTATION = '''
---
module: check_network
version_added: historical
short_description: check TCP flux
description:
- This module checks TCP flux using nc system command.
options:
  link:
    description:
      - A link is defined by a [hostname/ip address] and a port number
        A valid link is : "ip_address:port"
        A valid link is : "hostname:port" (You can give a hostname instead of ip address if resolved by host).
    required: true
author:
    - "Quentin Moulinier"
'''

EXAMPLES = '''
ansible <host> -M <path_to_module> -m check_network -a "link=localhost:22"
'''


def check_flux(destination, port):
    cmd = "nc %s %s < /dev/null" % (destination, port)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    process.wait()
    return process.returncode


def main():
    module = AnsibleModule(
        argument_spec=dict(
            link=dict(required=True, type='str'),
        ),
    )
    (destination, ip_port) = module.params['link'].split(':')
    if check_flux(destination, ip_port) == 0:
        module.exit_json()
    module.fail_json(msg="port %s is not opened on %s" % (ip_port, destination))


from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
