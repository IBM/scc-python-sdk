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
Unit Tests for NotificationsV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_scc.notifications_v1 import *
from ibm_scc.notifications_v1 import TestChannel as TestNotificationChannel


_service = NotificationsV1(
    authenticator=NoAuthAuthenticator()
    )

_base_url = 'https://us-south.secadvisor.cloud.ibm.com/notifications'
_service.set_service_url(_base_url)

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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels')
        mock_response = '{"channels": [{"channel_id": "channel_id", "name": "name", "description": "description", "type": "Webhook", "severity": {"critical": true, "high": true, "medium": true, "low": false}, "endpoint": "endpoint", "enabled": false, "alert_source": [{"provider_name": "VA", "finding_types": [{"anyKey": "anyValue"}]}], "frequency": "frequency"}]}'
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
        response = _service.list_all_channels(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels')
        mock_response = '{"channels": [{"channel_id": "channel_id", "name": "name", "description": "description", "type": "Webhook", "severity": {"critical": true, "high": true, "medium": true, "low": false}, "endpoint": "endpoint", "enabled": false, "alert_source": [{"provider_name": "VA", "finding_types": [{"anyKey": "anyValue"}]}], "frequency": "frequency"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.list_all_channels(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels')
        mock_response = '{"channels": [{"channel_id": "channel_id", "name": "name", "description": "description", "type": "Webhook", "severity": {"critical": true, "high": true, "medium": true, "low": false}, "endpoint": "endpoint", "enabled": false, "alert_source": [{"provider_name": "VA", "finding_types": [{"anyKey": "anyValue"}]}], "frequency": "frequency"}]}'
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
                _service.list_all_channels(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels')
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
        response = _service.create_notification_channel(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels')
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
        response = _service.create_notification_channel(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels')
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
                _service.create_notification_channel(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels')
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
        response = _service.delete_notification_channels(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels')
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
        response = _service.delete_notification_channels(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels')
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
                _service.delete_notification_channels(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels/testString')
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
        response = _service.delete_notification_channel(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels/testString')
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
        response = _service.delete_notification_channel(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels/testString')
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
                _service.delete_notification_channel(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels/testString')
        mock_response = '{"channel": {"channel_id": "channel_id", "name": "name", "description": "description", "type": "Webhook", "severity": {"critical": true, "high": true, "medium": true, "low": false}, "endpoint": "endpoint", "enabled": false, "alert_source": [{"provider_name": "VA", "finding_types": [{"anyKey": "anyValue"}]}], "frequency": "frequency"}}'
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
        response = _service.get_notification_channel(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels/testString')
        mock_response = '{"channel": {"channel_id": "channel_id", "name": "name", "description": "description", "type": "Webhook", "severity": {"critical": true, "high": true, "medium": true, "low": false}, "endpoint": "endpoint", "enabled": false, "alert_source": [{"provider_name": "VA", "finding_types": [{"anyKey": "anyValue"}]}], "frequency": "frequency"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'
        channel_id = 'testString'

        # Invoke method
        response = _service.get_notification_channel(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels/testString')
        mock_response = '{"channel": {"channel_id": "channel_id", "name": "name", "description": "description", "type": "Webhook", "severity": {"critical": true, "high": true, "medium": true, "low": false}, "endpoint": "endpoint", "enabled": false, "alert_source": [{"provider_name": "VA", "finding_types": [{"anyKey": "anyValue"}]}], "frequency": "frequency"}}'
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
                _service.get_notification_channel(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels/testString')
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
        response = _service.update_notification_channel(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels/testString')
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
        response = _service.update_notification_channel(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels/testString')
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
                _service.update_notification_channel(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels/testString/test')
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
        response = _service.test_notification_channel(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels/testString/test')
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
        response = _service.test_notification_channel(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/channels/testString/test')
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
                _service.test_notification_channel(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/public_key')
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
        response = _service.get_public_key(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/public_key')
        mock_response = '{"public_key": "public_key"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = 'testString'

        # Invoke method
        response = _service.get_public_key(
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
        url = self.preprocess_url(_base_url + '/v1/testString/notifications/public_key')
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
                _service.get_public_key(**req_copy)



# endregion
##############################################################################
# End of Service: NotificationChannel
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestChannelAlertSourceItem():
    """
    Test Class for ChannelAlertSourceItem
    """

    def test_channel_alert_source_item_serialization(self):
        """
        Test serialization/deserialization for ChannelAlertSourceItem
        """

        # Construct a json representation of a ChannelAlertSourceItem model
        channel_alert_source_item_model_json = {}
        channel_alert_source_item_model_json['provider_name'] = 'VA'
        channel_alert_source_item_model_json['finding_types'] = [{ 'foo': 'bar' }]

        # Construct a model instance of ChannelAlertSourceItem by calling from_dict on the json representation
        channel_alert_source_item_model = ChannelAlertSourceItem.from_dict(channel_alert_source_item_model_json)
        assert channel_alert_source_item_model != False

        # Construct a model instance of ChannelAlertSourceItem by calling from_dict on the json representation
        channel_alert_source_item_model_dict = ChannelAlertSourceItem.from_dict(channel_alert_source_item_model_json).__dict__
        channel_alert_source_item_model2 = ChannelAlertSourceItem(**channel_alert_source_item_model_dict)

        # Verify the model instances are equivalent
        assert channel_alert_source_item_model == channel_alert_source_item_model2

        # Convert model instance back to dict and verify no loss of data
        channel_alert_source_item_model_json2 = channel_alert_source_item_model.to_dict()
        assert channel_alert_source_item_model_json2 == channel_alert_source_item_model_json

class TestChannelDelete():
    """
    Test Class for ChannelDelete
    """

    def test_channel_delete_serialization(self):
        """
        Test serialization/deserialization for ChannelDelete
        """

        # Construct a json representation of a ChannelDelete model
        channel_delete_model_json = {}
        channel_delete_model_json['channel_id'] = 'testString'
        channel_delete_model_json['message'] = 'testString'

        # Construct a model instance of ChannelDelete by calling from_dict on the json representation
        channel_delete_model = ChannelDelete.from_dict(channel_delete_model_json)
        assert channel_delete_model != False

        # Construct a model instance of ChannelDelete by calling from_dict on the json representation
        channel_delete_model_dict = ChannelDelete.from_dict(channel_delete_model_json).__dict__
        channel_delete_model2 = ChannelDelete(**channel_delete_model_dict)

        # Verify the model instances are equivalent
        assert channel_delete_model == channel_delete_model2

        # Convert model instance back to dict and verify no loss of data
        channel_delete_model_json2 = channel_delete_model.to_dict()
        assert channel_delete_model_json2 == channel_delete_model_json

class TestChannelGet():
    """
    Test Class for ChannelGet
    """

    def test_channel_get_serialization(self):
        """
        Test serialization/deserialization for ChannelGet
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_severity_model = {} # ChannelSeverity
        channel_severity_model['critical'] = True
        channel_severity_model['high'] = True
        channel_severity_model['medium'] = True
        channel_severity_model['low'] = True

        channel_alert_source_item_model = {} # ChannelAlertSourceItem
        channel_alert_source_item_model['provider_name'] = 'VA'
        channel_alert_source_item_model['finding_types'] = [{ 'foo': 'bar' }]

        channel_model = {} # Channel
        channel_model['channel_id'] = 'testString'
        channel_model['name'] = 'testString'
        channel_model['description'] = 'testString'
        channel_model['type'] = 'Webhook'
        channel_model['severity'] = channel_severity_model
        channel_model['endpoint'] = 'testString'
        channel_model['enabled'] = True
        channel_model['alert_source'] = [channel_alert_source_item_model]
        channel_model['frequency'] = 'testString'

        # Construct a json representation of a ChannelGet model
        channel_get_model_json = {}
        channel_get_model_json['channel'] = channel_model

        # Construct a model instance of ChannelGet by calling from_dict on the json representation
        channel_get_model = ChannelGet.from_dict(channel_get_model_json)
        assert channel_get_model != False

        # Construct a model instance of ChannelGet by calling from_dict on the json representation
        channel_get_model_dict = ChannelGet.from_dict(channel_get_model_json).__dict__
        channel_get_model2 = ChannelGet(**channel_get_model_dict)

        # Verify the model instances are equivalent
        assert channel_get_model == channel_get_model2

        # Convert model instance back to dict and verify no loss of data
        channel_get_model_json2 = channel_get_model.to_dict()
        assert channel_get_model_json2 == channel_get_model_json

class TestChannelInfo():
    """
    Test Class for ChannelInfo
    """

    def test_channel_info_serialization(self):
        """
        Test serialization/deserialization for ChannelInfo
        """

        # Construct a json representation of a ChannelInfo model
        channel_info_model_json = {}
        channel_info_model_json['channel_id'] = 'testString'
        channel_info_model_json['status_code'] = 38

        # Construct a model instance of ChannelInfo by calling from_dict on the json representation
        channel_info_model = ChannelInfo.from_dict(channel_info_model_json)
        assert channel_info_model != False

        # Construct a model instance of ChannelInfo by calling from_dict on the json representation
        channel_info_model_dict = ChannelInfo.from_dict(channel_info_model_json).__dict__
        channel_info_model2 = ChannelInfo(**channel_info_model_dict)

        # Verify the model instances are equivalent
        assert channel_info_model == channel_info_model2

        # Convert model instance back to dict and verify no loss of data
        channel_info_model_json2 = channel_info_model.to_dict()
        assert channel_info_model_json2 == channel_info_model_json

class TestChannelSeverity():
    """
    Test Class for ChannelSeverity
    """

    def test_channel_severity_serialization(self):
        """
        Test serialization/deserialization for ChannelSeverity
        """

        # Construct a json representation of a ChannelSeverity model
        channel_severity_model_json = {}
        channel_severity_model_json['critical'] = True
        channel_severity_model_json['high'] = True
        channel_severity_model_json['medium'] = True
        channel_severity_model_json['low'] = True

        # Construct a model instance of ChannelSeverity by calling from_dict on the json representation
        channel_severity_model = ChannelSeverity.from_dict(channel_severity_model_json)
        assert channel_severity_model != False

        # Construct a model instance of ChannelSeverity by calling from_dict on the json representation
        channel_severity_model_dict = ChannelSeverity.from_dict(channel_severity_model_json).__dict__
        channel_severity_model2 = ChannelSeverity(**channel_severity_model_dict)

        # Verify the model instances are equivalent
        assert channel_severity_model == channel_severity_model2

        # Convert model instance back to dict and verify no loss of data
        channel_severity_model_json2 = channel_severity_model.to_dict()
        assert channel_severity_model_json2 == channel_severity_model_json

class TestChannelsDelete():
    """
    Test Class for ChannelsDelete
    """

    def test_channels_delete_serialization(self):
        """
        Test serialization/deserialization for ChannelsDelete
        """

        # Construct a json representation of a ChannelsDelete model
        channels_delete_model_json = {}
        channels_delete_model_json['message'] = 'testString'

        # Construct a model instance of ChannelsDelete by calling from_dict on the json representation
        channels_delete_model = ChannelsDelete.from_dict(channels_delete_model_json)
        assert channels_delete_model != False

        # Construct a model instance of ChannelsDelete by calling from_dict on the json representation
        channels_delete_model_dict = ChannelsDelete.from_dict(channels_delete_model_json).__dict__
        channels_delete_model2 = ChannelsDelete(**channels_delete_model_dict)

        # Verify the model instances are equivalent
        assert channels_delete_model == channels_delete_model2

        # Convert model instance back to dict and verify no loss of data
        channels_delete_model_json2 = channels_delete_model.to_dict()
        assert channels_delete_model_json2 == channels_delete_model_json

class TestChannelsList():
    """
    Test Class for ChannelsList
    """

    def test_channels_list_serialization(self):
        """
        Test serialization/deserialization for ChannelsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_severity_model = {} # ChannelSeverity
        channel_severity_model['critical'] = True
        channel_severity_model['high'] = True
        channel_severity_model['medium'] = True
        channel_severity_model['low'] = True

        channel_alert_source_item_model = {} # ChannelAlertSourceItem
        channel_alert_source_item_model['provider_name'] = 'VA'
        channel_alert_source_item_model['finding_types'] = [{ 'foo': 'bar' }]

        channel_model = {} # Channel
        channel_model['channel_id'] = 'testString'
        channel_model['name'] = 'testString'
        channel_model['description'] = 'testString'
        channel_model['type'] = 'Webhook'
        channel_model['severity'] = channel_severity_model
        channel_model['endpoint'] = 'testString'
        channel_model['enabled'] = True
        channel_model['alert_source'] = [channel_alert_source_item_model]
        channel_model['frequency'] = 'testString'

        # Construct a json representation of a ChannelsList model
        channels_list_model_json = {}
        channels_list_model_json['channels'] = [channel_model]

        # Construct a model instance of ChannelsList by calling from_dict on the json representation
        channels_list_model = ChannelsList.from_dict(channels_list_model_json)
        assert channels_list_model != False

        # Construct a model instance of ChannelsList by calling from_dict on the json representation
        channels_list_model_dict = ChannelsList.from_dict(channels_list_model_json).__dict__
        channels_list_model2 = ChannelsList(**channels_list_model_dict)

        # Verify the model instances are equivalent
        assert channels_list_model == channels_list_model2

        # Convert model instance back to dict and verify no loss of data
        channels_list_model_json2 = channels_list_model.to_dict()
        assert channels_list_model_json2 == channels_list_model_json

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

class TestPublicKeyGet():
    """
    Test Class for PublicKeyGet
    """

    def test_public_key_get_serialization(self):
        """
        Test serialization/deserialization for PublicKeyGet
        """

        # Construct a json representation of a PublicKeyGet model
        public_key_get_model_json = {}
        public_key_get_model_json['public_key'] = 'testString'

        # Construct a model instance of PublicKeyGet by calling from_dict on the json representation
        public_key_get_model = PublicKeyGet.from_dict(public_key_get_model_json)
        assert public_key_get_model != False

        # Construct a model instance of PublicKeyGet by calling from_dict on the json representation
        public_key_get_model_dict = PublicKeyGet.from_dict(public_key_get_model_json).__dict__
        public_key_get_model2 = PublicKeyGet(**public_key_get_model_dict)

        # Verify the model instances are equivalent
        assert public_key_get_model == public_key_get_model2

        # Convert model instance back to dict and verify no loss of data
        public_key_get_model_json2 = public_key_get_model.to_dict()
        assert public_key_get_model_json2 == public_key_get_model_json

class TestTestChannel():
    """
    Test Class for TestChannel
    """

    def test_test_channel_serialization(self):
        """
        Test serialization/deserialization for TestChannel
        """

        # Construct a json representation of a TestChannel model
        test_channel_model_json = {}
        test_channel_model_json['test'] = 'testString'

        # Construct a model instance of TestChannel by calling from_dict on the json representation
        test_channel_model = TestNotificationChannel.from_dict(test_channel_model_json)
        assert test_channel_model != False

        # Construct a model instance of TestChannel by calling from_dict on the json representation
        test_channel_model_dict = TestNotificationChannel.from_dict(test_channel_model_json).__dict__
        test_channel_model2 = TestNotificationChannel(**test_channel_model_dict)

        # Verify the model instances are equivalent
        assert test_channel_model == test_channel_model2

        # Convert model instance back to dict and verify no loss of data
        test_channel_model_json2 = test_channel_model.to_dict()
        assert test_channel_model_json2 == test_channel_model_json

class TestChannel():
    """
    Test Class for Channel
    """

    def test_channel_serialization(self):
        """
        Test serialization/deserialization for Channel
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_severity_model = {} # ChannelSeverity
        channel_severity_model['critical'] = True
        channel_severity_model['high'] = True
        channel_severity_model['medium'] = True
        channel_severity_model['low'] = True

        channel_alert_source_item_model = {} # ChannelAlertSourceItem
        channel_alert_source_item_model['provider_name'] = 'VA'
        channel_alert_source_item_model['finding_types'] = [{ 'foo': 'bar' }]

        # Construct a json representation of a Channel model
        channel_model_json = {}
        channel_model_json['channel_id'] = 'testString'
        channel_model_json['name'] = 'testString'
        channel_model_json['description'] = 'testString'
        channel_model_json['type'] = 'Webhook'
        channel_model_json['severity'] = channel_severity_model
        channel_model_json['endpoint'] = 'testString'
        channel_model_json['enabled'] = True
        channel_model_json['alert_source'] = [channel_alert_source_item_model]
        channel_model_json['frequency'] = 'testString'

        # Construct a model instance of Channel by calling from_dict on the json representation
        channel_model = Channel.from_dict(channel_model_json)
        assert channel_model != False

        # Construct a model instance of Channel by calling from_dict on the json representation
        channel_model_dict = Channel.from_dict(channel_model_json).__dict__
        channel_model2 = Channel(**channel_model_dict)

        # Verify the model instances are equivalent
        assert channel_model == channel_model2

        # Convert model instance back to dict and verify no loss of data
        channel_model_json2 = channel_model.to_dict()
        assert channel_model_json2 == channel_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
