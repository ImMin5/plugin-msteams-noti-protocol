import os
import logging
import time
import datetime

from spaceone.core import utils, config
from spaceone.tester import TestCase, print_json, to_json
from google.protobuf.json_format import MessageToDict

_LOGGER = logging.getLogger(__name__)

WEBHOOK_URL = 'https://megazone0.webhook.office.com/webhookb2/52026950-f304-44f0-b4af-87284eae1698@97f42f55-f1db-4804-b1eb-08db083efd4f/IncomingWebhook/9c3b45bf07234192922d4cc413f6a03d/76df7ac2-dc90-40e9-91a3-16c27c61ecc4'
if WEBHOOK_URL == None:
    print("""
##################################################
# ERROR
#
# Configure your MS Teams Webhook URL first for test
##################################################
example)
export SLACK_WEBHOOK_URL=<YOUR_SLACK_WEBHOOK_URL>
""")
    exit


class TestSlackNotification(TestCase):
    config = utils.load_yaml_from_file(
        os.environ.get('SPACEONE_TEST_CONFIG_FILE', './config.yml'))
    endpoints = config.get('ENDPOINTS', {})
    secret_data = {}
    channel_data = {
        'token': WEBHOOK_URL,
    }

    def test_init(self):
        v_info = self.notification.Protocol.init({'options': {}})
        print_json(v_info)

    def test_verify(self):
        options = {}
        self.notification.Protocol.verify({'options': options, 'secret_data': self.secret_data})

    def test_dispatch(self):
        options = {}

        self.notification.Notification.dispatch({
            'options': options,
            'message': {
                'title': 'This is sample notification',
                'link': 'https://spaceone.console.doodle.spaceone.dev/monitoring/alert-manager/escalation-policy',
                'image_url': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/jal.png',
                'description': 'Thresholds Crossed: 1 out of the last 1 datapoints [0.524033991396324 (29/06/21 05:06:00)] was less than the lower thresholds [0.6043306920412774] or greater than the upper thresholds [0.6544568893755576] (minimum 1 datapoint for OK -> ALARM transition).',
                'tags': [
                    {
                        'key': 'project_id',
                        'value': 'project-xxxxx',
                        'options': {'short': True}
                    },
                    {
                        'key': 'project_name',
                        'value': '스페이스원 웹서버',
                        'options': {'short': True}
                    },
                    {
                        'key': 'resource_id',
                        'value': 'Resource [Asia Pacific (Seoul)]:[AWS/NetworkELB]: net/af83f347171a044af96459ebb37c8225/743a23562a96c595'
                    },

                ],
                'callbacks': [{
                    'label': 'Acknowledge SpaceONE Alerts',
                    'url': 'https://monitoring-webhook.dev.spaceone.dev/monitoring/v1/alert/alert-61afa17a25bf/4186dacf2d69a689ca4dbed965ef6e2d/ACKNOWLEDGED'
                }],
                'occured_at': datetime.datetime.utcnow().isoformat()
            },
            'notification_type': 'WARNING',
            'secret_data': self.secret_data,
            'channel_data': self.channel_data
        })