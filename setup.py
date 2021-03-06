# coding:utf-8

import os
import sys
import platform
from setuptools import setup, find_packages

config_sample = '''
qy_access_key_id: 'QINGCLOUDACCESSKEYID'
qy_secret_access_key: 'QINGCLOUDSECRETACCESSKEYEXAMPLE'
zone: 'ZONEID'
'''

def is_windows():
    return platform.system().lower() == 'windows'

def prepare_config_file():
    config_file = os.path.expanduser('~/.qingcloud/config.yaml')
    if os.path.exists(config_file):
        return

    d = os.path.dirname(config_file)
    if not os.path.exists(d):
        os.makedirs(d)

    with open(config_file, 'w') as fd:
        fd.write(config_sample)

def setup_qingcloud_completer():
    # only support linux
    if is_windows():
        return

    cmd = 'complete -C qingcloud_completer qingcloud'
    complete_file = '/etc/bash_completion.d/qingcloud-cli'
    if not os.path.exists(os.path.dirname(complete_file)):
        with open(os.path.expanduser('~/.bash_profile'), 'a') as fd:
            fd.write('\n\n# QingCloud CLI\n%s\n' % cmd)
    else:
        with open((complete_file), 'w') as fd:
            fd.write(cmd)


if len(sys.argv) < 2 or sys.argv[1] != 'install':
    bin_scripts = ['bin/qingcloud', 'bin/qingcloud.cmd', 'bin/qingcloud_completer']
elif is_windows():
    bin_scripts = ['bin/qingcloud.cmd']
else:
    bin_scripts = ['bin/qingcloud', 'bin/qingcloud_completer']

setup(
    name = 'qingcloud-cli',
    version = '0.9.9',
    description = 'Command Line Interface for QingCloud.',
    long_description = open('README.rst', 'rb').read().decode('utf-8'),
    keywords = 'qingcloud iaas cli',
    author = 'Yunify Team',
    author_email = 'simon@yunify.com',
    url = 'https://docs.qingcloud.com/cli/',
    scripts=bin_scripts,
    packages = find_packages('.'),
    package_dir = {'qingcloud-cli': 'qingcloud'},
    namespace_packages = ['qingcloud'],
    include_package_data = True,
    install_requires = [
        'argparse>=1.1',
        'PyYAML>=3.1',
        'qingcloud-sdk>=0.9.1',
    ]
)

if len(sys.argv) >= 2 and sys.argv[1] == 'install':
    prepare_config_file()
    setup_qingcloud_completer()
