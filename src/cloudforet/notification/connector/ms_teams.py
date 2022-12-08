import logging
from ssl import SSLContext

from spaceone.core.connector import BaseConnector

__all__ = ['MSTeamsConnector']
_LOGGER = logging.getLogger(__name__)

sslcert = SSLContext()


class MSTeamsConnector(BaseConnector):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
