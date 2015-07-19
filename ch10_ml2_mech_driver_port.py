try:
    from neutron.openstack.common import log as logger
except ImportError:
    from oslo_log import log as logger
from neutron.plugins.ml2 import driver_api as api

driver_logger = logger.getLogger(__name__)


class CookbookMechanismDriver(api.MechanismDriver):

    def initialize(self):
        driver_logger.error("Inside Mech Driver Initialize")

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

