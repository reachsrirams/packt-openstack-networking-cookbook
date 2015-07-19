# Import Neutron Database API
from neutron.db import api as db
try:
    from neutron.openstack.common import log as logger
except ImportError:
    from oslo_log import log as logger
from neutron.plugins.ml2 import driver_api as api

# Import ML2 Database API
from neutron.plugins.ml2 import db as ml2_db


driver_logger = logger.getLogger(__name__)


class CookbookMechanismDriver(api.MechanismDriver):

    def initialize(self):
        driver_logger.error("Inside Mech Driver Initialize")

    def _log_network_information(self, method_name, current_context, prev_context):
        driver_logger.error("**** %s ****" % (method_name))
	# Print the Network Name using the context
        driver_logger.error("Current Network Name: %s" % (current_context['name']))
	# For create operation prev_context will be None. 
        if prev_context is not None:
            driver_logger.error("Previous Network Name: %s" % (prev_context['name']))
	# Print the Network Type
        driver_logger.error("Current Network Type: %s" % current_context['provider:network_type'])
        driver_logger.error("**** %s ****" % (method_name))

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
        pass

    def _log_subnet_information(self, method_name, current_context, prev_context):
        driver_logger.info("**** %s ****" % (method_name))
        driver_logger.info("Current Subnet Name: %s" % (current_context['name']))
        driver_logger.info("Current Subnet CIDR: %s" % (current_context['cidr']))
        # Extract the Network ID from the Subnet Context
        network_id = current_context['network_id']
        # Get the Neutron DB Session Handle
        session = db.get_session()
        # Using ML2 DB API, fetch the Network that matches the Network ID
        networks = ml2_db.get_network_segments(session, network_id)
        driver_logger.info("Network associated to the Subnet: %s" % (networks))
        driver_logger.info("**** %s ****" % (method_name))

    def create_subnet_postcommit(self, context):
        # Extract the current and the previous Subnet context
        current_subnet_context = context.current
        previous_subnet_context = context.original
        self._log_subnet_information("Create Subnet PostCommit", current_subnet_context, previous_subnet_context)

    def _log_port_information(self, method_name, context):
        driver_logger.info("**** %s ****" % (method_name))
        # Extract the current Port context 
        current_port_context = context.current
        # Extract the associated Network Context
        network_context = context.network
        driver_logger.info("Port Type: %s" % (current_port_context['device_owner']))
        driver_logger.info("IP Address of the Port: %s" % ((current_port_context['fixed_ips'][0])['ip_address']))
        driver_logger.info("Network name for the Port: %s" % (network_context.current['name']))
        driver_logger.info("Network type for the Port: %s" % (network_context.current['provider:network_type']))
        driver_logger.info("Segmentation ID for the Port: %s" % (network_context.current['provider:segmentation_id']))
        driver_logger.info("**** %s ****" % (method_name))

    def create_port_postcommit(self, context):
        self._log_port_information("Create Port PostCommit", context)

