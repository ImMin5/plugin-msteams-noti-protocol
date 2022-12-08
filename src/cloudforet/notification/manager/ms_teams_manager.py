from spaceone.core.manager import BaseManager
from cloudforet.notification.connector.ms_teams import MSTeamsConnector


class SlackManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = None

    def set_connector(self, token):
        self.conn: MSTeamsConnector = self.locator.get_connector('MSTeamsConnector', token=token)
