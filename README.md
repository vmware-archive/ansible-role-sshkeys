# ansible-role-sshkeys

[Ansible](https://github.com/ansible/ansible) module for creating
and rotating SSH keys on fleets of servers.  The work was inspired (though
dramatically altered and upgraded) by an
[article about the topic](https://derpops.bike/2014/06/07/ssh-key-rotation-with-ansible/)
authored (posted online) by Jesse Keating, June 7, 2014.

On every run, this role will
* create a new local ssh key,
* copy that key to all remote hosts
* replace our main local ssh key with the newly created key

General use case is to run this role in a playbook using the
`--ask-password` parameter to `ansible-playbook` to be able to run
future plays without password entry.  Re-running the same play without password
will result in rotating the keys of the local ssh user and all remote hosts.

For ansible to use the generated ssh key, make sure ansible.cfg has
a line like `private_key_file = your-private-key`, where `your-private-key` is the location
used in the variable `sshkeys_local_final_pub_key`

***When trying to rotate keys, unreachable hosts result in loss of key sync.
You will need to re-sync those hosts using a password when they are reachable.***

## Requirements

Must have ssh-keygen locally and be running openssh on the remote hosts

## Role Variables

Available variables can be found in [vars](defaults/main.yml).

Key variables are:

Local user who should own the ssh keys. By default, we'll use the user running the ansible play.

    sshkeys_remote_user
    sshkeys_remote_group

User and group that we will ssh in as on the remote side.
By default, these will be set to the `ansible_ssh_user`

    sshkeys_local_final_priv_key: "{{ sshkeys_local_dir }}/ansible_role_test_key"
    sshkeys_local_final_pub_key: "{{ sshkeys_local_final_priv_key }}.pub"

Location of the final public and private key storage.  These are the keys
ansible should use to connect to the remote hosts passwordless.

## Example playbook

```yamlex

---
- hosts: sshhosts
  roles:
    - sshkeys

```

# License and Copyright

Copyright 2015-2017 VMware, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Author Information

This role was created in 2015 by [Tom Hite / VMware](http://www.vmware.com/).
