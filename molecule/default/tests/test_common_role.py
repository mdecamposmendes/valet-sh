import os
import re
from zoneinfo import available_timezones
import pytest
import unittest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_if_packages_are_installed(host):
    required_package = ['git','curl']
    for each_package in required_package:
        assert host.package(each_package),is_installed

def test_if_vm_max_map_count_is_set(host):
    cmd = host.run('cat /proc/sys/vm/max_map_count')
    assert cmd.stdout == '262144\n'

def test_if_fs_inotify_max_user_watches_is_set(host):
    cmd = host.run('cat /proc/sys/fs/inotify/max_user_watches')
    assert cmd.stdout == '524288\n'

