# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Integration Tests for NotificationsV1
"""

import os
import pytest
import time
from ibm_cloud_sdk_core import *
from ibm_scc.notifications_v1 import *

# Config file name
config_file = 'notifications_v1.env'
account_id = os.getenv("ACCOUNT_ID")
testString = "testString"
channel_id = ""
identifier = "py-{0}".format(str(time.time()).split(".")[0])

class TestNotificationsV1():
    """
    Integration Test Class for NotificationsV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.notifications_service = NotificationsV1.new_instance(
                )
            assert cls.notifications_service is not None

            cls.config = read_external_sources(
                NotificationsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')

    @classmethod
    def teardown_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.notifications_service = NotificationsV1.new_instance(
                )
            assert cls.notifications_service is not None

            cls.config = read_external_sources(
                NotificationsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')
        print(f'cleaning up account: {account_id}\n')
        list_all_channels_response = cls.notifications_service.list_all_channels(
            account_id=account_id,
        )
        for channel in list_all_channels_response.get_result()['channels']:
            if channel['channel_id'] == channel_id:
                cls.notifications_service.delete_notification_channel(
                    account_id=account_id,
                    channel_id=channel['channel_id'],
                )
        print("cleanup was successful\n")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_all_channels(self):

        list_all_channels_response = self.notifications_service.list_all_channels(
            account_id=account_id,
        )

        assert list_all_channels_response.get_status_code() == 200
        channels_list = list_all_channels_response.get_result()
        assert channels_list is not None

    @needscredentials
    def test_create_notification_channel(self):

        # Construct a dict representation of a NotificationChannelAlertSourceItem model
        notification_channel_alert_source_item_model = {
            'provider_name': 'VA',
            'finding_types': ['image_with_vulnerabilities']
        }

        create_notification_channel_response = self.notifications_service.create_notification_channel(
            account_id=account_id,
            name=f'testString-{identifier}',
            type='Webhook',
            endpoint='https://webhook.site/136fe1e2-3c3f-4bff-925f-391fbb202546',
            description=testString,
            severity=['low'],
            enabled=True,
            alert_source=[notification_channel_alert_source_item_model],
        )

        global channel_id
        channel_id = create_notification_channel_response.get_result()['channel_id']

        assert create_notification_channel_response.get_status_code() == 200
        channel_info = create_notification_channel_response.get_result()
        assert channel_info is not None

    @needscredentials
    def test_get_notification_channel(self):

        get_notification_channel_response = self.notifications_service.get_notification_channel(
            account_id=account_id,
            channel_id=channel_id,
        )

        assert get_notification_channel_response.get_status_code() == 200
        channel_get = get_notification_channel_response.get_result()
        assert channel_get is not None

    @needscredentials
    def test_update_notification_channel(self):

        # Construct a dict representation of a NotificationChannelAlertSourceItem model
        notification_channel_alert_source_item_model = {
            'provider_name': 'VA',
            'finding_types': ['image_with_vulnerabilities']
        }

        update_notification_channel_response = self.notifications_service.update_notification_channel(
            account_id=account_id,
            channel_id=channel_id,
            name=f'testString-{identifier}',
            type='Webhook',
            endpoint='https://webhook.site/136fe1e2-3c3f-4bff-925f-391fbb202546',
            description=testString,
            severity=['low'],
            enabled=True,
            alert_source=[notification_channel_alert_source_item_model],
        )

        assert update_notification_channel_response.get_status_code() == 200
        channel_info = update_notification_channel_response.get_result()
        assert channel_info is not None

    @needscredentials
    def test_test_notification_channel(self):
        test_notification_channel_response = self.notifications_service.test_notification_channel(
            account_id=account_id,
            channel_id=channel_id,
        )

        assert test_notification_channel_response.get_status_code() == 200
        test_channel = test_notification_channel_response.get_result()
        assert test_channel is not None

    @needscredentials
    def test_get_public_key(self):
        get_public_key_response = self.notifications_service.get_public_key(
            account_id=account_id,
        )

        assert get_public_key_response.get_status_code() == 200
        public_key_get = get_public_key_response.get_result()
        assert public_key_get is not None

    @needscredentials
    def test_delete_notification_channel(self):
        delete_notification_channel_response = self.notifications_service.delete_notification_channel(
            account_id=account_id,
            channel_id=channel_id,
        )

        assert delete_notification_channel_response.get_status_code() == 200
        channel_delete = delete_notification_channel_response.get_result()
        assert channel_delete is not None

    @needscredentials
    def test_delete_notification_channels(self):
        # Construct a dict representation of a NotificationChannelAlertSourceItem model
        notification_channel_alert_source_item_model = {
            'provider_name': 'VA',
            'finding_types': ['image_with_vulnerabilities']
        }

        create_notification_channel_response = self.notifications_service.create_notification_channel(
            account_id=account_id,
            name=f'testString-{identifier}',
            type='Webhook',
            endpoint='https://webhook.site/136fe1e2-3c3f-4bff-925f-391fbb202546',
            description=testString,
            severity=['low'],
            enabled=True,
            alert_source=[notification_channel_alert_source_item_model],
        )

        channel_id = create_notification_channel_response.get_result()['channel_id']

        delete_notification_channels_response = self.notifications_service.delete_notification_channels(
            account_id=account_id,
            request_body=[channel_id],
        )

        assert delete_notification_channels_response.get_status_code() == 200
        channels_delete = delete_notification_channels_response.get_result()
        assert channels_delete is not None
