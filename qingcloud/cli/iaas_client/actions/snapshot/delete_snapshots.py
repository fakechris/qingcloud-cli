# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DeleteSnapshotsAction(BaseAction):

    action = 'DeleteSnapshots'
    command = 'delete-snapshots'
    usage = '%(prog)s -s "snapshot_id,..." [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
    
        parser.add_argument('-s', '--snapshots', dest='snapshots',
                action='store', type=str, default='',
                help='snapshots you want to delete.')
            
        parser.add_argument('-z', '--zone', dest='zone',
                action='store', type=str, default='pek1',
                help='the resource in zone.')
        
    @classmethod
    def build_directive(cls, options):
        if not options.snapshots:
            print 'error: [snapshots] should be specified'
            return None

        return {'snapshots': explode_array(options.snapshots),
            'zone': options.zone}

