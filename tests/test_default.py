from __future__ import print_function
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')

# Use testinfra to get a handy function to run commands locally
check_output = testinfra.get_backend(
    "local://"
).get_module("Command").check_output


def test_hosts_file(File):
    f = File('/root/.ssh/authorized_keys')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

    command = check_output(
        'cat ~/.ssh/ansible_role_test_key.pub')
    assert command == f.content_string.rstrip()
