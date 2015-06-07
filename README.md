# ansible-role-sshkeys

[Ansible](https://github.com/ansible/ansible) module for creating
and rotating SSH keys on fleets of servers.

## Requirements

This role currently supports only Debian/Ubuntu distros.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    sshkeys_user: vmware

The userid (login name) of the user that is the owner of the home directory in which new keys should be placed.
This also is the user for which the authorized_keys file will be updated with the new key.

    new_priv_key

Full path to where any private SSH keys, when generated, should be stored as operatins take place to distribute its public side.

    new_pub_key

Full path to where new public SSH keys, when generated, should be stored as operatins take place to distribute its public side.
Defaults to "{{ new_priv_key }}.pub" and that's sufficient for the vast majority of applications.

## Example playbook

```
---
- hosts: supervio
  sudo: True
  connection: local
  roles:
    - sshkeys
  vars:
    - packate: False
```

## License

TBD

## Author Information

This role was created in 2015 by [Tom Hite / VMware](http://www.vmware.com/).

The work was inspired (though dramatically altered and upgraded) by an
[article about the topic](https://derpops.bike/2014/06/07/ssh-key-rotation-with-ansible/).
The link above is often broken, but when alive will give a reasonable view of the genisis.
