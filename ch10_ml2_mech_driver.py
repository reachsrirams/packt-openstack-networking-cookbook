try:
    from neutron.openstack.common import log as logger
except ImportError:
    from oslo_log import log as logger 
from neutron.plugins.ml2 import driver_api as api

driver_logger = logger.getLogger(__name__)


class CookbookMechanismDriver(api.MechanismDriver):

    def initialize(self):
        driver_logger.error("Inside Mech Driver Initialize")

    def _log_network_information(method_name, network_context):
        driver_logger.error("*********** %s *********" % (method_name))
	driver_logger.error("Network Type: ".network_context['provider:network_type'])
        driver_logger.error("********************")

    def create_network_precommit(self, context):
        network_context = context.current
	_log_network_information("Create Network PreCommit", network_context)


    def create_network_postcommit(self, context):
        network_context = context.current
	_log_network_information("Create Network PostCommit", network_context)
	
    def update_network_precommit(self, context):
        pass

    def update_network_postcommit(self, context):
        pass

    def delete_network_precommit(self, context):
        pass

    def delete_network_postcommit(self, context):
        pass

    def create_subnet_precommit(self, context):
        pass

    def create_subnet_postcommit(self, context):
        pass

    def update_subnet_precommit(self, context):
        pass

    def update_subnet_postcommit(self, context):
        pass

    def delete_subnet_precommit(self, context):
        pass

    def delete_subnet_postcommit(self, context):
        pass

    def create_port_precommit(self, context):
        pass

    def create_port_postcommit(self, context):
        pass

    def update_port_precommit(self, context):
        pass

    def update_port_postcommit(self, context):
        pass

    def delete_port_precommit(self, context):
        pass

    def delete_port_postcommit(self, context):
        pass

    def bind_port(self, context):
        pass


