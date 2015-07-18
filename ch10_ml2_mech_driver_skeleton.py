try:
    from neutron.openstack.common import log as logger
except ImportError:
    from oslo_log import log as logger 
from neutron.plugins.ml2 import driver_api as api

driver_logger = logger.getLogger(__name__)


class CookbookMechanismDriver(api.MechanismDriver):

    def initialize(self):
        driver_logger.error("Inside Mech Driver Initialize")

    def create_network_postcommit(self, context):
        pass
	
    def update_network_postcommit(self, context):
        pass

    def update_network_precommit(self, context):
        pass

    def update_network_precommit(self, context):
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


