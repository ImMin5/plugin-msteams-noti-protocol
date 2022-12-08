from spaceone.core.manager import BaseManager
from cloudforet.notification.manager.ms_teams_manager import MSTeamsConnector


class NotificationManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dispatch(self, token, slack_channel, message, **kwargs):
        ms_teams_mgr: MSTeamsConnector = self.locator.get_manager('MSTeamsConnector')
