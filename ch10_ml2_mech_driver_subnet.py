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


