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
Unit Tests for NotificationsApiV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_security_and_compliance_center.notifications_api_v1 import *


service = NotificationsApiV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://notifications-api.cloud.ibm.com/notifications'
service.set_service_url(base_url)

##############################################################################
# Start of Service: NotificationChannel
##############################################################################
# region

class TestListAllChannels():
    """
    Test Class for list_all_channels
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_all_channels_all_params(self):
        """
        list_all_channels()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels')
        mock_response = '{"channels": [{"channel_id": "channel_id", "name": "name", "description": "description", "type": "Webhook", "severity": {"critical": true, "high": true, "medium": true, "low": false}, "endpoint": "endpoint", "enabled": false, "alert_source": [{"provider_name": "provider_name", "finding_types": ["finding_types"]}], "frequency": "frequency"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        transaction_id = 'testString'
        limit = 38
        skip = 38

        # Invoke method
        response = service.list_all_channels(
            account_id,
            transaction_id=transaction_id,
            limit=limit,
            skip=skip,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'skip={}'.format(skip) in query_string


    @responses.activate
    def test_list_all_channels_required_params(self):
        """
        test_list_all_channels_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels')
        mock_response = '{"channels": [{"channel_id": "channel_id", "name": "name", "description": "description", "type": "Webhook", "severity": {"critical": true, "high": true, "medium": true, "low": false}, "endpoint": "endpoint", "enabled": false, "alert_source": [{"provider_name": "provider_name", "finding_types": ["finding_types"]}], "frequency": "frequency"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.list_all_channels(
            account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_all_channels_value_error(self):
        """
        test_list_all_channels_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels')
        mock_response = '{"channels": [{"channel_id": "channel_id", "name": "name", "description": "description", "type": "Webhook", "severity": {"critical": true, "high": true, "medium": true, "low": false}, "endpoint": "endpoint", "enabled": false, "alert_source": [{"provider_name": "provider_name", "finding_types": ["finding_types"]}], "frequency": "frequency"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_all_channels(**req_copy)



class TestCreateNotificationChannel():
    """
    Test Class for create_notification_channel
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_notification_channel_all_params(self):
        """
        create_notification_channel()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels')
        mock_response = '{"channel_id": "channel_id", "status_code": 11}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a NotificationChannelAlertSourceItem model
        notification_channel_alert_source_item_model = {}
        notification_channel_alert_source_item_model['provider_name'] = 'testString'
        notification_channel_alert_source_item_model['finding_types'] = ['testString']

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        type = 'Webhook'
        endpoint = 'testString'
        description = 'testString'
        severity = ['low']
        enabled = True
        alert_source = [notification_channel_alert_source_item_model]
        transaction_id = 'testString'

        # Invoke method
        response = service.create_notification_channel(
            account_id,
            name,
            type,
            endpoint,
            description=description,
            severity=severity,
            enabled=enabled,
            alert_source=alert_source,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['type'] == 'Webhook'
        assert req_body['endpoint'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['severity'] == ['low']
        assert req_body['enabled'] == True
        assert req_body['alert_source'] == [notification_channel_alert_source_item_model]


    @responses.activate
    def test_create_notification_channel_required_params(self):
        """
        test_create_notification_channel_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels')
        mock_response = '{"channel_id": "channel_id", "status_code": 11}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a NotificationChannelAlertSourceItem model
        notification_channel_alert_source_item_model = {}
        notification_channel_alert_source_item_model['provider_name'] = 'testString'
        notification_channel_alert_source_item_model['finding_types'] = ['testString']

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        type = 'Webhook'
        endpoint = 'testString'
        description = 'testString'
        severity = ['low']
        enabled = True
        alert_source = [notification_channel_alert_source_item_model]

        # Invoke method
        response = service.create_notification_channel(
            account_id,
            name,
            type,
            endpoint,
            description=description,
            severity=severity,
            enabled=enabled,
            alert_source=alert_source,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['type'] == 'Webhook'
        assert req_body['endpoint'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['severity'] == ['low']
        assert req_body['enabled'] == True
        assert req_body['alert_source'] == [notification_channel_alert_source_item_model]


    @responses.activate
    def test_create_notification_channel_value_error(self):
        """
        test_create_notification_channel_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels')
        mock_response = '{"channel_id": "channel_id", "status_code": 11}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a NotificationChannelAlertSourceItem model
        notification_channel_alert_source_item_model = {}
        notification_channel_alert_source_item_model['provider_name'] = 'testString'
        notification_channel_alert_source_item_model['finding_types'] = ['testString']

        # Set up parameter values
        account_id = 'testString'
        name = 'testString'
        type = 'Webhook'
        endpoint = 'testString'
        description = 'testString'
        severity = ['low']
        enabled = True
        alert_source = [notification_channel_alert_source_item_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "name": name,
            "type": type,
            "endpoint": endpoint,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_notification_channel(**req_copy)



class TestDeleteNotificationChannels():
    """
    Test Class for delete_notification_channels
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_notification_channels_all_params(self):
        """
        delete_notification_channels()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels')
        mock_response = '{"message": "message"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        request_body = ['testString']
        transaction_id = 'testString'

        # Invoke method
        response = service.delete_notification_channels(
            account_id,
            request_body,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == request_body


    @responses.activate
    def test_delete_notification_channels_required_params(self):
        """
        test_delete_notification_channels_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels')
        mock_response = '{"message": "message"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        request_body = ['testString']

        # Invoke method
        response = service.delete_notification_channels(
            account_id,
            request_body,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == request_body


    @responses.activate
    def test_delete_notification_channels_value_error(self):
        """
        test_delete_notification_channels_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels')
        mock_response = '{"message": "message"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        request_body = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "request_body": request_body,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_notification_channels(**req_copy)



class TestDeleteNotificationChannel():
    """
    Test Class for delete_notification_channel
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_notification_channel_all_params(self):
        """
        delete_notification_channel()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels/testString')
        mock_response = '{"channel_id": "channel_id", "message": "message"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.delete_notification_channel(
            account_id,
            channel_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_notification_channel_required_params(self):
        """
        test_delete_notification_channel_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels/testString')
        mock_response = '{"channel_id": "channel_id", "message": "message"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'

        # Invoke method
        response = service.delete_notification_channel(
            account_id,
            channel_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_notification_channel_value_error(self):
        """
        test_delete_notification_channel_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels/testString')
        mock_response = '{"channel_id": "channel_id", "message": "message"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "channel_id": channel_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_notification_channel(**req_copy)



class TestGetNotificationChannel():
    """
    Test Class for get_notification_channel
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_notification_channel_all_params(self):
        """
        get_notification_channel()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels/testString')
        mock_response = '{"channel": {"channel_id": "channel_id", "name": "name", "description": "description", "type": "Webhook", "severity": {"critical": true, "high": true, "medium": true, "low": false}, "endpoint": "endpoint", "enabled": false, "alert_source": [{"provider_name": "provider_name", "finding_types": ["finding_types"]}], "frequency": "frequency"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.get_notification_channel(
            account_id,
            channel_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_notification_channel_required_params(self):
        """
        test_get_notification_channel_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels/testString')
        mock_response = '{"channel": {"channel_id": "channel_id", "name": "name", "description": "description", "type": "Webhook", "severity": {"critical": true, "high": true, "medium": true, "low": false}, "endpoint": "endpoint", "enabled": false, "alert_source": [{"provider_name": "provider_name", "finding_types": ["finding_types"]}], "frequency": "frequency"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'

        # Invoke method
        response = service.get_notification_channel(
            account_id,
            channel_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_notification_channel_value_error(self):
        """
        test_get_notification_channel_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels/testString')
        mock_response = '{"channel": {"channel_id": "channel_id", "name": "name", "description": "description", "type": "Webhook", "severity": {"critical": true, "high": true, "medium": true, "low": false}, "endpoint": "endpoint", "enabled": false, "alert_source": [{"provider_name": "provider_name", "finding_types": ["finding_types"]}], "frequency": "frequency"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "channel_id": channel_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_notification_channel(**req_copy)



class TestUpdateNotificationChannel():
    """
    Test Class for update_notification_channel
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_notification_channel_all_params(self):
        """
        update_notification_channel()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels/testString')
        mock_response = '{"channel_id": "channel_id", "status_code": 11}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a NotificationChannelAlertSourceItem model
        notification_channel_alert_source_item_model = {}
        notification_channel_alert_source_item_model['provider_name'] = 'testString'
        notification_channel_alert_source_item_model['finding_types'] = ['testString']

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'
        name = 'testString'
        type = 'Webhook'
        endpoint = 'testString'
        description = 'testString'
        severity = ['low']
        enabled = True
        alert_source = [notification_channel_alert_source_item_model]
        transaction_id = 'testString'

        # Invoke method
        response = service.update_notification_channel(
            account_id,
            channel_id,
            name,
            type,
            endpoint,
            description=description,
            severity=severity,
            enabled=enabled,
            alert_source=alert_source,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['type'] == 'Webhook'
        assert req_body['endpoint'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['severity'] == ['low']
        assert req_body['enabled'] == True
        assert req_body['alert_source'] == [notification_channel_alert_source_item_model]


    @responses.activate
    def test_update_notification_channel_required_params(self):
        """
        test_update_notification_channel_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels/testString')
        mock_response = '{"channel_id": "channel_id", "status_code": 11}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a NotificationChannelAlertSourceItem model
        notification_channel_alert_source_item_model = {}
        notification_channel_alert_source_item_model['provider_name'] = 'testString'
        notification_channel_alert_source_item_model['finding_types'] = ['testString']

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'
        name = 'testString'
        type = 'Webhook'
        endpoint = 'testString'
        description = 'testString'
        severity = ['low']
        enabled = True
        alert_source = [notification_channel_alert_source_item_model]

        # Invoke method
        response = service.update_notification_channel(
            account_id,
            channel_id,
            name,
            type,
            endpoint,
            description=description,
            severity=severity,
            enabled=enabled,
            alert_source=alert_source,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['type'] == 'Webhook'
        assert req_body['endpoint'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['severity'] == ['low']
        assert req_body['enabled'] == True
        assert req_body['alert_source'] == [notification_channel_alert_source_item_model]


    @responses.activate
    def test_update_notification_channel_value_error(self):
        """
        test_update_notification_channel_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels/testString')
        mock_response = '{"channel_id": "channel_id", "status_code": 11}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a NotificationChannelAlertSourceItem model
        notification_channel_alert_source_item_model = {}
        notification_channel_alert_source_item_model['provider_name'] = 'testString'
        notification_channel_alert_source_item_model['finding_types'] = ['testString']

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'
        name = 'testString'
        type = 'Webhook'
        endpoint = 'testString'
        description = 'testString'
        severity = ['low']
        enabled = True
        alert_source = [notification_channel_alert_source_item_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "channel_id": channel_id,
            "name": name,
            "type": type,
            "endpoint": endpoint,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_notification_channel(**req_copy)



class TestTestNotificationChannel():
    """
    Test Class for test_notification_channel
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_test_notification_channel_all_params(self):
        """
        test_notification_channel()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels/testString/test')
        mock_response = '{"test": "test"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.test_notification_channel(
            account_id,
            channel_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_test_notification_channel_required_params(self):
        """
        test_test_notification_channel_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels/testString/test')
        mock_response = '{"test": "test"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'

        # Invoke method
        response = service.test_notification_channel(
            account_id,
            channel_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_test_notification_channel_value_error(self):
        """
        test_test_notification_channel_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/channels/testString/test')
        mock_response = '{"test": "test"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
            "channel_id": channel_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.test_notification_channel(**req_copy)



class TestGetPublicKey():
    """
    Test Class for get_public_key
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_public_key_all_params(self):
        """
        get_public_key()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/public_key')
        mock_response = '{"public_key": "public_key"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = service.get_public_key(
            account_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_public_key_required_params(self):
        """
        test_get_public_key_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/public_key')
        mock_response = '{"public_key": "public_key"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = service.get_public_key(
            account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_public_key_value_error(self):
        """
        test_get_public_key_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/notifications/public_key')
        mock_response = '{"public_key": "public_key"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_public_key(**req_copy)



# endregion
##############################################################################
# End of Service: NotificationChannel
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestChannelResponseDefinitionAlertSourceItem():
    """
    Test Class for ChannelResponseDefinitionAlertSourceItem
    """

    def test_channel_response_definition_alert_source_item_serialization(self):
        """
        Test serialization/deserialization for ChannelResponseDefinitionAlertSourceItem
        """

        # Construct a json representation of a ChannelResponseDefinitionAlertSourceItem model
        channel_response_definition_alert_source_item_model_json = {}
        channel_response_definition_alert_source_item_model_json['provider_name'] = 'testString'
        channel_response_definition_alert_source_item_model_json['finding_types'] = ['testString']

        # Construct a model instance of ChannelResponseDefinitionAlertSourceItem by calling from_dict on the json representation
        channel_response_definition_alert_source_item_model = ChannelResponseDefinitionAlertSourceItem.from_dict(channel_response_definition_alert_source_item_model_json)
        assert channel_response_definition_alert_source_item_model != False

        # Construct a model instance of ChannelResponseDefinitionAlertSourceItem by calling from_dict on the json representation
        channel_response_definition_alert_source_item_model_dict = ChannelResponseDefinitionAlertSourceItem.from_dict(channel_response_definition_alert_source_item_model_json).__dict__
        channel_response_definition_alert_source_item_model2 = ChannelResponseDefinitionAlertSourceItem(**channel_response_definition_alert_source_item_model_dict)

        # Verify the model instances are equivalent
        assert channel_response_definition_alert_source_item_model == channel_response_definition_alert_source_item_model2

        # Convert model instance back to dict and verify no loss of data
        channel_response_definition_alert_source_item_model_json2 = channel_response_definition_alert_source_item_model.to_dict()
        assert channel_response_definition_alert_source_item_model_json2 == channel_response_definition_alert_source_item_model_json

class TestChannelResponseDefinitionSeverity():
    """
    Test Class for ChannelResponseDefinitionSeverity
    """

    def test_channel_response_definition_severity_serialization(self):
        """
        Test serialization/deserialization for ChannelResponseDefinitionSeverity
        """

        # Construct a json representation of a ChannelResponseDefinitionSeverity model
        channel_response_definition_severity_model_json = {}
        channel_response_definition_severity_model_json['critical'] = True
        channel_response_definition_severity_model_json['high'] = True
        channel_response_definition_severity_model_json['medium'] = True
        channel_response_definition_severity_model_json['low'] = True

        # Construct a model instance of ChannelResponseDefinitionSeverity by calling from_dict on the json representation
        channel_response_definition_severity_model = ChannelResponseDefinitionSeverity.from_dict(channel_response_definition_severity_model_json)
        assert channel_response_definition_severity_model != False

        # Construct a model instance of ChannelResponseDefinitionSeverity by calling from_dict on the json representation
        channel_response_definition_severity_model_dict = ChannelResponseDefinitionSeverity.from_dict(channel_response_definition_severity_model_json).__dict__
        channel_response_definition_severity_model2 = ChannelResponseDefinitionSeverity(**channel_response_definition_severity_model_dict)

        # Verify the model instances are equivalent
        assert channel_response_definition_severity_model == channel_response_definition_severity_model2

        # Convert model instance back to dict and verify no loss of data
        channel_response_definition_severity_model_json2 = channel_response_definition_severity_model.to_dict()
        assert channel_response_definition_severity_model_json2 == channel_response_definition_severity_model_json

class TestNotificationChannelAlertSourceItem():
    """
    Test Class for NotificationChannelAlertSourceItem
    """

    def test_notification_channel_alert_source_item_serialization(self):
        """
        Test serialization/deserialization for NotificationChannelAlertSourceItem
        """

        # Construct a json representation of a NotificationChannelAlertSourceItem model
        notification_channel_alert_source_item_model_json = {}
        notification_channel_alert_source_item_model_json['provider_name'] = 'testString'
        notification_channel_alert_source_item_model_json['finding_types'] = ['testString']

        # Construct a model instance of NotificationChannelAlertSourceItem by calling from_dict on the json representation
        notification_channel_alert_source_item_model = NotificationChannelAlertSourceItem.from_dict(notification_channel_alert_source_item_model_json)
        assert notification_channel_alert_source_item_model != False

        # Construct a model instance of NotificationChannelAlertSourceItem by calling from_dict on the json representation
        notification_channel_alert_source_item_model_dict = NotificationChannelAlertSourceItem.from_dict(notification_channel_alert_source_item_model_json).__dict__
        notification_channel_alert_source_item_model2 = NotificationChannelAlertSourceItem(**notification_channel_alert_source_item_model_dict)

        # Verify the model instances are equivalent
        assert notification_channel_alert_source_item_model == notification_channel_alert_source_item_model2

        # Convert model instance back to dict and verify no loss of data
        notification_channel_alert_source_item_model_json2 = notification_channel_alert_source_item_model.to_dict()
        assert notification_channel_alert_source_item_model_json2 == notification_channel_alert_source_item_model_json

class TestBulkDeleteChannelsResponse():
    """
    Test Class for BulkDeleteChannelsResponse
    """

    def test_bulk_delete_channels_response_serialization(self):
        """
        Test serialization/deserialization for BulkDeleteChannelsResponse
        """

        # Construct a json representation of a BulkDeleteChannelsResponse model
        bulk_delete_channels_response_model_json = {}
        bulk_delete_channels_response_model_json['message'] = 'testString'

        # Construct a model instance of BulkDeleteChannelsResponse by calling from_dict on the json representation
        bulk_delete_channels_response_model = BulkDeleteChannelsResponse.from_dict(bulk_delete_channels_response_model_json)
        assert bulk_delete_channels_response_model != False

        # Construct a model instance of BulkDeleteChannelsResponse by calling from_dict on the json representation
        bulk_delete_channels_response_model_dict = BulkDeleteChannelsResponse.from_dict(bulk_delete_channels_response_model_json).__dict__
        bulk_delete_channels_response_model2 = BulkDeleteChannelsResponse(**bulk_delete_channels_response_model_dict)

        # Verify the model instances are equivalent
        assert bulk_delete_channels_response_model == bulk_delete_channels_response_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_delete_channels_response_model_json2 = bulk_delete_channels_response_model.to_dict()
        assert bulk_delete_channels_response_model_json2 == bulk_delete_channels_response_model_json

class TestChannelResponseDefinition():
    """
    Test Class for ChannelResponseDefinition
    """

    def test_channel_response_definition_serialization(self):
        """
        Test serialization/deserialization for ChannelResponseDefinition
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_response_definition_severity_model = {} # ChannelResponseDefinitionSeverity
        channel_response_definition_severity_model['critical'] = True
        channel_response_definition_severity_model['high'] = True
        channel_response_definition_severity_model['medium'] = True
        channel_response_definition_severity_model['low'] = True

        channel_response_definition_alert_source_item_model = {} # ChannelResponseDefinitionAlertSourceItem
        channel_response_definition_alert_source_item_model['provider_name'] = 'testString'
        channel_response_definition_alert_source_item_model['finding_types'] = ['testString']

        # Construct a json representation of a ChannelResponseDefinition model
        channel_response_definition_model_json = {}
        channel_response_definition_model_json['channel_id'] = 'testString'
        channel_response_definition_model_json['name'] = 'testString'
        channel_response_definition_model_json['description'] = 'testString'
        channel_response_definition_model_json['type'] = 'Webhook'
        channel_response_definition_model_json['severity'] = channel_response_definition_severity_model
        channel_response_definition_model_json['endpoint'] = 'testString'
        channel_response_definition_model_json['enabled'] = True
        channel_response_definition_model_json['alert_source'] = [channel_response_definition_alert_source_item_model]
        channel_response_definition_model_json['frequency'] = 'testString'

        # Construct a model instance of ChannelResponseDefinition by calling from_dict on the json representation
        channel_response_definition_model = ChannelResponseDefinition.from_dict(channel_response_definition_model_json)
        assert channel_response_definition_model != False

        # Construct a model instance of ChannelResponseDefinition by calling from_dict on the json representation
        channel_response_definition_model_dict = ChannelResponseDefinition.from_dict(channel_response_definition_model_json).__dict__
        channel_response_definition_model2 = ChannelResponseDefinition(**channel_response_definition_model_dict)

        # Verify the model instances are equivalent
        assert channel_response_definition_model == channel_response_definition_model2

        # Convert model instance back to dict and verify no loss of data
        channel_response_definition_model_json2 = channel_response_definition_model.to_dict()
        assert channel_response_definition_model_json2 == channel_response_definition_model_json

class TestCreateChannelsResponse():
    """
    Test Class for CreateChannelsResponse
    """

    def test_create_channels_response_serialization(self):
        """
        Test serialization/deserialization for CreateChannelsResponse
        """

        # Construct a json representation of a CreateChannelsResponse model
        create_channels_response_model_json = {}
        create_channels_response_model_json['channel_id'] = 'testString'
        create_channels_response_model_json['status_code'] = 38

        # Construct a model instance of CreateChannelsResponse by calling from_dict on the json representation
        create_channels_response_model = CreateChannelsResponse.from_dict(create_channels_response_model_json)
        assert create_channels_response_model != False

        # Construct a model instance of CreateChannelsResponse by calling from_dict on the json representation
        create_channels_response_model_dict = CreateChannelsResponse.from_dict(create_channels_response_model_json).__dict__
        create_channels_response_model2 = CreateChannelsResponse(**create_channels_response_model_dict)

        # Verify the model instances are equivalent
        assert create_channels_response_model == create_channels_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_channels_response_model_json2 = create_channels_response_model.to_dict()
        assert create_channels_response_model_json2 == create_channels_response_model_json

class TestDeleteChannelResponse():
    """
    Test Class for DeleteChannelResponse
    """

    def test_delete_channel_response_serialization(self):
        """
        Test serialization/deserialization for DeleteChannelResponse
        """

        # Construct a json representation of a DeleteChannelResponse model
        delete_channel_response_model_json = {}
        delete_channel_response_model_json['channel_id'] = 'testString'
        delete_channel_response_model_json['message'] = 'testString'

        # Construct a model instance of DeleteChannelResponse by calling from_dict on the json representation
        delete_channel_response_model = DeleteChannelResponse.from_dict(delete_channel_response_model_json)
        assert delete_channel_response_model != False

        # Construct a model instance of DeleteChannelResponse by calling from_dict on the json representation
        delete_channel_response_model_dict = DeleteChannelResponse.from_dict(delete_channel_response_model_json).__dict__
        delete_channel_response_model2 = DeleteChannelResponse(**delete_channel_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_channel_response_model == delete_channel_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_channel_response_model_json2 = delete_channel_response_model.to_dict()
        assert delete_channel_response_model_json2 == delete_channel_response_model_json

class TestGetChannelResponse():
    """
    Test Class for GetChannelResponse
    """

    def test_get_channel_response_serialization(self):
        """
        Test serialization/deserialization for GetChannelResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_response_definition_severity_model = {} # ChannelResponseDefinitionSeverity
        channel_response_definition_severity_model['critical'] = True
        channel_response_definition_severity_model['high'] = True
        channel_response_definition_severity_model['medium'] = True
        channel_response_definition_severity_model['low'] = True

        channel_response_definition_alert_source_item_model = {} # ChannelResponseDefinitionAlertSourceItem
        channel_response_definition_alert_source_item_model['provider_name'] = 'testString'
        channel_response_definition_alert_source_item_model['finding_types'] = ['testString']

        channel_response_definition_model = {} # ChannelResponseDefinition
        channel_response_definition_model['channel_id'] = 'testString'
        channel_response_definition_model['name'] = 'testString'
        channel_response_definition_model['description'] = 'testString'
        channel_response_definition_model['type'] = 'Webhook'
        channel_response_definition_model['severity'] = channel_response_definition_severity_model
        channel_response_definition_model['endpoint'] = 'testString'
        channel_response_definition_model['enabled'] = True
        channel_response_definition_model['alert_source'] = [channel_response_definition_alert_source_item_model]
        channel_response_definition_model['frequency'] = 'testString'

        # Construct a json representation of a GetChannelResponse model
        get_channel_response_model_json = {}
        get_channel_response_model_json['channel'] = channel_response_definition_model

        # Construct a model instance of GetChannelResponse by calling from_dict on the json representation
        get_channel_response_model = GetChannelResponse.from_dict(get_channel_response_model_json)
        assert get_channel_response_model != False

        # Construct a model instance of GetChannelResponse by calling from_dict on the json representation
        get_channel_response_model_dict = GetChannelResponse.from_dict(get_channel_response_model_json).__dict__
        get_channel_response_model2 = GetChannelResponse(**get_channel_response_model_dict)

        # Verify the model instances are equivalent
        assert get_channel_response_model == get_channel_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_channel_response_model_json2 = get_channel_response_model.to_dict()
        assert get_channel_response_model_json2 == get_channel_response_model_json

class TestListChannelsResponse():
    """
    Test Class for ListChannelsResponse
    """

    def test_list_channels_response_serialization(self):
        """
        Test serialization/deserialization for ListChannelsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_response_definition_severity_model = {} # ChannelResponseDefinitionSeverity
        channel_response_definition_severity_model['critical'] = True
        channel_response_definition_severity_model['high'] = True
        channel_response_definition_severity_model['medium'] = True
        channel_response_definition_severity_model['low'] = True

        channel_response_definition_alert_source_item_model = {} # ChannelResponseDefinitionAlertSourceItem
        channel_response_definition_alert_source_item_model['provider_name'] = 'testString'
        channel_response_definition_alert_source_item_model['finding_types'] = ['testString']

        channel_response_definition_model = {} # ChannelResponseDefinition
        channel_response_definition_model['channel_id'] = 'testString'
        channel_response_definition_model['name'] = 'testString'
        channel_response_definition_model['description'] = 'testString'
        channel_response_definition_model['type'] = 'Webhook'
        channel_response_definition_model['severity'] = channel_response_definition_severity_model
        channel_response_definition_model['endpoint'] = 'testString'
        channel_response_definition_model['enabled'] = True
        channel_response_definition_model['alert_source'] = [channel_response_definition_alert_source_item_model]
        channel_response_definition_model['frequency'] = 'testString'

        # Construct a json representation of a ListChannelsResponse model
        list_channels_response_model_json = {}
        list_channels_response_model_json['channels'] = [channel_response_definition_model]

        # Construct a model instance of ListChannelsResponse by calling from_dict on the json representation
        list_channels_response_model = ListChannelsResponse.from_dict(list_channels_response_model_json)
        assert list_channels_response_model != False

        # Construct a model instance of ListChannelsResponse by calling from_dict on the json representation
        list_channels_response_model_dict = ListChannelsResponse.from_dict(list_channels_response_model_json).__dict__
        list_channels_response_model2 = ListChannelsResponse(**list_channels_response_model_dict)

        # Verify the model instances are equivalent
        assert list_channels_response_model == list_channels_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_channels_response_model_json2 = list_channels_response_model.to_dict()
        assert list_channels_response_model_json2 == list_channels_response_model_json

class TestPublicKeyResponse():
    """
    Test Class for PublicKeyResponse
    """

    def test_public_key_response_serialization(self):
        """
        Test serialization/deserialization for PublicKeyResponse
        """

        # Construct a json representation of a PublicKeyResponse model
        public_key_response_model_json = {}
        public_key_response_model_json['public_key'] = 'testString'

        # Construct a model instance of PublicKeyResponse by calling from_dict on the json representation
        public_key_response_model = PublicKeyResponse.from_dict(public_key_response_model_json)
        assert public_key_response_model != False

        # Construct a model instance of PublicKeyResponse by calling from_dict on the json representation
        public_key_response_model_dict = PublicKeyResponse.from_dict(public_key_response_model_json).__dict__
        public_key_response_model2 = PublicKeyResponse(**public_key_response_model_dict)

        # Verify the model instances are equivalent
        assert public_key_response_model == public_key_response_model2

        # Convert model instance back to dict and verify no loss of data
        public_key_response_model_json2 = public_key_response_model.to_dict()
        assert public_key_response_model_json2 == public_key_response_model_json

class TestTestChannelResponse():
    """
    Test Class for TestChannelResponse
    """

    def test_test_channel_response_serialization(self):
        """
        Test serialization/deserialization for TestChannelResponse
        """

        # Construct a json representation of a TestChannelResponse model
        test_channel_response_model_json = {}
        test_channel_response_model_json['test'] = 'testString'

        # Construct a model instance of TestChannelResponse by calling from_dict on the json representation
        test_channel_response_model = TestChannelResponse.from_dict(test_channel_response_model_json)
        assert test_channel_response_model != False

        # Construct a model instance of TestChannelResponse by calling from_dict on the json representation
        test_channel_response_model_dict = TestChannelResponse.from_dict(test_channel_response_model_json).__dict__
        test_channel_response_model2 = TestChannelResponse(**test_channel_response_model_dict)

        # Verify the model instances are equivalent
        assert test_channel_response_model == test_channel_response_model2

        # Convert model instance back to dict and verify no loss of data
        test_channel_response_model_json2 = test_channel_response_model.to_dict()
        assert test_channel_response_model_json2 == test_channel_response_model_json

class TestUpdateChannelResponse():
    """
    Test Class for UpdateChannelResponse
    """

    def test_update_channel_response_serialization(self):
        """
        Test serialization/deserialization for UpdateChannelResponse
        """

        # Construct a json representation of a UpdateChannelResponse model
        update_channel_response_model_json = {}
        update_channel_response_model_json['channel_id'] = 'testString'
        update_channel_response_model_json['status_code'] = 38

        # Construct a model instance of UpdateChannelResponse by calling from_dict on the json representation
        update_channel_response_model = UpdateChannelResponse.from_dict(update_channel_response_model_json)
        assert update_channel_response_model != False

        # Construct a model instance of UpdateChannelResponse by calling from_dict on the json representation
        update_channel_response_model_dict = UpdateChannelResponse.from_dict(update_channel_response_model_json).__dict__
        update_channel_response_model2 = UpdateChannelResponse(**update_channel_response_model_dict)

        # Verify the model instances are equivalent
        assert update_channel_response_model == update_channel_response_model2

        # Convert model instance back to dict and verify no loss of data
        update_channel_response_model_json2 = update_channel_response_model.to_dict()
        assert update_channel_response_model_json2 == update_channel_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
