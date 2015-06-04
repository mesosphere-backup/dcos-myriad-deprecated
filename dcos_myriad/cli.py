"""Run and manage Myriad Named nodes

Usage:
    dcos myriad --info
    dcos myriad --version
    dcos myriad state
    dcos myriad config
    dcos myriad flexup 	 <count> <profile>
    dcos myriad flexdown <count>
    dcos myriad webui

Options:
    -h, --help       Show this screen
    --info           Show a short description of this subcommand
    --version               Show version
	
Positional Arguments:
    <count>     The number of nodes to increase or decrease in your cluster
    <profile>	The profile size to add (small, medium, large)
"""
from __future__ import print_function
import docopt
from dcos import cmds, emitting, http, mesos, util
from dcos.errors import DCOSException
from dcos_myriad import constants

emitter = emitting.FlatEmitter()
logger = util.get_logger(__name__)


def main():
    try:
        return _main()
    except DCOSException as e:
        emitter.publish(e)
        return 1


def _main():
    util.configure_logger_from_environ()

    args = docopt.docopt(
        __doc__,
        version='myriad cli version {}'.format(constants.version))

    http.silence_requests_warnings()

    return cmds.execute(_cmds(), args)


def _cmds():
    """
    :returns: all the supported commands
    :rtype: list of dcos.cmds.Command
    """

    return [

        cmds.Command(
            hierarchy=['myriad'],
            arg_keys=['--info'],
            function=_info),
    ]


def _info(info):
    """
    :param info: Whether to output a description of this subcommand
    :type info: boolean
    :returns: process status
    :rtype: int
    """

    emitter.publish(__doc__.split('\n')[0])
    return 0

