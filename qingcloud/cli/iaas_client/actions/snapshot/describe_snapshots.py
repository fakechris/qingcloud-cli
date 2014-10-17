# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeSnapshotsAction(BaseAction):

    action = 'DescribeSnapshots'
    command = 'describe-snapshots'
    usage = '%(prog)s -r "resource_id" -z <zone_id> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-r', '--resource', dest='resource',
                action='store', type=str, default='',
                help='snapshots you want to describe.')
            
        parser.add_argument('-z', '--zone', dest='zone',
                action='store', type=str, default='pek1',
                help='the resource in zone.')

    @classmethod
    def build_directive(cls, options):
        if not options.resource:
            print 'error: [resource] should be specified'
            return None
        return {
                'resource': options.resource,
                'zone': options.zone,
                'limit': 100
                }
