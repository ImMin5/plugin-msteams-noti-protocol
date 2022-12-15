import logging
import pymsteams
from spaceone.core.connector import BaseConnector


__all__ = ['MSTeamsConnector']
_LOGGER = logging.getLogger(__name__)


class MSTeamsConnector(BaseConnector):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = pymsteams.connectorcard(hookurl=kwargs.get('hookurl'))

    def send(self):
        self.client.send()
