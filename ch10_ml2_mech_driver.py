# Import Neutron Database API
from neutron.db import api as db
try:
    from neutron.openstack.common import log as logger
except ImportError:
    from oslo_log import log as logger
from neutron.plugins.ml2 import driver_api as api

import ch10_ml2_mech_driver_skeleton as cookbook_skeleton_driver

driver_logger = logger.getLogger(__name__)


class CookbookMechanismDriver(cookbook_network_driver.CookbookSkeletonMechanismDriver)

    def initialize(self):
        driver_logger.error("Inside Mech Driver Initialize")

