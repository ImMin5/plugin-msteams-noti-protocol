import logging
from spaceone.core.manager import BaseManager
from cloudforet.notification.manager.ms_teams_manager import MSTeamsManager

_LOGGER = logging.getLogger(__name__)

class NotificationManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dispatch(self, hookurl, message, **kwargs):
        _LOGGER.debug(f'manager dispatch')
        ms_teams_mgr: MSTeamsManager = self.locator.get_manager('MSTeamsManager')
        ms_teams_mgr.set_connector(hookurl)
        ms_teams_mgr.make_message(message, **kwargs)
        ms_teams_mgr.send_message()
