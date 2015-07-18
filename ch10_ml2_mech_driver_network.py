try:
    from neutron.openstack.common import log as logger
except ImportError:
    from oslo_log import log as logger 
from neutron.plugins.ml2 import driver_api as api

driver_logger = logger.getLogger(__name__)


class CookbookMechanismDriver(api.MechanismDriver):

    def initialize(self):
        driver_logger.error("Inside Mech Driver Initialize")

    def _log_network_information(self, method_name, current_context, prev_context):
        driver_logger.error("**** %s ****" % (method_name))
        driver_logger.error("Current Network Name: %s" % (current_context['name']))
        if prev_context is not None:
            driver_logger.error("Previous Network Name: %s" % (prev_context['name']))
        driver_logger.error("Current Network Type: %s" % current_context['provider:network_type'])
        driver_logger.error("**** %s ****" % (method_name))

    def create_network_postcommit(self, context):
        current_network_context = context.current
        previous_network_context = context.original
	self._log_network_information("Create Network PostCommit", current_network_context, previous_network_context)
	
    def update_network_postcommit(self, context):
        current_network_context = context.current
        previous_network_context = context.original
	self._log_network_information("Update Network PostCommit", current_network_context, previous_network_context)
        pass


