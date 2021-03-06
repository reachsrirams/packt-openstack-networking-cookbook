# Import Neutron Database API
from neutron.db import api as db
from oslo_log import log as logger
from neutron.plugins.ml2 import driver_api as api

import ch10_ml2_mech_driver_network as cookbook_network_driver
import ch10_ml2_mech_driver_subnet as cookbook_subnet_driver
import ch10_ml2_mech_driver_port as cookbook_port_driver

driver_logger = logger.getLogger(__name__)


class CookbookMechanismDriver(cookbook_network_driver.CookbookNetworkMechanismDriver,
                        cookbook_subnet_driver.CookbookSubnetMechanismDriver,
                        cookbook_port_driver.CookbookPortMechanismDriver):

    def initialize(self):
        driver_logger.info("Inside Mech Driver Initialize")


