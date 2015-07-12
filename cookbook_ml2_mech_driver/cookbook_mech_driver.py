import sys
import re
import socket

from neutron.db import api as db
from neutron.plugins.ml2 import db as ml2_db
from neutron.plugins.ml2 import driver_api as api
from neutron.openstack.common import log as logger

driver_logger = logger.getLogger(__name__)


class CookbookMechanismDriver(api.MechanismDriver):

    def initialize(self):
        driver_logger.error("Inside Mech Driver Initialize")


    def create_network_precommit(self, context):
        driver_logger.error("Inside Nework Precommit")
        network_context = context.current
        plugin_context = context._plugin_context
	driver_logger.error(network_context)
        driver_logger.error("******")
	driver_logger.error(plugin_context)


    def create_network_postcommit(self, context):
        driver_logger.error("Inside Nework Postcommit")
        network_context = context.current
        plugin_context = context._plugin_context
	driver_logger.error(network_context)
        driver_logger.error("******")
	driver_logger.error(plugin_context)
	
