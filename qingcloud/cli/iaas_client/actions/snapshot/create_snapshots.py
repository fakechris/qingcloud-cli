# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class CreateSnapshotsAction(BaseAction):

    action = 'CreateSnapshots'
    command = 'create-snapshots'
    usage = '%(prog)s --resource <resource_id,...> --zone <zone_id> --name <snapshotname> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-r', '--resource', dest='resource',
                action='store', type=str, default='',
                help='resource to be captured.')

        parser.add_argument('-z', '--zone', dest='zone',
                action='store', type=str, default='pek1',
                help='the resource in zone.')

        parser.add_argument('-n', '--name', dest='name',
                action='store', type=str, default='',
                help='snapshot name to be created.')

    @classmethod
    def build_directive(cls, options):
        required_params = {'resource': options.resource,
            'zone': options.zone,
            'name': options.name}
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'error: [%s] should be specified' % param
                return None

        return {
                'resources': explode_array(options.resource),
                'zone' : options.zone,
                'is_full' : 0,
                'snapshot_name': options.name
                }
