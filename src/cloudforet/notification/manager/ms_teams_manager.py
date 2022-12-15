from spaceone.core.manager import BaseManager
from cloudforet.notification.connector.ms_teams import MSTeamsConnector
import pymsteams

class MSTeamsManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = None

    def set_connector(self, hookurl):
        self.conn: MSTeamsConnector = self.locator.get_connector('MSTeamsConnector', hookurl=hookurl)

    def make_message(self, message, **kwargs):
        message_section = pymsteams.cardsection

        message_section.title("this is title")
        self.conn.client.addSectoin(message_section)

    def send_message(self):
        self.conn.send()
