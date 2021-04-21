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
from ibm_cloud_sdk_core import *
from ibm_security_and_compliance_center.notifications_v1 import *

# Config file name
config_file = 'notifications_v1.env'

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

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_all_channels(self):

        list_all_channels_response = self.notifications_service.list_all_channels(
            account_id='testString',
            transaction_id='testString',
            limit=38,
            skip=38
        )

        assert list_all_channels_response.get_status_code() == 200
        channels_list = list_all_channels_response.get_result()
        assert channels_list is not None

    @needscredentials
    def test_create_notification_channel(self):

        # Construct a dict representation of a NotificationChannelAlertSourceItem model
        notification_channel_alert_source_item_model = {
            'provider_name': 'testString',
            'finding_types': ['testString']
        }

        create_notification_channel_response = self.notifications_service.create_notification_channel(
            account_id='testString',
            name='testString',
            type='Webhook',
            endpoint='testString',
            description='testString',
            severity=['low'],
            enabled=True,
            alert_source=[notification_channel_alert_source_item_model],
            transaction_id='testString'
        )

        assert create_notification_channel_response.get_status_code() == 200
        channel_info = create_notification_channel_response.get_result()
        assert channel_info is not None

    @needscredentials
    def test_get_notification_channel(self):

        get_notification_channel_response = self.notifications_service.get_notification_channel(
            account_id='testString',
            channel_id='testString',
            transaction_id='testString'
        )

        assert get_notification_channel_response.get_status_code() == 200
        channel_get = get_notification_channel_response.get_result()
        assert channel_get is not None

    @needscredentials
    def test_update_notification_channel(self):

        # Construct a dict representation of a NotificationChannelAlertSourceItem model
        notification_channel_alert_source_item_model = {
            'provider_name': 'testString',
            'finding_types': ['testString']
        }

        update_notification_channel_response = self.notifications_service.update_notification_channel(
            account_id='testString',
            channel_id='testString',
            name='testString',
            type='Webhook',
            endpoint='testString',
            description='testString',
            severity=['low'],
            enabled=True,
            alert_source=[notification_channel_alert_source_item_model],
            transaction_id='testString'
        )

        assert update_notification_channel_response.get_status_code() == 200
        channel_info = update_notification_channel_response.get_result()
        assert channel_info is not None

    @needscredentials
    def test_test_notification_channel(self):

        test_notification_channel_response = self.notifications_service.test_notification_channel(
            account_id='testString',
            channel_id='testString',
            transaction_id='testString'
        )

        assert test_notification_channel_response.get_status_code() == 200
        test_channel = test_notification_channel_response.get_result()
        assert test_channel is not None

    @needscredentials
    def test_get_public_key(self):

        get_public_key_response = self.notifications_service.get_public_key(
            account_id='testString',
            transaction_id='testString'
        )

        assert get_public_key_response.get_status_code() == 200
        public_key_get = get_public_key_response.get_result()
        assert public_key_get is not None

    @needscredentials
    def test_delete_notification_channels(self):

        delete_notification_channels_response = self.notifications_service.delete_notification_channels(
            account_id='testString',
            request_body=['testString'],
            transaction_id='testString'
        )

        assert delete_notification_channels_response.get_status_code() == 200
        channels_delete = delete_notification_channels_response.get_result()
        assert channels_delete is not None

    @needscredentials
    def test_delete_notification_channel(self):

        delete_notification_channel_response = self.notifications_service.delete_notification_channel(
            account_id='testString',
            channel_id='testString',
            transaction_id='testString'
        )

        assert delete_notification_channel_response.get_status_code() == 200
        channel_delete = delete_notification_channel_response.get_result()
        assert channel_delete is not None

