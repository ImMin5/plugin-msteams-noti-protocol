import time
import logging

from spaceone.core import utils
from spaceone.core.service import *
from cloudforet.notification.manager.notification_manager import NotificationManager

_LOGGER = logging.getLogger(__name__)


@authentication_handler
class NotificationService(BaseService):

    def __init__(self, metadata):
        super().__init__(metadata)
