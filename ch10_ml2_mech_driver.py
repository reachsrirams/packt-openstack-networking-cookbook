# Import Neutron Database API
from neutron.db import api as db
from oslo_log import log as logger
from neutron.plugins.ml2 import driver_api as api

driver_logger = logger.getLogger(__name__)


class CookbookMechanismDriver(api.MechanismDriver):

    def initialize(self):
        driver_logger.info("Inside Mech Driver Initialize")

