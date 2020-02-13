"""
from tracking.harvest import harvest_tracking_fleetcare
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Runs harvest_tracking_email to harvest points"

    def handle(self, *args, **options):
        help = "Runs harvest_tracking_email to harvest points"

        harvest_tracking_fleetcare()
"""

from tracking.harvest import harvest_tracking_fleetcare
from django.core.management.base import BaseCommand

import logging
LOGGER = logging.getLogger('tracking_points')

class Command(BaseCommand):
    help = "Runs harvest_tracking_email to harvest points"

    def handle(self, *args, **options):


        LOGGER.info('Harvesting Fleetcare feed')
        try:
            harvest_tracking_fleetcare()
            print("Harvested from Fleetcare; created.")
            #LOGGER.info("Updated {} of {} scanned DFES devices".format(updated, num_records))
        except Exception as e:
            LOGGER.error(e)

