from oslo_log import log as logger
from neutron.plugins.ml2 import driver_api as api

driver_logger = logger.getLogger(__name__)


class CookbookNetworkMechanismDriver(api.MechanismDriver):

    def _log_network_information(self, method_name, current_context, prev_context):
        driver_logger.info("**** %s ****" % (method_name))
	# Print the Network Name using the context
        driver_logger.info("Current Network Name: %s" % (current_context['name']))
	# For create operation prev_context will be None.
        if prev_context is not None:
            driver_logger.info("Previous Network Name: %s" % (prev_context['name']))
	# Print the Network Type
        driver_logger.info("Current Network Type: %s" % current_context['provider:network_type'])
        driver_logger.info("**** %s ****" % (method_name))

    def create_network_postcommit(self, context):
	# Extract the current and the previous network context
        current_network_context = context.current
        previous_network_context = context.original
	self._log_network_information("Create Network PostCommit", current_network_context, previous_network_context)

    def update_network_postcommit(self, context):
	# Extract the current and the previous network context
        current_network_context = context.current
        previous_network_context = context.original
	self._log_network_information("Update Network PostCommit", current_network_context, previous_network_context)


