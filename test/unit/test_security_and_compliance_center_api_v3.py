# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2025.
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
Unit Tests for SecurityAndComplianceCenterApiV3
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_scc.security_and_compliance_center_api_v3 import *


_service = SecurityAndComplianceCenterApiV3(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://us-south.compliance.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """

    # Form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


def test_get_service_url_for_region():
    """
    get_service_url_for_region()
    """
    assert SecurityAndComplianceCenterApiV3.get_service_url_for_region('INVALID_REGION') is None
    assert SecurityAndComplianceCenterApiV3.get_service_url_for_region('us-south') == 'https://us-south.compliance.cloud.ibm.com'
    assert SecurityAndComplianceCenterApiV3.get_service_url_for_region('eu-de') == 'https://eu-de.compliance.cloud.ibm.com'
    assert SecurityAndComplianceCenterApiV3.get_service_url_for_region('eu-fr2') == 'https://eu-fr2.compliance.cloud.ibm.com'
    assert SecurityAndComplianceCenterApiV3.get_service_url_for_region('ca-tor') == 'https://ca-tor.compliance.cloud.ibm.com'
    assert SecurityAndComplianceCenterApiV3.get_service_url_for_region('au-syd') == 'https://au-syd.compliance.cloud.ibm.com'
    assert SecurityAndComplianceCenterApiV3.get_service_url_for_region('eu-es') == 'https://eu-es.compliance.cloud.ibm.com'


##############################################################################
# Start of Service: Setting
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecurityAndComplianceCenterApiV3.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecurityAndComplianceCenterApiV3)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecurityAndComplianceCenterApiV3.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetSettings:
    """
    Test Class for get_settings
    """

    @responses.activate
    def test_get_settings_all_params(self):
        """
        get_settings()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/settings')
        mock_response = '{"event_notifications": {"instance_crn": "crn:v1:bluemix:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::", "updated_on": "2019-01-01T12:00:00.000Z", "source_id": "crn:v1:bluemix:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::", "source_description": "This source is used for integration with IBM Cloud Security and Compliance Center.", "source_name": "compliance"}, "object_storage": {"instance_crn": "instance_crn", "bucket": "bucket", "bucket_location": "bucket_location", "bucket_endpoint": "bucket_endpoint", "updated_on": "2019-01-01T12:00:00.000Z"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Invoke method
        response = _service.get_settings(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_settings_all_params_with_retries(self):
        # Enable retries and run test_get_settings_all_params.
        _service.enable_retries()
        self.test_get_settings_all_params()

        # Disable retries and run test_get_settings_all_params.
        _service.disable_retries()
        self.test_get_settings_all_params()

    @responses.activate
    def test_get_settings_value_error(self):
        """
        test_get_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/settings')
        mock_response = '{"event_notifications": {"instance_crn": "crn:v1:bluemix:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::", "updated_on": "2019-01-01T12:00:00.000Z", "source_id": "crn:v1:bluemix:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::", "source_description": "This source is used for integration with IBM Cloud Security and Compliance Center.", "source_name": "compliance"}, "object_storage": {"instance_crn": "instance_crn", "bucket": "bucket", "bucket_location": "bucket_location", "bucket_endpoint": "bucket_endpoint", "updated_on": "2019-01-01T12:00:00.000Z"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_settings(**req_copy)

    def test_get_settings_value_error_with_retries(self):
        # Enable retries and run test_get_settings_value_error.
        _service.enable_retries()
        self.test_get_settings_value_error()

        # Disable retries and run test_get_settings_value_error.
        _service.disable_retries()
        self.test_get_settings_value_error()


class TestUpdateSettings:
    """
    Test Class for update_settings
    """

    @responses.activate
    def test_update_settings_all_params(self):
        """
        update_settings()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/settings')
        mock_response = '{"event_notifications": {"instance_crn": "crn:v1:bluemix:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::", "updated_on": "2019-01-01T12:00:00.000Z", "source_id": "crn:v1:bluemix:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::", "source_description": "This source is used for integration with IBM Cloud Security and Compliance Center.", "source_name": "compliance"}, "object_storage": {"instance_crn": "instance_crn", "bucket": "bucket", "bucket_location": "bucket_location", "bucket_endpoint": "bucket_endpoint", "updated_on": "2019-01-01T12:00:00.000Z"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ObjectStoragePrototype model
        object_storage_prototype_model = {}
        object_storage_prototype_model['bucket'] = 'px-scan-results'
        object_storage_prototype_model['instance_crn'] = 'crn:v1:staging:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::'

        # Construct a dict representation of a EventNotificationsPrototype model
        event_notifications_prototype_model = {}
        event_notifications_prototype_model['instance_crn'] = 'crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::'
        event_notifications_prototype_model['source_description'] = 'This source is used for integration with IBM Cloud Security and Compliance Center.'
        event_notifications_prototype_model['source_name'] = 'scc-sdk-integration'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        object_storage = object_storage_prototype_model
        event_notifications = event_notifications_prototype_model

        # Invoke method
        response = _service.update_settings(
            instance_id,
            object_storage=object_storage,
            event_notifications=event_notifications,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['object_storage'] == object_storage_prototype_model
        assert req_body['event_notifications'] == event_notifications_prototype_model

    def test_update_settings_all_params_with_retries(self):
        # Enable retries and run test_update_settings_all_params.
        _service.enable_retries()
        self.test_update_settings_all_params()

        # Disable retries and run test_update_settings_all_params.
        _service.disable_retries()
        self.test_update_settings_all_params()

    @responses.activate
    def test_update_settings_value_error(self):
        """
        test_update_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/settings')
        mock_response = '{"event_notifications": {"instance_crn": "crn:v1:bluemix:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::", "updated_on": "2019-01-01T12:00:00.000Z", "source_id": "crn:v1:bluemix:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::", "source_description": "This source is used for integration with IBM Cloud Security and Compliance Center.", "source_name": "compliance"}, "object_storage": {"instance_crn": "instance_crn", "bucket": "bucket", "bucket_location": "bucket_location", "bucket_endpoint": "bucket_endpoint", "updated_on": "2019-01-01T12:00:00.000Z"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ObjectStoragePrototype model
        object_storage_prototype_model = {}
        object_storage_prototype_model['bucket'] = 'px-scan-results'
        object_storage_prototype_model['instance_crn'] = 'crn:v1:staging:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::'

        # Construct a dict representation of a EventNotificationsPrototype model
        event_notifications_prototype_model = {}
        event_notifications_prototype_model['instance_crn'] = 'crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::'
        event_notifications_prototype_model['source_description'] = 'This source is used for integration with IBM Cloud Security and Compliance Center.'
        event_notifications_prototype_model['source_name'] = 'scc-sdk-integration'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        object_storage = object_storage_prototype_model
        event_notifications = event_notifications_prototype_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_settings(**req_copy)

    def test_update_settings_value_error_with_retries(self):
        # Enable retries and run test_update_settings_value_error.
        _service.enable_retries()
        self.test_update_settings_value_error()

        # Disable retries and run test_update_settings_value_error.
        _service.disable_retries()
        self.test_update_settings_value_error()


class TestPostTestEvent:
    """
    Test Class for post_test_event
    """

    @responses.activate
    def test_post_test_event_all_params(self):
        """
        post_test_event()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/test_event')
        mock_response = '{"success": false}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Invoke method
        response = _service.post_test_event(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_post_test_event_all_params_with_retries(self):
        # Enable retries and run test_post_test_event_all_params.
        _service.enable_retries()
        self.test_post_test_event_all_params()

        # Disable retries and run test_post_test_event_all_params.
        _service.disable_retries()
        self.test_post_test_event_all_params()

    @responses.activate
    def test_post_test_event_value_error(self):
        """
        test_post_test_event_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/test_event')
        mock_response = '{"success": false}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.post_test_event(**req_copy)

    def test_post_test_event_value_error_with_retries(self):
        # Enable retries and run test_post_test_event_value_error.
        _service.enable_retries()
        self.test_post_test_event_value_error()

        # Disable retries and run test_post_test_event_value_error.
        _service.disable_retries()
        self.test_post_test_event_value_error()


# endregion
##############################################################################
# End of Service: Setting
##############################################################################

##############################################################################
# Start of Service: Attachment
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecurityAndComplianceCenterApiV3.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecurityAndComplianceCenterApiV3)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecurityAndComplianceCenterApiV3.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListInstanceAttachments:
    """
    Test Class for list_instance_attachments
    """

    @responses.activate
    def test_list_instance_attachments_all_params(self):
        """
        list_instance_attachments()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/attachments')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "attachments": [{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        account_id = 'testString'
        version_group_label = '6702d85a-6437-4d6f-8701-c0146648787b'
        limit = 25
        sort = 'created_on'
        direction = 'desc'
        start = 'testString'

        # Invoke method
        response = _service.list_instance_attachments(
            instance_id,
            account_id=account_id,
            version_group_label=version_group_label,
            limit=limit,
            sort=sort,
            direction=direction,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'version_group_label={}'.format(version_group_label) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'direction={}'.format(direction) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_instance_attachments_all_params_with_retries(self):
        # Enable retries and run test_list_instance_attachments_all_params.
        _service.enable_retries()
        self.test_list_instance_attachments_all_params()

        # Disable retries and run test_list_instance_attachments_all_params.
        _service.disable_retries()
        self.test_list_instance_attachments_all_params()

    @responses.activate
    def test_list_instance_attachments_required_params(self):
        """
        test_list_instance_attachments_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/attachments')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "attachments": [{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Invoke method
        response = _service.list_instance_attachments(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_instance_attachments_required_params_with_retries(self):
        # Enable retries and run test_list_instance_attachments_required_params.
        _service.enable_retries()
        self.test_list_instance_attachments_required_params()

        # Disable retries and run test_list_instance_attachments_required_params.
        _service.disable_retries()
        self.test_list_instance_attachments_required_params()

    @responses.activate
    def test_list_instance_attachments_value_error(self):
        """
        test_list_instance_attachments_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/attachments')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "attachments": [{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_instance_attachments(**req_copy)

    def test_list_instance_attachments_value_error_with_retries(self):
        # Enable retries and run test_list_instance_attachments_value_error.
        _service.enable_retries()
        self.test_list_instance_attachments_value_error()

        # Disable retries and run test_list_instance_attachments_value_error.
        _service.disable_retries()
        self.test_list_instance_attachments_value_error()

    @responses.activate
    def test_list_instance_attachments_with_pager_get_next(self):
        """
        test_list_instance_attachments_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/attachments')
        mock_response1 = '{"next":{"start":"1"},"attachments":[{"attachment_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}],"description":"description","name":"name","notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["failed_control_ids"]}},"schedule":"daily","scope":[{"id":"id"}],"status":"enabled","data_selection_range":{"start_date":"2025-02-28T05:42:58.000Z","end_date":"2025-02-28T05:42:58.000Z"},"account_id":"account_id","created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","id":"id","instance_id":"instance_id","last_scan":{"id":"id","status":"status","time":"2019-01-01T12:00:00.000Z"},"next_scan_time":"2019-01-01T12:00:00.000Z","profile_id":"profile_id","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z"}],"total_count":2,"limit":1}'
        mock_response2 = '{"attachments":[{"attachment_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}],"description":"description","name":"name","notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["failed_control_ids"]}},"schedule":"daily","scope":[{"id":"id"}],"status":"enabled","data_selection_range":{"start_date":"2025-02-28T05:42:58.000Z","end_date":"2025-02-28T05:42:58.000Z"},"account_id":"account_id","created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","id":"id","instance_id":"instance_id","last_scan":{"id":"id","status":"status","time":"2019-01-01T12:00:00.000Z"},"next_scan_time":"2019-01-01T12:00:00.000Z","profile_id":"profile_id","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = InstanceAttachmentsPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id='testString',
            version_group_label='6702d85a-6437-4d6f-8701-c0146648787b',
            limit=10,
            sort='created_on',
            direction='desc',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_instance_attachments_with_pager_get_all(self):
        """
        test_list_instance_attachments_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/attachments')
        mock_response1 = '{"next":{"start":"1"},"attachments":[{"attachment_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}],"description":"description","name":"name","notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["failed_control_ids"]}},"schedule":"daily","scope":[{"id":"id"}],"status":"enabled","data_selection_range":{"start_date":"2025-02-28T05:42:58.000Z","end_date":"2025-02-28T05:42:58.000Z"},"account_id":"account_id","created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","id":"id","instance_id":"instance_id","last_scan":{"id":"id","status":"status","time":"2019-01-01T12:00:00.000Z"},"next_scan_time":"2019-01-01T12:00:00.000Z","profile_id":"profile_id","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z"}],"total_count":2,"limit":1}'
        mock_response2 = '{"attachments":[{"attachment_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}],"description":"description","name":"name","notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["failed_control_ids"]}},"schedule":"daily","scope":[{"id":"id"}],"status":"enabled","data_selection_range":{"start_date":"2025-02-28T05:42:58.000Z","end_date":"2025-02-28T05:42:58.000Z"},"account_id":"account_id","created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","id":"id","instance_id":"instance_id","last_scan":{"id":"id","status":"status","time":"2019-01-01T12:00:00.000Z"},"next_scan_time":"2019-01-01T12:00:00.000Z","profile_id":"profile_id","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = InstanceAttachmentsPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id='testString',
            version_group_label='6702d85a-6437-4d6f-8701-c0146648787b',
            limit=10,
            sort='created_on',
            direction='desc',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateProfileAttachment:
    """
    Test Class for create_profile_attachment
    """

    @responses.activate
    def test_create_profile_attachment_all_params(self):
        """
        create_profile_attachment()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments')
        mock_response = '{"profile_id": "profile_id", "attachments": [{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['assessment_type'] = 'automated'
        parameter_model['assessment_id'] = 'rule-e16fcfea-fe21-4d30-a721-423611481fea'
        parameter_model['parameter_name'] = 'tls_version'
        parameter_model['parameter_display_name'] = 'IBM Cloud Internet Services TLS version'
        parameter_model['parameter_type'] = 'string_list'
        parameter_model['parameter_value'] = '["1.2", "1.3"]'

        # Construct a dict representation of a AttachmentNotificationsControls model
        attachment_notifications_controls_model = {}
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = []

        # Construct a dict representation of a AttachmentNotifications model
        attachment_notifications_model = {}
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        # Construct a dict representation of a MultiCloudScopePayloadById model
        multi_cloud_scope_payload_model = {}
        multi_cloud_scope_payload_model['id'] = '8baad3b5-2e69-4027-9967-efac19508e1c'

        # Construct a dict representation of a DateRange model
        date_range_model = {}
        date_range_model['start_date'] = '2025-02-28T05:42:58Z'
        date_range_model['end_date'] = '2025-02-28T05:42:58Z'

        # Construct a dict representation of a ProfileAttachmentBase model
        profile_attachment_base_model = {}
        profile_attachment_base_model['attachment_parameters'] = [parameter_model]
        profile_attachment_base_model['description'] = 'This is a profile attachment targeting IBM CIS Foundation using a SDK'
        profile_attachment_base_model['name'] = 'Profile Attachment for IBM CIS Foundation SDK test'
        profile_attachment_base_model['notifications'] = attachment_notifications_model
        profile_attachment_base_model['schedule'] = 'daily'
        profile_attachment_base_model['scope'] = [multi_cloud_scope_payload_model]
        profile_attachment_base_model['status'] = 'disabled'
        profile_attachment_base_model['data_selection_range'] = date_range_model

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        new_attachments = [profile_attachment_base_model]
        new_profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3'
        account_id = 'testString'

        # Invoke method
        response = _service.create_profile_attachment(
            instance_id,
            profile_id,
            new_attachments,
            new_profile_id=new_profile_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachments'] == [profile_attachment_base_model]
        assert req_body['profile_id'] == '9c265b4a-4cdf-47f1-acd3-17b5808f7f3'

    def test_create_profile_attachment_all_params_with_retries(self):
        # Enable retries and run test_create_profile_attachment_all_params.
        _service.enable_retries()
        self.test_create_profile_attachment_all_params()

        # Disable retries and run test_create_profile_attachment_all_params.
        _service.disable_retries()
        self.test_create_profile_attachment_all_params()

    @responses.activate
    def test_create_profile_attachment_required_params(self):
        """
        test_create_profile_attachment_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments')
        mock_response = '{"profile_id": "profile_id", "attachments": [{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['assessment_type'] = 'automated'
        parameter_model['assessment_id'] = 'rule-e16fcfea-fe21-4d30-a721-423611481fea'
        parameter_model['parameter_name'] = 'tls_version'
        parameter_model['parameter_display_name'] = 'IBM Cloud Internet Services TLS version'
        parameter_model['parameter_type'] = 'string_list'
        parameter_model['parameter_value'] = '["1.2", "1.3"]'

        # Construct a dict representation of a AttachmentNotificationsControls model
        attachment_notifications_controls_model = {}
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = []

        # Construct a dict representation of a AttachmentNotifications model
        attachment_notifications_model = {}
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        # Construct a dict representation of a MultiCloudScopePayloadById model
        multi_cloud_scope_payload_model = {}
        multi_cloud_scope_payload_model['id'] = '8baad3b5-2e69-4027-9967-efac19508e1c'

        # Construct a dict representation of a DateRange model
        date_range_model = {}
        date_range_model['start_date'] = '2025-02-28T05:42:58Z'
        date_range_model['end_date'] = '2025-02-28T05:42:58Z'

        # Construct a dict representation of a ProfileAttachmentBase model
        profile_attachment_base_model = {}
        profile_attachment_base_model['attachment_parameters'] = [parameter_model]
        profile_attachment_base_model['description'] = 'This is a profile attachment targeting IBM CIS Foundation using a SDK'
        profile_attachment_base_model['name'] = 'Profile Attachment for IBM CIS Foundation SDK test'
        profile_attachment_base_model['notifications'] = attachment_notifications_model
        profile_attachment_base_model['schedule'] = 'daily'
        profile_attachment_base_model['scope'] = [multi_cloud_scope_payload_model]
        profile_attachment_base_model['status'] = 'disabled'
        profile_attachment_base_model['data_selection_range'] = date_range_model

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        new_attachments = [profile_attachment_base_model]
        new_profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3'

        # Invoke method
        response = _service.create_profile_attachment(
            instance_id,
            profile_id,
            new_attachments,
            new_profile_id=new_profile_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachments'] == [profile_attachment_base_model]
        assert req_body['profile_id'] == '9c265b4a-4cdf-47f1-acd3-17b5808f7f3'

    def test_create_profile_attachment_required_params_with_retries(self):
        # Enable retries and run test_create_profile_attachment_required_params.
        _service.enable_retries()
        self.test_create_profile_attachment_required_params()

        # Disable retries and run test_create_profile_attachment_required_params.
        _service.disable_retries()
        self.test_create_profile_attachment_required_params()

    @responses.activate
    def test_create_profile_attachment_value_error(self):
        """
        test_create_profile_attachment_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments')
        mock_response = '{"profile_id": "profile_id", "attachments": [{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['assessment_type'] = 'automated'
        parameter_model['assessment_id'] = 'rule-e16fcfea-fe21-4d30-a721-423611481fea'
        parameter_model['parameter_name'] = 'tls_version'
        parameter_model['parameter_display_name'] = 'IBM Cloud Internet Services TLS version'
        parameter_model['parameter_type'] = 'string_list'
        parameter_model['parameter_value'] = '["1.2", "1.3"]'

        # Construct a dict representation of a AttachmentNotificationsControls model
        attachment_notifications_controls_model = {}
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = []

        # Construct a dict representation of a AttachmentNotifications model
        attachment_notifications_model = {}
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        # Construct a dict representation of a MultiCloudScopePayloadById model
        multi_cloud_scope_payload_model = {}
        multi_cloud_scope_payload_model['id'] = '8baad3b5-2e69-4027-9967-efac19508e1c'

        # Construct a dict representation of a DateRange model
        date_range_model = {}
        date_range_model['start_date'] = '2025-02-28T05:42:58Z'
        date_range_model['end_date'] = '2025-02-28T05:42:58Z'

        # Construct a dict representation of a ProfileAttachmentBase model
        profile_attachment_base_model = {}
        profile_attachment_base_model['attachment_parameters'] = [parameter_model]
        profile_attachment_base_model['description'] = 'This is a profile attachment targeting IBM CIS Foundation using a SDK'
        profile_attachment_base_model['name'] = 'Profile Attachment for IBM CIS Foundation SDK test'
        profile_attachment_base_model['notifications'] = attachment_notifications_model
        profile_attachment_base_model['schedule'] = 'daily'
        profile_attachment_base_model['scope'] = [multi_cloud_scope_payload_model]
        profile_attachment_base_model['status'] = 'disabled'
        profile_attachment_base_model['data_selection_range'] = date_range_model

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        new_attachments = [profile_attachment_base_model]
        new_profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_id": profile_id,
            "new_attachments": new_attachments,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_profile_attachment(**req_copy)

    def test_create_profile_attachment_value_error_with_retries(self):
        # Enable retries and run test_create_profile_attachment_value_error.
        _service.enable_retries()
        self.test_create_profile_attachment_value_error()

        # Disable retries and run test_create_profile_attachment_value_error.
        _service.disable_retries()
        self.test_create_profile_attachment_value_error()


class TestGetProfileAttachment:
    """
    Test Class for get_profile_attachment
    """

    @responses.activate
    def test_get_profile_attachment_all_params(self):
        """
        get_profile_attachment()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments/testString')
        mock_response = '{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        attachment_id = 'testString'
        account_id = 'testString'

        # Invoke method
        response = _service.get_profile_attachment(
            instance_id,
            profile_id,
            attachment_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_get_profile_attachment_all_params_with_retries(self):
        # Enable retries and run test_get_profile_attachment_all_params.
        _service.enable_retries()
        self.test_get_profile_attachment_all_params()

        # Disable retries and run test_get_profile_attachment_all_params.
        _service.disable_retries()
        self.test_get_profile_attachment_all_params()

    @responses.activate
    def test_get_profile_attachment_required_params(self):
        """
        test_get_profile_attachment_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments/testString')
        mock_response = '{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        attachment_id = 'testString'

        # Invoke method
        response = _service.get_profile_attachment(
            instance_id,
            profile_id,
            attachment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_profile_attachment_required_params_with_retries(self):
        # Enable retries and run test_get_profile_attachment_required_params.
        _service.enable_retries()
        self.test_get_profile_attachment_required_params()

        # Disable retries and run test_get_profile_attachment_required_params.
        _service.disable_retries()
        self.test_get_profile_attachment_required_params()

    @responses.activate
    def test_get_profile_attachment_value_error(self):
        """
        test_get_profile_attachment_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments/testString')
        mock_response = '{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        attachment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_id": profile_id,
            "attachment_id": attachment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_profile_attachment(**req_copy)

    def test_get_profile_attachment_value_error_with_retries(self):
        # Enable retries and run test_get_profile_attachment_value_error.
        _service.enable_retries()
        self.test_get_profile_attachment_value_error()

        # Disable retries and run test_get_profile_attachment_value_error.
        _service.disable_retries()
        self.test_get_profile_attachment_value_error()


class TestReplaceProfileAttachment:
    """
    Test Class for replace_profile_attachment
    """

    @responses.activate
    def test_replace_profile_attachment_all_params(self):
        """
        replace_profile_attachment()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments/testString')
        mock_response = '{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        # Construct a dict representation of a AttachmentNotificationsControls model
        attachment_notifications_controls_model = {}
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = ['testString']

        # Construct a dict representation of a AttachmentNotifications model
        attachment_notifications_model = {}
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        # Construct a dict representation of a MultiCloudScopePayloadById model
        multi_cloud_scope_payload_model = {}
        multi_cloud_scope_payload_model['id'] = 'testString'

        # Construct a dict representation of a DateRange model
        date_range_model = {}
        date_range_model['start_date'] = '2025-02-28T05:42:58Z'
        date_range_model['end_date'] = '2025-02-28T05:42:58Z'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        attachment_id = 'testString'
        attachment_parameters = [parameter_model]
        description = 'testString'
        name = 'testString'
        notifications = attachment_notifications_model
        schedule = 'daily'
        scope = [multi_cloud_scope_payload_model]
        status = 'enabled'
        data_selection_range = date_range_model
        account_id = 'testString'

        # Invoke method
        response = _service.replace_profile_attachment(
            instance_id,
            profile_id,
            attachment_id,
            attachment_parameters,
            description,
            name,
            notifications,
            schedule,
            scope,
            status,
            data_selection_range=data_selection_range,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachment_parameters'] == [parameter_model]
        assert req_body['description'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['notifications'] == attachment_notifications_model
        assert req_body['schedule'] == 'daily'
        assert req_body['scope'] == [multi_cloud_scope_payload_model]
        assert req_body['status'] == 'enabled'
        assert req_body['data_selection_range'] == date_range_model

    def test_replace_profile_attachment_all_params_with_retries(self):
        # Enable retries and run test_replace_profile_attachment_all_params.
        _service.enable_retries()
        self.test_replace_profile_attachment_all_params()

        # Disable retries and run test_replace_profile_attachment_all_params.
        _service.disable_retries()
        self.test_replace_profile_attachment_all_params()

    @responses.activate
    def test_replace_profile_attachment_required_params(self):
        """
        test_replace_profile_attachment_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments/testString')
        mock_response = '{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        # Construct a dict representation of a AttachmentNotificationsControls model
        attachment_notifications_controls_model = {}
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = ['testString']

        # Construct a dict representation of a AttachmentNotifications model
        attachment_notifications_model = {}
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        # Construct a dict representation of a MultiCloudScopePayloadById model
        multi_cloud_scope_payload_model = {}
        multi_cloud_scope_payload_model['id'] = 'testString'

        # Construct a dict representation of a DateRange model
        date_range_model = {}
        date_range_model['start_date'] = '2025-02-28T05:42:58Z'
        date_range_model['end_date'] = '2025-02-28T05:42:58Z'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        attachment_id = 'testString'
        attachment_parameters = [parameter_model]
        description = 'testString'
        name = 'testString'
        notifications = attachment_notifications_model
        schedule = 'daily'
        scope = [multi_cloud_scope_payload_model]
        status = 'enabled'
        data_selection_range = date_range_model

        # Invoke method
        response = _service.replace_profile_attachment(
            instance_id,
            profile_id,
            attachment_id,
            attachment_parameters,
            description,
            name,
            notifications,
            schedule,
            scope,
            status,
            data_selection_range=data_selection_range,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachment_parameters'] == [parameter_model]
        assert req_body['description'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['notifications'] == attachment_notifications_model
        assert req_body['schedule'] == 'daily'
        assert req_body['scope'] == [multi_cloud_scope_payload_model]
        assert req_body['status'] == 'enabled'
        assert req_body['data_selection_range'] == date_range_model

    def test_replace_profile_attachment_required_params_with_retries(self):
        # Enable retries and run test_replace_profile_attachment_required_params.
        _service.enable_retries()
        self.test_replace_profile_attachment_required_params()

        # Disable retries and run test_replace_profile_attachment_required_params.
        _service.disable_retries()
        self.test_replace_profile_attachment_required_params()

    @responses.activate
    def test_replace_profile_attachment_value_error(self):
        """
        test_replace_profile_attachment_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments/testString')
        mock_response = '{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        # Construct a dict representation of a AttachmentNotificationsControls model
        attachment_notifications_controls_model = {}
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = ['testString']

        # Construct a dict representation of a AttachmentNotifications model
        attachment_notifications_model = {}
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        # Construct a dict representation of a MultiCloudScopePayloadById model
        multi_cloud_scope_payload_model = {}
        multi_cloud_scope_payload_model['id'] = 'testString'

        # Construct a dict representation of a DateRange model
        date_range_model = {}
        date_range_model['start_date'] = '2025-02-28T05:42:58Z'
        date_range_model['end_date'] = '2025-02-28T05:42:58Z'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        attachment_id = 'testString'
        attachment_parameters = [parameter_model]
        description = 'testString'
        name = 'testString'
        notifications = attachment_notifications_model
        schedule = 'daily'
        scope = [multi_cloud_scope_payload_model]
        status = 'enabled'
        data_selection_range = date_range_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_id": profile_id,
            "attachment_id": attachment_id,
            "attachment_parameters": attachment_parameters,
            "description": description,
            "name": name,
            "notifications": notifications,
            "schedule": schedule,
            "scope": scope,
            "status": status,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_profile_attachment(**req_copy)

    def test_replace_profile_attachment_value_error_with_retries(self):
        # Enable retries and run test_replace_profile_attachment_value_error.
        _service.enable_retries()
        self.test_replace_profile_attachment_value_error()

        # Disable retries and run test_replace_profile_attachment_value_error.
        _service.disable_retries()
        self.test_replace_profile_attachment_value_error()


class TestDeleteProfileAttachment:
    """
    Test Class for delete_profile_attachment
    """

    @responses.activate
    def test_delete_profile_attachment_all_params(self):
        """
        delete_profile_attachment()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments/testString')
        mock_response = '{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        attachment_id = 'testString'
        account_id = 'testString'

        # Invoke method
        response = _service.delete_profile_attachment(
            instance_id,
            profile_id,
            attachment_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_delete_profile_attachment_all_params_with_retries(self):
        # Enable retries and run test_delete_profile_attachment_all_params.
        _service.enable_retries()
        self.test_delete_profile_attachment_all_params()

        # Disable retries and run test_delete_profile_attachment_all_params.
        _service.disable_retries()
        self.test_delete_profile_attachment_all_params()

    @responses.activate
    def test_delete_profile_attachment_required_params(self):
        """
        test_delete_profile_attachment_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments/testString')
        mock_response = '{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        attachment_id = 'testString'

        # Invoke method
        response = _service.delete_profile_attachment(
            instance_id,
            profile_id,
            attachment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_profile_attachment_required_params_with_retries(self):
        # Enable retries and run test_delete_profile_attachment_required_params.
        _service.enable_retries()
        self.test_delete_profile_attachment_required_params()

        # Disable retries and run test_delete_profile_attachment_required_params.
        _service.disable_retries()
        self.test_delete_profile_attachment_required_params()

    @responses.activate
    def test_delete_profile_attachment_value_error(self):
        """
        test_delete_profile_attachment_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments/testString')
        mock_response = '{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        attachment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_id": profile_id,
            "attachment_id": attachment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_profile_attachment(**req_copy)

    def test_delete_profile_attachment_value_error_with_retries(self):
        # Enable retries and run test_delete_profile_attachment_value_error.
        _service.enable_retries()
        self.test_delete_profile_attachment_value_error()

        # Disable retries and run test_delete_profile_attachment_value_error.
        _service.disable_retries()
        self.test_delete_profile_attachment_value_error()


class TestUpgradeAttachment:
    """
    Test Class for upgrade_attachment
    """

    @responses.activate
    def test_upgrade_attachment_all_params(self):
        """
        upgrade_attachment()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments/testString/upgrade')
        mock_response = '{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        attachment_id = 'testString'
        attachment_parameters = [parameter_model]
        account_id = 'testString'

        # Invoke method
        response = _service.upgrade_attachment(
            instance_id,
            profile_id,
            attachment_id,
            attachment_parameters,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachment_parameters'] == [parameter_model]

    def test_upgrade_attachment_all_params_with_retries(self):
        # Enable retries and run test_upgrade_attachment_all_params.
        _service.enable_retries()
        self.test_upgrade_attachment_all_params()

        # Disable retries and run test_upgrade_attachment_all_params.
        _service.disable_retries()
        self.test_upgrade_attachment_all_params()

    @responses.activate
    def test_upgrade_attachment_required_params(self):
        """
        test_upgrade_attachment_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments/testString/upgrade')
        mock_response = '{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        attachment_id = 'testString'
        attachment_parameters = [parameter_model]

        # Invoke method
        response = _service.upgrade_attachment(
            instance_id,
            profile_id,
            attachment_id,
            attachment_parameters,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachment_parameters'] == [parameter_model]

    def test_upgrade_attachment_required_params_with_retries(self):
        # Enable retries and run test_upgrade_attachment_required_params.
        _service.enable_retries()
        self.test_upgrade_attachment_required_params()

        # Disable retries and run test_upgrade_attachment_required_params.
        _service.disable_retries()
        self.test_upgrade_attachment_required_params()

    @responses.activate
    def test_upgrade_attachment_value_error(self):
        """
        test_upgrade_attachment_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments/testString/upgrade')
        mock_response = '{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        attachment_id = 'testString'
        attachment_parameters = [parameter_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_id": profile_id,
            "attachment_id": attachment_id,
            "attachment_parameters": attachment_parameters,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.upgrade_attachment(**req_copy)

    def test_upgrade_attachment_value_error_with_retries(self):
        # Enable retries and run test_upgrade_attachment_value_error.
        _service.enable_retries()
        self.test_upgrade_attachment_value_error()

        # Disable retries and run test_upgrade_attachment_value_error.
        _service.disable_retries()
        self.test_upgrade_attachment_value_error()


class TestCreateScan:
    """
    Test Class for create_scan
    """

    @responses.activate
    def test_create_scan_all_params(self):
        """
        create_scan()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scans')
        mock_response = '{"id": "id", "account_id": "account_id", "attachment_id": "attachment_id", "report_id": "report_id", "status": "status", "last_scan_time": "2019-01-01T12:00:00.000Z", "next_scan_time": "2019-01-01T12:00:00.000Z", "scan_type": "scan_type", "occurence": 9}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        attachment_id = '4deb572c-9f37-4126-9cc0-d550672533cb'
        account_id = 'testString'

        # Invoke method
        response = _service.create_scan(
            instance_id,
            attachment_id=attachment_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachment_id'] == '4deb572c-9f37-4126-9cc0-d550672533cb'

    def test_create_scan_all_params_with_retries(self):
        # Enable retries and run test_create_scan_all_params.
        _service.enable_retries()
        self.test_create_scan_all_params()

        # Disable retries and run test_create_scan_all_params.
        _service.disable_retries()
        self.test_create_scan_all_params()

    @responses.activate
    def test_create_scan_required_params(self):
        """
        test_create_scan_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scans')
        mock_response = '{"id": "id", "account_id": "account_id", "attachment_id": "attachment_id", "report_id": "report_id", "status": "status", "last_scan_time": "2019-01-01T12:00:00.000Z", "next_scan_time": "2019-01-01T12:00:00.000Z", "scan_type": "scan_type", "occurence": 9}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        attachment_id = '4deb572c-9f37-4126-9cc0-d550672533cb'

        # Invoke method
        response = _service.create_scan(
            instance_id,
            attachment_id=attachment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachment_id'] == '4deb572c-9f37-4126-9cc0-d550672533cb'

    def test_create_scan_required_params_with_retries(self):
        # Enable retries and run test_create_scan_required_params.
        _service.enable_retries()
        self.test_create_scan_required_params()

        # Disable retries and run test_create_scan_required_params.
        _service.disable_retries()
        self.test_create_scan_required_params()

    @responses.activate
    def test_create_scan_value_error(self):
        """
        test_create_scan_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scans')
        mock_response = '{"id": "id", "account_id": "account_id", "attachment_id": "attachment_id", "report_id": "report_id", "status": "status", "last_scan_time": "2019-01-01T12:00:00.000Z", "next_scan_time": "2019-01-01T12:00:00.000Z", "scan_type": "scan_type", "occurence": 9}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        attachment_id = '4deb572c-9f37-4126-9cc0-d550672533cb'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_scan(**req_copy)

    def test_create_scan_value_error_with_retries(self):
        # Enable retries and run test_create_scan_value_error.
        _service.enable_retries()
        self.test_create_scan_value_error()

        # Disable retries and run test_create_scan_value_error.
        _service.disable_retries()
        self.test_create_scan_value_error()


# endregion
##############################################################################
# End of Service: Attachment
##############################################################################

##############################################################################
# Start of Service: ControlLibrary
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecurityAndComplianceCenterApiV3.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecurityAndComplianceCenterApiV3)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecurityAndComplianceCenterApiV3.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateControlLibrary:
    """
    Test Class for create_control_library
    """

    @responses.activate
    def test_create_control_library_all_params(self):
        """
        create_control_library()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries')
        mock_response = '{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AssessmentPrototype model
        assessment_prototype_model = {}
        assessment_prototype_model['assessment_id'] = 'rule-d1bd9f3f-bee1-46c5-9533-da8bba9eed4e'
        assessment_prototype_model['assessment_description'] = 'This rule will check on regulation'

        # Construct a dict representation of a ControlSpecificationPrototype model
        control_specification_prototype_model = {}
        control_specification_prototype_model['component_id'] = 'apprapp'
        control_specification_prototype_model['environment'] = 'ibm-cloud'
        control_specification_prototype_model['control_specification_id'] = 'testString'
        control_specification_prototype_model['control_specification_description'] = 'This field is used to describe a control specification'
        control_specification_prototype_model['assessments'] = [assessment_prototype_model]

        # Construct a dict representation of a ControlDoc model
        control_doc_model = {}
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a ControlPrototype model
        control_prototype_model = {}
        control_prototype_model['control_name'] = 'security'
        control_prototype_model['control_description'] = 'This is a description of a control'
        control_prototype_model['control_category'] = 'test-control'
        control_prototype_model['control_requirement'] = True
        control_prototype_model['control_parent'] = 'testString'
        control_prototype_model['control_specifications'] = [control_specification_prototype_model]
        control_prototype_model['control_docs'] = control_doc_model
        control_prototype_model['status'] = 'disabled'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        control_library_name = 'custom control library from SDK'
        control_library_description = 'This is a custom control library made from the SDK test framework'
        control_library_type = 'custom'
        control_library_version = '0.0.1'
        controls = [control_prototype_model]
        account_id = 'testString'

        # Invoke method
        response = _service.create_control_library(
            instance_id,
            control_library_name,
            control_library_description,
            control_library_type,
            control_library_version,
            controls,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['control_library_name'] == 'custom control library from SDK'
        assert req_body['control_library_description'] == 'This is a custom control library made from the SDK test framework'
        assert req_body['control_library_type'] == 'custom'
        assert req_body['control_library_version'] == '0.0.1'
        assert req_body['controls'] == [control_prototype_model]

    def test_create_control_library_all_params_with_retries(self):
        # Enable retries and run test_create_control_library_all_params.
        _service.enable_retries()
        self.test_create_control_library_all_params()

        # Disable retries and run test_create_control_library_all_params.
        _service.disable_retries()
        self.test_create_control_library_all_params()

    @responses.activate
    def test_create_control_library_required_params(self):
        """
        test_create_control_library_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries')
        mock_response = '{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AssessmentPrototype model
        assessment_prototype_model = {}
        assessment_prototype_model['assessment_id'] = 'rule-d1bd9f3f-bee1-46c5-9533-da8bba9eed4e'
        assessment_prototype_model['assessment_description'] = 'This rule will check on regulation'

        # Construct a dict representation of a ControlSpecificationPrototype model
        control_specification_prototype_model = {}
        control_specification_prototype_model['component_id'] = 'apprapp'
        control_specification_prototype_model['environment'] = 'ibm-cloud'
        control_specification_prototype_model['control_specification_id'] = 'testString'
        control_specification_prototype_model['control_specification_description'] = 'This field is used to describe a control specification'
        control_specification_prototype_model['assessments'] = [assessment_prototype_model]

        # Construct a dict representation of a ControlDoc model
        control_doc_model = {}
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a ControlPrototype model
        control_prototype_model = {}
        control_prototype_model['control_name'] = 'security'
        control_prototype_model['control_description'] = 'This is a description of a control'
        control_prototype_model['control_category'] = 'test-control'
        control_prototype_model['control_requirement'] = True
        control_prototype_model['control_parent'] = 'testString'
        control_prototype_model['control_specifications'] = [control_specification_prototype_model]
        control_prototype_model['control_docs'] = control_doc_model
        control_prototype_model['status'] = 'disabled'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        control_library_name = 'custom control library from SDK'
        control_library_description = 'This is a custom control library made from the SDK test framework'
        control_library_type = 'custom'
        control_library_version = '0.0.1'
        controls = [control_prototype_model]

        # Invoke method
        response = _service.create_control_library(
            instance_id,
            control_library_name,
            control_library_description,
            control_library_type,
            control_library_version,
            controls,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['control_library_name'] == 'custom control library from SDK'
        assert req_body['control_library_description'] == 'This is a custom control library made from the SDK test framework'
        assert req_body['control_library_type'] == 'custom'
        assert req_body['control_library_version'] == '0.0.1'
        assert req_body['controls'] == [control_prototype_model]

    def test_create_control_library_required_params_with_retries(self):
        # Enable retries and run test_create_control_library_required_params.
        _service.enable_retries()
        self.test_create_control_library_required_params()

        # Disable retries and run test_create_control_library_required_params.
        _service.disable_retries()
        self.test_create_control_library_required_params()

    @responses.activate
    def test_create_control_library_value_error(self):
        """
        test_create_control_library_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries')
        mock_response = '{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AssessmentPrototype model
        assessment_prototype_model = {}
        assessment_prototype_model['assessment_id'] = 'rule-d1bd9f3f-bee1-46c5-9533-da8bba9eed4e'
        assessment_prototype_model['assessment_description'] = 'This rule will check on regulation'

        # Construct a dict representation of a ControlSpecificationPrototype model
        control_specification_prototype_model = {}
        control_specification_prototype_model['component_id'] = 'apprapp'
        control_specification_prototype_model['environment'] = 'ibm-cloud'
        control_specification_prototype_model['control_specification_id'] = 'testString'
        control_specification_prototype_model['control_specification_description'] = 'This field is used to describe a control specification'
        control_specification_prototype_model['assessments'] = [assessment_prototype_model]

        # Construct a dict representation of a ControlDoc model
        control_doc_model = {}
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a ControlPrototype model
        control_prototype_model = {}
        control_prototype_model['control_name'] = 'security'
        control_prototype_model['control_description'] = 'This is a description of a control'
        control_prototype_model['control_category'] = 'test-control'
        control_prototype_model['control_requirement'] = True
        control_prototype_model['control_parent'] = 'testString'
        control_prototype_model['control_specifications'] = [control_specification_prototype_model]
        control_prototype_model['control_docs'] = control_doc_model
        control_prototype_model['status'] = 'disabled'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        control_library_name = 'custom control library from SDK'
        control_library_description = 'This is a custom control library made from the SDK test framework'
        control_library_type = 'custom'
        control_library_version = '0.0.1'
        controls = [control_prototype_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "control_library_name": control_library_name,
            "control_library_description": control_library_description,
            "control_library_type": control_library_type,
            "control_library_version": control_library_version,
            "controls": controls,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_control_library(**req_copy)

    def test_create_control_library_value_error_with_retries(self):
        # Enable retries and run test_create_control_library_value_error.
        _service.enable_retries()
        self.test_create_control_library_value_error()

        # Disable retries and run test_create_control_library_value_error.
        _service.disable_retries()
        self.test_create_control_library_value_error()


class TestListControlLibraries:
    """
    Test Class for list_control_libraries
    """

    @responses.activate
    def test_list_control_libraries_all_params(self):
        """
        list_control_libraries()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "control_libraries": [{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        account_id = 'testString'
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_control_libraries(
            instance_id,
            account_id=account_id,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_control_libraries_all_params_with_retries(self):
        # Enable retries and run test_list_control_libraries_all_params.
        _service.enable_retries()
        self.test_list_control_libraries_all_params()

        # Disable retries and run test_list_control_libraries_all_params.
        _service.disable_retries()
        self.test_list_control_libraries_all_params()

    @responses.activate
    def test_list_control_libraries_required_params(self):
        """
        test_list_control_libraries_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "control_libraries": [{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Invoke method
        response = _service.list_control_libraries(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_control_libraries_required_params_with_retries(self):
        # Enable retries and run test_list_control_libraries_required_params.
        _service.enable_retries()
        self.test_list_control_libraries_required_params()

        # Disable retries and run test_list_control_libraries_required_params.
        _service.disable_retries()
        self.test_list_control_libraries_required_params()

    @responses.activate
    def test_list_control_libraries_value_error(self):
        """
        test_list_control_libraries_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "control_libraries": [{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_control_libraries(**req_copy)

    def test_list_control_libraries_value_error_with_retries(self):
        # Enable retries and run test_list_control_libraries_value_error.
        _service.enable_retries()
        self.test_list_control_libraries_value_error()

        # Disable retries and run test_list_control_libraries_value_error.
        _service.disable_retries()
        self.test_list_control_libraries_value_error()

    @responses.activate
    def test_list_control_libraries_with_pager_get_next(self):
        """
        test_list_control_libraries_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries')
        mock_response1 = '{"next":{"start":"1"},"control_libraries":[{"control_library_name":"control_library_name","control_library_description":"control_library_description","control_library_type":"custom","control_library_version":"control_library_version","controls":[{"control_name":"control_name","control_id":"control_id","control_description":"control_description","control_category":"control_category","control_parent":"control_parent","control_severity":"control_severity","control_tags":["control_tags"],"control_specifications":[{"id":"id","responsibility":"responsibility","component_id":"component_id","component_name":"component_name","component_type":"component_type","environment":"environment","description":"description","assessments_count":17,"assessments":[{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]}]}],"control_docs":{"control_docs_id":"control_docs_id","control_docs_type":"control_docs_type"},"status":"status"}],"id":"id","account_id":"account_id","version_group_label":"version_group_label","latest":true,"created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","hierarchy_enabled":false,"controls_count":14,"control_parents_count":21}],"total_count":2,"limit":1}'
        mock_response2 = '{"control_libraries":[{"control_library_name":"control_library_name","control_library_description":"control_library_description","control_library_type":"custom","control_library_version":"control_library_version","controls":[{"control_name":"control_name","control_id":"control_id","control_description":"control_description","control_category":"control_category","control_parent":"control_parent","control_severity":"control_severity","control_tags":["control_tags"],"control_specifications":[{"id":"id","responsibility":"responsibility","component_id":"component_id","component_name":"component_name","component_type":"component_type","environment":"environment","description":"description","assessments_count":17,"assessments":[{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]}]}],"control_docs":{"control_docs_id":"control_docs_id","control_docs_type":"control_docs_type"},"status":"status"}],"id":"id","account_id":"account_id","version_group_label":"version_group_label","latest":true,"created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","hierarchy_enabled":false,"controls_count":14,"control_parents_count":21}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = ControlLibrariesPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_control_libraries_with_pager_get_all(self):
        """
        test_list_control_libraries_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries')
        mock_response1 = '{"next":{"start":"1"},"control_libraries":[{"control_library_name":"control_library_name","control_library_description":"control_library_description","control_library_type":"custom","control_library_version":"control_library_version","controls":[{"control_name":"control_name","control_id":"control_id","control_description":"control_description","control_category":"control_category","control_parent":"control_parent","control_severity":"control_severity","control_tags":["control_tags"],"control_specifications":[{"id":"id","responsibility":"responsibility","component_id":"component_id","component_name":"component_name","component_type":"component_type","environment":"environment","description":"description","assessments_count":17,"assessments":[{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]}]}],"control_docs":{"control_docs_id":"control_docs_id","control_docs_type":"control_docs_type"},"status":"status"}],"id":"id","account_id":"account_id","version_group_label":"version_group_label","latest":true,"created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","hierarchy_enabled":false,"controls_count":14,"control_parents_count":21}],"total_count":2,"limit":1}'
        mock_response2 = '{"control_libraries":[{"control_library_name":"control_library_name","control_library_description":"control_library_description","control_library_type":"custom","control_library_version":"control_library_version","controls":[{"control_name":"control_name","control_id":"control_id","control_description":"control_description","control_category":"control_category","control_parent":"control_parent","control_severity":"control_severity","control_tags":["control_tags"],"control_specifications":[{"id":"id","responsibility":"responsibility","component_id":"component_id","component_name":"component_name","component_type":"component_type","environment":"environment","description":"description","assessments_count":17,"assessments":[{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]}]}],"control_docs":{"control_docs_id":"control_docs_id","control_docs_type":"control_docs_type"},"status":"status"}],"id":"id","account_id":"account_id","version_group_label":"version_group_label","latest":true,"created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","hierarchy_enabled":false,"controls_count":14,"control_parents_count":21}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = ControlLibrariesPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestReplaceCustomControlLibrary:
    """
    Test Class for replace_custom_control_library
    """

    @responses.activate
    def test_replace_custom_control_library_all_params(self):
        """
        replace_custom_control_library()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries/testString')
        mock_response = '{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AssessmentPrototype model
        assessment_prototype_model = {}
        assessment_prototype_model['assessment_id'] = 'rule-d1bd9f3f-bee1-46c5-9533-da8bba9eed4e'
        assessment_prototype_model['assessment_description'] = 'This rule will check on regulation'

        # Construct a dict representation of a ControlSpecificationPrototype model
        control_specification_prototype_model = {}
        control_specification_prototype_model['component_id'] = 'apprapp'
        control_specification_prototype_model['environment'] = 'ibm-cloud'
        control_specification_prototype_model['control_specification_id'] = 'testString'
        control_specification_prototype_model['control_specification_description'] = 'This field is used to describe a control specification'
        control_specification_prototype_model['assessments'] = [assessment_prototype_model]

        # Construct a dict representation of a ControlDoc model
        control_doc_model = {}
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a ControlPrototype model
        control_prototype_model = {}
        control_prototype_model['control_name'] = 'security'
        control_prototype_model['control_description'] = 'This is a description of a control'
        control_prototype_model['control_category'] = 'test-control'
        control_prototype_model['control_requirement'] = True
        control_prototype_model['control_parent'] = 'testString'
        control_prototype_model['control_specifications'] = [control_specification_prototype_model]
        control_prototype_model['control_docs'] = control_doc_model
        control_prototype_model['status'] = 'disabled'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        control_library_id = 'testString'
        control_library_name = 'custom control library from SDK'
        control_library_description = 'This is a custom control library made from the SDK test framework'
        control_library_type = 'custom'
        control_library_version = '0.0.2'
        controls = [control_prototype_model]
        bss_account = 'testString'

        # Invoke method
        response = _service.replace_custom_control_library(
            instance_id,
            control_library_id,
            control_library_name,
            control_library_description,
            control_library_type,
            control_library_version,
            controls,
            bss_account=bss_account,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'bss_account={}'.format(bss_account) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['control_library_name'] == 'custom control library from SDK'
        assert req_body['control_library_description'] == 'This is a custom control library made from the SDK test framework'
        assert req_body['control_library_type'] == 'custom'
        assert req_body['control_library_version'] == '0.0.2'
        assert req_body['controls'] == [control_prototype_model]

    def test_replace_custom_control_library_all_params_with_retries(self):
        # Enable retries and run test_replace_custom_control_library_all_params.
        _service.enable_retries()
        self.test_replace_custom_control_library_all_params()

        # Disable retries and run test_replace_custom_control_library_all_params.
        _service.disable_retries()
        self.test_replace_custom_control_library_all_params()

    @responses.activate
    def test_replace_custom_control_library_required_params(self):
        """
        test_replace_custom_control_library_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries/testString')
        mock_response = '{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AssessmentPrototype model
        assessment_prototype_model = {}
        assessment_prototype_model['assessment_id'] = 'rule-d1bd9f3f-bee1-46c5-9533-da8bba9eed4e'
        assessment_prototype_model['assessment_description'] = 'This rule will check on regulation'

        # Construct a dict representation of a ControlSpecificationPrototype model
        control_specification_prototype_model = {}
        control_specification_prototype_model['component_id'] = 'apprapp'
        control_specification_prototype_model['environment'] = 'ibm-cloud'
        control_specification_prototype_model['control_specification_id'] = 'testString'
        control_specification_prototype_model['control_specification_description'] = 'This field is used to describe a control specification'
        control_specification_prototype_model['assessments'] = [assessment_prototype_model]

        # Construct a dict representation of a ControlDoc model
        control_doc_model = {}
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a ControlPrototype model
        control_prototype_model = {}
        control_prototype_model['control_name'] = 'security'
        control_prototype_model['control_description'] = 'This is a description of a control'
        control_prototype_model['control_category'] = 'test-control'
        control_prototype_model['control_requirement'] = True
        control_prototype_model['control_parent'] = 'testString'
        control_prototype_model['control_specifications'] = [control_specification_prototype_model]
        control_prototype_model['control_docs'] = control_doc_model
        control_prototype_model['status'] = 'disabled'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        control_library_id = 'testString'
        control_library_name = 'custom control library from SDK'
        control_library_description = 'This is a custom control library made from the SDK test framework'
        control_library_type = 'custom'
        control_library_version = '0.0.2'
        controls = [control_prototype_model]

        # Invoke method
        response = _service.replace_custom_control_library(
            instance_id,
            control_library_id,
            control_library_name,
            control_library_description,
            control_library_type,
            control_library_version,
            controls,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['control_library_name'] == 'custom control library from SDK'
        assert req_body['control_library_description'] == 'This is a custom control library made from the SDK test framework'
        assert req_body['control_library_type'] == 'custom'
        assert req_body['control_library_version'] == '0.0.2'
        assert req_body['controls'] == [control_prototype_model]

    def test_replace_custom_control_library_required_params_with_retries(self):
        # Enable retries and run test_replace_custom_control_library_required_params.
        _service.enable_retries()
        self.test_replace_custom_control_library_required_params()

        # Disable retries and run test_replace_custom_control_library_required_params.
        _service.disable_retries()
        self.test_replace_custom_control_library_required_params()

    @responses.activate
    def test_replace_custom_control_library_value_error(self):
        """
        test_replace_custom_control_library_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries/testString')
        mock_response = '{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AssessmentPrototype model
        assessment_prototype_model = {}
        assessment_prototype_model['assessment_id'] = 'rule-d1bd9f3f-bee1-46c5-9533-da8bba9eed4e'
        assessment_prototype_model['assessment_description'] = 'This rule will check on regulation'

        # Construct a dict representation of a ControlSpecificationPrototype model
        control_specification_prototype_model = {}
        control_specification_prototype_model['component_id'] = 'apprapp'
        control_specification_prototype_model['environment'] = 'ibm-cloud'
        control_specification_prototype_model['control_specification_id'] = 'testString'
        control_specification_prototype_model['control_specification_description'] = 'This field is used to describe a control specification'
        control_specification_prototype_model['assessments'] = [assessment_prototype_model]

        # Construct a dict representation of a ControlDoc model
        control_doc_model = {}
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a ControlPrototype model
        control_prototype_model = {}
        control_prototype_model['control_name'] = 'security'
        control_prototype_model['control_description'] = 'This is a description of a control'
        control_prototype_model['control_category'] = 'test-control'
        control_prototype_model['control_requirement'] = True
        control_prototype_model['control_parent'] = 'testString'
        control_prototype_model['control_specifications'] = [control_specification_prototype_model]
        control_prototype_model['control_docs'] = control_doc_model
        control_prototype_model['status'] = 'disabled'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        control_library_id = 'testString'
        control_library_name = 'custom control library from SDK'
        control_library_description = 'This is a custom control library made from the SDK test framework'
        control_library_type = 'custom'
        control_library_version = '0.0.2'
        controls = [control_prototype_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "control_library_id": control_library_id,
            "control_library_name": control_library_name,
            "control_library_description": control_library_description,
            "control_library_type": control_library_type,
            "control_library_version": control_library_version,
            "controls": controls,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_custom_control_library(**req_copy)

    def test_replace_custom_control_library_value_error_with_retries(self):
        # Enable retries and run test_replace_custom_control_library_value_error.
        _service.enable_retries()
        self.test_replace_custom_control_library_value_error()

        # Disable retries and run test_replace_custom_control_library_value_error.
        _service.disable_retries()
        self.test_replace_custom_control_library_value_error()


class TestGetControlLibrary:
    """
    Test Class for get_control_library
    """

    @responses.activate
    def test_get_control_library_all_params(self):
        """
        get_control_library()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries/testString')
        mock_response = '{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        control_library_id = 'testString'
        account_id = 'testString'

        # Invoke method
        response = _service.get_control_library(
            instance_id,
            control_library_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_get_control_library_all_params_with_retries(self):
        # Enable retries and run test_get_control_library_all_params.
        _service.enable_retries()
        self.test_get_control_library_all_params()

        # Disable retries and run test_get_control_library_all_params.
        _service.disable_retries()
        self.test_get_control_library_all_params()

    @responses.activate
    def test_get_control_library_required_params(self):
        """
        test_get_control_library_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries/testString')
        mock_response = '{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        control_library_id = 'testString'

        # Invoke method
        response = _service.get_control_library(
            instance_id,
            control_library_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_control_library_required_params_with_retries(self):
        # Enable retries and run test_get_control_library_required_params.
        _service.enable_retries()
        self.test_get_control_library_required_params()

        # Disable retries and run test_get_control_library_required_params.
        _service.disable_retries()
        self.test_get_control_library_required_params()

    @responses.activate
    def test_get_control_library_value_error(self):
        """
        test_get_control_library_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries/testString')
        mock_response = '{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        control_library_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "control_library_id": control_library_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_control_library(**req_copy)

    def test_get_control_library_value_error_with_retries(self):
        # Enable retries and run test_get_control_library_value_error.
        _service.enable_retries()
        self.test_get_control_library_value_error()

        # Disable retries and run test_get_control_library_value_error.
        _service.disable_retries()
        self.test_get_control_library_value_error()


class TestDeleteCustomControlLibrary:
    """
    Test Class for delete_custom_control_library
    """

    @responses.activate
    def test_delete_custom_control_library_all_params(self):
        """
        delete_custom_control_library()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries/testString')
        mock_response = '{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        control_library_id = 'testString'
        account_id = 'testString'

        # Invoke method
        response = _service.delete_custom_control_library(
            instance_id,
            control_library_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_delete_custom_control_library_all_params_with_retries(self):
        # Enable retries and run test_delete_custom_control_library_all_params.
        _service.enable_retries()
        self.test_delete_custom_control_library_all_params()

        # Disable retries and run test_delete_custom_control_library_all_params.
        _service.disable_retries()
        self.test_delete_custom_control_library_all_params()

    @responses.activate
    def test_delete_custom_control_library_required_params(self):
        """
        test_delete_custom_control_library_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries/testString')
        mock_response = '{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        control_library_id = 'testString'

        # Invoke method
        response = _service.delete_custom_control_library(
            instance_id,
            control_library_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_custom_control_library_required_params_with_retries(self):
        # Enable retries and run test_delete_custom_control_library_required_params.
        _service.enable_retries()
        self.test_delete_custom_control_library_required_params()

        # Disable retries and run test_delete_custom_control_library_required_params.
        _service.disable_retries()
        self.test_delete_custom_control_library_required_params()

    @responses.activate
    def test_delete_custom_control_library_value_error(self):
        """
        test_delete_custom_control_library_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/control_libraries/testString')
        mock_response = '{"control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "custom", "control_library_version": "control_library_version", "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "status"}], "id": "id", "account_id": "account_id", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        control_library_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "control_library_id": control_library_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_custom_control_library(**req_copy)

    def test_delete_custom_control_library_value_error_with_retries(self):
        # Enable retries and run test_delete_custom_control_library_value_error.
        _service.enable_retries()
        self.test_delete_custom_control_library_value_error()

        # Disable retries and run test_delete_custom_control_library_value_error.
        _service.disable_retries()
        self.test_delete_custom_control_library_value_error()


# endregion
##############################################################################
# End of Service: ControlLibrary
##############################################################################

##############################################################################
# Start of Service: Profile
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecurityAndComplianceCenterApiV3.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecurityAndComplianceCenterApiV3)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecurityAndComplianceCenterApiV3.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateProfile:
    """
    Test Class for create_profile
    """

    @responses.activate
    def test_create_profile_all_params(self):
        """
        create_profile()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles')
        mock_response = '{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProfileControlsPrototype model
        profile_controls_prototype_model = {}
        profile_controls_prototype_model['control_library_id'] = 'a046fb6b-aba5-4646-b190-a2c76241e7af'
        profile_controls_prototype_model['control_id'] = '60dae3b5-6104-4b3e-bac7-26cc7b741aca'

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'automated'
        default_parameters_model['assessment_id'] = 'rule-e16fcfea-fe21-4d30-a721-423611481fea'
        default_parameters_model['parameter_name'] = 'tls_version'
        default_parameters_model['parameter_default_value'] = '["1.2","1.3"]'
        default_parameters_model['parameter_display_name'] = 'IBM Cloud Internet Services TLS version'
        default_parameters_model['parameter_type'] = 'string_list'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_name = 'Example Profile'
        profile_version = '0.0.1'
        controls = [profile_controls_prototype_model]
        default_parameters = [default_parameters_model]
        profile_description = 'This profile is created as an example of the SDK gen'
        latest = True
        version_group_label = 'testString'
        account_id = 'testString'

        # Invoke method
        response = _service.create_profile(
            instance_id,
            profile_name,
            profile_version,
            controls,
            default_parameters,
            profile_description=profile_description,
            latest=latest,
            version_group_label=version_group_label,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['profile_name'] == 'Example Profile'
        assert req_body['profile_version'] == '0.0.1'
        assert req_body['controls'] == [profile_controls_prototype_model]
        assert req_body['default_parameters'] == [default_parameters_model]
        assert req_body['profile_description'] == 'This profile is created as an example of the SDK gen'
        assert req_body['latest'] == True
        assert req_body['version_group_label'] == 'testString'

    def test_create_profile_all_params_with_retries(self):
        # Enable retries and run test_create_profile_all_params.
        _service.enable_retries()
        self.test_create_profile_all_params()

        # Disable retries and run test_create_profile_all_params.
        _service.disable_retries()
        self.test_create_profile_all_params()

    @responses.activate
    def test_create_profile_required_params(self):
        """
        test_create_profile_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles')
        mock_response = '{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProfileControlsPrototype model
        profile_controls_prototype_model = {}
        profile_controls_prototype_model['control_library_id'] = 'a046fb6b-aba5-4646-b190-a2c76241e7af'
        profile_controls_prototype_model['control_id'] = '60dae3b5-6104-4b3e-bac7-26cc7b741aca'

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'automated'
        default_parameters_model['assessment_id'] = 'rule-e16fcfea-fe21-4d30-a721-423611481fea'
        default_parameters_model['parameter_name'] = 'tls_version'
        default_parameters_model['parameter_default_value'] = '["1.2","1.3"]'
        default_parameters_model['parameter_display_name'] = 'IBM Cloud Internet Services TLS version'
        default_parameters_model['parameter_type'] = 'string_list'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_name = 'Example Profile'
        profile_version = '0.0.1'
        controls = [profile_controls_prototype_model]
        default_parameters = [default_parameters_model]
        profile_description = 'This profile is created as an example of the SDK gen'
        latest = True
        version_group_label = 'testString'

        # Invoke method
        response = _service.create_profile(
            instance_id,
            profile_name,
            profile_version,
            controls,
            default_parameters,
            profile_description=profile_description,
            latest=latest,
            version_group_label=version_group_label,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['profile_name'] == 'Example Profile'
        assert req_body['profile_version'] == '0.0.1'
        assert req_body['controls'] == [profile_controls_prototype_model]
        assert req_body['default_parameters'] == [default_parameters_model]
        assert req_body['profile_description'] == 'This profile is created as an example of the SDK gen'
        assert req_body['latest'] == True
        assert req_body['version_group_label'] == 'testString'

    def test_create_profile_required_params_with_retries(self):
        # Enable retries and run test_create_profile_required_params.
        _service.enable_retries()
        self.test_create_profile_required_params()

        # Disable retries and run test_create_profile_required_params.
        _service.disable_retries()
        self.test_create_profile_required_params()

    @responses.activate
    def test_create_profile_value_error(self):
        """
        test_create_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles')
        mock_response = '{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProfileControlsPrototype model
        profile_controls_prototype_model = {}
        profile_controls_prototype_model['control_library_id'] = 'a046fb6b-aba5-4646-b190-a2c76241e7af'
        profile_controls_prototype_model['control_id'] = '60dae3b5-6104-4b3e-bac7-26cc7b741aca'

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'automated'
        default_parameters_model['assessment_id'] = 'rule-e16fcfea-fe21-4d30-a721-423611481fea'
        default_parameters_model['parameter_name'] = 'tls_version'
        default_parameters_model['parameter_default_value'] = '["1.2","1.3"]'
        default_parameters_model['parameter_display_name'] = 'IBM Cloud Internet Services TLS version'
        default_parameters_model['parameter_type'] = 'string_list'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_name = 'Example Profile'
        profile_version = '0.0.1'
        controls = [profile_controls_prototype_model]
        default_parameters = [default_parameters_model]
        profile_description = 'This profile is created as an example of the SDK gen'
        latest = True
        version_group_label = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_name": profile_name,
            "profile_version": profile_version,
            "controls": controls,
            "default_parameters": default_parameters,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_profile(**req_copy)

    def test_create_profile_value_error_with_retries(self):
        # Enable retries and run test_create_profile_value_error.
        _service.enable_retries()
        self.test_create_profile_value_error()

        # Disable retries and run test_create_profile_value_error.
        _service.disable_retries()
        self.test_create_profile_value_error()


class TestListProfiles:
    """
    Test Class for list_profiles
    """

    @responses.activate
    def test_list_profiles_all_params(self):
        """
        list_profiles()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "profiles": [{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        account_id = 'testString'
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_profiles(
            instance_id,
            account_id=account_id,
            limit=limit,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_profiles_all_params_with_retries(self):
        # Enable retries and run test_list_profiles_all_params.
        _service.enable_retries()
        self.test_list_profiles_all_params()

        # Disable retries and run test_list_profiles_all_params.
        _service.disable_retries()
        self.test_list_profiles_all_params()

    @responses.activate
    def test_list_profiles_required_params(self):
        """
        test_list_profiles_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "profiles": [{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Invoke method
        response = _service.list_profiles(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_profiles_required_params_with_retries(self):
        # Enable retries and run test_list_profiles_required_params.
        _service.enable_retries()
        self.test_list_profiles_required_params()

        # Disable retries and run test_list_profiles_required_params.
        _service.disable_retries()
        self.test_list_profiles_required_params()

    @responses.activate
    def test_list_profiles_value_error(self):
        """
        test_list_profiles_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "profiles": [{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_profiles(**req_copy)

    def test_list_profiles_value_error_with_retries(self):
        # Enable retries and run test_list_profiles_value_error.
        _service.enable_retries()
        self.test_list_profiles_value_error()

        # Disable retries and run test_list_profiles_value_error.
        _service.disable_retries()
        self.test_list_profiles_value_error()

    @responses.activate
    def test_list_profiles_with_pager_get_next(self):
        """
        test_list_profiles_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"profiles":[{"id":"id","profile_name":"profile_name","instance_id":"instance_id","hierarchy_enabled":false,"profile_description":"profile_description","profile_type":"custom","profile_version":"profile_version","version_group_label":"version_group_label","latest":true,"created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","controls_count":14,"attachments_count":17,"controls":[{"control_requirement":false,"control_library_id":"control_library_id","control_id":"control_id","control_library_version":"control_library_version","control_name":"control_name","control_description":"control_description","control_severity":"control_severity","control_category":"control_category","control_parent":"control_parent","control_docs":{"control_docs_id":"control_docs_id","control_docs_type":"control_docs_type"},"control_specifications":[{"id":"id","responsibility":"responsibility","component_id":"component_id","component_name":"component_name","component_type":"component_type","environment":"environment","description":"description","assessments_count":17,"assessments":[{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]}]}]}],"default_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"parameter_name","parameter_default_value":"parameter_default_value","parameter_display_name":"parameter_display_name","parameter_type":"parameter_type"}]}]}'
        mock_response2 = '{"total_count":2,"limit":1,"profiles":[{"id":"id","profile_name":"profile_name","instance_id":"instance_id","hierarchy_enabled":false,"profile_description":"profile_description","profile_type":"custom","profile_version":"profile_version","version_group_label":"version_group_label","latest":true,"created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","controls_count":14,"attachments_count":17,"controls":[{"control_requirement":false,"control_library_id":"control_library_id","control_id":"control_id","control_library_version":"control_library_version","control_name":"control_name","control_description":"control_description","control_severity":"control_severity","control_category":"control_category","control_parent":"control_parent","control_docs":{"control_docs_id":"control_docs_id","control_docs_type":"control_docs_type"},"control_specifications":[{"id":"id","responsibility":"responsibility","component_id":"component_id","component_name":"component_name","component_type":"component_type","environment":"environment","description":"description","assessments_count":17,"assessments":[{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]}]}]}],"default_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"parameter_name","parameter_default_value":"parameter_default_value","parameter_display_name":"parameter_display_name","parameter_type":"parameter_type"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = ProfilesPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_profiles_with_pager_get_all(self):
        """
        test_list_profiles_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"profiles":[{"id":"id","profile_name":"profile_name","instance_id":"instance_id","hierarchy_enabled":false,"profile_description":"profile_description","profile_type":"custom","profile_version":"profile_version","version_group_label":"version_group_label","latest":true,"created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","controls_count":14,"attachments_count":17,"controls":[{"control_requirement":false,"control_library_id":"control_library_id","control_id":"control_id","control_library_version":"control_library_version","control_name":"control_name","control_description":"control_description","control_severity":"control_severity","control_category":"control_category","control_parent":"control_parent","control_docs":{"control_docs_id":"control_docs_id","control_docs_type":"control_docs_type"},"control_specifications":[{"id":"id","responsibility":"responsibility","component_id":"component_id","component_name":"component_name","component_type":"component_type","environment":"environment","description":"description","assessments_count":17,"assessments":[{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]}]}]}],"default_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"parameter_name","parameter_default_value":"parameter_default_value","parameter_display_name":"parameter_display_name","parameter_type":"parameter_type"}]}]}'
        mock_response2 = '{"total_count":2,"limit":1,"profiles":[{"id":"id","profile_name":"profile_name","instance_id":"instance_id","hierarchy_enabled":false,"profile_description":"profile_description","profile_type":"custom","profile_version":"profile_version","version_group_label":"version_group_label","latest":true,"created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","controls_count":14,"attachments_count":17,"controls":[{"control_requirement":false,"control_library_id":"control_library_id","control_id":"control_id","control_library_version":"control_library_version","control_name":"control_name","control_description":"control_description","control_severity":"control_severity","control_category":"control_category","control_parent":"control_parent","control_docs":{"control_docs_id":"control_docs_id","control_docs_type":"control_docs_type"},"control_specifications":[{"id":"id","responsibility":"responsibility","component_id":"component_id","component_name":"component_name","component_type":"component_type","environment":"environment","description":"description","assessments_count":17,"assessments":[{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]}]}]}],"default_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"parameter_name","parameter_default_value":"parameter_default_value","parameter_display_name":"parameter_display_name","parameter_type":"parameter_type"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = ProfilesPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestReplaceProfile:
    """
    Test Class for replace_profile
    """

    @responses.activate
    def test_replace_profile_all_params(self):
        """
        replace_profile()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ControlDoc model
        control_doc_model = {}
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        # Construct a dict representation of a Assessment model
        assessment_model = {}
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        # Construct a dict representation of a ControlSpecification model
        control_specification_model = {}
        control_specification_model['id'] = 'testString'
        control_specification_model['responsibility'] = 'testString'
        control_specification_model['component_id'] = 'testString'
        control_specification_model['component_name'] = 'testString'
        control_specification_model['component_type'] = 'testString'
        control_specification_model['environment'] = 'testString'
        control_specification_model['description'] = 'testString'
        control_specification_model['assessments_count'] = 38
        control_specification_model['assessments'] = [assessment_model]

        # Construct a dict representation of a ProfileControls model
        profile_controls_model = {}
        profile_controls_model['control_requirement'] = True
        profile_controls_model['control_library_id'] = 'a046fb6b-aba5-4646-b190-a2c76241e7af'
        profile_controls_model['control_id'] = '60dae3b5-6104-4b3e-bac7-26cc7b741aca'
        profile_controls_model['control_library_version'] = 'testString'
        profile_controls_model['control_name'] = 'testString'
        profile_controls_model['control_description'] = 'testString'
        profile_controls_model['control_severity'] = 'testString'
        profile_controls_model['control_category'] = 'testString'
        profile_controls_model['control_parent'] = 'testString'
        profile_controls_model['control_docs'] = control_doc_model
        profile_controls_model['control_specifications'] = [control_specification_model]

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'automated'
        default_parameters_model['assessment_id'] = 'rule-e16fcfea-fe21-4d30-a721-423611481fea'
        default_parameters_model['parameter_name'] = 'tls_version'
        default_parameters_model['parameter_default_value'] = '["1.2","1.3"]'
        default_parameters_model['parameter_display_name'] = 'IBM Cloud Internet Services TLS version'
        default_parameters_model['parameter_type'] = 'string_list'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'
        new_profile_type = 'custom'
        new_controls = [profile_controls_model]
        new_default_parameters = [default_parameters_model]
        new_id = 'testString'
        new_profile_name = 'Example Profile Updated'
        new_instance_id = 'testString'
        new_hierarchy_enabled = True
        new_profile_description = 'This profile has been updated'
        new_profile_version = '0.0.2'
        new_version_group_label = 'testString'
        new_latest = True
        new_created_by = 'testString'
        new_created_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        new_updated_by = 'testString'
        new_updated_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        new_controls_count = 38
        new_attachments_count = 38
        account_id = 'testString'

        # Invoke method
        response = _service.replace_profile(
            instance_id,
            profile_id,
            new_profile_type,
            new_controls,
            new_default_parameters,
            new_id=new_id,
            new_profile_name=new_profile_name,
            new_instance_id=new_instance_id,
            new_hierarchy_enabled=new_hierarchy_enabled,
            new_profile_description=new_profile_description,
            new_profile_version=new_profile_version,
            new_version_group_label=new_version_group_label,
            new_latest=new_latest,
            new_created_by=new_created_by,
            new_created_on=new_created_on,
            new_updated_by=new_updated_by,
            new_updated_on=new_updated_on,
            new_controls_count=new_controls_count,
            new_attachments_count=new_attachments_count,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['profile_type'] == 'custom'
        assert req_body['controls'] == [profile_controls_model]
        assert req_body['default_parameters'] == [default_parameters_model]
        assert req_body['id'] == 'testString'
        assert req_body['profile_name'] == 'Example Profile Updated'
        assert req_body['instance_id'] == 'testString'
        assert req_body['hierarchy_enabled'] == True
        assert req_body['profile_description'] == 'This profile has been updated'
        assert req_body['profile_version'] == '0.0.2'
        assert req_body['version_group_label'] == 'testString'
        assert req_body['latest'] == True
        assert req_body['created_by'] == 'testString'
        assert req_body['created_on'] == '2019-01-01T12:00:00Z'
        assert req_body['updated_by'] == 'testString'
        assert req_body['updated_on'] == '2019-01-01T12:00:00Z'
        assert req_body['controls_count'] == 38
        assert req_body['attachments_count'] == 38

    def test_replace_profile_all_params_with_retries(self):
        # Enable retries and run test_replace_profile_all_params.
        _service.enable_retries()
        self.test_replace_profile_all_params()

        # Disable retries and run test_replace_profile_all_params.
        _service.disable_retries()
        self.test_replace_profile_all_params()

    @responses.activate
    def test_replace_profile_required_params(self):
        """
        test_replace_profile_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ControlDoc model
        control_doc_model = {}
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        # Construct a dict representation of a Assessment model
        assessment_model = {}
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        # Construct a dict representation of a ControlSpecification model
        control_specification_model = {}
        control_specification_model['id'] = 'testString'
        control_specification_model['responsibility'] = 'testString'
        control_specification_model['component_id'] = 'testString'
        control_specification_model['component_name'] = 'testString'
        control_specification_model['component_type'] = 'testString'
        control_specification_model['environment'] = 'testString'
        control_specification_model['description'] = 'testString'
        control_specification_model['assessments_count'] = 38
        control_specification_model['assessments'] = [assessment_model]

        # Construct a dict representation of a ProfileControls model
        profile_controls_model = {}
        profile_controls_model['control_requirement'] = True
        profile_controls_model['control_library_id'] = 'a046fb6b-aba5-4646-b190-a2c76241e7af'
        profile_controls_model['control_id'] = '60dae3b5-6104-4b3e-bac7-26cc7b741aca'
        profile_controls_model['control_library_version'] = 'testString'
        profile_controls_model['control_name'] = 'testString'
        profile_controls_model['control_description'] = 'testString'
        profile_controls_model['control_severity'] = 'testString'
        profile_controls_model['control_category'] = 'testString'
        profile_controls_model['control_parent'] = 'testString'
        profile_controls_model['control_docs'] = control_doc_model
        profile_controls_model['control_specifications'] = [control_specification_model]

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'automated'
        default_parameters_model['assessment_id'] = 'rule-e16fcfea-fe21-4d30-a721-423611481fea'
        default_parameters_model['parameter_name'] = 'tls_version'
        default_parameters_model['parameter_default_value'] = '["1.2","1.3"]'
        default_parameters_model['parameter_display_name'] = 'IBM Cloud Internet Services TLS version'
        default_parameters_model['parameter_type'] = 'string_list'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'
        new_profile_type = 'custom'
        new_controls = [profile_controls_model]
        new_default_parameters = [default_parameters_model]
        new_id = 'testString'
        new_profile_name = 'Example Profile Updated'
        new_instance_id = 'testString'
        new_hierarchy_enabled = True
        new_profile_description = 'This profile has been updated'
        new_profile_version = '0.0.2'
        new_version_group_label = 'testString'
        new_latest = True
        new_created_by = 'testString'
        new_created_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        new_updated_by = 'testString'
        new_updated_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        new_controls_count = 38
        new_attachments_count = 38

        # Invoke method
        response = _service.replace_profile(
            instance_id,
            profile_id,
            new_profile_type,
            new_controls,
            new_default_parameters,
            new_id=new_id,
            new_profile_name=new_profile_name,
            new_instance_id=new_instance_id,
            new_hierarchy_enabled=new_hierarchy_enabled,
            new_profile_description=new_profile_description,
            new_profile_version=new_profile_version,
            new_version_group_label=new_version_group_label,
            new_latest=new_latest,
            new_created_by=new_created_by,
            new_created_on=new_created_on,
            new_updated_by=new_updated_by,
            new_updated_on=new_updated_on,
            new_controls_count=new_controls_count,
            new_attachments_count=new_attachments_count,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['profile_type'] == 'custom'
        assert req_body['controls'] == [profile_controls_model]
        assert req_body['default_parameters'] == [default_parameters_model]
        assert req_body['id'] == 'testString'
        assert req_body['profile_name'] == 'Example Profile Updated'
        assert req_body['instance_id'] == 'testString'
        assert req_body['hierarchy_enabled'] == True
        assert req_body['profile_description'] == 'This profile has been updated'
        assert req_body['profile_version'] == '0.0.2'
        assert req_body['version_group_label'] == 'testString'
        assert req_body['latest'] == True
        assert req_body['created_by'] == 'testString'
        assert req_body['created_on'] == '2019-01-01T12:00:00Z'
        assert req_body['updated_by'] == 'testString'
        assert req_body['updated_on'] == '2019-01-01T12:00:00Z'
        assert req_body['controls_count'] == 38
        assert req_body['attachments_count'] == 38

    def test_replace_profile_required_params_with_retries(self):
        # Enable retries and run test_replace_profile_required_params.
        _service.enable_retries()
        self.test_replace_profile_required_params()

        # Disable retries and run test_replace_profile_required_params.
        _service.disable_retries()
        self.test_replace_profile_required_params()

    @responses.activate
    def test_replace_profile_value_error(self):
        """
        test_replace_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ControlDoc model
        control_doc_model = {}
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        # Construct a dict representation of a Assessment model
        assessment_model = {}
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        # Construct a dict representation of a ControlSpecification model
        control_specification_model = {}
        control_specification_model['id'] = 'testString'
        control_specification_model['responsibility'] = 'testString'
        control_specification_model['component_id'] = 'testString'
        control_specification_model['component_name'] = 'testString'
        control_specification_model['component_type'] = 'testString'
        control_specification_model['environment'] = 'testString'
        control_specification_model['description'] = 'testString'
        control_specification_model['assessments_count'] = 38
        control_specification_model['assessments'] = [assessment_model]

        # Construct a dict representation of a ProfileControls model
        profile_controls_model = {}
        profile_controls_model['control_requirement'] = True
        profile_controls_model['control_library_id'] = 'a046fb6b-aba5-4646-b190-a2c76241e7af'
        profile_controls_model['control_id'] = '60dae3b5-6104-4b3e-bac7-26cc7b741aca'
        profile_controls_model['control_library_version'] = 'testString'
        profile_controls_model['control_name'] = 'testString'
        profile_controls_model['control_description'] = 'testString'
        profile_controls_model['control_severity'] = 'testString'
        profile_controls_model['control_category'] = 'testString'
        profile_controls_model['control_parent'] = 'testString'
        profile_controls_model['control_docs'] = control_doc_model
        profile_controls_model['control_specifications'] = [control_specification_model]

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'automated'
        default_parameters_model['assessment_id'] = 'rule-e16fcfea-fe21-4d30-a721-423611481fea'
        default_parameters_model['parameter_name'] = 'tls_version'
        default_parameters_model['parameter_default_value'] = '["1.2","1.3"]'
        default_parameters_model['parameter_display_name'] = 'IBM Cloud Internet Services TLS version'
        default_parameters_model['parameter_type'] = 'string_list'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'
        new_profile_type = 'custom'
        new_controls = [profile_controls_model]
        new_default_parameters = [default_parameters_model]
        new_id = 'testString'
        new_profile_name = 'Example Profile Updated'
        new_instance_id = 'testString'
        new_hierarchy_enabled = True
        new_profile_description = 'This profile has been updated'
        new_profile_version = '0.0.2'
        new_version_group_label = 'testString'
        new_latest = True
        new_created_by = 'testString'
        new_created_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        new_updated_by = 'testString'
        new_updated_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        new_controls_count = 38
        new_attachments_count = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_id": profile_id,
            "new_profile_type": new_profile_type,
            "new_controls": new_controls,
            "new_default_parameters": new_default_parameters,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_profile(**req_copy)

    def test_replace_profile_value_error_with_retries(self):
        # Enable retries and run test_replace_profile_value_error.
        _service.enable_retries()
        self.test_replace_profile_value_error()

        # Disable retries and run test_replace_profile_value_error.
        _service.disable_retries()
        self.test_replace_profile_value_error()


class TestGetProfile:
    """
    Test Class for get_profile
    """

    @responses.activate
    def test_get_profile_all_params(self):
        """
        get_profile()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'
        account_id = 'testString'

        # Invoke method
        response = _service.get_profile(
            instance_id,
            profile_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_get_profile_all_params_with_retries(self):
        # Enable retries and run test_get_profile_all_params.
        _service.enable_retries()
        self.test_get_profile_all_params()

        # Disable retries and run test_get_profile_all_params.
        _service.disable_retries()
        self.test_get_profile_all_params()

    @responses.activate
    def test_get_profile_required_params(self):
        """
        test_get_profile_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'

        # Invoke method
        response = _service.get_profile(
            instance_id,
            profile_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_profile_required_params_with_retries(self):
        # Enable retries and run test_get_profile_required_params.
        _service.enable_retries()
        self.test_get_profile_required_params()

        # Disable retries and run test_get_profile_required_params.
        _service.disable_retries()
        self.test_get_profile_required_params()

    @responses.activate
    def test_get_profile_value_error(self):
        """
        test_get_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_profile(**req_copy)

    def test_get_profile_value_error_with_retries(self):
        # Enable retries and run test_get_profile_value_error.
        _service.enable_retries()
        self.test_get_profile_value_error()

        # Disable retries and run test_get_profile_value_error.
        _service.disable_retries()
        self.test_get_profile_value_error()


class TestDeleteCustomProfile:
    """
    Test Class for delete_custom_profile
    """

    @responses.activate
    def test_delete_custom_profile_all_params(self):
        """
        delete_custom_profile()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'
        account_id = 'testString'

        # Invoke method
        response = _service.delete_custom_profile(
            instance_id,
            profile_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_delete_custom_profile_all_params_with_retries(self):
        # Enable retries and run test_delete_custom_profile_all_params.
        _service.enable_retries()
        self.test_delete_custom_profile_all_params()

        # Disable retries and run test_delete_custom_profile_all_params.
        _service.disable_retries()
        self.test_delete_custom_profile_all_params()

    @responses.activate
    def test_delete_custom_profile_required_params(self):
        """
        test_delete_custom_profile_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'

        # Invoke method
        response = _service.delete_custom_profile(
            instance_id,
            profile_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_custom_profile_required_params_with_retries(self):
        # Enable retries and run test_delete_custom_profile_required_params.
        _service.enable_retries()
        self.test_delete_custom_profile_required_params()

        # Disable retries and run test_delete_custom_profile_required_params.
        _service.disable_retries()
        self.test_delete_custom_profile_required_params()

    @responses.activate
    def test_delete_custom_profile_value_error(self):
        """
        test_delete_custom_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "instance_id": "instance_id", "hierarchy_enabled": false, "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17, "controls": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_custom_profile(**req_copy)

    def test_delete_custom_profile_value_error_with_retries(self):
        # Enable retries and run test_delete_custom_profile_value_error.
        _service.enable_retries()
        self.test_delete_custom_profile_value_error()

        # Disable retries and run test_delete_custom_profile_value_error.
        _service.disable_retries()
        self.test_delete_custom_profile_value_error()


class TestReplaceProfileParameters:
    """
    Test Class for replace_profile_parameters
    """

    @responses.activate
    def test_replace_profile_parameters_all_params(self):
        """
        replace_profile_parameters()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString/parameters')
        mock_response = '{"id": "id", "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'testString'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'
        default_parameters = [default_parameters_model]
        id = 'testString'
        account_id = 'testString'

        # Invoke method
        response = _service.replace_profile_parameters(
            instance_id,
            profile_id,
            default_parameters,
            id=id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['default_parameters'] == [default_parameters_model]
        assert req_body['id'] == 'testString'

    def test_replace_profile_parameters_all_params_with_retries(self):
        # Enable retries and run test_replace_profile_parameters_all_params.
        _service.enable_retries()
        self.test_replace_profile_parameters_all_params()

        # Disable retries and run test_replace_profile_parameters_all_params.
        _service.disable_retries()
        self.test_replace_profile_parameters_all_params()

    @responses.activate
    def test_replace_profile_parameters_required_params(self):
        """
        test_replace_profile_parameters_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString/parameters')
        mock_response = '{"id": "id", "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'testString'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'
        default_parameters = [default_parameters_model]
        id = 'testString'

        # Invoke method
        response = _service.replace_profile_parameters(
            instance_id,
            profile_id,
            default_parameters,
            id=id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['default_parameters'] == [default_parameters_model]
        assert req_body['id'] == 'testString'

    def test_replace_profile_parameters_required_params_with_retries(self):
        # Enable retries and run test_replace_profile_parameters_required_params.
        _service.enable_retries()
        self.test_replace_profile_parameters_required_params()

        # Disable retries and run test_replace_profile_parameters_required_params.
        _service.disable_retries()
        self.test_replace_profile_parameters_required_params()

    @responses.activate
    def test_replace_profile_parameters_value_error(self):
        """
        test_replace_profile_parameters_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString/parameters')
        mock_response = '{"id": "id", "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'testString'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'
        default_parameters = [default_parameters_model]
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_id": profile_id,
            "default_parameters": default_parameters,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_profile_parameters(**req_copy)

    def test_replace_profile_parameters_value_error_with_retries(self):
        # Enable retries and run test_replace_profile_parameters_value_error.
        _service.enable_retries()
        self.test_replace_profile_parameters_value_error()

        # Disable retries and run test_replace_profile_parameters_value_error.
        _service.disable_retries()
        self.test_replace_profile_parameters_value_error()


class TestListProfileParameters:
    """
    Test Class for list_profile_parameters
    """

    @responses.activate
    def test_list_profile_parameters_all_params(self):
        """
        list_profile_parameters()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString/parameters')
        mock_response = '{"id": "id", "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'

        # Invoke method
        response = _service.list_profile_parameters(
            instance_id,
            profile_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_profile_parameters_all_params_with_retries(self):
        # Enable retries and run test_list_profile_parameters_all_params.
        _service.enable_retries()
        self.test_list_profile_parameters_all_params()

        # Disable retries and run test_list_profile_parameters_all_params.
        _service.disable_retries()
        self.test_list_profile_parameters_all_params()

    @responses.activate
    def test_list_profile_parameters_value_error(self):
        """
        test_list_profile_parameters_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/testString/parameters')
        mock_response = '{"id": "id", "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_profile_parameters(**req_copy)

    def test_list_profile_parameters_value_error_with_retries(self):
        # Enable retries and run test_list_profile_parameters_value_error.
        _service.enable_retries()
        self.test_list_profile_parameters_value_error()

        # Disable retries and run test_list_profile_parameters_value_error.
        _service.disable_retries()
        self.test_list_profile_parameters_value_error()


class TestCompareProfiles:
    """
    Test Class for compare_profiles
    """

    @responses.activate
    def test_compare_profiles_all_params(self):
        """
        compare_profiles()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/2f598907-970d-4d52-9071-5cc95912f55e/compare')
        mock_response = '{"current_predefined_version": {"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14}, "latest_predefined_version": {"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14}, "controls_changes": {"total_added": 11, "total_removed": 13, "total_updated": 13, "added": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "removed": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "updated": [{"current": {"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}, "latest": {"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}}]}, "default_parameters_changes": {"total_added": 11, "total_removed": 13, "total_updated": 13, "added": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}], "removed": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}], "updated": [{"current": {"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}, "latest": {"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '2f598907-970d-4d52-9071-5cc95912f55e'
        account_id = 'testString'

        # Invoke method
        response = _service.compare_profiles(
            instance_id,
            profile_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_compare_profiles_all_params_with_retries(self):
        # Enable retries and run test_compare_profiles_all_params.
        _service.enable_retries()
        self.test_compare_profiles_all_params()

        # Disable retries and run test_compare_profiles_all_params.
        _service.disable_retries()
        self.test_compare_profiles_all_params()

    @responses.activate
    def test_compare_profiles_required_params(self):
        """
        test_compare_profiles_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/2f598907-970d-4d52-9071-5cc95912f55e/compare')
        mock_response = '{"current_predefined_version": {"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14}, "latest_predefined_version": {"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14}, "controls_changes": {"total_added": 11, "total_removed": 13, "total_updated": 13, "added": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "removed": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "updated": [{"current": {"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}, "latest": {"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}}]}, "default_parameters_changes": {"total_added": 11, "total_removed": 13, "total_updated": 13, "added": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}], "removed": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}], "updated": [{"current": {"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}, "latest": {"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '2f598907-970d-4d52-9071-5cc95912f55e'

        # Invoke method
        response = _service.compare_profiles(
            instance_id,
            profile_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_compare_profiles_required_params_with_retries(self):
        # Enable retries and run test_compare_profiles_required_params.
        _service.enable_retries()
        self.test_compare_profiles_required_params()

        # Disable retries and run test_compare_profiles_required_params.
        _service.disable_retries()
        self.test_compare_profiles_required_params()

    @responses.activate
    def test_compare_profiles_value_error(self):
        """
        test_compare_profiles_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/2f598907-970d-4d52-9071-5cc95912f55e/compare')
        mock_response = '{"current_predefined_version": {"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14}, "latest_predefined_version": {"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "custom", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14}, "controls_changes": {"total_added": 11, "total_removed": 13, "total_updated": 13, "added": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "removed": [{"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "updated": [{"current": {"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}, "latest": {"control_requirement": false, "control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "responsibility", "component_id": "component_id", "component_name": "component_name", "component_type": "component_type", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}}]}, "default_parameters_changes": {"total_added": 11, "total_removed": 13, "total_updated": 13, "added": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}], "removed": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}], "updated": [{"current": {"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}, "latest": {"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "parameter_type"}}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '2f598907-970d-4d52-9071-5cc95912f55e'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.compare_profiles(**req_copy)

    def test_compare_profiles_value_error_with_retries(self):
        # Enable retries and run test_compare_profiles_value_error.
        _service.enable_retries()
        self.test_compare_profiles_value_error()

        # Disable retries and run test_compare_profiles_value_error.
        _service.disable_retries()
        self.test_compare_profiles_value_error()


class TestListProfileAttachments:
    """
    Test Class for list_profile_attachments
    """

    @responses.activate
    def test_list_profile_attachments_all_params(self):
        """
        list_profile_attachments()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "attachments": [{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'
        account_id = 'testString'

        # Invoke method
        response = _service.list_profile_attachments(
            instance_id,
            profile_id,
            account_id=account_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string

    def test_list_profile_attachments_all_params_with_retries(self):
        # Enable retries and run test_list_profile_attachments_all_params.
        _service.enable_retries()
        self.test_list_profile_attachments_all_params()

        # Disable retries and run test_list_profile_attachments_all_params.
        _service.disable_retries()
        self.test_list_profile_attachments_all_params()

    @responses.activate
    def test_list_profile_attachments_required_params(self):
        """
        test_list_profile_attachments_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "attachments": [{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'

        # Invoke method
        response = _service.list_profile_attachments(
            instance_id,
            profile_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_profile_attachments_required_params_with_retries(self):
        # Enable retries and run test_list_profile_attachments_required_params.
        _service.enable_retries()
        self.test_list_profile_attachments_required_params()

        # Disable retries and run test_list_profile_attachments_required_params.
        _service.disable_retries()
        self.test_list_profile_attachments_required_params()

    @responses.activate
    def test_list_profile_attachments_value_error(self):
        """
        test_list_profile_attachments_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/profiles/9c265b4a-4cdf-47f1-acd3-17b5808f7f3f/attachments')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "attachments": [{"attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "description": "description", "name": "name", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}, "schedule": "daily", "scope": [{"id": "id"}], "status": "enabled", "data_selection_range": {"start_date": "2025-02-28T05:42:58.000Z", "end_date": "2025-02-28T05:42:58.000Z"}, "account_id": "account_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "id": "id", "instance_id": "instance_id", "last_scan": {"id": "id", "status": "status", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "profile_id": "profile_id", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        profile_id = '9c265b4a-4cdf-47f1-acd3-17b5808f7f3f'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "profile_id": profile_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_profile_attachments(**req_copy)

    def test_list_profile_attachments_value_error_with_retries(self):
        # Enable retries and run test_list_profile_attachments_value_error.
        _service.enable_retries()
        self.test_list_profile_attachments_value_error()

        # Disable retries and run test_list_profile_attachments_value_error.
        _service.disable_retries()
        self.test_list_profile_attachments_value_error()


# endregion
##############################################################################
# End of Service: Profile
##############################################################################

##############################################################################
# Start of Service: Scope
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecurityAndComplianceCenterApiV3.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecurityAndComplianceCenterApiV3)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecurityAndComplianceCenterApiV3.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateScope:
    """
    Test Class for create_scope
    """

    @responses.activate
    def test_create_scope_all_params(self):
        """
        create_scope()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes')
        mock_response = '{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ScopePropertyScopeAny model
        scope_property_model = {}
        scope_property_model['name'] = 'scope_id'
        scope_property_model['value'] = 'ff88f007f9ff4622aac4fbc0eda36255'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        name = 'ibm scope'
        description = 'The scope that is defined for IBM resources.'
        environment = 'ibm-cloud'
        properties = [scope_property_model]

        # Invoke method
        response = _service.create_scope(
            instance_id,
            name=name,
            description=description,
            environment=environment,
            properties=properties,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'ibm scope'
        assert req_body['description'] == 'The scope that is defined for IBM resources.'
        assert req_body['environment'] == 'ibm-cloud'
        assert req_body['properties'] == [scope_property_model]

    def test_create_scope_all_params_with_retries(self):
        # Enable retries and run test_create_scope_all_params.
        _service.enable_retries()
        self.test_create_scope_all_params()

        # Disable retries and run test_create_scope_all_params.
        _service.disable_retries()
        self.test_create_scope_all_params()

    @responses.activate
    def test_create_scope_value_error(self):
        """
        test_create_scope_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes')
        mock_response = '{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ScopePropertyScopeAny model
        scope_property_model = {}
        scope_property_model['name'] = 'scope_id'
        scope_property_model['value'] = 'ff88f007f9ff4622aac4fbc0eda36255'

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        name = 'ibm scope'
        description = 'The scope that is defined for IBM resources.'
        environment = 'ibm-cloud'
        properties = [scope_property_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_scope(**req_copy)

    def test_create_scope_value_error_with_retries(self):
        # Enable retries and run test_create_scope_value_error.
        _service.enable_retries()
        self.test_create_scope_value_error()

        # Disable retries and run test_create_scope_value_error.
        _service.disable_retries()
        self.test_create_scope_value_error()


class TestListScopes:
    """
    Test Class for list_scopes
    """

    @responses.activate
    def test_list_scopes_all_params(self):
        """
        list_scopes()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "scopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        limit = 50
        start = 'testString'
        name = 'testString'
        description = 'testString'
        environment = 'testString'

        # Invoke method
        response = _service.list_scopes(
            instance_id,
            limit=limit,
            start=start,
            name=name,
            description=description,
            environment=environment,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'description={}'.format(description) in query_string
        assert 'environment={}'.format(environment) in query_string

    def test_list_scopes_all_params_with_retries(self):
        # Enable retries and run test_list_scopes_all_params.
        _service.enable_retries()
        self.test_list_scopes_all_params()

        # Disable retries and run test_list_scopes_all_params.
        _service.disable_retries()
        self.test_list_scopes_all_params()

    @responses.activate
    def test_list_scopes_required_params(self):
        """
        test_list_scopes_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "scopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Invoke method
        response = _service.list_scopes(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_scopes_required_params_with_retries(self):
        # Enable retries and run test_list_scopes_required_params.
        _service.enable_retries()
        self.test_list_scopes_required_params()

        # Disable retries and run test_list_scopes_required_params.
        _service.disable_retries()
        self.test_list_scopes_required_params()

    @responses.activate
    def test_list_scopes_value_error(self):
        """
        test_list_scopes_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "scopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_scopes(**req_copy)

    def test_list_scopes_value_error_with_retries(self):
        # Enable retries and run test_list_scopes_value_error.
        _service.enable_retries()
        self.test_list_scopes_value_error()

        # Disable retries and run test_list_scopes_value_error.
        _service.disable_retries()
        self.test_list_scopes_value_error()

    @responses.activate
    def test_list_scopes_with_pager_get_next(self):
        """
        test_list_scopes_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"scopes":[{"id":"id","name":"name","description":"description","environment":"environment","properties":[{"name":"name","value":"anyValue"}],"account_id":"account_id","instance_id":"instance_id","created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","attachment_count":16}]}'
        mock_response2 = '{"total_count":2,"limit":1,"scopes":[{"id":"id","name":"name","description":"description","environment":"environment","properties":[{"name":"name","value":"anyValue"}],"account_id":"account_id","instance_id":"instance_id","created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","attachment_count":16}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = ScopesPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            limit=10,
            name='testString',
            description='testString',
            environment='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_scopes_with_pager_get_all(self):
        """
        test_list_scopes_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"scopes":[{"id":"id","name":"name","description":"description","environment":"environment","properties":[{"name":"name","value":"anyValue"}],"account_id":"account_id","instance_id":"instance_id","created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","attachment_count":16}]}'
        mock_response2 = '{"total_count":2,"limit":1,"scopes":[{"id":"id","name":"name","description":"description","environment":"environment","properties":[{"name":"name","value":"anyValue"}],"account_id":"account_id","instance_id":"instance_id","created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","attachment_count":16}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = ScopesPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            limit=10,
            name='testString',
            description='testString',
            environment='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestUpdateScope:
    """
    Test Class for update_scope
    """

    @responses.activate
    def test_update_scope_all_params(self):
        """
        update_scope()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'
        name = 'updated name of scope'
        description = 'updated scope description'

        # Invoke method
        response = _service.update_scope(
            instance_id,
            scope_id,
            name=name,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'updated name of scope'
        assert req_body['description'] == 'updated scope description'

    def test_update_scope_all_params_with_retries(self):
        # Enable retries and run test_update_scope_all_params.
        _service.enable_retries()
        self.test_update_scope_all_params()

        # Disable retries and run test_update_scope_all_params.
        _service.disable_retries()
        self.test_update_scope_all_params()

    @responses.activate
    def test_update_scope_value_error(self):
        """
        test_update_scope_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'
        name = 'updated name of scope'
        description = 'updated scope description'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "scope_id": scope_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_scope(**req_copy)

    def test_update_scope_value_error_with_retries(self):
        # Enable retries and run test_update_scope_value_error.
        _service.enable_retries()
        self.test_update_scope_value_error()

        # Disable retries and run test_update_scope_value_error.
        _service.disable_retries()
        self.test_update_scope_value_error()


class TestGetScope:
    """
    Test Class for get_scope
    """

    @responses.activate
    def test_get_scope_all_params(self):
        """
        get_scope()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'

        # Invoke method
        response = _service.get_scope(
            instance_id,
            scope_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_scope_all_params_with_retries(self):
        # Enable retries and run test_get_scope_all_params.
        _service.enable_retries()
        self.test_get_scope_all_params()

        # Disable retries and run test_get_scope_all_params.
        _service.disable_retries()
        self.test_get_scope_all_params()

    @responses.activate
    def test_get_scope_value_error(self):
        """
        test_get_scope_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "scope_id": scope_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_scope(**req_copy)

    def test_get_scope_value_error_with_retries(self):
        # Enable retries and run test_get_scope_value_error.
        _service.enable_retries()
        self.test_get_scope_value_error()

        # Disable retries and run test_get_scope_value_error.
        _service.disable_retries()
        self.test_get_scope_value_error()


class TestDeleteScope:
    """
    Test Class for delete_scope
    """

    @responses.activate
    def test_delete_scope_all_params(self):
        """
        delete_scope()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'

        # Invoke method
        response = _service.delete_scope(
            instance_id,
            scope_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_scope_all_params_with_retries(self):
        # Enable retries and run test_delete_scope_all_params.
        _service.enable_retries()
        self.test_delete_scope_all_params()

        # Disable retries and run test_delete_scope_all_params.
        _service.disable_retries()
        self.test_delete_scope_all_params()

    @responses.activate
    def test_delete_scope_value_error(self):
        """
        test_delete_scope_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "scope_id": scope_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_scope(**req_copy)

    def test_delete_scope_value_error_with_retries(self):
        # Enable retries and run test_delete_scope_value_error.
        _service.enable_retries()
        self.test_delete_scope_value_error()

        # Disable retries and run test_delete_scope_value_error.
        _service.disable_retries()
        self.test_delete_scope_value_error()


class TestCreateSubscope:
    """
    Test Class for create_subscope
    """

    @responses.activate
    def test_create_subscope_all_params(self):
        """
        create_subscope()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes')
        mock_response = '{"subscopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ScopePropertyScopeAny model
        scope_property_model = {}
        scope_property_model['name'] = 'scope_id'
        scope_property_model['value'] = '1f689f08ec9b47b885c2659c17029581'

        # Construct a dict representation of a ScopePrototype model
        scope_prototype_model = {}
        scope_prototype_model['name'] = 'ibm subscope update'
        scope_prototype_model['description'] = 'The subscope that is defined for IBM resources.'
        scope_prototype_model['environment'] = 'ibm-cloud'
        scope_prototype_model['properties'] = [scope_property_model]

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'
        subscopes = [scope_prototype_model]

        # Invoke method
        response = _service.create_subscope(
            instance_id,
            scope_id,
            subscopes,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['subscopes'] == [scope_prototype_model]

    def test_create_subscope_all_params_with_retries(self):
        # Enable retries and run test_create_subscope_all_params.
        _service.enable_retries()
        self.test_create_subscope_all_params()

        # Disable retries and run test_create_subscope_all_params.
        _service.disable_retries()
        self.test_create_subscope_all_params()

    @responses.activate
    def test_create_subscope_value_error(self):
        """
        test_create_subscope_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes')
        mock_response = '{"subscopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ScopePropertyScopeAny model
        scope_property_model = {}
        scope_property_model['name'] = 'scope_id'
        scope_property_model['value'] = '1f689f08ec9b47b885c2659c17029581'

        # Construct a dict representation of a ScopePrototype model
        scope_prototype_model = {}
        scope_prototype_model['name'] = 'ibm subscope update'
        scope_prototype_model['description'] = 'The subscope that is defined for IBM resources.'
        scope_prototype_model['environment'] = 'ibm-cloud'
        scope_prototype_model['properties'] = [scope_property_model]

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'
        subscopes = [scope_prototype_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "scope_id": scope_id,
            "subscopes": subscopes,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_subscope(**req_copy)

    def test_create_subscope_value_error_with_retries(self):
        # Enable retries and run test_create_subscope_value_error.
        _service.enable_retries()
        self.test_create_subscope_value_error()

        # Disable retries and run test_create_subscope_value_error.
        _service.disable_retries()
        self.test_create_subscope_value_error()


class TestListSubscopes:
    """
    Test Class for list_subscopes
    """

    @responses.activate
    def test_list_subscopes_all_params(self):
        """
        list_subscopes()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "subscopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'
        limit = 50
        start = 'testString'
        name = 'testString'
        description = 'testString'
        environment = 'testString'

        # Invoke method
        response = _service.list_subscopes(
            instance_id,
            scope_id,
            limit=limit,
            start=start,
            name=name,
            description=description,
            environment=environment,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'description={}'.format(description) in query_string
        assert 'environment={}'.format(environment) in query_string

    def test_list_subscopes_all_params_with_retries(self):
        # Enable retries and run test_list_subscopes_all_params.
        _service.enable_retries()
        self.test_list_subscopes_all_params()

        # Disable retries and run test_list_subscopes_all_params.
        _service.disable_retries()
        self.test_list_subscopes_all_params()

    @responses.activate
    def test_list_subscopes_required_params(self):
        """
        test_list_subscopes_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "subscopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'

        # Invoke method
        response = _service.list_subscopes(
            instance_id,
            scope_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_subscopes_required_params_with_retries(self):
        # Enable retries and run test_list_subscopes_required_params.
        _service.enable_retries()
        self.test_list_subscopes_required_params()

        # Disable retries and run test_list_subscopes_required_params.
        _service.disable_retries()
        self.test_list_subscopes_required_params()

    @responses.activate
    def test_list_subscopes_value_error(self):
        """
        test_list_subscopes_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "subscopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "scope_id": scope_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_subscopes(**req_copy)

    def test_list_subscopes_value_error_with_retries(self):
        # Enable retries and run test_list_subscopes_value_error.
        _service.enable_retries()
        self.test_list_subscopes_value_error()

        # Disable retries and run test_list_subscopes_value_error.
        _service.disable_retries()
        self.test_list_subscopes_value_error()

    @responses.activate
    def test_list_subscopes_with_pager_get_next(self):
        """
        test_list_subscopes_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes')
        mock_response1 = '{"next":{"start":"1"},"subscopes":[{"id":"id","name":"name","description":"description","environment":"environment","properties":[{"name":"name","value":"anyValue"}]}],"total_count":2,"limit":1}'
        mock_response2 = '{"subscopes":[{"id":"id","name":"name","description":"description","environment":"environment","properties":[{"name":"name","value":"anyValue"}]}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = SubscopesPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id='testString',
            limit=10,
            name='testString',
            description='testString',
            environment='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_subscopes_with_pager_get_all(self):
        """
        test_list_subscopes_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes')
        mock_response1 = '{"next":{"start":"1"},"subscopes":[{"id":"id","name":"name","description":"description","environment":"environment","properties":[{"name":"name","value":"anyValue"}]}],"total_count":2,"limit":1}'
        mock_response2 = '{"subscopes":[{"id":"id","name":"name","description":"description","environment":"environment","properties":[{"name":"name","value":"anyValue"}]}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = SubscopesPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id='testString',
            limit=10,
            name='testString',
            description='testString',
            environment='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetSubscope:
    """
    Test Class for get_subscope
    """

    @responses.activate
    def test_get_subscope_all_params(self):
        """
        get_subscope()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'
        subscope_id = 'testString'

        # Invoke method
        response = _service.get_subscope(
            instance_id,
            scope_id,
            subscope_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_subscope_all_params_with_retries(self):
        # Enable retries and run test_get_subscope_all_params.
        _service.enable_retries()
        self.test_get_subscope_all_params()

        # Disable retries and run test_get_subscope_all_params.
        _service.disable_retries()
        self.test_get_subscope_all_params()

    @responses.activate
    def test_get_subscope_value_error(self):
        """
        test_get_subscope_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'
        subscope_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "scope_id": scope_id,
            "subscope_id": subscope_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_subscope(**req_copy)

    def test_get_subscope_value_error_with_retries(self):
        # Enable retries and run test_get_subscope_value_error.
        _service.enable_retries()
        self.test_get_subscope_value_error()

        # Disable retries and run test_get_subscope_value_error.
        _service.disable_retries()
        self.test_get_subscope_value_error()


class TestUpdateSubscope:
    """
    Test Class for update_subscope
    """

    @responses.activate
    def test_update_subscope_all_params(self):
        """
        update_subscope()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'
        subscope_id = 'testString'
        name = 'updated name of scope'
        description = 'updated scope description'

        # Invoke method
        response = _service.update_subscope(
            instance_id,
            scope_id,
            subscope_id,
            name=name,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'updated name of scope'
        assert req_body['description'] == 'updated scope description'

    def test_update_subscope_all_params_with_retries(self):
        # Enable retries and run test_update_subscope_all_params.
        _service.enable_retries()
        self.test_update_subscope_all_params()

        # Disable retries and run test_update_subscope_all_params.
        _service.disable_retries()
        self.test_update_subscope_all_params()

    @responses.activate
    def test_update_subscope_value_error(self):
        """
        test_update_subscope_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'
        subscope_id = 'testString'
        name = 'updated name of scope'
        description = 'updated scope description'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "scope_id": scope_id,
            "subscope_id": subscope_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_subscope(**req_copy)

    def test_update_subscope_value_error_with_retries(self):
        # Enable retries and run test_update_subscope_value_error.
        _service.enable_retries()
        self.test_update_subscope_value_error()

        # Disable retries and run test_update_subscope_value_error.
        _service.disable_retries()
        self.test_update_subscope_value_error()


class TestDeleteSubscope:
    """
    Test Class for delete_subscope
    """

    @responses.activate
    def test_delete_subscope_all_params(self):
        """
        delete_subscope()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'
        subscope_id = 'testString'

        # Invoke method
        response = _service.delete_subscope(
            instance_id,
            scope_id,
            subscope_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_subscope_all_params_with_retries(self):
        # Enable retries and run test_delete_subscope_all_params.
        _service.enable_retries()
        self.test_delete_subscope_all_params()

        # Disable retries and run test_delete_subscope_all_params.
        _service.disable_retries()
        self.test_delete_subscope_all_params()

    @responses.activate
    def test_delete_subscope_value_error(self):
        """
        test_delete_subscope_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/scopes/testString/subscopes/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'
        subscope_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "scope_id": scope_id,
            "subscope_id": subscope_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_subscope(**req_copy)

    def test_delete_subscope_value_error_with_retries(self):
        # Enable retries and run test_delete_subscope_value_error.
        _service.enable_retries()
        self.test_delete_subscope_value_error()

        # Disable retries and run test_delete_subscope_value_error.
        _service.disable_retries()
        self.test_delete_subscope_value_error()


# endregion
##############################################################################
# End of Service: Scope
##############################################################################

##############################################################################
# Start of Service: Target
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecurityAndComplianceCenterApiV3.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecurityAndComplianceCenterApiV3)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecurityAndComplianceCenterApiV3.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateTarget:
    """
    Test Class for create_target
    """

    @responses.activate
    def test_create_target_all_params(self):
        """
        create_target()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/targets')
        mock_response = '{"id": "a2366444-ad87-40b1-81d0-476df1cc1f18", "account_id": "be200c80cabc456e91139e4152327823", "trusted_profile_id": "Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3", "name": "Target Account-A", "credentials": [{"type": "iam_credentials", "secret_crn": "secret_crn", "secret_name": "my secret", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135, "service_name": "pm-20", "instance_crn": "instance_crn"}]}], "created_by": "IBMid-270007EPPC", "created_on": "2024-02-07T05:42:58.000Z", "updated_by": "IBMid-270007EPPC", "updated_on": "2024-02-07T05:42:58.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a Account model
        account_model = {}
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        # Construct a dict representation of a Tags model
        tags_model = {}
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        resource_model['home_account_id'] = '2411ffdc16844b07b42521c3443f456d'
        resource_model['id'] = 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::'
        resource_model['resource_name'] = 'jeff\'s key'
        resource_model['account'] = account_model
        resource_model['component_id'] = 'cloud-object_storage'
        resource_model['component_name'] = 'cloud-object_storage'
        resource_model['environment'] = 'ibm cloud'
        resource_model['tags'] = tags_model
        resource_model['status'] = 'compliant'
        resource_model['total_count'] = 140
        resource_model['pass_count'] = 123
        resource_model['failure_count'] = 12
        resource_model['error_count'] = 5
        resource_model['skipped_count'] = 7
        resource_model['completed_count'] = 135
        resource_model['service_name'] = 'pm-20'
        resource_model['instance_crn'] = 'testString'

        # Construct a dict representation of a Credential model
        credential_model = {}
        credential_model['secret_crn'] = 'testString'
        credential_model['resources'] = [resource_model]

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        account_id = '62ecf99b240144dea9125666249edfcb'
        trusted_profile_id = 'Profile-cb2c1829-9a8d-4218-b9cd-9f83fc814e54'
        name = 'Target for IBM account'
        credentials = [credential_model]

        # Invoke method
        response = _service.create_target(
            instance_id,
            account_id,
            trusted_profile_id,
            name,
            credentials=credentials,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == '62ecf99b240144dea9125666249edfcb'
        assert req_body['trusted_profile_id'] == 'Profile-cb2c1829-9a8d-4218-b9cd-9f83fc814e54'
        assert req_body['name'] == 'Target for IBM account'
        assert req_body['credentials'] == [credential_model]

    def test_create_target_all_params_with_retries(self):
        # Enable retries and run test_create_target_all_params.
        _service.enable_retries()
        self.test_create_target_all_params()

        # Disable retries and run test_create_target_all_params.
        _service.disable_retries()
        self.test_create_target_all_params()

    @responses.activate
    def test_create_target_value_error(self):
        """
        test_create_target_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/targets')
        mock_response = '{"id": "a2366444-ad87-40b1-81d0-476df1cc1f18", "account_id": "be200c80cabc456e91139e4152327823", "trusted_profile_id": "Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3", "name": "Target Account-A", "credentials": [{"type": "iam_credentials", "secret_crn": "secret_crn", "secret_name": "my secret", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135, "service_name": "pm-20", "instance_crn": "instance_crn"}]}], "created_by": "IBMid-270007EPPC", "created_on": "2024-02-07T05:42:58.000Z", "updated_by": "IBMid-270007EPPC", "updated_on": "2024-02-07T05:42:58.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a Account model
        account_model = {}
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        # Construct a dict representation of a Tags model
        tags_model = {}
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        resource_model['home_account_id'] = '2411ffdc16844b07b42521c3443f456d'
        resource_model['id'] = 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::'
        resource_model['resource_name'] = 'jeff\'s key'
        resource_model['account'] = account_model
        resource_model['component_id'] = 'cloud-object_storage'
        resource_model['component_name'] = 'cloud-object_storage'
        resource_model['environment'] = 'ibm cloud'
        resource_model['tags'] = tags_model
        resource_model['status'] = 'compliant'
        resource_model['total_count'] = 140
        resource_model['pass_count'] = 123
        resource_model['failure_count'] = 12
        resource_model['error_count'] = 5
        resource_model['skipped_count'] = 7
        resource_model['completed_count'] = 135
        resource_model['service_name'] = 'pm-20'
        resource_model['instance_crn'] = 'testString'

        # Construct a dict representation of a Credential model
        credential_model = {}
        credential_model['secret_crn'] = 'testString'
        credential_model['resources'] = [resource_model]

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        account_id = '62ecf99b240144dea9125666249edfcb'
        trusted_profile_id = 'Profile-cb2c1829-9a8d-4218-b9cd-9f83fc814e54'
        name = 'Target for IBM account'
        credentials = [credential_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "account_id": account_id,
            "trusted_profile_id": trusted_profile_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_target(**req_copy)

    def test_create_target_value_error_with_retries(self):
        # Enable retries and run test_create_target_value_error.
        _service.enable_retries()
        self.test_create_target_value_error()

        # Disable retries and run test_create_target_value_error.
        _service.disable_retries()
        self.test_create_target_value_error()


class TestListTargets:
    """
    Test Class for list_targets
    """

    @responses.activate
    def test_list_targets_all_params(self):
        """
        list_targets()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/targets')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "targets": [{"id": "a2366444-ad87-40b1-81d0-476df1cc1f18", "account_id": "be200c80cabc456e91139e4152327823", "trusted_profile_id": "Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3", "name": "Target Account-A", "credentials": [{"type": "iam_credentials", "secret_crn": "secret_crn", "secret_name": "my secret", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135, "service_name": "pm-20", "instance_crn": "instance_crn"}]}], "created_by": "IBMid-270007EPPC", "created_on": "2024-02-07T05:42:58.000Z", "updated_by": "IBMid-270007EPPC", "updated_on": "2024-02-07T05:42:58.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Invoke method
        response = _service.list_targets(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_targets_all_params_with_retries(self):
        # Enable retries and run test_list_targets_all_params.
        _service.enable_retries()
        self.test_list_targets_all_params()

        # Disable retries and run test_list_targets_all_params.
        _service.disable_retries()
        self.test_list_targets_all_params()

    @responses.activate
    def test_list_targets_value_error(self):
        """
        test_list_targets_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/targets')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "targets": [{"id": "a2366444-ad87-40b1-81d0-476df1cc1f18", "account_id": "be200c80cabc456e91139e4152327823", "trusted_profile_id": "Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3", "name": "Target Account-A", "credentials": [{"type": "iam_credentials", "secret_crn": "secret_crn", "secret_name": "my secret", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135, "service_name": "pm-20", "instance_crn": "instance_crn"}]}], "created_by": "IBMid-270007EPPC", "created_on": "2024-02-07T05:42:58.000Z", "updated_by": "IBMid-270007EPPC", "updated_on": "2024-02-07T05:42:58.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_targets(**req_copy)

    def test_list_targets_value_error_with_retries(self):
        # Enable retries and run test_list_targets_value_error.
        _service.enable_retries()
        self.test_list_targets_value_error()

        # Disable retries and run test_list_targets_value_error.
        _service.disable_retries()
        self.test_list_targets_value_error()


class TestGetTarget:
    """
    Test Class for get_target
    """

    @responses.activate
    def test_get_target_all_params(self):
        """
        get_target()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/targets/testString')
        mock_response = '{"id": "a2366444-ad87-40b1-81d0-476df1cc1f18", "account_id": "be200c80cabc456e91139e4152327823", "trusted_profile_id": "Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3", "name": "Target Account-A", "credentials": [{"type": "iam_credentials", "secret_crn": "secret_crn", "secret_name": "my secret", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135, "service_name": "pm-20", "instance_crn": "instance_crn"}]}], "created_by": "IBMid-270007EPPC", "created_on": "2024-02-07T05:42:58.000Z", "updated_by": "IBMid-270007EPPC", "updated_on": "2024-02-07T05:42:58.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        target_id = 'testString'

        # Invoke method
        response = _service.get_target(
            instance_id,
            target_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_target_all_params_with_retries(self):
        # Enable retries and run test_get_target_all_params.
        _service.enable_retries()
        self.test_get_target_all_params()

        # Disable retries and run test_get_target_all_params.
        _service.disable_retries()
        self.test_get_target_all_params()

    @responses.activate
    def test_get_target_value_error(self):
        """
        test_get_target_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/targets/testString')
        mock_response = '{"id": "a2366444-ad87-40b1-81d0-476df1cc1f18", "account_id": "be200c80cabc456e91139e4152327823", "trusted_profile_id": "Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3", "name": "Target Account-A", "credentials": [{"type": "iam_credentials", "secret_crn": "secret_crn", "secret_name": "my secret", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135, "service_name": "pm-20", "instance_crn": "instance_crn"}]}], "created_by": "IBMid-270007EPPC", "created_on": "2024-02-07T05:42:58.000Z", "updated_by": "IBMid-270007EPPC", "updated_on": "2024-02-07T05:42:58.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        target_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "target_id": target_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_target(**req_copy)

    def test_get_target_value_error_with_retries(self):
        # Enable retries and run test_get_target_value_error.
        _service.enable_retries()
        self.test_get_target_value_error()

        # Disable retries and run test_get_target_value_error.
        _service.disable_retries()
        self.test_get_target_value_error()


class TestReplaceTarget:
    """
    Test Class for replace_target
    """

    @responses.activate
    def test_replace_target_all_params(self):
        """
        replace_target()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/targets/testString')
        mock_response = '{"id": "a2366444-ad87-40b1-81d0-476df1cc1f18", "account_id": "be200c80cabc456e91139e4152327823", "trusted_profile_id": "Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3", "name": "Target Account-A", "credentials": [{"type": "iam_credentials", "secret_crn": "secret_crn", "secret_name": "my secret", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135, "service_name": "pm-20", "instance_crn": "instance_crn"}]}], "created_by": "IBMid-270007EPPC", "created_on": "2024-02-07T05:42:58.000Z", "updated_by": "IBMid-270007EPPC", "updated_on": "2024-02-07T05:42:58.000Z"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Account model
        account_model = {}
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        # Construct a dict representation of a Tags model
        tags_model = {}
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        resource_model['home_account_id'] = '2411ffdc16844b07b42521c3443f456d'
        resource_model['id'] = 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::'
        resource_model['resource_name'] = 'jeff\'s key'
        resource_model['account'] = account_model
        resource_model['component_id'] = 'cloud-object_storage'
        resource_model['component_name'] = 'cloud-object_storage'
        resource_model['environment'] = 'ibm cloud'
        resource_model['tags'] = tags_model
        resource_model['status'] = 'compliant'
        resource_model['total_count'] = 140
        resource_model['pass_count'] = 123
        resource_model['failure_count'] = 12
        resource_model['error_count'] = 5
        resource_model['skipped_count'] = 7
        resource_model['completed_count'] = 135
        resource_model['service_name'] = 'pm-20'
        resource_model['instance_crn'] = 'testString'

        # Construct a dict representation of a Credential model
        credential_model = {}
        credential_model['secret_crn'] = 'dummy'
        credential_model['resources'] = [resource_model]

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        target_id = 'testString'
        account_id = 'be200c80cabc456e91139e4152327823'
        trusted_profile_id = 'Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3'
        name = 'Sample Target Name'
        credentials = [credential_model]

        # Invoke method
        response = _service.replace_target(
            instance_id,
            target_id,
            account_id,
            trusted_profile_id,
            name,
            credentials=credentials,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == 'be200c80cabc456e91139e4152327823'
        assert req_body['trusted_profile_id'] == 'Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3'
        assert req_body['name'] == 'Sample Target Name'
        assert req_body['credentials'] == [credential_model]

    def test_replace_target_all_params_with_retries(self):
        # Enable retries and run test_replace_target_all_params.
        _service.enable_retries()
        self.test_replace_target_all_params()

        # Disable retries and run test_replace_target_all_params.
        _service.disable_retries()
        self.test_replace_target_all_params()

    @responses.activate
    def test_replace_target_value_error(self):
        """
        test_replace_target_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/targets/testString')
        mock_response = '{"id": "a2366444-ad87-40b1-81d0-476df1cc1f18", "account_id": "be200c80cabc456e91139e4152327823", "trusted_profile_id": "Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3", "name": "Target Account-A", "credentials": [{"type": "iam_credentials", "secret_crn": "secret_crn", "secret_name": "my secret", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135, "service_name": "pm-20", "instance_crn": "instance_crn"}]}], "created_by": "IBMid-270007EPPC", "created_on": "2024-02-07T05:42:58.000Z", "updated_by": "IBMid-270007EPPC", "updated_on": "2024-02-07T05:42:58.000Z"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Account model
        account_model = {}
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        # Construct a dict representation of a Tags model
        tags_model = {}
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        # Construct a dict representation of a Resource model
        resource_model = {}
        resource_model['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        resource_model['home_account_id'] = '2411ffdc16844b07b42521c3443f456d'
        resource_model['id'] = 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::'
        resource_model['resource_name'] = 'jeff\'s key'
        resource_model['account'] = account_model
        resource_model['component_id'] = 'cloud-object_storage'
        resource_model['component_name'] = 'cloud-object_storage'
        resource_model['environment'] = 'ibm cloud'
        resource_model['tags'] = tags_model
        resource_model['status'] = 'compliant'
        resource_model['total_count'] = 140
        resource_model['pass_count'] = 123
        resource_model['failure_count'] = 12
        resource_model['error_count'] = 5
        resource_model['skipped_count'] = 7
        resource_model['completed_count'] = 135
        resource_model['service_name'] = 'pm-20'
        resource_model['instance_crn'] = 'testString'

        # Construct a dict representation of a Credential model
        credential_model = {}
        credential_model['secret_crn'] = 'dummy'
        credential_model['resources'] = [resource_model]

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        target_id = 'testString'
        account_id = 'be200c80cabc456e91139e4152327823'
        trusted_profile_id = 'Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3'
        name = 'Sample Target Name'
        credentials = [credential_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "target_id": target_id,
            "account_id": account_id,
            "trusted_profile_id": trusted_profile_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_target(**req_copy)

    def test_replace_target_value_error_with_retries(self):
        # Enable retries and run test_replace_target_value_error.
        _service.enable_retries()
        self.test_replace_target_value_error()

        # Disable retries and run test_replace_target_value_error.
        _service.disable_retries()
        self.test_replace_target_value_error()


class TestDeleteTarget:
    """
    Test Class for delete_target
    """

    @responses.activate
    def test_delete_target_all_params(self):
        """
        delete_target()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/targets/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        target_id = 'testString'

        # Invoke method
        response = _service.delete_target(
            instance_id,
            target_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_target_all_params_with_retries(self):
        # Enable retries and run test_delete_target_all_params.
        _service.enable_retries()
        self.test_delete_target_all_params()

        # Disable retries and run test_delete_target_all_params.
        _service.disable_retries()
        self.test_delete_target_all_params()

    @responses.activate
    def test_delete_target_value_error(self):
        """
        test_delete_target_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/targets/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        target_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "target_id": target_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_target(**req_copy)

    def test_delete_target_value_error_with_retries(self):
        # Enable retries and run test_delete_target_value_error.
        _service.enable_retries()
        self.test_delete_target_value_error()

        # Disable retries and run test_delete_target_value_error.
        _service.disable_retries()
        self.test_delete_target_value_error()


# endregion
##############################################################################
# End of Service: Target
##############################################################################

##############################################################################
# Start of Service: ProviderTypeInstance
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecurityAndComplianceCenterApiV3.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecurityAndComplianceCenterApiV3)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecurityAndComplianceCenterApiV3.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateProviderTypeInstance:
    """
    Test Class for create_provider_type_instance
    """

    @responses.activate
    def test_create_provider_type_instance_all_params(self):
        """
        create_provider_type_instance()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types/3e25966275dccfa2c3a34786919c5af7/provider_type_instances')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        provider_type_id = '3e25966275dccfa2c3a34786919c5af7'
        name = 'workload-protection-instance-1'
        attributes = {'wp_crn': 'crn:v1:staging:public:sysdig-secure:eu-gb:a/14q5SEnVIbwxzvP4AWPCjr2dJg5BAvPb:d1461d1ae-df1eee12fa81812e0-12-aa259::'}

        # Invoke method
        response = _service.create_provider_type_instance(
            instance_id,
            provider_type_id,
            name=name,
            attributes=attributes,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'workload-protection-instance-1'
        assert req_body['attributes'] == {'wp_crn': 'crn:v1:staging:public:sysdig-secure:eu-gb:a/14q5SEnVIbwxzvP4AWPCjr2dJg5BAvPb:d1461d1ae-df1eee12fa81812e0-12-aa259::'}

    def test_create_provider_type_instance_all_params_with_retries(self):
        # Enable retries and run test_create_provider_type_instance_all_params.
        _service.enable_retries()
        self.test_create_provider_type_instance_all_params()

        # Disable retries and run test_create_provider_type_instance_all_params.
        _service.disable_retries()
        self.test_create_provider_type_instance_all_params()

    @responses.activate
    def test_create_provider_type_instance_value_error(self):
        """
        test_create_provider_type_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types/3e25966275dccfa2c3a34786919c5af7/provider_type_instances')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        provider_type_id = '3e25966275dccfa2c3a34786919c5af7'
        name = 'workload-protection-instance-1'
        attributes = {'wp_crn': 'crn:v1:staging:public:sysdig-secure:eu-gb:a/14q5SEnVIbwxzvP4AWPCjr2dJg5BAvPb:d1461d1ae-df1eee12fa81812e0-12-aa259::'}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "provider_type_id": provider_type_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_provider_type_instance(**req_copy)

    def test_create_provider_type_instance_value_error_with_retries(self):
        # Enable retries and run test_create_provider_type_instance_value_error.
        _service.enable_retries()
        self.test_create_provider_type_instance_value_error()

        # Disable retries and run test_create_provider_type_instance_value_error.
        _service.disable_retries()
        self.test_create_provider_type_instance_value_error()


class TestListProviderTypeInstances:
    """
    Test Class for list_provider_type_instances
    """

    @responses.activate
    def test_list_provider_type_instances_all_params(self):
        """
        list_provider_type_instances()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types/3e25966275dccfa2c3a34786919c5af7/provider_type_instances')
        mock_response = '{"provider_type_instances": [{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        provider_type_id = '3e25966275dccfa2c3a34786919c5af7'

        # Invoke method
        response = _service.list_provider_type_instances(
            instance_id,
            provider_type_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_provider_type_instances_all_params_with_retries(self):
        # Enable retries and run test_list_provider_type_instances_all_params.
        _service.enable_retries()
        self.test_list_provider_type_instances_all_params()

        # Disable retries and run test_list_provider_type_instances_all_params.
        _service.disable_retries()
        self.test_list_provider_type_instances_all_params()

    @responses.activate
    def test_list_provider_type_instances_value_error(self):
        """
        test_list_provider_type_instances_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types/3e25966275dccfa2c3a34786919c5af7/provider_type_instances')
        mock_response = '{"provider_type_instances": [{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        provider_type_id = '3e25966275dccfa2c3a34786919c5af7'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "provider_type_id": provider_type_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_provider_type_instances(**req_copy)

    def test_list_provider_type_instances_value_error_with_retries(self):
        # Enable retries and run test_list_provider_type_instances_value_error.
        _service.enable_retries()
        self.test_list_provider_type_instances_value_error()

        # Disable retries and run test_list_provider_type_instances_value_error.
        _service.disable_retries()
        self.test_list_provider_type_instances_value_error()


class TestGetProviderTypeInstance:
    """
    Test Class for get_provider_type_instance
    """

    @responses.activate
    def test_get_provider_type_instance_all_params(self):
        """
        get_provider_type_instance()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types/3e25966275dccfa2c3a34786919c5af7/provider_type_instances/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        provider_type_id = '3e25966275dccfa2c3a34786919c5af7'
        provider_type_instance_id = 'testString'

        # Invoke method
        response = _service.get_provider_type_instance(
            instance_id,
            provider_type_id,
            provider_type_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_provider_type_instance_all_params_with_retries(self):
        # Enable retries and run test_get_provider_type_instance_all_params.
        _service.enable_retries()
        self.test_get_provider_type_instance_all_params()

        # Disable retries and run test_get_provider_type_instance_all_params.
        _service.disable_retries()
        self.test_get_provider_type_instance_all_params()

    @responses.activate
    def test_get_provider_type_instance_value_error(self):
        """
        test_get_provider_type_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types/3e25966275dccfa2c3a34786919c5af7/provider_type_instances/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        provider_type_id = '3e25966275dccfa2c3a34786919c5af7'
        provider_type_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "provider_type_id": provider_type_id,
            "provider_type_instance_id": provider_type_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_provider_type_instance(**req_copy)

    def test_get_provider_type_instance_value_error_with_retries(self):
        # Enable retries and run test_get_provider_type_instance_value_error.
        _service.enable_retries()
        self.test_get_provider_type_instance_value_error()

        # Disable retries and run test_get_provider_type_instance_value_error.
        _service.disable_retries()
        self.test_get_provider_type_instance_value_error()


class TestUpdateProviderTypeInstance:
    """
    Test Class for update_provider_type_instance
    """

    @responses.activate
    def test_update_provider_type_instance_all_params(self):
        """
        update_provider_type_instance()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types/3e25966275dccfa2c3a34786919c5af7/provider_type_instances/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        provider_type_id = '3e25966275dccfa2c3a34786919c5af7'
        provider_type_instance_id = 'testString'
        name = 'workload-protection-instance-1'
        attributes = {'wp_crn': 'crn:v1:staging:public:sysdig-secure:eu-gb:a/14q5SEnVIbwxzvP4AWPCjr2dJg5BAvPb:d1461d1ae-df1eee12fa81812e0-12-aa259::'}

        # Invoke method
        response = _service.update_provider_type_instance(
            instance_id,
            provider_type_id,
            provider_type_instance_id,
            name=name,
            attributes=attributes,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'workload-protection-instance-1'
        assert req_body['attributes'] == {'wp_crn': 'crn:v1:staging:public:sysdig-secure:eu-gb:a/14q5SEnVIbwxzvP4AWPCjr2dJg5BAvPb:d1461d1ae-df1eee12fa81812e0-12-aa259::'}

    def test_update_provider_type_instance_all_params_with_retries(self):
        # Enable retries and run test_update_provider_type_instance_all_params.
        _service.enable_retries()
        self.test_update_provider_type_instance_all_params()

        # Disable retries and run test_update_provider_type_instance_all_params.
        _service.disable_retries()
        self.test_update_provider_type_instance_all_params()

    @responses.activate
    def test_update_provider_type_instance_value_error(self):
        """
        test_update_provider_type_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types/3e25966275dccfa2c3a34786919c5af7/provider_type_instances/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        provider_type_id = '3e25966275dccfa2c3a34786919c5af7'
        provider_type_instance_id = 'testString'
        name = 'workload-protection-instance-1'
        attributes = {'wp_crn': 'crn:v1:staging:public:sysdig-secure:eu-gb:a/14q5SEnVIbwxzvP4AWPCjr2dJg5BAvPb:d1461d1ae-df1eee12fa81812e0-12-aa259::'}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "provider_type_id": provider_type_id,
            "provider_type_instance_id": provider_type_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_provider_type_instance(**req_copy)

    def test_update_provider_type_instance_value_error_with_retries(self):
        # Enable retries and run test_update_provider_type_instance_value_error.
        _service.enable_retries()
        self.test_update_provider_type_instance_value_error()

        # Disable retries and run test_update_provider_type_instance_value_error.
        _service.disable_retries()
        self.test_update_provider_type_instance_value_error()


class TestDeleteProviderTypeInstance:
    """
    Test Class for delete_provider_type_instance
    """

    @responses.activate
    def test_delete_provider_type_instance_all_params(self):
        """
        delete_provider_type_instance()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types/3e25966275dccfa2c3a34786919c5af7/provider_type_instances/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        provider_type_id = '3e25966275dccfa2c3a34786919c5af7'
        provider_type_instance_id = 'testString'

        # Invoke method
        response = _service.delete_provider_type_instance(
            instance_id,
            provider_type_id,
            provider_type_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_provider_type_instance_all_params_with_retries(self):
        # Enable retries and run test_delete_provider_type_instance_all_params.
        _service.enable_retries()
        self.test_delete_provider_type_instance_all_params()

        # Disable retries and run test_delete_provider_type_instance_all_params.
        _service.disable_retries()
        self.test_delete_provider_type_instance_all_params()

    @responses.activate
    def test_delete_provider_type_instance_value_error(self):
        """
        test_delete_provider_type_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types/3e25966275dccfa2c3a34786919c5af7/provider_type_instances/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        provider_type_id = '3e25966275dccfa2c3a34786919c5af7'
        provider_type_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "provider_type_id": provider_type_id,
            "provider_type_instance_id": provider_type_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_provider_type_instance(**req_copy)

    def test_delete_provider_type_instance_value_error_with_retries(self):
        # Enable retries and run test_delete_provider_type_instance_value_error.
        _service.enable_retries()
        self.test_delete_provider_type_instance_value_error()

        # Disable retries and run test_delete_provider_type_instance_value_error.
        _service.disable_retries()
        self.test_delete_provider_type_instance_value_error()


# endregion
##############################################################################
# End of Service: ProviderTypeInstance
##############################################################################

##############################################################################
# Start of Service: ProviderType
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecurityAndComplianceCenterApiV3.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecurityAndComplianceCenterApiV3)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecurityAndComplianceCenterApiV3.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListProviderTypes:
    """
    Test Class for list_provider_types
    """

    @responses.activate
    def test_list_provider_types_all_params(self):
        """
        list_provider_types()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types')
        mock_response = '{"provider_types": [{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection", "description": "Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.", "s2s_enabled": true, "instance_limit": 1, "mode": "PULL", "data_type": "com.sysdig.secure.results", "icon": "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+", "label": {"text": "1 per instance", "tip": "Only 1 per instance"}, "attributes": {"mapKey": {"type": "text", "display_name": "Workload Protection Instance CRN"}}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Invoke method
        response = _service.list_provider_types(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_provider_types_all_params_with_retries(self):
        # Enable retries and run test_list_provider_types_all_params.
        _service.enable_retries()
        self.test_list_provider_types_all_params()

        # Disable retries and run test_list_provider_types_all_params.
        _service.disable_retries()
        self.test_list_provider_types_all_params()

    @responses.activate
    def test_list_provider_types_value_error(self):
        """
        test_list_provider_types_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types')
        mock_response = '{"provider_types": [{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection", "description": "Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.", "s2s_enabled": true, "instance_limit": 1, "mode": "PULL", "data_type": "com.sysdig.secure.results", "icon": "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+", "label": {"text": "1 per instance", "tip": "Only 1 per instance"}, "attributes": {"mapKey": {"type": "text", "display_name": "Workload Protection Instance CRN"}}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_provider_types(**req_copy)

    def test_list_provider_types_value_error_with_retries(self):
        # Enable retries and run test_list_provider_types_value_error.
        _service.enable_retries()
        self.test_list_provider_types_value_error()

        # Disable retries and run test_list_provider_types_value_error.
        _service.disable_retries()
        self.test_list_provider_types_value_error()


class TestGetProviderTypeById:
    """
    Test Class for get_provider_type_by_id
    """

    @responses.activate
    def test_get_provider_type_by_id_all_params(self):
        """
        get_provider_type_by_id()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types/3e25966275dccfa2c3a34786919c5af7')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection", "description": "Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.", "s2s_enabled": true, "instance_limit": 1, "mode": "PULL", "data_type": "com.sysdig.secure.results", "icon": "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+", "label": {"text": "1 per instance", "tip": "Only 1 per instance"}, "attributes": {"mapKey": {"type": "text", "display_name": "Workload Protection Instance CRN"}}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        provider_type_id = '3e25966275dccfa2c3a34786919c5af7'

        # Invoke method
        response = _service.get_provider_type_by_id(
            instance_id,
            provider_type_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_provider_type_by_id_all_params_with_retries(self):
        # Enable retries and run test_get_provider_type_by_id_all_params.
        _service.enable_retries()
        self.test_get_provider_type_by_id_all_params()

        # Disable retries and run test_get_provider_type_by_id_all_params.
        _service.disable_retries()
        self.test_get_provider_type_by_id_all_params()

    @responses.activate
    def test_get_provider_type_by_id_value_error(self):
        """
        test_get_provider_type_by_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/provider_types/3e25966275dccfa2c3a34786919c5af7')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection", "description": "Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.", "s2s_enabled": true, "instance_limit": 1, "mode": "PULL", "data_type": "com.sysdig.secure.results", "icon": "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+", "label": {"text": "1 per instance", "tip": "Only 1 per instance"}, "attributes": {"mapKey": {"type": "text", "display_name": "Workload Protection Instance CRN"}}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        provider_type_id = '3e25966275dccfa2c3a34786919c5af7'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "provider_type_id": provider_type_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_provider_type_by_id(**req_copy)

    def test_get_provider_type_by_id_value_error_with_retries(self):
        # Enable retries and run test_get_provider_type_by_id_value_error.
        _service.enable_retries()
        self.test_get_provider_type_by_id_value_error()

        # Disable retries and run test_get_provider_type_by_id_value_error.
        _service.disable_retries()
        self.test_get_provider_type_by_id_value_error()


# endregion
##############################################################################
# End of Service: ProviderType
##############################################################################

##############################################################################
# Start of Service: Report
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecurityAndComplianceCenterApiV3.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecurityAndComplianceCenterApiV3)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecurityAndComplianceCenterApiV3.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetLatestReports:
    """
    Test Class for get_latest_reports
    """

    @responses.activate
    def test_get_latest_reports_all_params(self):
        """
        get_latest_reports()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/latest')
        mock_response = '{"home_account_id": "home_account_id", "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "score": {"passed": 1, "total_count": 4, "percent": 25}, "reports": [{"id": "44a5-a292-32114fa73558", "type": "scheduled", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "instance_id", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "scope": {"id": "2411ffdc16844b07b42521c3443f456d", "type": "account"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": "anyValue", "scopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}], "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}, "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7, "not_compliant_controls": [{"id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "control_name": "ibm-cloud-rule", "control_description": "Ensure security questions are registered by the account owner"}]}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "scopes": [{"id": "id", "name": "name", "href": "href", "environment": "environment"}], "additional_details": {"created_by": "Security and Compliance Center", "labels": ["labels"], "links": [{"description": "description", "href": "href"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        sort = 'profile_name'

        # Invoke method
        response = _service.get_latest_reports(
            instance_id,
            sort=sort,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'sort={}'.format(sort) in query_string

    def test_get_latest_reports_all_params_with_retries(self):
        # Enable retries and run test_get_latest_reports_all_params.
        _service.enable_retries()
        self.test_get_latest_reports_all_params()

        # Disable retries and run test_get_latest_reports_all_params.
        _service.disable_retries()
        self.test_get_latest_reports_all_params()

    @responses.activate
    def test_get_latest_reports_required_params(self):
        """
        test_get_latest_reports_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/latest')
        mock_response = '{"home_account_id": "home_account_id", "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "score": {"passed": 1, "total_count": 4, "percent": 25}, "reports": [{"id": "44a5-a292-32114fa73558", "type": "scheduled", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "instance_id", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "scope": {"id": "2411ffdc16844b07b42521c3443f456d", "type": "account"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": "anyValue", "scopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}], "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}, "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7, "not_compliant_controls": [{"id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "control_name": "ibm-cloud-rule", "control_description": "Ensure security questions are registered by the account owner"}]}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "scopes": [{"id": "id", "name": "name", "href": "href", "environment": "environment"}], "additional_details": {"created_by": "Security and Compliance Center", "labels": ["labels"], "links": [{"description": "description", "href": "href"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Invoke method
        response = _service.get_latest_reports(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_latest_reports_required_params_with_retries(self):
        # Enable retries and run test_get_latest_reports_required_params.
        _service.enable_retries()
        self.test_get_latest_reports_required_params()

        # Disable retries and run test_get_latest_reports_required_params.
        _service.disable_retries()
        self.test_get_latest_reports_required_params()

    @responses.activate
    def test_get_latest_reports_value_error(self):
        """
        test_get_latest_reports_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/latest')
        mock_response = '{"home_account_id": "home_account_id", "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "score": {"passed": 1, "total_count": 4, "percent": 25}, "reports": [{"id": "44a5-a292-32114fa73558", "type": "scheduled", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "instance_id", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "scope": {"id": "2411ffdc16844b07b42521c3443f456d", "type": "account"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": "anyValue", "scopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}], "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}, "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7, "not_compliant_controls": [{"id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "control_name": "ibm-cloud-rule", "control_description": "Ensure security questions are registered by the account owner"}]}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "scopes": [{"id": "id", "name": "name", "href": "href", "environment": "environment"}], "additional_details": {"created_by": "Security and Compliance Center", "labels": ["labels"], "links": [{"description": "description", "href": "href"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_latest_reports(**req_copy)

    def test_get_latest_reports_value_error_with_retries(self):
        # Enable retries and run test_get_latest_reports_value_error.
        _service.enable_retries()
        self.test_get_latest_reports_value_error()

        # Disable retries and run test_get_latest_reports_value_error.
        _service.disable_retries()
        self.test_get_latest_reports_value_error()


class TestListReports:
    """
    Test Class for list_reports
    """

    @responses.activate
    def test_list_reports_all_params(self):
        """
        list_reports()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "home_account_id": "home_account_id", "reports": [{"id": "44a5-a292-32114fa73558", "type": "scheduled", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "instance_id", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "scope": {"id": "2411ffdc16844b07b42521c3443f456d", "type": "account"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": "anyValue", "scopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}], "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}, "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7, "not_compliant_controls": [{"id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "control_name": "ibm-cloud-rule", "control_description": "Ensure security questions are registered by the account owner"}]}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "scopes": [{"id": "id", "name": "name", "href": "href", "environment": "environment"}], "additional_details": {"created_by": "Security and Compliance Center", "labels": ["labels"], "links": [{"description": "description", "href": "href"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_attachment_id = 'testString'
        group_id = 'testString'
        report_profile_id = 'testString'
        type = 'scheduled'
        start = 'testString'
        limit = 50
        sort = 'profile_name'

        # Invoke method
        response = _service.list_reports(
            instance_id,
            report_attachment_id=report_attachment_id,
            group_id=group_id,
            report_profile_id=report_profile_id,
            type=type,
            start=start,
            limit=limit,
            sort=sort,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'report_attachment_id={}'.format(report_attachment_id) in query_string
        assert 'group_id={}'.format(group_id) in query_string
        assert 'report_profile_id={}'.format(report_profile_id) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'sort={}'.format(sort) in query_string

    def test_list_reports_all_params_with_retries(self):
        # Enable retries and run test_list_reports_all_params.
        _service.enable_retries()
        self.test_list_reports_all_params()

        # Disable retries and run test_list_reports_all_params.
        _service.disable_retries()
        self.test_list_reports_all_params()

    @responses.activate
    def test_list_reports_required_params(self):
        """
        test_list_reports_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "home_account_id": "home_account_id", "reports": [{"id": "44a5-a292-32114fa73558", "type": "scheduled", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "instance_id", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "scope": {"id": "2411ffdc16844b07b42521c3443f456d", "type": "account"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": "anyValue", "scopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}], "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}, "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7, "not_compliant_controls": [{"id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "control_name": "ibm-cloud-rule", "control_description": "Ensure security questions are registered by the account owner"}]}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "scopes": [{"id": "id", "name": "name", "href": "href", "environment": "environment"}], "additional_details": {"created_by": "Security and Compliance Center", "labels": ["labels"], "links": [{"description": "description", "href": "href"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Invoke method
        response = _service.list_reports(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_reports_required_params_with_retries(self):
        # Enable retries and run test_list_reports_required_params.
        _service.enable_retries()
        self.test_list_reports_required_params()

        # Disable retries and run test_list_reports_required_params.
        _service.disable_retries()
        self.test_list_reports_required_params()

    @responses.activate
    def test_list_reports_value_error(self):
        """
        test_list_reports_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "home_account_id": "home_account_id", "reports": [{"id": "44a5-a292-32114fa73558", "type": "scheduled", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "instance_id", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "scope": {"id": "2411ffdc16844b07b42521c3443f456d", "type": "account"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": "anyValue", "scopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}], "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}, "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7, "not_compliant_controls": [{"id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "control_name": "ibm-cloud-rule", "control_description": "Ensure security questions are registered by the account owner"}]}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "scopes": [{"id": "id", "name": "name", "href": "href", "environment": "environment"}], "additional_details": {"created_by": "Security and Compliance Center", "labels": ["labels"], "links": [{"description": "description", "href": "href"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_reports(**req_copy)

    def test_list_reports_value_error_with_retries(self):
        # Enable retries and run test_list_reports_value_error.
        _service.enable_retries()
        self.test_list_reports_value_error()

        # Disable retries and run test_list_reports_value_error.
        _service.disable_retries()
        self.test_list_reports_value_error()

    @responses.activate
    def test_list_reports_with_pager_get_next(self):
        """
        test_list_reports_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports')
        mock_response1 = '{"next":{"start":"1"},"reports":[{"id":"44a5-a292-32114fa73558","type":"scheduled","group_id":"55b6-b3A4-432250b84669","created_on":"2022-08-15T12:30:01Z","scan_time":"2022-08-15T12:30:01Z","cos_object":"crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7","instance_id":"instance_id","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"profile":{"id":"44a5-a292-32114fa73558","name":"IBM FS Cloud","version":"0.1"},"scope":{"id":"2411ffdc16844b07b42521c3443f456d","type":"account"},"attachment":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"resource group - Default","description":"Scoped to the Default resource group","schedule":"daily","scope":"anyValue","scopes":[{"id":"id","name":"name","description":"description","environment":"environment","properties":[{"name":"name","value":"anyValue"}],"account_id":"account_id","instance_id":"instance_id","created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","attachment_count":16}],"notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["failed_control_ids"]}}},"controls_summary":{"status":"compliant","total_count":150,"compliant_count":130,"not_compliant_count":5,"unable_to_perform_count":5,"user_evaluation_required_count":10,"not_applicable_count":7,"not_compliant_controls":[{"id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","control_name":"ibm-cloud-rule","control_description":"Ensure security questions are registered by the account owner"}]},"evaluations_summary":{"status":"compliant","total_count":140,"pass_count":123,"failure_count":12,"error_count":5,"skipped_count":7,"completed_count":135},"tags":{"user":["user"],"access":["access"],"service":["service"]},"scopes":[{"id":"id","name":"name","href":"href","environment":"environment"}],"additional_details":{"created_by":"Security and Compliance Center","labels":["labels"],"links":[{"description":"description","href":"href"}]}}],"total_count":2,"limit":1}'
        mock_response2 = '{"reports":[{"id":"44a5-a292-32114fa73558","type":"scheduled","group_id":"55b6-b3A4-432250b84669","created_on":"2022-08-15T12:30:01Z","scan_time":"2022-08-15T12:30:01Z","cos_object":"crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7","instance_id":"instance_id","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"profile":{"id":"44a5-a292-32114fa73558","name":"IBM FS Cloud","version":"0.1"},"scope":{"id":"2411ffdc16844b07b42521c3443f456d","type":"account"},"attachment":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"resource group - Default","description":"Scoped to the Default resource group","schedule":"daily","scope":"anyValue","scopes":[{"id":"id","name":"name","description":"description","environment":"environment","properties":[{"name":"name","value":"anyValue"}],"account_id":"account_id","instance_id":"instance_id","created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","attachment_count":16}],"notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["failed_control_ids"]}}},"controls_summary":{"status":"compliant","total_count":150,"compliant_count":130,"not_compliant_count":5,"unable_to_perform_count":5,"user_evaluation_required_count":10,"not_applicable_count":7,"not_compliant_controls":[{"id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","control_name":"ibm-cloud-rule","control_description":"Ensure security questions are registered by the account owner"}]},"evaluations_summary":{"status":"compliant","total_count":140,"pass_count":123,"failure_count":12,"error_count":5,"skipped_count":7,"completed_count":135},"tags":{"user":["user"],"access":["access"],"service":["service"]},"scopes":[{"id":"id","name":"name","href":"href","environment":"environment"}],"additional_details":{"created_by":"Security and Compliance Center","labels":["labels"],"links":[{"description":"description","href":"href"}]}}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = ReportsPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_attachment_id='testString',
            group_id='testString',
            report_profile_id='testString',
            type='scheduled',
            limit=10,
            sort='profile_name',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_reports_with_pager_get_all(self):
        """
        test_list_reports_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports')
        mock_response1 = '{"next":{"start":"1"},"reports":[{"id":"44a5-a292-32114fa73558","type":"scheduled","group_id":"55b6-b3A4-432250b84669","created_on":"2022-08-15T12:30:01Z","scan_time":"2022-08-15T12:30:01Z","cos_object":"crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7","instance_id":"instance_id","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"profile":{"id":"44a5-a292-32114fa73558","name":"IBM FS Cloud","version":"0.1"},"scope":{"id":"2411ffdc16844b07b42521c3443f456d","type":"account"},"attachment":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"resource group - Default","description":"Scoped to the Default resource group","schedule":"daily","scope":"anyValue","scopes":[{"id":"id","name":"name","description":"description","environment":"environment","properties":[{"name":"name","value":"anyValue"}],"account_id":"account_id","instance_id":"instance_id","created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","attachment_count":16}],"notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["failed_control_ids"]}}},"controls_summary":{"status":"compliant","total_count":150,"compliant_count":130,"not_compliant_count":5,"unable_to_perform_count":5,"user_evaluation_required_count":10,"not_applicable_count":7,"not_compliant_controls":[{"id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","control_name":"ibm-cloud-rule","control_description":"Ensure security questions are registered by the account owner"}]},"evaluations_summary":{"status":"compliant","total_count":140,"pass_count":123,"failure_count":12,"error_count":5,"skipped_count":7,"completed_count":135},"tags":{"user":["user"],"access":["access"],"service":["service"]},"scopes":[{"id":"id","name":"name","href":"href","environment":"environment"}],"additional_details":{"created_by":"Security and Compliance Center","labels":["labels"],"links":[{"description":"description","href":"href"}]}}],"total_count":2,"limit":1}'
        mock_response2 = '{"reports":[{"id":"44a5-a292-32114fa73558","type":"scheduled","group_id":"55b6-b3A4-432250b84669","created_on":"2022-08-15T12:30:01Z","scan_time":"2022-08-15T12:30:01Z","cos_object":"crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7","instance_id":"instance_id","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"profile":{"id":"44a5-a292-32114fa73558","name":"IBM FS Cloud","version":"0.1"},"scope":{"id":"2411ffdc16844b07b42521c3443f456d","type":"account"},"attachment":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"resource group - Default","description":"Scoped to the Default resource group","schedule":"daily","scope":"anyValue","scopes":[{"id":"id","name":"name","description":"description","environment":"environment","properties":[{"name":"name","value":"anyValue"}],"account_id":"account_id","instance_id":"instance_id","created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","attachment_count":16}],"notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["failed_control_ids"]}}},"controls_summary":{"status":"compliant","total_count":150,"compliant_count":130,"not_compliant_count":5,"unable_to_perform_count":5,"user_evaluation_required_count":10,"not_applicable_count":7,"not_compliant_controls":[{"id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","control_name":"ibm-cloud-rule","control_description":"Ensure security questions are registered by the account owner"}]},"evaluations_summary":{"status":"compliant","total_count":140,"pass_count":123,"failure_count":12,"error_count":5,"skipped_count":7,"completed_count":135},"tags":{"user":["user"],"access":["access"],"service":["service"]},"scopes":[{"id":"id","name":"name","href":"href","environment":"environment"}],"additional_details":{"created_by":"Security and Compliance Center","labels":["labels"],"links":[{"description":"description","href":"href"}]}}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = ReportsPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_attachment_id='testString',
            group_id='testString',
            report_profile_id='testString',
            type='scheduled',
            limit=10,
            sort='profile_name',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetReport:
    """
    Test Class for get_report
    """

    @responses.activate
    def test_get_report_all_params(self):
        """
        get_report()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString')
        mock_response = '{"id": "44a5-a292-32114fa73558", "type": "scheduled", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "instance_id", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "scope": {"id": "2411ffdc16844b07b42521c3443f456d", "type": "account"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": "anyValue", "scopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}], "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}, "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7, "not_compliant_controls": [{"id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "control_name": "ibm-cloud-rule", "control_description": "Ensure security questions are registered by the account owner"}]}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "scopes": [{"id": "id", "name": "name", "href": "href", "environment": "environment"}], "additional_details": {"created_by": "Security and Compliance Center", "labels": ["labels"], "links": [{"description": "description", "href": "href"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        scope_id = 'testString'
        subscope_id = 'testString'

        # Invoke method
        response = _service.get_report(
            report_id,
            instance_id,
            scope_id=scope_id,
            subscope_id=subscope_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'scope_id={}'.format(scope_id) in query_string
        assert 'subscope_id={}'.format(subscope_id) in query_string

    def test_get_report_all_params_with_retries(self):
        # Enable retries and run test_get_report_all_params.
        _service.enable_retries()
        self.test_get_report_all_params()

        # Disable retries and run test_get_report_all_params.
        _service.disable_retries()
        self.test_get_report_all_params()

    @responses.activate
    def test_get_report_required_params(self):
        """
        test_get_report_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString')
        mock_response = '{"id": "44a5-a292-32114fa73558", "type": "scheduled", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "instance_id", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "scope": {"id": "2411ffdc16844b07b42521c3443f456d", "type": "account"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": "anyValue", "scopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}], "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}, "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7, "not_compliant_controls": [{"id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "control_name": "ibm-cloud-rule", "control_description": "Ensure security questions are registered by the account owner"}]}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "scopes": [{"id": "id", "name": "name", "href": "href", "environment": "environment"}], "additional_details": {"created_by": "Security and Compliance Center", "labels": ["labels"], "links": [{"description": "description", "href": "href"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Invoke method
        response = _service.get_report(
            report_id,
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_report_required_params_with_retries(self):
        # Enable retries and run test_get_report_required_params.
        _service.enable_retries()
        self.test_get_report_required_params()

        # Disable retries and run test_get_report_required_params.
        _service.disable_retries()
        self.test_get_report_required_params()

    @responses.activate
    def test_get_report_value_error(self):
        """
        test_get_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString')
        mock_response = '{"id": "44a5-a292-32114fa73558", "type": "scheduled", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "instance_id", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "scope": {"id": "2411ffdc16844b07b42521c3443f456d", "type": "account"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": "anyValue", "scopes": [{"id": "id", "name": "name", "description": "description", "environment": "environment", "properties": [{"name": "name", "value": "anyValue"}], "account_id": "account_id", "instance_id": "instance_id", "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "attachment_count": 16}], "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}, "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7, "not_compliant_controls": [{"id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "control_name": "ibm-cloud-rule", "control_description": "Ensure security questions are registered by the account owner"}]}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "scopes": [{"id": "id", "name": "name", "href": "href", "environment": "environment"}], "additional_details": {"created_by": "Security and Compliance Center", "labels": ["labels"], "links": [{"description": "description", "href": "href"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "report_id": report_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_report(**req_copy)

    def test_get_report_value_error_with_retries(self):
        # Enable retries and run test_get_report_value_error.
        _service.enable_retries()
        self.test_get_report_value_error()

        # Disable retries and run test_get_report_value_error.
        _service.disable_retries()
        self.test_get_report_value_error()


class TestGetReportSummary:
    """
    Test Class for get_report_summary
    """

    @responses.activate
    def test_get_report_summary_all_params(self):
        """
        get_report_summary()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/summary')
        mock_response = '{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "instance_id": "84644a08-31b6-4988-b504-49a46ca69ccd", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "score": {"passed": 1, "total_count": 4, "percent": 25}, "evaluations": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "controls": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}, "resources": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7, "top_failed": [{"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "my-bucket", "account": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "service": "cloud-object-storage", "service_display_name": "cloud-object-storage", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Invoke method
        response = _service.get_report_summary(
            instance_id,
            report_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_report_summary_all_params_with_retries(self):
        # Enable retries and run test_get_report_summary_all_params.
        _service.enable_retries()
        self.test_get_report_summary_all_params()

        # Disable retries and run test_get_report_summary_all_params.
        _service.disable_retries()
        self.test_get_report_summary_all_params()

    @responses.activate
    def test_get_report_summary_value_error(self):
        """
        test_get_report_summary_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/summary')
        mock_response = '{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "instance_id": "84644a08-31b6-4988-b504-49a46ca69ccd", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "score": {"passed": 1, "total_count": 4, "percent": 25}, "evaluations": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}, "controls": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}, "resources": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7, "top_failed": [{"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "my-bucket", "account": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "service": "cloud-object-storage", "service_display_name": "cloud-object-storage", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "report_id": report_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_report_summary(**req_copy)

    def test_get_report_summary_value_error_with_retries(self):
        # Enable retries and run test_get_report_summary_value_error.
        _service.enable_retries()
        self.test_get_report_summary_value_error()

        # Disable retries and run test_get_report_summary_value_error.
        _service.disable_retries()
        self.test_get_report_summary_value_error()


class TestGetReportDownloadFile:
    """
    Test Class for get_report_download_file
    """

    @responses.activate
    def test_get_report_download_file_all_params(self):
        """
        get_report_download_file()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/download')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/csv',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        accept = 'application/csv'
        exclude_summary = True

        # Invoke method
        response = _service.get_report_download_file(
            instance_id,
            report_id,
            accept=accept,
            exclude_summary=exclude_summary,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'exclude_summary={}'.format('true' if exclude_summary else 'false') in query_string

    def test_get_report_download_file_all_params_with_retries(self):
        # Enable retries and run test_get_report_download_file_all_params.
        _service.enable_retries()
        self.test_get_report_download_file_all_params()

        # Disable retries and run test_get_report_download_file_all_params.
        _service.disable_retries()
        self.test_get_report_download_file_all_params()

    @responses.activate
    def test_get_report_download_file_required_params(self):
        """
        test_get_report_download_file_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/download')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/csv',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Invoke method
        response = _service.get_report_download_file(
            instance_id,
            report_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_report_download_file_required_params_with_retries(self):
        # Enable retries and run test_get_report_download_file_required_params.
        _service.enable_retries()
        self.test_get_report_download_file_required_params()

        # Disable retries and run test_get_report_download_file_required_params.
        _service.disable_retries()
        self.test_get_report_download_file_required_params()

    @responses.activate
    def test_get_report_download_file_value_error(self):
        """
        test_get_report_download_file_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/download')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/csv',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "report_id": report_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_report_download_file(**req_copy)

    def test_get_report_download_file_value_error_with_retries(self):
        # Enable retries and run test_get_report_download_file_value_error.
        _service.enable_retries()
        self.test_get_report_download_file_value_error()

        # Disable retries and run test_get_report_download_file_value_error.
        _service.disable_retries()
        self.test_get_report_download_file_value_error()


class TestGetReportControls:
    """
    Test Class for get_report_controls
    """

    @responses.activate
    def test_get_report_controls_all_params(self):
        """
        get_report_controls()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/controls')
        mock_response = '{"report_id": "report_id", "home_account_id": "home_account_id", "controls": [{"report_id": "6f1fdb98-c08b-41a8-a2f9-df10b51ff34a", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "531fc3e28bfc43c5a2cea07786d93f5c", "control_library_id": "531fc3e28bfc43c5a2cea07786d93f5c", "control_library_version": "v1.2.3", "control_name": "Password Management", "control_description": "Password Management", "control_category": "Access Control", "control_specifications": [{"control_specification_id": "18d32a4430e54c81a6668952609763b2", "control_specification_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "responsibility": "user", "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}], "status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}], "resource_tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        control_id = 'testString'
        control_name = 'testString'
        control_description = 'testString'
        control_category = 'testString'
        status = 'compliant'
        sort = 'control_name'
        scope_id = 'testString'
        subscope_id = 'testString'

        # Invoke method
        response = _service.get_report_controls(
            instance_id,
            report_id,
            control_id=control_id,
            control_name=control_name,
            control_description=control_description,
            control_category=control_category,
            status=status,
            sort=sort,
            scope_id=scope_id,
            subscope_id=subscope_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'control_id={}'.format(control_id) in query_string
        assert 'control_name={}'.format(control_name) in query_string
        assert 'control_description={}'.format(control_description) in query_string
        assert 'control_category={}'.format(control_category) in query_string
        assert 'status={}'.format(status) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'scope_id={}'.format(scope_id) in query_string
        assert 'subscope_id={}'.format(subscope_id) in query_string

    def test_get_report_controls_all_params_with_retries(self):
        # Enable retries and run test_get_report_controls_all_params.
        _service.enable_retries()
        self.test_get_report_controls_all_params()

        # Disable retries and run test_get_report_controls_all_params.
        _service.disable_retries()
        self.test_get_report_controls_all_params()

    @responses.activate
    def test_get_report_controls_required_params(self):
        """
        test_get_report_controls_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/controls')
        mock_response = '{"report_id": "report_id", "home_account_id": "home_account_id", "controls": [{"report_id": "6f1fdb98-c08b-41a8-a2f9-df10b51ff34a", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "531fc3e28bfc43c5a2cea07786d93f5c", "control_library_id": "531fc3e28bfc43c5a2cea07786d93f5c", "control_library_version": "v1.2.3", "control_name": "Password Management", "control_description": "Password Management", "control_category": "Access Control", "control_specifications": [{"control_specification_id": "18d32a4430e54c81a6668952609763b2", "control_specification_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "responsibility": "user", "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}], "status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}], "resource_tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Invoke method
        response = _service.get_report_controls(
            instance_id,
            report_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_report_controls_required_params_with_retries(self):
        # Enable retries and run test_get_report_controls_required_params.
        _service.enable_retries()
        self.test_get_report_controls_required_params()

        # Disable retries and run test_get_report_controls_required_params.
        _service.disable_retries()
        self.test_get_report_controls_required_params()

    @responses.activate
    def test_get_report_controls_value_error(self):
        """
        test_get_report_controls_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/controls')
        mock_response = '{"report_id": "report_id", "home_account_id": "home_account_id", "controls": [{"report_id": "6f1fdb98-c08b-41a8-a2f9-df10b51ff34a", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "531fc3e28bfc43c5a2cea07786d93f5c", "control_library_id": "531fc3e28bfc43c5a2cea07786d93f5c", "control_library_version": "v1.2.3", "control_name": "Password Management", "control_description": "Password Management", "control_category": "Access Control", "control_specifications": [{"control_specification_id": "18d32a4430e54c81a6668952609763b2", "control_specification_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "responsibility": "user", "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}], "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}], "status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}], "resource_tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "report_id": report_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_report_controls(**req_copy)

    def test_get_report_controls_value_error_with_retries(self):
        # Enable retries and run test_get_report_controls_value_error.
        _service.enable_retries()
        self.test_get_report_controls_value_error()

        # Disable retries and run test_get_report_controls_value_error.
        _service.disable_retries()
        self.test_get_report_controls_value_error()


class TestGetReportRule:
    """
    Test Class for get_report_rule
    """

    @responses.activate
    def test_get_report_rule_all_params(self):
        """
        get_report_rule()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/rules/rule-61fa114a-2bb9-43fd-8068-b873b48bdf79')
        mock_response = '{"id": "rule-7b0560a4-df94-4629-bb76-680f3155ddda", "type": "user_defined/system_defined", "description": "rule", "version": "1.2.3", "account_id": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "created_on": "2022-08-15T12:30:01.000Z", "created_by": "IBMid-12345", "updated_on": "2022-08-15T12:30:01.000Z", "updated_by": "IBMid-12345", "labels": ["labels"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        rule_id = 'rule-61fa114a-2bb9-43fd-8068-b873b48bdf79'

        # Invoke method
        response = _service.get_report_rule(
            instance_id,
            report_id,
            rule_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_report_rule_all_params_with_retries(self):
        # Enable retries and run test_get_report_rule_all_params.
        _service.enable_retries()
        self.test_get_report_rule_all_params()

        # Disable retries and run test_get_report_rule_all_params.
        _service.disable_retries()
        self.test_get_report_rule_all_params()

    @responses.activate
    def test_get_report_rule_value_error(self):
        """
        test_get_report_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/rules/rule-61fa114a-2bb9-43fd-8068-b873b48bdf79')
        mock_response = '{"id": "rule-7b0560a4-df94-4629-bb76-680f3155ddda", "type": "user_defined/system_defined", "description": "rule", "version": "1.2.3", "account_id": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "created_on": "2022-08-15T12:30:01.000Z", "created_by": "IBMid-12345", "updated_on": "2022-08-15T12:30:01.000Z", "updated_by": "IBMid-12345", "labels": ["labels"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        rule_id = 'rule-61fa114a-2bb9-43fd-8068-b873b48bdf79'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "report_id": report_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_report_rule(**req_copy)

    def test_get_report_rule_value_error_with_retries(self):
        # Enable retries and run test_get_report_rule_value_error.
        _service.enable_retries()
        self.test_get_report_rule_value_error()

        # Disable retries and run test_get_report_rule_value_error.
        _service.disable_retries()
        self.test_get_report_rule_value_error()


class TestListReportEvaluations:
    """
    Test Class for list_report_evaluations
    """

    @responses.activate
    def test_list_report_evaluations_all_params(self):
        """
        list_report_evaluations()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/evaluations')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "report_id": "report_id", "home_account_id": "home_account_id", "evaluations": [{"report_id": "report_id", "home_account_id": "be200c80cabc456e91139e4152327456", "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "assessment": {"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}, "evaluate_time": "2022-06-30T11:03:44.630150782Z", "target": {"id": "crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket", "account_id": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "service_name": "cloud-object-storage", "service_display_name": "cloud-object-storage", "resource_crn": "crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket", "resource_name": "mybucket", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}}, "status": "failure", "reason": "One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met", "details": {"properties": [{"property": "property", "property_description": "property_description", "operator": "string_equals", "expected_value": "anyValue", "found_value": "anyValue"}], "provider_info": {"provider_type": "provider_type"}}, "evaluated_by": "abc@ibm.com"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        assessment_id = 'testString'
        assessment_method = 'testString'
        component_id = 'testString'
        target_id = 'testString'
        target_env = 'testString'
        target_name = 'testString'
        status = 'failure'
        start = 'testString'
        limit = 50
        sort = 'assessment_id'
        scope_id = 'testString'
        subscope_id = 'testString'

        # Invoke method
        response = _service.list_report_evaluations(
            instance_id,
            report_id,
            assessment_id=assessment_id,
            assessment_method=assessment_method,
            component_id=component_id,
            target_id=target_id,
            target_env=target_env,
            target_name=target_name,
            status=status,
            start=start,
            limit=limit,
            sort=sort,
            scope_id=scope_id,
            subscope_id=subscope_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'assessment_id={}'.format(assessment_id) in query_string
        assert 'assessment_method={}'.format(assessment_method) in query_string
        assert 'component_id={}'.format(component_id) in query_string
        assert 'target_id={}'.format(target_id) in query_string
        assert 'target_env={}'.format(target_env) in query_string
        assert 'target_name={}'.format(target_name) in query_string
        assert 'status={}'.format(status) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'scope_id={}'.format(scope_id) in query_string
        assert 'subscope_id={}'.format(subscope_id) in query_string

    def test_list_report_evaluations_all_params_with_retries(self):
        # Enable retries and run test_list_report_evaluations_all_params.
        _service.enable_retries()
        self.test_list_report_evaluations_all_params()

        # Disable retries and run test_list_report_evaluations_all_params.
        _service.disable_retries()
        self.test_list_report_evaluations_all_params()

    @responses.activate
    def test_list_report_evaluations_required_params(self):
        """
        test_list_report_evaluations_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/evaluations')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "report_id": "report_id", "home_account_id": "home_account_id", "evaluations": [{"report_id": "report_id", "home_account_id": "be200c80cabc456e91139e4152327456", "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "assessment": {"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}, "evaluate_time": "2022-06-30T11:03:44.630150782Z", "target": {"id": "crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket", "account_id": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "service_name": "cloud-object-storage", "service_display_name": "cloud-object-storage", "resource_crn": "crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket", "resource_name": "mybucket", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}}, "status": "failure", "reason": "One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met", "details": {"properties": [{"property": "property", "property_description": "property_description", "operator": "string_equals", "expected_value": "anyValue", "found_value": "anyValue"}], "provider_info": {"provider_type": "provider_type"}}, "evaluated_by": "abc@ibm.com"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Invoke method
        response = _service.list_report_evaluations(
            instance_id,
            report_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_report_evaluations_required_params_with_retries(self):
        # Enable retries and run test_list_report_evaluations_required_params.
        _service.enable_retries()
        self.test_list_report_evaluations_required_params()

        # Disable retries and run test_list_report_evaluations_required_params.
        _service.disable_retries()
        self.test_list_report_evaluations_required_params()

    @responses.activate
    def test_list_report_evaluations_value_error(self):
        """
        test_list_report_evaluations_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/evaluations')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "report_id": "report_id", "home_account_id": "home_account_id", "evaluations": [{"report_id": "report_id", "home_account_id": "be200c80cabc456e91139e4152327456", "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "assessment": {"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}, "evaluate_time": "2022-06-30T11:03:44.630150782Z", "target": {"id": "crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket", "account_id": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "service_name": "cloud-object-storage", "service_display_name": "cloud-object-storage", "resource_crn": "crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket", "resource_name": "mybucket", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}}, "status": "failure", "reason": "One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met", "details": {"properties": [{"property": "property", "property_description": "property_description", "operator": "string_equals", "expected_value": "anyValue", "found_value": "anyValue"}], "provider_info": {"provider_type": "provider_type"}}, "evaluated_by": "abc@ibm.com"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "report_id": report_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_report_evaluations(**req_copy)

    def test_list_report_evaluations_value_error_with_retries(self):
        # Enable retries and run test_list_report_evaluations_value_error.
        _service.enable_retries()
        self.test_list_report_evaluations_value_error()

        # Disable retries and run test_list_report_evaluations_value_error.
        _service.disable_retries()
        self.test_list_report_evaluations_value_error()

    @responses.activate
    def test_list_report_evaluations_with_pager_get_next(self):
        """
        test_list_report_evaluations_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/evaluations')
        mock_response1 = '{"next":{"start":"1"},"evaluations":[{"report_id":"report_id","home_account_id":"be200c80cabc456e91139e4152327456","component_id":"cloud-object_storage","component_name":"cloud-object_storage","assessment":{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]},"evaluate_time":"2022-06-30T11:03:44.630150782Z","target":{"id":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","account_id":"59bcbfa6ea2f006b4ed7094c1a08dcdd","service_name":"cloud-object-storage","service_display_name":"cloud-object-storage","resource_crn":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","resource_name":"mybucket","tags":{"user":["user"],"access":["access"],"service":["service"]}},"status":"failure","reason":"One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met","details":{"properties":[{"property":"property","property_description":"property_description","operator":"string_equals","expected_value":"anyValue","found_value":"anyValue"}],"provider_info":{"provider_type":"provider_type"}},"evaluated_by":"abc@ibm.com"}],"total_count":2,"limit":1}'
        mock_response2 = '{"evaluations":[{"report_id":"report_id","home_account_id":"be200c80cabc456e91139e4152327456","component_id":"cloud-object_storage","component_name":"cloud-object_storage","assessment":{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]},"evaluate_time":"2022-06-30T11:03:44.630150782Z","target":{"id":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","account_id":"59bcbfa6ea2f006b4ed7094c1a08dcdd","service_name":"cloud-object-storage","service_display_name":"cloud-object-storage","resource_crn":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","resource_name":"mybucket","tags":{"user":["user"],"access":["access"],"service":["service"]}},"status":"failure","reason":"One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met","details":{"properties":[{"property":"property","property_description":"property_description","operator":"string_equals","expected_value":"anyValue","found_value":"anyValue"}],"provider_info":{"provider_type":"provider_type"}},"evaluated_by":"abc@ibm.com"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = ReportEvaluationsPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id='testString',
            assessment_id='testString',
            assessment_method='testString',
            component_id='testString',
            target_id='testString',
            target_env='testString',
            target_name='testString',
            status='failure',
            limit=10,
            sort='assessment_id',
            scope_id='testString',
            subscope_id='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_report_evaluations_with_pager_get_all(self):
        """
        test_list_report_evaluations_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/evaluations')
        mock_response1 = '{"next":{"start":"1"},"evaluations":[{"report_id":"report_id","home_account_id":"be200c80cabc456e91139e4152327456","component_id":"cloud-object_storage","component_name":"cloud-object_storage","assessment":{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]},"evaluate_time":"2022-06-30T11:03:44.630150782Z","target":{"id":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","account_id":"59bcbfa6ea2f006b4ed7094c1a08dcdd","service_name":"cloud-object-storage","service_display_name":"cloud-object-storage","resource_crn":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","resource_name":"mybucket","tags":{"user":["user"],"access":["access"],"service":["service"]}},"status":"failure","reason":"One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met","details":{"properties":[{"property":"property","property_description":"property_description","operator":"string_equals","expected_value":"anyValue","found_value":"anyValue"}],"provider_info":{"provider_type":"provider_type"}},"evaluated_by":"abc@ibm.com"}],"total_count":2,"limit":1}'
        mock_response2 = '{"evaluations":[{"report_id":"report_id","home_account_id":"be200c80cabc456e91139e4152327456","component_id":"cloud-object_storage","component_name":"cloud-object_storage","assessment":{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]},"evaluate_time":"2022-06-30T11:03:44.630150782Z","target":{"id":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","account_id":"59bcbfa6ea2f006b4ed7094c1a08dcdd","service_name":"cloud-object-storage","service_display_name":"cloud-object-storage","resource_crn":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","resource_name":"mybucket","tags":{"user":["user"],"access":["access"],"service":["service"]}},"status":"failure","reason":"One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met","details":{"properties":[{"property":"property","property_description":"property_description","operator":"string_equals","expected_value":"anyValue","found_value":"anyValue"}],"provider_info":{"provider_type":"provider_type"}},"evaluated_by":"abc@ibm.com"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = ReportEvaluationsPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id='testString',
            assessment_id='testString',
            assessment_method='testString',
            component_id='testString',
            target_id='testString',
            target_env='testString',
            target_name='testString',
            status='failure',
            limit=10,
            sort='assessment_id',
            scope_id='testString',
            subscope_id='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestListReportResources:
    """
    Test Class for list_report_resources
    """

    @responses.activate
    def test_list_report_resources_all_params(self):
        """
        list_report_resources()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/resources')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "report_id": "report_id", "home_account_id": "home_account_id", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135, "service_name": "pm-20", "instance_crn": "instance_crn"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        id = 'testString'
        resource_name = 'testString'
        account_id = 'testString'
        component_id = 'testString'
        status = 'compliant'
        sort = 'account_id'
        start = 'testString'
        limit = 50
        scope_id = 'testString'
        subscope_id = 'testString'

        # Invoke method
        response = _service.list_report_resources(
            instance_id,
            report_id,
            id=id,
            resource_name=resource_name,
            account_id=account_id,
            component_id=component_id,
            status=status,
            sort=sort,
            start=start,
            limit=limit,
            scope_id=scope_id,
            subscope_id=subscope_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'id={}'.format(id) in query_string
        assert 'resource_name={}'.format(resource_name) in query_string
        assert 'account_id={}'.format(account_id) in query_string
        assert 'component_id={}'.format(component_id) in query_string
        assert 'status={}'.format(status) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'scope_id={}'.format(scope_id) in query_string
        assert 'subscope_id={}'.format(subscope_id) in query_string

    def test_list_report_resources_all_params_with_retries(self):
        # Enable retries and run test_list_report_resources_all_params.
        _service.enable_retries()
        self.test_list_report_resources_all_params()

        # Disable retries and run test_list_report_resources_all_params.
        _service.disable_retries()
        self.test_list_report_resources_all_params()

    @responses.activate
    def test_list_report_resources_required_params(self):
        """
        test_list_report_resources_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/resources')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "report_id": "report_id", "home_account_id": "home_account_id", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135, "service_name": "pm-20", "instance_crn": "instance_crn"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Invoke method
        response = _service.list_report_resources(
            instance_id,
            report_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_report_resources_required_params_with_retries(self):
        # Enable retries and run test_list_report_resources_required_params.
        _service.enable_retries()
        self.test_list_report_resources_required_params()

        # Disable retries and run test_list_report_resources_required_params.
        _service.disable_retries()
        self.test_list_report_resources_required_params()

    @responses.activate
    def test_list_report_resources_value_error(self):
        """
        test_list_report_resources_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/resources')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "report_id": "report_id", "home_account_id": "home_account_id", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "home_account_id": "2411ffdc16844b07b42521c3443f456d", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "component_id": "cloud-object_storage", "component_name": "cloud-object_storage", "environment": "ibm cloud", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "skipped_count": 7, "completed_count": 135, "service_name": "pm-20", "instance_crn": "instance_crn"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "report_id": report_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_report_resources(**req_copy)

    def test_list_report_resources_value_error_with_retries(self):
        # Enable retries and run test_list_report_resources_value_error.
        _service.enable_retries()
        self.test_list_report_resources_value_error()

        # Disable retries and run test_list_report_resources_value_error.
        _service.disable_retries()
        self.test_list_report_resources_value_error()

    @responses.activate
    def test_list_report_resources_with_pager_get_next(self):
        """
        test_list_report_resources_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/resources')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"resources":[{"report_id":"30b434b3-cb08-4845-af10-7a8fc682b6a8","home_account_id":"2411ffdc16844b07b42521c3443f456d","id":"crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::","resource_name":"jeff\'s key","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"component_id":"cloud-object_storage","component_name":"cloud-object_storage","environment":"ibm cloud","tags":{"user":["user"],"access":["access"],"service":["service"]},"status":"compliant","total_count":140,"pass_count":123,"failure_count":12,"error_count":5,"skipped_count":7,"completed_count":135,"service_name":"pm-20","instance_crn":"instance_crn"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"report_id":"30b434b3-cb08-4845-af10-7a8fc682b6a8","home_account_id":"2411ffdc16844b07b42521c3443f456d","id":"crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::","resource_name":"jeff\'s key","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"component_id":"cloud-object_storage","component_name":"cloud-object_storage","environment":"ibm cloud","tags":{"user":["user"],"access":["access"],"service":["service"]},"status":"compliant","total_count":140,"pass_count":123,"failure_count":12,"error_count":5,"skipped_count":7,"completed_count":135,"service_name":"pm-20","instance_crn":"instance_crn"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = ReportResourcesPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id='testString',
            id='testString',
            resource_name='testString',
            account_id='testString',
            component_id='testString',
            status='compliant',
            sort='account_id',
            limit=10,
            scope_id='testString',
            subscope_id='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_report_resources_with_pager_get_all(self):
        """
        test_list_report_resources_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/resources')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"resources":[{"report_id":"30b434b3-cb08-4845-af10-7a8fc682b6a8","home_account_id":"2411ffdc16844b07b42521c3443f456d","id":"crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::","resource_name":"jeff\'s key","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"component_id":"cloud-object_storage","component_name":"cloud-object_storage","environment":"ibm cloud","tags":{"user":["user"],"access":["access"],"service":["service"]},"status":"compliant","total_count":140,"pass_count":123,"failure_count":12,"error_count":5,"skipped_count":7,"completed_count":135,"service_name":"pm-20","instance_crn":"instance_crn"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"report_id":"30b434b3-cb08-4845-af10-7a8fc682b6a8","home_account_id":"2411ffdc16844b07b42521c3443f456d","id":"crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::","resource_name":"jeff\'s key","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"component_id":"cloud-object_storage","component_name":"cloud-object_storage","environment":"ibm cloud","tags":{"user":["user"],"access":["access"],"service":["service"]},"status":"compliant","total_count":140,"pass_count":123,"failure_count":12,"error_count":5,"skipped_count":7,"completed_count":135,"service_name":"pm-20","instance_crn":"instance_crn"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = ReportResourcesPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id='testString',
            id='testString',
            resource_name='testString',
            account_id='testString',
            component_id='testString',
            status='compliant',
            sort='account_id',
            limit=10,
            scope_id='testString',
            subscope_id='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetReportTags:
    """
    Test Class for get_report_tags
    """

    @responses.activate
    def test_get_report_tags_all_params(self):
        """
        get_report_tags()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/tags')
        mock_response = '{"report_id": "report_id", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Invoke method
        response = _service.get_report_tags(
            instance_id,
            report_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_report_tags_all_params_with_retries(self):
        # Enable retries and run test_get_report_tags_all_params.
        _service.enable_retries()
        self.test_get_report_tags_all_params()

        # Disable retries and run test_get_report_tags_all_params.
        _service.disable_retries()
        self.test_get_report_tags_all_params()

    @responses.activate
    def test_get_report_tags_value_error(self):
        """
        test_get_report_tags_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/tags')
        mock_response = '{"report_id": "report_id", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "report_id": report_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_report_tags(**req_copy)

    def test_get_report_tags_value_error_with_retries(self):
        # Enable retries and run test_get_report_tags_value_error.
        _service.enable_retries()
        self.test_get_report_tags_value_error()

        # Disable retries and run test_get_report_tags_value_error.
        _service.disable_retries()
        self.test_get_report_tags_value_error()


class TestGetReportViolationsDrift:
    """
    Test Class for get_report_violations_drift
    """

    @responses.activate
    def test_get_report_violations_drift_all_params(self):
        """
        get_report_violations_drift()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/violations_drift')
        mock_response = '{"home_account_id": "home_account_id", "report_group_id": "report_group_id", "data_points": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "report_group_id": "55b6-b3A4-432250b84669", "scan_time": "2022-08-15T12:30:01Z", "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        scan_time_duration = 0
        scope_id = 'testString'
        subscope_id = 'testString'

        # Invoke method
        response = _service.get_report_violations_drift(
            instance_id,
            report_id,
            scan_time_duration=scan_time_duration,
            scope_id=scope_id,
            subscope_id=subscope_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'scan_time_duration={}'.format(scan_time_duration) in query_string
        assert 'scope_id={}'.format(scope_id) in query_string
        assert 'subscope_id={}'.format(subscope_id) in query_string

    def test_get_report_violations_drift_all_params_with_retries(self):
        # Enable retries and run test_get_report_violations_drift_all_params.
        _service.enable_retries()
        self.test_get_report_violations_drift_all_params()

        # Disable retries and run test_get_report_violations_drift_all_params.
        _service.disable_retries()
        self.test_get_report_violations_drift_all_params()

    @responses.activate
    def test_get_report_violations_drift_required_params(self):
        """
        test_get_report_violations_drift_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/violations_drift')
        mock_response = '{"home_account_id": "home_account_id", "report_group_id": "report_group_id", "data_points": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "report_group_id": "55b6-b3A4-432250b84669", "scan_time": "2022-08-15T12:30:01Z", "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Invoke method
        response = _service.get_report_violations_drift(
            instance_id,
            report_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_report_violations_drift_required_params_with_retries(self):
        # Enable retries and run test_get_report_violations_drift_required_params.
        _service.enable_retries()
        self.test_get_report_violations_drift_required_params()

        # Disable retries and run test_get_report_violations_drift_required_params.
        _service.disable_retries()
        self.test_get_report_violations_drift_required_params()

    @responses.activate
    def test_get_report_violations_drift_value_error(self):
        """
        test_get_report_violations_drift_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/violations_drift')
        mock_response = '{"home_account_id": "home_account_id", "report_group_id": "report_group_id", "data_points": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "report_group_id": "55b6-b3A4-432250b84669", "scan_time": "2022-08-15T12:30:01Z", "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "not_applicable_count": 7}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "report_id": report_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_report_violations_drift(**req_copy)

    def test_get_report_violations_drift_value_error_with_retries(self):
        # Enable retries and run test_get_report_violations_drift_value_error.
        _service.enable_retries()
        self.test_get_report_violations_drift_value_error()

        # Disable retries and run test_get_report_violations_drift_value_error.
        _service.disable_retries()
        self.test_get_report_violations_drift_value_error()


class TestListScanReports:
    """
    Test Class for list_scan_reports
    """

    @responses.activate
    def test_list_scan_reports_all_params(self):
        """
        list_scan_reports()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/scan_reports')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "scope_id": "44a5-a292-32114fa73558", "subscope_id": "44a5-a292-32114fa73555", "scan_reports": [{"id": "e44316e3-53bc-449b-a808-c16df680d462", "scan_id": "44a5-a292-32114fa73553", "instance_id": "instance_id", "scope_id": "44a5-a292-32114fa73558", "subscope_id": "44a5-a292-32114fa73555", "status": "completed", "created_on": "2024-05-08T12:30:01.000Z", "format": "pdf", "href": "href"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        scope_id = 'testString'
        subscope_id = 'testString'
        sort = 'status'

        # Invoke method
        response = _service.list_scan_reports(
            instance_id,
            report_id,
            scope_id=scope_id,
            subscope_id=subscope_id,
            sort=sort,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'scope_id={}'.format(scope_id) in query_string
        assert 'subscope_id={}'.format(subscope_id) in query_string
        assert 'sort={}'.format(sort) in query_string

    def test_list_scan_reports_all_params_with_retries(self):
        # Enable retries and run test_list_scan_reports_all_params.
        _service.enable_retries()
        self.test_list_scan_reports_all_params()

        # Disable retries and run test_list_scan_reports_all_params.
        _service.disable_retries()
        self.test_list_scan_reports_all_params()

    @responses.activate
    def test_list_scan_reports_required_params(self):
        """
        test_list_scan_reports_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/scan_reports')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "scope_id": "44a5-a292-32114fa73558", "subscope_id": "44a5-a292-32114fa73555", "scan_reports": [{"id": "e44316e3-53bc-449b-a808-c16df680d462", "scan_id": "44a5-a292-32114fa73553", "instance_id": "instance_id", "scope_id": "44a5-a292-32114fa73558", "subscope_id": "44a5-a292-32114fa73555", "status": "completed", "created_on": "2024-05-08T12:30:01.000Z", "format": "pdf", "href": "href"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Invoke method
        response = _service.list_scan_reports(
            instance_id,
            report_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_scan_reports_required_params_with_retries(self):
        # Enable retries and run test_list_scan_reports_required_params.
        _service.enable_retries()
        self.test_list_scan_reports_required_params()

        # Disable retries and run test_list_scan_reports_required_params.
        _service.disable_retries()
        self.test_list_scan_reports_required_params()

    @responses.activate
    def test_list_scan_reports_value_error(self):
        """
        test_list_scan_reports_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/scan_reports')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "scope_id": "44a5-a292-32114fa73558", "subscope_id": "44a5-a292-32114fa73555", "scan_reports": [{"id": "e44316e3-53bc-449b-a808-c16df680d462", "scan_id": "44a5-a292-32114fa73553", "instance_id": "instance_id", "scope_id": "44a5-a292-32114fa73558", "subscope_id": "44a5-a292-32114fa73555", "status": "completed", "created_on": "2024-05-08T12:30:01.000Z", "format": "pdf", "href": "href"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "report_id": report_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_scan_reports(**req_copy)

    def test_list_scan_reports_value_error_with_retries(self):
        # Enable retries and run test_list_scan_reports_value_error.
        _service.enable_retries()
        self.test_list_scan_reports_value_error()

        # Disable retries and run test_list_scan_reports_value_error.
        _service.disable_retries()
        self.test_list_scan_reports_value_error()


class TestCreateScanReport:
    """
    Test Class for create_scan_report
    """

    @responses.activate
    def test_create_scan_report_all_params(self):
        """
        create_scan_report()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/scan_reports')
        mock_response = '{"id": "id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        format = 'csv'
        scope_id = '132009ff-b982-412e-a110-ad8797e10f84'
        subscope_id = 'c7ddcbcc-6a43-4ab3-b6a7-b2d8f65cd54a'

        # Invoke method
        response = _service.create_scan_report(
            instance_id,
            report_id,
            format,
            scope_id=scope_id,
            subscope_id=subscope_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['format'] == 'csv'
        assert req_body['scope_id'] == '132009ff-b982-412e-a110-ad8797e10f84'
        assert req_body['subscope_id'] == 'c7ddcbcc-6a43-4ab3-b6a7-b2d8f65cd54a'

    def test_create_scan_report_all_params_with_retries(self):
        # Enable retries and run test_create_scan_report_all_params.
        _service.enable_retries()
        self.test_create_scan_report_all_params()

        # Disable retries and run test_create_scan_report_all_params.
        _service.disable_retries()
        self.test_create_scan_report_all_params()

    @responses.activate
    def test_create_scan_report_value_error(self):
        """
        test_create_scan_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/scan_reports')
        mock_response = '{"id": "id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        format = 'csv'
        scope_id = '132009ff-b982-412e-a110-ad8797e10f84'
        subscope_id = 'c7ddcbcc-6a43-4ab3-b6a7-b2d8f65cd54a'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "report_id": report_id,
            "format": format,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_scan_report(**req_copy)

    def test_create_scan_report_value_error_with_retries(self):
        # Enable retries and run test_create_scan_report_value_error.
        _service.enable_retries()
        self.test_create_scan_report_value_error()

        # Disable retries and run test_create_scan_report_value_error.
        _service.disable_retries()
        self.test_create_scan_report_value_error()


class TestGetScanReport:
    """
    Test Class for get_scan_report
    """

    @responses.activate
    def test_get_scan_report_all_params(self):
        """
        get_scan_report()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/scan_reports/testString')
        mock_response = '{"id": "e44316e3-53bc-449b-a808-c16df680d462", "scan_id": "44a5-a292-32114fa73553", "instance_id": "instance_id", "scope_id": "44a5-a292-32114fa73558", "subscope_id": "44a5-a292-32114fa73555", "status": "completed", "created_on": "2024-05-08T12:30:01.000Z", "format": "pdf", "href": "href"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        job_id = 'testString'

        # Invoke method
        response = _service.get_scan_report(
            instance_id,
            report_id,
            job_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_scan_report_all_params_with_retries(self):
        # Enable retries and run test_get_scan_report_all_params.
        _service.enable_retries()
        self.test_get_scan_report_all_params()

        # Disable retries and run test_get_scan_report_all_params.
        _service.disable_retries()
        self.test_get_scan_report_all_params()

    @responses.activate
    def test_get_scan_report_value_error(self):
        """
        test_get_scan_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/scan_reports/testString')
        mock_response = '{"id": "e44316e3-53bc-449b-a808-c16df680d462", "scan_id": "44a5-a292-32114fa73553", "instance_id": "instance_id", "scope_id": "44a5-a292-32114fa73558", "subscope_id": "44a5-a292-32114fa73555", "status": "completed", "created_on": "2024-05-08T12:30:01.000Z", "format": "pdf", "href": "href"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        job_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "report_id": report_id,
            "job_id": job_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_scan_report(**req_copy)

    def test_get_scan_report_value_error_with_retries(self):
        # Enable retries and run test_get_scan_report_value_error.
        _service.enable_retries()
        self.test_get_scan_report_value_error()

        # Disable retries and run test_get_scan_report_value_error.
        _service.disable_retries()
        self.test_get_scan_report_value_error()


class TestGetScanReportDownloadFile:
    """
    Test Class for get_scan_report_download_file
    """

    @responses.activate
    def test_get_scan_report_download_file_all_params(self):
        """
        get_scan_report_download_file()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/scan_reports/testString/download')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/csv',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        job_id = 'testString'
        accept = 'application/csv'

        # Invoke method
        response = _service.get_scan_report_download_file(
            instance_id,
            report_id,
            job_id,
            accept=accept,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_scan_report_download_file_all_params_with_retries(self):
        # Enable retries and run test_get_scan_report_download_file_all_params.
        _service.enable_retries()
        self.test_get_scan_report_download_file_all_params()

        # Disable retries and run test_get_scan_report_download_file_all_params.
        _service.disable_retries()
        self.test_get_scan_report_download_file_all_params()

    @responses.activate
    def test_get_scan_report_download_file_required_params(self):
        """
        test_get_scan_report_download_file_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/scan_reports/testString/download')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/csv',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        job_id = 'testString'

        # Invoke method
        response = _service.get_scan_report_download_file(
            instance_id,
            report_id,
            job_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_scan_report_download_file_required_params_with_retries(self):
        # Enable retries and run test_get_scan_report_download_file_required_params.
        _service.enable_retries()
        self.test_get_scan_report_download_file_required_params()

        # Disable retries and run test_get_scan_report_download_file_required_params.
        _service.disable_retries()
        self.test_get_scan_report_download_file_required_params()

    @responses.activate
    def test_get_scan_report_download_file_value_error(self):
        """
        test_get_scan_report_download_file_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/reports/testString/scan_reports/testString/download')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/csv',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        report_id = 'testString'
        job_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "report_id": report_id,
            "job_id": job_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_scan_report_download_file(**req_copy)

    def test_get_scan_report_download_file_value_error_with_retries(self):
        # Enable retries and run test_get_scan_report_download_file_value_error.
        _service.enable_retries()
        self.test_get_scan_report_download_file_value_error()

        # Disable retries and run test_get_scan_report_download_file_value_error.
        _service.disable_retries()
        self.test_get_scan_report_download_file_value_error()


# endregion
##############################################################################
# End of Service: Report
##############################################################################

##############################################################################
# Start of Service: Rule
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecurityAndComplianceCenterApiV3.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecurityAndComplianceCenterApiV3)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecurityAndComplianceCenterApiV3.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListRules:
    """
    Test Class for list_rules
    """

    @responses.activate
    def test_list_rules_all_params(self):
        """
        list_rules()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "rules": [{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "anyValue"}], "ref": "ref"}, "required_config": {"description": "description", "property": "property", "operator": "string_equals", "value": "anyValue"}, "labels": ["labels"]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        limit = 50
        start = 'testString'
        type = 'system_defined'
        search = 'testString'
        service_name = 'testString'
        sort = 'updated_on'

        # Invoke method
        response = _service.list_rules(
            instance_id,
            limit=limit,
            start=start,
            type=type,
            search=search,
            service_name=service_name,
            sort=sort,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'search={}'.format(search) in query_string
        assert 'service_name={}'.format(service_name) in query_string
        assert 'sort={}'.format(sort) in query_string

    def test_list_rules_all_params_with_retries(self):
        # Enable retries and run test_list_rules_all_params.
        _service.enable_retries()
        self.test_list_rules_all_params()

        # Disable retries and run test_list_rules_all_params.
        _service.disable_retries()
        self.test_list_rules_all_params()

    @responses.activate
    def test_list_rules_required_params(self):
        """
        test_list_rules_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "rules": [{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "anyValue"}], "ref": "ref"}, "required_config": {"description": "description", "property": "property", "operator": "string_equals", "value": "anyValue"}, "labels": ["labels"]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Invoke method
        response = _service.list_rules(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_rules_required_params_with_retries(self):
        # Enable retries and run test_list_rules_required_params.
        _service.enable_retries()
        self.test_list_rules_required_params()

        # Disable retries and run test_list_rules_required_params.
        _service.disable_retries()
        self.test_list_rules_required_params()

    @responses.activate
    def test_list_rules_value_error(self):
        """
        test_list_rules_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "rules": [{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "anyValue"}], "ref": "ref"}, "required_config": {"description": "description", "property": "property", "operator": "string_equals", "value": "anyValue"}, "labels": ["labels"]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_rules(**req_copy)

    def test_list_rules_value_error_with_retries(self):
        # Enable retries and run test_list_rules_value_error.
        _service.enable_retries()
        self.test_list_rules_value_error()

        # Disable retries and run test_list_rules_value_error.
        _service.disable_retries()
        self.test_list_rules_value_error()

    @responses.activate
    def test_list_rules_with_pager_get_next(self):
        """
        test_list_rules_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"rules":[{"created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","id":"id","account_id":"account_id","description":"description","type":"user_defined","version":"version","import":{"parameters":[{"name":"name","display_name":"display_name","description":"description","type":"string"}]},"target":{"service_name":"service_name","service_display_name":"service_display_name","resource_kind":"resource_kind","additional_target_attributes":[{"name":"name","operator":"string_equals","value":"anyValue"}],"ref":"ref"},"required_config":{"description":"description","property":"property","operator":"string_equals","value":"anyValue"},"labels":["labels"]}]}'
        mock_response2 = '{"total_count":2,"limit":1,"rules":[{"created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","id":"id","account_id":"account_id","description":"description","type":"user_defined","version":"version","import":{"parameters":[{"name":"name","display_name":"display_name","description":"description","type":"string"}]},"target":{"service_name":"service_name","service_display_name":"service_display_name","resource_kind":"resource_kind","additional_target_attributes":[{"name":"name","operator":"string_equals","value":"anyValue"}],"ref":"ref"},"required_config":{"description":"description","property":"property","operator":"string_equals","value":"anyValue"},"labels":["labels"]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = RulesPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            limit=10,
            type='system_defined',
            search='testString',
            service_name='testString',
            sort='updated_on',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_rules_with_pager_get_all(self):
        """
        test_list_rules_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"rules":[{"created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","id":"id","account_id":"account_id","description":"description","type":"user_defined","version":"version","import":{"parameters":[{"name":"name","display_name":"display_name","description":"description","type":"string"}]},"target":{"service_name":"service_name","service_display_name":"service_display_name","resource_kind":"resource_kind","additional_target_attributes":[{"name":"name","operator":"string_equals","value":"anyValue"}],"ref":"ref"},"required_config":{"description":"description","property":"property","operator":"string_equals","value":"anyValue"},"labels":["labels"]}]}'
        mock_response2 = '{"total_count":2,"limit":1,"rules":[{"created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","id":"id","account_id":"account_id","description":"description","type":"user_defined","version":"version","import":{"parameters":[{"name":"name","display_name":"display_name","description":"description","type":"string"}]},"target":{"service_name":"service_name","service_display_name":"service_display_name","resource_kind":"resource_kind","additional_target_attributes":[{"name":"name","operator":"string_equals","value":"anyValue"}],"ref":"ref"},"required_config":{"description":"description","property":"property","operator":"string_equals","value":"anyValue"},"labels":["labels"]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = RulesPager(
            client=_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            limit=10,
            type='system_defined',
            search='testString',
            service_name='testString',
            sort='updated_on',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateRule:
    """
    Test Class for create_rule
    """

    @responses.activate
    def test_create_rule_all_params(self):
        """
        create_rule()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "anyValue"}], "ref": "ref"}, "required_config": {"description": "description", "property": "property", "operator": "string_equals", "value": "anyValue"}, "labels": ["labels"]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AdditionalTargetAttribute model
        additional_target_attribute_model = {}
        additional_target_attribute_model['name'] = 'location'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'us-east'

        # Construct a dict representation of a RuleTargetPrototype model
        rule_target_prototype_model = {}
        rule_target_prototype_model['service_name'] = 'cloud-object-storage'
        rule_target_prototype_model['resource_kind'] = 'bucket'
        rule_target_prototype_model['additional_target_attributes'] = [additional_target_attribute_model]

        # Construct a dict representation of a RequiredConfigConditionBase model
        required_config_model = {}
        required_config_model['description'] = 'The Cloud Object Storage rule.'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        # Construct a dict representation of a RuleParameter model
        rule_parameter_model = {}
        rule_parameter_model['name'] = 'hard_quota'
        rule_parameter_model['display_name'] = 'The Cloud Object Storage bucket quota.'
        rule_parameter_model['description'] = 'The maximum bytes that are allocated to the Cloud Object Storage bucket.'
        rule_parameter_model['type'] = 'numeric'

        # Construct a dict representation of a Import model
        import_model = {}
        import_model['parameters'] = [rule_parameter_model]

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        description = 'Example rule'
        target = rule_target_prototype_model
        required_config = required_config_model
        version = '1.0.0'
        import_ = import_model
        labels = []

        # Invoke method
        response = _service.create_rule(
            instance_id,
            description,
            target,
            required_config,
            version=version,
            import_=import_,
            labels=labels,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'Example rule'
        assert req_body['target'] == rule_target_prototype_model
        assert req_body['required_config'] == required_config_model
        assert req_body['version'] == '1.0.0'
        assert req_body['import'] == import_model
        assert req_body['labels'] == []

    def test_create_rule_all_params_with_retries(self):
        # Enable retries and run test_create_rule_all_params.
        _service.enable_retries()
        self.test_create_rule_all_params()

        # Disable retries and run test_create_rule_all_params.
        _service.disable_retries()
        self.test_create_rule_all_params()

    @responses.activate
    def test_create_rule_value_error(self):
        """
        test_create_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "anyValue"}], "ref": "ref"}, "required_config": {"description": "description", "property": "property", "operator": "string_equals", "value": "anyValue"}, "labels": ["labels"]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AdditionalTargetAttribute model
        additional_target_attribute_model = {}
        additional_target_attribute_model['name'] = 'location'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'us-east'

        # Construct a dict representation of a RuleTargetPrototype model
        rule_target_prototype_model = {}
        rule_target_prototype_model['service_name'] = 'cloud-object-storage'
        rule_target_prototype_model['resource_kind'] = 'bucket'
        rule_target_prototype_model['additional_target_attributes'] = [additional_target_attribute_model]

        # Construct a dict representation of a RequiredConfigConditionBase model
        required_config_model = {}
        required_config_model['description'] = 'The Cloud Object Storage rule.'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        # Construct a dict representation of a RuleParameter model
        rule_parameter_model = {}
        rule_parameter_model['name'] = 'hard_quota'
        rule_parameter_model['display_name'] = 'The Cloud Object Storage bucket quota.'
        rule_parameter_model['description'] = 'The maximum bytes that are allocated to the Cloud Object Storage bucket.'
        rule_parameter_model['type'] = 'numeric'

        # Construct a dict representation of a Import model
        import_model = {}
        import_model['parameters'] = [rule_parameter_model]

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        description = 'Example rule'
        target = rule_target_prototype_model
        required_config = required_config_model
        version = '1.0.0'
        import_ = import_model
        labels = []

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "description": description,
            "target": target,
            "required_config": required_config,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_rule(**req_copy)

    def test_create_rule_value_error_with_retries(self):
        # Enable retries and run test_create_rule_value_error.
        _service.enable_retries()
        self.test_create_rule_value_error()

        # Disable retries and run test_create_rule_value_error.
        _service.disable_retries()
        self.test_create_rule_value_error()


class TestGetRule:
    """
    Test Class for get_rule
    """

    @responses.activate
    def test_get_rule_all_params(self):
        """
        get_rule()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules/testString')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "anyValue"}], "ref": "ref"}, "required_config": {"description": "description", "property": "property", "operator": "string_equals", "value": "anyValue"}, "labels": ["labels"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        rule_id = 'testString'

        # Invoke method
        response = _service.get_rule(
            instance_id,
            rule_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_rule_all_params_with_retries(self):
        # Enable retries and run test_get_rule_all_params.
        _service.enable_retries()
        self.test_get_rule_all_params()

        # Disable retries and run test_get_rule_all_params.
        _service.disable_retries()
        self.test_get_rule_all_params()

    @responses.activate
    def test_get_rule_value_error(self):
        """
        test_get_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules/testString')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "anyValue"}], "ref": "ref"}, "required_config": {"description": "description", "property": "property", "operator": "string_equals", "value": "anyValue"}, "labels": ["labels"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_rule(**req_copy)

    def test_get_rule_value_error_with_retries(self):
        # Enable retries and run test_get_rule_value_error.
        _service.enable_retries()
        self.test_get_rule_value_error()

        # Disable retries and run test_get_rule_value_error.
        _service.disable_retries()
        self.test_get_rule_value_error()


class TestReplaceRule:
    """
    Test Class for replace_rule
    """

    @responses.activate
    def test_replace_rule_all_params(self):
        """
        replace_rule()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules/testString')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "anyValue"}], "ref": "ref"}, "required_config": {"description": "description", "property": "property", "operator": "string_equals", "value": "anyValue"}, "labels": ["labels"]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AdditionalTargetAttribute model
        additional_target_attribute_model = {}
        additional_target_attribute_model['name'] = 'location'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'us-south'

        # Construct a dict representation of a RuleTargetPrototype model
        rule_target_prototype_model = {}
        rule_target_prototype_model['service_name'] = 'cloud-object-storage'
        rule_target_prototype_model['resource_kind'] = 'bucket'
        rule_target_prototype_model['additional_target_attributes'] = [additional_target_attribute_model]

        # Construct a dict representation of a RequiredConfigConditionBase model
        required_config_model = {}
        required_config_model['description'] = 'The Cloud Object Storage rule.'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        # Construct a dict representation of a RuleParameter model
        rule_parameter_model = {}
        rule_parameter_model['name'] = 'hard_quota'
        rule_parameter_model['display_name'] = 'The Cloud Object Storage bucket quota.'
        rule_parameter_model['description'] = 'The maximum bytes that are allocated to the Cloud Object Storage bucket.'
        rule_parameter_model['type'] = 'numeric'

        # Construct a dict representation of a Import model
        import_model = {}
        import_model['parameters'] = [rule_parameter_model]

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        rule_id = 'testString'
        if_match = 'testString'
        description = 'Example rule'
        target = rule_target_prototype_model
        required_config = required_config_model
        version = '1.0.1'
        import_ = import_model
        labels = []

        # Invoke method
        response = _service.replace_rule(
            instance_id,
            rule_id,
            if_match,
            description,
            target,
            required_config,
            version=version,
            import_=import_,
            labels=labels,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'Example rule'
        assert req_body['target'] == rule_target_prototype_model
        assert req_body['required_config'] == required_config_model
        assert req_body['version'] == '1.0.1'
        assert req_body['import'] == import_model
        assert req_body['labels'] == []

    def test_replace_rule_all_params_with_retries(self):
        # Enable retries and run test_replace_rule_all_params.
        _service.enable_retries()
        self.test_replace_rule_all_params()

        # Disable retries and run test_replace_rule_all_params.
        _service.disable_retries()
        self.test_replace_rule_all_params()

    @responses.activate
    def test_replace_rule_value_error(self):
        """
        test_replace_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules/testString')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "anyValue"}], "ref": "ref"}, "required_config": {"description": "description", "property": "property", "operator": "string_equals", "value": "anyValue"}, "labels": ["labels"]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AdditionalTargetAttribute model
        additional_target_attribute_model = {}
        additional_target_attribute_model['name'] = 'location'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'us-south'

        # Construct a dict representation of a RuleTargetPrototype model
        rule_target_prototype_model = {}
        rule_target_prototype_model['service_name'] = 'cloud-object-storage'
        rule_target_prototype_model['resource_kind'] = 'bucket'
        rule_target_prototype_model['additional_target_attributes'] = [additional_target_attribute_model]

        # Construct a dict representation of a RequiredConfigConditionBase model
        required_config_model = {}
        required_config_model['description'] = 'The Cloud Object Storage rule.'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        # Construct a dict representation of a RuleParameter model
        rule_parameter_model = {}
        rule_parameter_model['name'] = 'hard_quota'
        rule_parameter_model['display_name'] = 'The Cloud Object Storage bucket quota.'
        rule_parameter_model['description'] = 'The maximum bytes that are allocated to the Cloud Object Storage bucket.'
        rule_parameter_model['type'] = 'numeric'

        # Construct a dict representation of a Import model
        import_model = {}
        import_model['parameters'] = [rule_parameter_model]

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        rule_id = 'testString'
        if_match = 'testString'
        description = 'Example rule'
        target = rule_target_prototype_model
        required_config = required_config_model
        version = '1.0.1'
        import_ = import_model
        labels = []

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "rule_id": rule_id,
            "if_match": if_match,
            "description": description,
            "target": target,
            "required_config": required_config,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_rule(**req_copy)

    def test_replace_rule_value_error_with_retries(self):
        # Enable retries and run test_replace_rule_value_error.
        _service.enable_retries()
        self.test_replace_rule_value_error()

        # Disable retries and run test_replace_rule_value_error.
        _service.disable_retries()
        self.test_replace_rule_value_error()


class TestDeleteRule:
    """
    Test Class for delete_rule
    """

    @responses.activate
    def test_delete_rule_all_params(self):
        """
        delete_rule()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        rule_id = 'testString'

        # Invoke method
        response = _service.delete_rule(
            instance_id,
            rule_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_rule_all_params_with_retries(self):
        # Enable retries and run test_delete_rule_all_params.
        _service.enable_retries()
        self.test_delete_rule_all_params()

        # Disable retries and run test_delete_rule_all_params.
        _service.disable_retries()
        self.test_delete_rule_all_params()

    @responses.activate
    def test_delete_rule_value_error(self):
        """
        test_delete_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/acd7032c-15a3-484f-bf5b-67d41534d940/v3/rules/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'acd7032c-15a3-484f-bf5b-67d41534d940'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_rule(**req_copy)

    def test_delete_rule_value_error_with_retries(self):
        # Enable retries and run test_delete_rule_value_error.
        _service.enable_retries()
        self.test_delete_rule_value_error()

        # Disable retries and run test_delete_rule_value_error.
        _service.disable_retries()
        self.test_delete_rule_value_error()


# endregion
##############################################################################
# End of Service: Rule
##############################################################################

##############################################################################
# Start of Service: Service
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = SecurityAndComplianceCenterApiV3.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SecurityAndComplianceCenterApiV3)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SecurityAndComplianceCenterApiV3.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListServices:
    """
    Test Class for list_services
    """

    @responses.activate
    def test_list_services_all_params(self):
        """
        list_services()
        """
        # Set up mock
        url = preprocess_url('/v3/services')
        mock_response = '{"services": [{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "service_name": "service_name", "service_display_name": "service_display_name", "description": "description", "monitoring_enabled": true, "enforcement_enabled": false, "service_listing_enabled": false, "config_information_point": {"type": "type", "endpoints": [{"host": "host", "path": "path", "region": "region", "advisory_call_limit": 19}]}, "supported_configs": [{"resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "anyValue"}], "properties": [{"name": "name", "description": "description", "type": "string"}], "description": "description", "cip_requires_service_instance": false, "resource_group_support": true, "tagging_support": false, "inherit_tags": true}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_services()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_services_all_params_with_retries(self):
        # Enable retries and run test_list_services_all_params.
        _service.enable_retries()
        self.test_list_services_all_params()

        # Disable retries and run test_list_services_all_params.
        _service.disable_retries()
        self.test_list_services_all_params()


class TestGetService:
    """
    Test Class for get_service
    """

    @responses.activate
    def test_get_service_all_params(self):
        """
        get_service()
        """
        # Set up mock
        url = preprocess_url('/v3/services/cloud-object-storage')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "service_name": "service_name", "service_display_name": "service_display_name", "description": "description", "monitoring_enabled": true, "enforcement_enabled": false, "service_listing_enabled": false, "config_information_point": {"type": "type", "endpoints": [{"host": "host", "path": "path", "region": "region", "advisory_call_limit": 19}]}, "supported_configs": [{"resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "anyValue"}], "properties": [{"name": "name", "description": "description", "type": "string"}], "description": "description", "cip_requires_service_instance": false, "resource_group_support": true, "tagging_support": false, "inherit_tags": true}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        services_name = 'cloud-object-storage'

        # Invoke method
        response = _service.get_service(
            services_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_service_all_params_with_retries(self):
        # Enable retries and run test_get_service_all_params.
        _service.enable_retries()
        self.test_get_service_all_params()

        # Disable retries and run test_get_service_all_params.
        _service.disable_retries()
        self.test_get_service_all_params()

    @responses.activate
    def test_get_service_value_error(self):
        """
        test_get_service_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/services/cloud-object-storage')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "service_name": "service_name", "service_display_name": "service_display_name", "description": "description", "monitoring_enabled": true, "enforcement_enabled": false, "service_listing_enabled": false, "config_information_point": {"type": "type", "endpoints": [{"host": "host", "path": "path", "region": "region", "advisory_call_limit": 19}]}, "supported_configs": [{"resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "anyValue"}], "properties": [{"name": "name", "description": "description", "type": "string"}], "description": "description", "cip_requires_service_instance": false, "resource_group_support": true, "tagging_support": false, "inherit_tags": true}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        services_name = 'cloud-object-storage'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "services_name": services_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_service(**req_copy)

    def test_get_service_value_error_with_retries(self):
        # Enable retries and run test_get_service_value_error.
        _service.enable_retries()
        self.test_get_service_value_error()

        # Disable retries and run test_get_service_value_error.
        _service.disable_retries()
        self.test_get_service_value_error()


# endregion
##############################################################################
# End of Service: Service
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_Account:
    """
    Test Class for Account
    """

    def test_account_serialization(self):
        """
        Test serialization/deserialization for Account
        """

        # Construct a json representation of a Account model
        account_model_json = {}
        account_model_json['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model_json['name'] = 'NIST'
        account_model_json['type'] = 'account_type'

        # Construct a model instance of Account by calling from_dict on the json representation
        account_model = Account.from_dict(account_model_json)
        assert account_model != False

        # Construct a model instance of Account by calling from_dict on the json representation
        account_model_dict = Account.from_dict(account_model_json).__dict__
        account_model2 = Account(**account_model_dict)

        # Verify the model instances are equivalent
        assert account_model == account_model2

        # Convert model instance back to dict and verify no loss of data
        account_model_json2 = account_model.to_dict()
        assert account_model_json2 == account_model_json


class TestModel_AdditionalDetails:
    """
    Test Class for AdditionalDetails
    """

    def test_additional_details_serialization(self):
        """
        Test serialization/deserialization for AdditionalDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        link_model = {}  # Link
        link_model['description'] = 'testString'
        link_model['href'] = 'testString'

        # Construct a json representation of a AdditionalDetails model
        additional_details_model_json = {}
        additional_details_model_json['created_by'] = 'Security and Compliance Center'
        additional_details_model_json['labels'] = ['testString']
        additional_details_model_json['links'] = [link_model]

        # Construct a model instance of AdditionalDetails by calling from_dict on the json representation
        additional_details_model = AdditionalDetails.from_dict(additional_details_model_json)
        assert additional_details_model != False

        # Construct a model instance of AdditionalDetails by calling from_dict on the json representation
        additional_details_model_dict = AdditionalDetails.from_dict(additional_details_model_json).__dict__
        additional_details_model2 = AdditionalDetails(**additional_details_model_dict)

        # Verify the model instances are equivalent
        assert additional_details_model == additional_details_model2

        # Convert model instance back to dict and verify no loss of data
        additional_details_model_json2 = additional_details_model.to_dict()
        assert additional_details_model_json2 == additional_details_model_json


class TestModel_AdditionalProperty:
    """
    Test Class for AdditionalProperty
    """

    def test_additional_property_serialization(self):
        """
        Test serialization/deserialization for AdditionalProperty
        """

        # Construct a json representation of a AdditionalProperty model
        additional_property_model_json = {}
        additional_property_model_json['type'] = 'text'
        additional_property_model_json['display_name'] = 'Workload Protection Instance CRN'

        # Construct a model instance of AdditionalProperty by calling from_dict on the json representation
        additional_property_model = AdditionalProperty.from_dict(additional_property_model_json)
        assert additional_property_model != False

        # Construct a model instance of AdditionalProperty by calling from_dict on the json representation
        additional_property_model_dict = AdditionalProperty.from_dict(additional_property_model_json).__dict__
        additional_property_model2 = AdditionalProperty(**additional_property_model_dict)

        # Verify the model instances are equivalent
        assert additional_property_model == additional_property_model2

        # Convert model instance back to dict and verify no loss of data
        additional_property_model_json2 = additional_property_model.to_dict()
        assert additional_property_model_json2 == additional_property_model_json


class TestModel_AdditionalTargetAttribute:
    """
    Test Class for AdditionalTargetAttribute
    """

    def test_additional_target_attribute_serialization(self):
        """
        Test serialization/deserialization for AdditionalTargetAttribute
        """

        # Construct a json representation of a AdditionalTargetAttribute model
        additional_target_attribute_model_json = {}
        additional_target_attribute_model_json['name'] = 'testString'
        additional_target_attribute_model_json['operator'] = 'string_equals'
        additional_target_attribute_model_json['value'] = 'testString'

        # Construct a model instance of AdditionalTargetAttribute by calling from_dict on the json representation
        additional_target_attribute_model = AdditionalTargetAttribute.from_dict(additional_target_attribute_model_json)
        assert additional_target_attribute_model != False

        # Construct a model instance of AdditionalTargetAttribute by calling from_dict on the json representation
        additional_target_attribute_model_dict = AdditionalTargetAttribute.from_dict(additional_target_attribute_model_json).__dict__
        additional_target_attribute_model2 = AdditionalTargetAttribute(**additional_target_attribute_model_dict)

        # Verify the model instances are equivalent
        assert additional_target_attribute_model == additional_target_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        additional_target_attribute_model_json2 = additional_target_attribute_model.to_dict()
        assert additional_target_attribute_model_json2 == additional_target_attribute_model_json


class TestModel_Assessment:
    """
    Test Class for Assessment
    """

    def test_assessment_serialization(self):
        """
        Test serialization/deserialization for Assessment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        # Construct a json representation of a Assessment model
        assessment_model_json = {}
        assessment_model_json['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model_json['assessment_type'] = 'ibm-cloud-rule'
        assessment_model_json['assessment_method'] = 'ibm-cloud-rule'
        assessment_model_json['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model_json['parameter_count'] = 1
        assessment_model_json['parameters'] = [parameter_model]

        # Construct a model instance of Assessment by calling from_dict on the json representation
        assessment_model = Assessment.from_dict(assessment_model_json)
        assert assessment_model != False

        # Construct a model instance of Assessment by calling from_dict on the json representation
        assessment_model_dict = Assessment.from_dict(assessment_model_json).__dict__
        assessment_model2 = Assessment(**assessment_model_dict)

        # Verify the model instances are equivalent
        assert assessment_model == assessment_model2

        # Convert model instance back to dict and verify no loss of data
        assessment_model_json2 = assessment_model.to_dict()
        assert assessment_model_json2 == assessment_model_json


class TestModel_AssessmentPrototype:
    """
    Test Class for AssessmentPrototype
    """

    def test_assessment_prototype_serialization(self):
        """
        Test serialization/deserialization for AssessmentPrototype
        """

        # Construct a json representation of a AssessmentPrototype model
        assessment_prototype_model_json = {}
        assessment_prototype_model_json['assessment_id'] = 'testString'
        assessment_prototype_model_json['assessment_description'] = 'testString'

        # Construct a model instance of AssessmentPrototype by calling from_dict on the json representation
        assessment_prototype_model = AssessmentPrototype.from_dict(assessment_prototype_model_json)
        assert assessment_prototype_model != False

        # Construct a model instance of AssessmentPrototype by calling from_dict on the json representation
        assessment_prototype_model_dict = AssessmentPrototype.from_dict(assessment_prototype_model_json).__dict__
        assessment_prototype_model2 = AssessmentPrototype(**assessment_prototype_model_dict)

        # Verify the model instances are equivalent
        assert assessment_prototype_model == assessment_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        assessment_prototype_model_json2 = assessment_prototype_model.to_dict()
        assert assessment_prototype_model_json2 == assessment_prototype_model_json


class TestModel_AssessmentWithStats:
    """
    Test Class for AssessmentWithStats
    """

    def test_assessment_with_stats_serialization(self):
        """
        Test serialization/deserialization for AssessmentWithStats
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        # Construct a json representation of a AssessmentWithStats model
        assessment_with_stats_model_json = {}
        assessment_with_stats_model_json['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_with_stats_model_json['assessment_type'] = 'ibm-cloud-rule'
        assessment_with_stats_model_json['assessment_method'] = 'ibm-cloud-rule'
        assessment_with_stats_model_json['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_with_stats_model_json['parameter_count'] = 1
        assessment_with_stats_model_json['parameters'] = [parameter_model]
        assessment_with_stats_model_json['total_count'] = 140
        assessment_with_stats_model_json['pass_count'] = 123
        assessment_with_stats_model_json['failure_count'] = 12
        assessment_with_stats_model_json['error_count'] = 5
        assessment_with_stats_model_json['completed_count'] = 135

        # Construct a model instance of AssessmentWithStats by calling from_dict on the json representation
        assessment_with_stats_model = AssessmentWithStats.from_dict(assessment_with_stats_model_json)
        assert assessment_with_stats_model != False

        # Construct a model instance of AssessmentWithStats by calling from_dict on the json representation
        assessment_with_stats_model_dict = AssessmentWithStats.from_dict(assessment_with_stats_model_json).__dict__
        assessment_with_stats_model2 = AssessmentWithStats(**assessment_with_stats_model_dict)

        # Verify the model instances are equivalent
        assert assessment_with_stats_model == assessment_with_stats_model2

        # Convert model instance back to dict and verify no loss of data
        assessment_with_stats_model_json2 = assessment_with_stats_model.to_dict()
        assert assessment_with_stats_model_json2 == assessment_with_stats_model_json


class TestModel_Attachment:
    """
    Test Class for Attachment
    """

    def test_attachment_serialization(self):
        """
        Test serialization/deserialization for Attachment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_property_model = {}  # ScopePropertyScopeAny
        scope_property_model['name'] = 'testString'
        scope_property_model['value'] = 'testString'

        scope_model = {}  # Scope
        scope_model['id'] = 'testString'
        scope_model['name'] = 'testString'
        scope_model['description'] = 'testString'
        scope_model['environment'] = 'testString'
        scope_model['properties'] = [scope_property_model]
        scope_model['account_id'] = 'testString'
        scope_model['instance_id'] = 'testString'
        scope_model['created_by'] = 'testString'
        scope_model['created_on'] = '2019-01-01T12:00:00Z'
        scope_model['updated_by'] = 'testString'
        scope_model['updated_on'] = '2019-01-01T12:00:00Z'
        scope_model['attachment_count'] = 72.5

        attachment_notifications_controls_model = {}  # AttachmentNotificationsControls
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = ['testString']

        attachment_notifications_model = {}  # AttachmentNotifications
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        # Construct a json representation of a Attachment model
        attachment_model_json = {}
        attachment_model_json['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        attachment_model_json['name'] = 'resource group - Default'
        attachment_model_json['description'] = 'Scoped to the Default resource group'
        attachment_model_json['schedule'] = 'daily'
        attachment_model_json['scope'] = 'testString'
        attachment_model_json['scopes'] = [scope_model]
        attachment_model_json['notifications'] = attachment_notifications_model

        # Construct a model instance of Attachment by calling from_dict on the json representation
        attachment_model = Attachment.from_dict(attachment_model_json)
        assert attachment_model != False

        # Construct a model instance of Attachment by calling from_dict on the json representation
        attachment_model_dict = Attachment.from_dict(attachment_model_json).__dict__
        attachment_model2 = Attachment(**attachment_model_dict)

        # Verify the model instances are equivalent
        assert attachment_model == attachment_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_model_json2 = attachment_model.to_dict()
        assert attachment_model_json2 == attachment_model_json


class TestModel_AttachmentNotifications:
    """
    Test Class for AttachmentNotifications
    """

    def test_attachment_notifications_serialization(self):
        """
        Test serialization/deserialization for AttachmentNotifications
        """

        # Construct dict forms of any model objects needed in order to build this model.

        attachment_notifications_controls_model = {}  # AttachmentNotificationsControls
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = ['testString']

        # Construct a json representation of a AttachmentNotifications model
        attachment_notifications_model_json = {}
        attachment_notifications_model_json['enabled'] = True
        attachment_notifications_model_json['controls'] = attachment_notifications_controls_model

        # Construct a model instance of AttachmentNotifications by calling from_dict on the json representation
        attachment_notifications_model = AttachmentNotifications.from_dict(attachment_notifications_model_json)
        assert attachment_notifications_model != False

        # Construct a model instance of AttachmentNotifications by calling from_dict on the json representation
        attachment_notifications_model_dict = AttachmentNotifications.from_dict(attachment_notifications_model_json).__dict__
        attachment_notifications_model2 = AttachmentNotifications(**attachment_notifications_model_dict)

        # Verify the model instances are equivalent
        assert attachment_notifications_model == attachment_notifications_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_notifications_model_json2 = attachment_notifications_model.to_dict()
        assert attachment_notifications_model_json2 == attachment_notifications_model_json


class TestModel_AttachmentNotificationsControls:
    """
    Test Class for AttachmentNotificationsControls
    """

    def test_attachment_notifications_controls_serialization(self):
        """
        Test serialization/deserialization for AttachmentNotificationsControls
        """

        # Construct a json representation of a AttachmentNotificationsControls model
        attachment_notifications_controls_model_json = {}
        attachment_notifications_controls_model_json['threshold_limit'] = 15
        attachment_notifications_controls_model_json['failed_control_ids'] = ['testString']

        # Construct a model instance of AttachmentNotificationsControls by calling from_dict on the json representation
        attachment_notifications_controls_model = AttachmentNotificationsControls.from_dict(attachment_notifications_controls_model_json)
        assert attachment_notifications_controls_model != False

        # Construct a model instance of AttachmentNotificationsControls by calling from_dict on the json representation
        attachment_notifications_controls_model_dict = AttachmentNotificationsControls.from_dict(attachment_notifications_controls_model_json).__dict__
        attachment_notifications_controls_model2 = AttachmentNotificationsControls(**attachment_notifications_controls_model_dict)

        # Verify the model instances are equivalent
        assert attachment_notifications_controls_model == attachment_notifications_controls_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_notifications_controls_model_json2 = attachment_notifications_controls_model.to_dict()
        assert attachment_notifications_controls_model_json2 == attachment_notifications_controls_model_json


class TestModel_ComparePredefinedProfilesResponse:
    """
    Test Class for ComparePredefinedProfilesResponse
    """

    def test_compare_predefined_profiles_response_serialization(self):
        """
        Test serialization/deserialization for ComparePredefinedProfilesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        compare_profile_response_model = {}  # CompareProfileResponse
        compare_profile_response_model['id'] = 'testString'
        compare_profile_response_model['profile_name'] = 'testString'
        compare_profile_response_model['profile_description'] = 'testString'
        compare_profile_response_model['profile_type'] = 'custom'
        compare_profile_response_model['profile_version'] = 'testString'
        compare_profile_response_model['version_group_label'] = 'testString'
        compare_profile_response_model['latest'] = True
        compare_profile_response_model['created_by'] = 'testString'
        compare_profile_response_model['created_on'] = '2019-01-01T12:00:00Z'
        compare_profile_response_model['updated_by'] = 'testString'
        compare_profile_response_model['updated_on'] = '2019-01-01T12:00:00Z'
        compare_profile_response_model['controls_count'] = 38

        control_doc_model = {}  # ControlDoc
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        control_specification_model = {}  # ControlSpecification
        control_specification_model['id'] = 'testString'
        control_specification_model['responsibility'] = 'testString'
        control_specification_model['component_id'] = 'testString'
        control_specification_model['component_name'] = 'testString'
        control_specification_model['component_type'] = 'testString'
        control_specification_model['environment'] = 'testString'
        control_specification_model['description'] = 'testString'
        control_specification_model['assessments_count'] = 38
        control_specification_model['assessments'] = [assessment_model]

        profile_controls_model = {}  # ProfileControls
        profile_controls_model['control_requirement'] = True
        profile_controls_model['control_library_id'] = 'testString'
        profile_controls_model['control_id'] = 'testString'
        profile_controls_model['control_library_version'] = 'testString'
        profile_controls_model['control_name'] = 'testString'
        profile_controls_model['control_description'] = 'testString'
        profile_controls_model['control_severity'] = 'testString'
        profile_controls_model['control_category'] = 'testString'
        profile_controls_model['control_parent'] = 'testString'
        profile_controls_model['control_docs'] = control_doc_model
        profile_controls_model['control_specifications'] = [control_specification_model]

        control_changes_updated_model = {}  # ControlChangesUpdated
        control_changes_updated_model['current'] = profile_controls_model
        control_changes_updated_model['latest'] = profile_controls_model

        control_changes_model = {}  # ControlChanges
        control_changes_model['total_added'] = 38
        control_changes_model['total_removed'] = 38
        control_changes_model['total_updated'] = 38
        control_changes_model['added'] = [profile_controls_model]
        control_changes_model['removed'] = [profile_controls_model]
        control_changes_model['updated'] = [control_changes_updated_model]

        default_parameters_model = {}  # DefaultParameters
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'testString'

        default_parameters_difference_model = {}  # DefaultParametersDifference
        default_parameters_difference_model['current'] = default_parameters_model
        default_parameters_difference_model['latest'] = default_parameters_model

        default_parameters_changes_model = {}  # DefaultParametersChanges
        default_parameters_changes_model['total_added'] = 38
        default_parameters_changes_model['total_removed'] = 38
        default_parameters_changes_model['total_updated'] = 38
        default_parameters_changes_model['added'] = [default_parameters_model]
        default_parameters_changes_model['removed'] = [default_parameters_model]
        default_parameters_changes_model['updated'] = [default_parameters_difference_model]

        # Construct a json representation of a ComparePredefinedProfilesResponse model
        compare_predefined_profiles_response_model_json = {}
        compare_predefined_profiles_response_model_json['current_predefined_version'] = compare_profile_response_model
        compare_predefined_profiles_response_model_json['latest_predefined_version'] = compare_profile_response_model
        compare_predefined_profiles_response_model_json['controls_changes'] = control_changes_model
        compare_predefined_profiles_response_model_json['default_parameters_changes'] = default_parameters_changes_model

        # Construct a model instance of ComparePredefinedProfilesResponse by calling from_dict on the json representation
        compare_predefined_profiles_response_model = ComparePredefinedProfilesResponse.from_dict(compare_predefined_profiles_response_model_json)
        assert compare_predefined_profiles_response_model != False

        # Construct a model instance of ComparePredefinedProfilesResponse by calling from_dict on the json representation
        compare_predefined_profiles_response_model_dict = ComparePredefinedProfilesResponse.from_dict(compare_predefined_profiles_response_model_json).__dict__
        compare_predefined_profiles_response_model2 = ComparePredefinedProfilesResponse(**compare_predefined_profiles_response_model_dict)

        # Verify the model instances are equivalent
        assert compare_predefined_profiles_response_model == compare_predefined_profiles_response_model2

        # Convert model instance back to dict and verify no loss of data
        compare_predefined_profiles_response_model_json2 = compare_predefined_profiles_response_model.to_dict()
        assert compare_predefined_profiles_response_model_json2 == compare_predefined_profiles_response_model_json


class TestModel_CompareProfileResponse:
    """
    Test Class for CompareProfileResponse
    """

    def test_compare_profile_response_serialization(self):
        """
        Test serialization/deserialization for CompareProfileResponse
        """

        # Construct a json representation of a CompareProfileResponse model
        compare_profile_response_model_json = {}
        compare_profile_response_model_json['id'] = 'testString'
        compare_profile_response_model_json['profile_name'] = 'testString'
        compare_profile_response_model_json['profile_description'] = 'testString'
        compare_profile_response_model_json['profile_type'] = 'custom'
        compare_profile_response_model_json['profile_version'] = 'testString'
        compare_profile_response_model_json['version_group_label'] = 'testString'
        compare_profile_response_model_json['latest'] = True
        compare_profile_response_model_json['created_by'] = 'testString'
        compare_profile_response_model_json['created_on'] = '2019-01-01T12:00:00Z'
        compare_profile_response_model_json['updated_by'] = 'testString'
        compare_profile_response_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        compare_profile_response_model_json['controls_count'] = 38

        # Construct a model instance of CompareProfileResponse by calling from_dict on the json representation
        compare_profile_response_model = CompareProfileResponse.from_dict(compare_profile_response_model_json)
        assert compare_profile_response_model != False

        # Construct a model instance of CompareProfileResponse by calling from_dict on the json representation
        compare_profile_response_model_dict = CompareProfileResponse.from_dict(compare_profile_response_model_json).__dict__
        compare_profile_response_model2 = CompareProfileResponse(**compare_profile_response_model_dict)

        # Verify the model instances are equivalent
        assert compare_profile_response_model == compare_profile_response_model2

        # Convert model instance back to dict and verify no loss of data
        compare_profile_response_model_json2 = compare_profile_response_model.to_dict()
        assert compare_profile_response_model_json2 == compare_profile_response_model_json


class TestModel_ComplianceScore:
    """
    Test Class for ComplianceScore
    """

    def test_compliance_score_serialization(self):
        """
        Test serialization/deserialization for ComplianceScore
        """

        # Construct a json representation of a ComplianceScore model
        compliance_score_model_json = {}
        compliance_score_model_json['passed'] = 1
        compliance_score_model_json['total_count'] = 4
        compliance_score_model_json['percent'] = 25

        # Construct a model instance of ComplianceScore by calling from_dict on the json representation
        compliance_score_model = ComplianceScore.from_dict(compliance_score_model_json)
        assert compliance_score_model != False

        # Construct a model instance of ComplianceScore by calling from_dict on the json representation
        compliance_score_model_dict = ComplianceScore.from_dict(compliance_score_model_json).__dict__
        compliance_score_model2 = ComplianceScore(**compliance_score_model_dict)

        # Verify the model instances are equivalent
        assert compliance_score_model == compliance_score_model2

        # Convert model instance back to dict and verify no loss of data
        compliance_score_model_json2 = compliance_score_model.to_dict()
        assert compliance_score_model_json2 == compliance_score_model_json


class TestModel_ComplianceStats:
    """
    Test Class for ComplianceStats
    """

    def test_compliance_stats_serialization(self):
        """
        Test serialization/deserialization for ComplianceStats
        """

        # Construct a json representation of a ComplianceStats model
        compliance_stats_model_json = {}
        compliance_stats_model_json['status'] = 'compliant'
        compliance_stats_model_json['total_count'] = 150
        compliance_stats_model_json['compliant_count'] = 130
        compliance_stats_model_json['not_compliant_count'] = 5
        compliance_stats_model_json['unable_to_perform_count'] = 5
        compliance_stats_model_json['user_evaluation_required_count'] = 10
        compliance_stats_model_json['not_applicable_count'] = 7

        # Construct a model instance of ComplianceStats by calling from_dict on the json representation
        compliance_stats_model = ComplianceStats.from_dict(compliance_stats_model_json)
        assert compliance_stats_model != False

        # Construct a model instance of ComplianceStats by calling from_dict on the json representation
        compliance_stats_model_dict = ComplianceStats.from_dict(compliance_stats_model_json).__dict__
        compliance_stats_model2 = ComplianceStats(**compliance_stats_model_dict)

        # Verify the model instances are equivalent
        assert compliance_stats_model == compliance_stats_model2

        # Convert model instance back to dict and verify no loss of data
        compliance_stats_model_json2 = compliance_stats_model.to_dict()
        assert compliance_stats_model_json2 == compliance_stats_model_json


class TestModel_ComplianceStatsWithNonCompliant:
    """
    Test Class for ComplianceStatsWithNonCompliant
    """

    def test_compliance_stats_with_non_compliant_serialization(self):
        """
        Test serialization/deserialization for ComplianceStatsWithNonCompliant
        """

        # Construct dict forms of any model objects needed in order to build this model.

        control_summary_model = {}  # ControlSummary
        control_summary_model['id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        control_summary_model['control_name'] = 'ibm-cloud-rule'
        control_summary_model['control_description'] = 'Ensure security questions are registered by the account owner'

        # Construct a json representation of a ComplianceStatsWithNonCompliant model
        compliance_stats_with_non_compliant_model_json = {}
        compliance_stats_with_non_compliant_model_json['status'] = 'compliant'
        compliance_stats_with_non_compliant_model_json['total_count'] = 150
        compliance_stats_with_non_compliant_model_json['compliant_count'] = 130
        compliance_stats_with_non_compliant_model_json['not_compliant_count'] = 5
        compliance_stats_with_non_compliant_model_json['unable_to_perform_count'] = 5
        compliance_stats_with_non_compliant_model_json['user_evaluation_required_count'] = 10
        compliance_stats_with_non_compliant_model_json['not_applicable_count'] = 7
        compliance_stats_with_non_compliant_model_json['not_compliant_controls'] = [control_summary_model]

        # Construct a model instance of ComplianceStatsWithNonCompliant by calling from_dict on the json representation
        compliance_stats_with_non_compliant_model = ComplianceStatsWithNonCompliant.from_dict(compliance_stats_with_non_compliant_model_json)
        assert compliance_stats_with_non_compliant_model != False

        # Construct a model instance of ComplianceStatsWithNonCompliant by calling from_dict on the json representation
        compliance_stats_with_non_compliant_model_dict = ComplianceStatsWithNonCompliant.from_dict(compliance_stats_with_non_compliant_model_json).__dict__
        compliance_stats_with_non_compliant_model2 = ComplianceStatsWithNonCompliant(**compliance_stats_with_non_compliant_model_dict)

        # Verify the model instances are equivalent
        assert compliance_stats_with_non_compliant_model == compliance_stats_with_non_compliant_model2

        # Convert model instance back to dict and verify no loss of data
        compliance_stats_with_non_compliant_model_json2 = compliance_stats_with_non_compliant_model.to_dict()
        assert compliance_stats_with_non_compliant_model_json2 == compliance_stats_with_non_compliant_model_json


class TestModel_ConfigurationInformationPoints:
    """
    Test Class for ConfigurationInformationPoints
    """

    def test_configuration_information_points_serialization(self):
        """
        Test serialization/deserialization for ConfigurationInformationPoints
        """

        # Construct dict forms of any model objects needed in order to build this model.

        endpoint_model = {}  # Endpoint
        endpoint_model['host'] = 'testString'
        endpoint_model['path'] = 'testString'
        endpoint_model['region'] = 'testString'
        endpoint_model['advisory_call_limit'] = 38

        # Construct a json representation of a ConfigurationInformationPoints model
        configuration_information_points_model_json = {}
        configuration_information_points_model_json['type'] = 'testString'
        configuration_information_points_model_json['endpoints'] = [endpoint_model]

        # Construct a model instance of ConfigurationInformationPoints by calling from_dict on the json representation
        configuration_information_points_model = ConfigurationInformationPoints.from_dict(configuration_information_points_model_json)
        assert configuration_information_points_model != False

        # Construct a model instance of ConfigurationInformationPoints by calling from_dict on the json representation
        configuration_information_points_model_dict = ConfigurationInformationPoints.from_dict(configuration_information_points_model_json).__dict__
        configuration_information_points_model2 = ConfigurationInformationPoints(**configuration_information_points_model_dict)

        # Verify the model instances are equivalent
        assert configuration_information_points_model == configuration_information_points_model2

        # Convert model instance back to dict and verify no loss of data
        configuration_information_points_model_json2 = configuration_information_points_model.to_dict()
        assert configuration_information_points_model_json2 == configuration_information_points_model_json


class TestModel_Control:
    """
    Test Class for Control
    """

    def test_control_serialization(self):
        """
        Test serialization/deserialization for Control
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        control_specification_model = {}  # ControlSpecification
        control_specification_model['id'] = 'testString'
        control_specification_model['responsibility'] = 'testString'
        control_specification_model['component_id'] = 'testString'
        control_specification_model['component_name'] = 'testString'
        control_specification_model['component_type'] = 'testString'
        control_specification_model['environment'] = 'testString'
        control_specification_model['description'] = 'testString'
        control_specification_model['assessments_count'] = 38
        control_specification_model['assessments'] = [assessment_model]

        control_doc_model = {}  # ControlDoc
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        # Construct a json representation of a Control model
        control_model_json = {}
        control_model_json['control_name'] = 'testString'
        control_model_json['control_id'] = 'testString'
        control_model_json['control_description'] = 'testString'
        control_model_json['control_category'] = 'testString'
        control_model_json['control_parent'] = 'testString'
        control_model_json['control_severity'] = 'testString'
        control_model_json['control_tags'] = ['testString']
        control_model_json['control_specifications'] = [control_specification_model]
        control_model_json['control_docs'] = control_doc_model
        control_model_json['status'] = 'testString'

        # Construct a model instance of Control by calling from_dict on the json representation
        control_model = Control.from_dict(control_model_json)
        assert control_model != False

        # Construct a model instance of Control by calling from_dict on the json representation
        control_model_dict = Control.from_dict(control_model_json).__dict__
        control_model2 = Control(**control_model_dict)

        # Verify the model instances are equivalent
        assert control_model == control_model2

        # Convert model instance back to dict and verify no loss of data
        control_model_json2 = control_model.to_dict()
        assert control_model_json2 == control_model_json


class TestModel_ControlChanges:
    """
    Test Class for ControlChanges
    """

    def test_control_changes_serialization(self):
        """
        Test serialization/deserialization for ControlChanges
        """

        # Construct dict forms of any model objects needed in order to build this model.

        control_doc_model = {}  # ControlDoc
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        control_specification_model = {}  # ControlSpecification
        control_specification_model['id'] = 'testString'
        control_specification_model['responsibility'] = 'testString'
        control_specification_model['component_id'] = 'testString'
        control_specification_model['component_name'] = 'testString'
        control_specification_model['component_type'] = 'testString'
        control_specification_model['environment'] = 'testString'
        control_specification_model['description'] = 'testString'
        control_specification_model['assessments_count'] = 38
        control_specification_model['assessments'] = [assessment_model]

        profile_controls_model = {}  # ProfileControls
        profile_controls_model['control_requirement'] = True
        profile_controls_model['control_library_id'] = 'testString'
        profile_controls_model['control_id'] = 'testString'
        profile_controls_model['control_library_version'] = 'testString'
        profile_controls_model['control_name'] = 'testString'
        profile_controls_model['control_description'] = 'testString'
        profile_controls_model['control_severity'] = 'testString'
        profile_controls_model['control_category'] = 'testString'
        profile_controls_model['control_parent'] = 'testString'
        profile_controls_model['control_docs'] = control_doc_model
        profile_controls_model['control_specifications'] = [control_specification_model]

        control_changes_updated_model = {}  # ControlChangesUpdated
        control_changes_updated_model['current'] = profile_controls_model
        control_changes_updated_model['latest'] = profile_controls_model

        # Construct a json representation of a ControlChanges model
        control_changes_model_json = {}
        control_changes_model_json['total_added'] = 38
        control_changes_model_json['total_removed'] = 38
        control_changes_model_json['total_updated'] = 38
        control_changes_model_json['added'] = [profile_controls_model]
        control_changes_model_json['removed'] = [profile_controls_model]
        control_changes_model_json['updated'] = [control_changes_updated_model]

        # Construct a model instance of ControlChanges by calling from_dict on the json representation
        control_changes_model = ControlChanges.from_dict(control_changes_model_json)
        assert control_changes_model != False

        # Construct a model instance of ControlChanges by calling from_dict on the json representation
        control_changes_model_dict = ControlChanges.from_dict(control_changes_model_json).__dict__
        control_changes_model2 = ControlChanges(**control_changes_model_dict)

        # Verify the model instances are equivalent
        assert control_changes_model == control_changes_model2

        # Convert model instance back to dict and verify no loss of data
        control_changes_model_json2 = control_changes_model.to_dict()
        assert control_changes_model_json2 == control_changes_model_json


class TestModel_ControlChangesUpdated:
    """
    Test Class for ControlChangesUpdated
    """

    def test_control_changes_updated_serialization(self):
        """
        Test serialization/deserialization for ControlChangesUpdated
        """

        # Construct dict forms of any model objects needed in order to build this model.

        control_doc_model = {}  # ControlDoc
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        control_specification_model = {}  # ControlSpecification
        control_specification_model['id'] = 'testString'
        control_specification_model['responsibility'] = 'testString'
        control_specification_model['component_id'] = 'testString'
        control_specification_model['component_name'] = 'testString'
        control_specification_model['component_type'] = 'testString'
        control_specification_model['environment'] = 'testString'
        control_specification_model['description'] = 'testString'
        control_specification_model['assessments_count'] = 38
        control_specification_model['assessments'] = [assessment_model]

        profile_controls_model = {}  # ProfileControls
        profile_controls_model['control_requirement'] = True
        profile_controls_model['control_library_id'] = 'testString'
        profile_controls_model['control_id'] = 'testString'
        profile_controls_model['control_library_version'] = 'testString'
        profile_controls_model['control_name'] = 'testString'
        profile_controls_model['control_description'] = 'testString'
        profile_controls_model['control_severity'] = 'testString'
        profile_controls_model['control_category'] = 'testString'
        profile_controls_model['control_parent'] = 'testString'
        profile_controls_model['control_docs'] = control_doc_model
        profile_controls_model['control_specifications'] = [control_specification_model]

        # Construct a json representation of a ControlChangesUpdated model
        control_changes_updated_model_json = {}
        control_changes_updated_model_json['current'] = profile_controls_model
        control_changes_updated_model_json['latest'] = profile_controls_model

        # Construct a model instance of ControlChangesUpdated by calling from_dict on the json representation
        control_changes_updated_model = ControlChangesUpdated.from_dict(control_changes_updated_model_json)
        assert control_changes_updated_model != False

        # Construct a model instance of ControlChangesUpdated by calling from_dict on the json representation
        control_changes_updated_model_dict = ControlChangesUpdated.from_dict(control_changes_updated_model_json).__dict__
        control_changes_updated_model2 = ControlChangesUpdated(**control_changes_updated_model_dict)

        # Verify the model instances are equivalent
        assert control_changes_updated_model == control_changes_updated_model2

        # Convert model instance back to dict and verify no loss of data
        control_changes_updated_model_json2 = control_changes_updated_model.to_dict()
        assert control_changes_updated_model_json2 == control_changes_updated_model_json


class TestModel_ControlDoc:
    """
    Test Class for ControlDoc
    """

    def test_control_doc_serialization(self):
        """
        Test serialization/deserialization for ControlDoc
        """

        # Construct a json representation of a ControlDoc model
        control_doc_model_json = {}
        control_doc_model_json['control_docs_id'] = 'testString'
        control_doc_model_json['control_docs_type'] = 'testString'

        # Construct a model instance of ControlDoc by calling from_dict on the json representation
        control_doc_model = ControlDoc.from_dict(control_doc_model_json)
        assert control_doc_model != False

        # Construct a model instance of ControlDoc by calling from_dict on the json representation
        control_doc_model_dict = ControlDoc.from_dict(control_doc_model_json).__dict__
        control_doc_model2 = ControlDoc(**control_doc_model_dict)

        # Verify the model instances are equivalent
        assert control_doc_model == control_doc_model2

        # Convert model instance back to dict and verify no loss of data
        control_doc_model_json2 = control_doc_model.to_dict()
        assert control_doc_model_json2 == control_doc_model_json


class TestModel_ControlLibrary:
    """
    Test Class for ControlLibrary
    """

    def test_control_library_serialization(self):
        """
        Test serialization/deserialization for ControlLibrary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        control_specification_model = {}  # ControlSpecification
        control_specification_model['id'] = 'testString'
        control_specification_model['responsibility'] = 'testString'
        control_specification_model['component_id'] = 'testString'
        control_specification_model['component_name'] = 'testString'
        control_specification_model['component_type'] = 'testString'
        control_specification_model['environment'] = 'testString'
        control_specification_model['description'] = 'testString'
        control_specification_model['assessments_count'] = 38
        control_specification_model['assessments'] = [assessment_model]

        control_doc_model = {}  # ControlDoc
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        control_model = {}  # Control
        control_model['control_name'] = 'testString'
        control_model['control_id'] = 'testString'
        control_model['control_description'] = 'testString'
        control_model['control_category'] = 'testString'
        control_model['control_parent'] = 'testString'
        control_model['control_severity'] = 'testString'
        control_model['control_tags'] = ['testString']
        control_model['control_specifications'] = [control_specification_model]
        control_model['control_docs'] = control_doc_model
        control_model['status'] = 'testString'

        # Construct a json representation of a ControlLibrary model
        control_library_model_json = {}
        control_library_model_json['control_library_name'] = 'testString'
        control_library_model_json['control_library_description'] = 'testString'
        control_library_model_json['control_library_type'] = 'custom'
        control_library_model_json['control_library_version'] = 'testString'
        control_library_model_json['controls'] = [control_model]
        control_library_model_json['id'] = 'testString'
        control_library_model_json['account_id'] = 'testString'
        control_library_model_json['version_group_label'] = 'testString'
        control_library_model_json['latest'] = True
        control_library_model_json['created_by'] = 'testString'
        control_library_model_json['created_on'] = '2019-01-01T12:00:00Z'
        control_library_model_json['updated_by'] = 'testString'
        control_library_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        control_library_model_json['hierarchy_enabled'] = True
        control_library_model_json['controls_count'] = 38
        control_library_model_json['control_parents_count'] = 38

        # Construct a model instance of ControlLibrary by calling from_dict on the json representation
        control_library_model = ControlLibrary.from_dict(control_library_model_json)
        assert control_library_model != False

        # Construct a model instance of ControlLibrary by calling from_dict on the json representation
        control_library_model_dict = ControlLibrary.from_dict(control_library_model_json).__dict__
        control_library_model2 = ControlLibrary(**control_library_model_dict)

        # Verify the model instances are equivalent
        assert control_library_model == control_library_model2

        # Convert model instance back to dict and verify no loss of data
        control_library_model_json2 = control_library_model.to_dict()
        assert control_library_model_json2 == control_library_model_json


class TestModel_ControlLibraryCollection:
    """
    Test Class for ControlLibraryCollection
    """

    def test_control_library_collection_serialization(self):
        """
        Test serialization/deserialization for ControlLibraryCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_first_model = {}  # PageHRefFirst
        page_h_ref_first_model['href'] = 'testString'

        page_h_ref_next_model = {}  # PageHRefNext
        page_h_ref_next_model['href'] = 'testString'
        page_h_ref_next_model['start'] = 'testString'

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        control_specification_model = {}  # ControlSpecification
        control_specification_model['id'] = 'testString'
        control_specification_model['responsibility'] = 'testString'
        control_specification_model['component_id'] = 'testString'
        control_specification_model['component_name'] = 'testString'
        control_specification_model['component_type'] = 'testString'
        control_specification_model['environment'] = 'testString'
        control_specification_model['description'] = 'testString'
        control_specification_model['assessments_count'] = 38
        control_specification_model['assessments'] = [assessment_model]

        control_doc_model = {}  # ControlDoc
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        control_model = {}  # Control
        control_model['control_name'] = 'testString'
        control_model['control_id'] = 'testString'
        control_model['control_description'] = 'testString'
        control_model['control_category'] = 'testString'
        control_model['control_parent'] = 'testString'
        control_model['control_severity'] = 'testString'
        control_model['control_tags'] = ['testString']
        control_model['control_specifications'] = [control_specification_model]
        control_model['control_docs'] = control_doc_model
        control_model['status'] = 'testString'

        control_library_model = {}  # ControlLibrary
        control_library_model['control_library_name'] = 'testString'
        control_library_model['control_library_description'] = 'testString'
        control_library_model['control_library_type'] = 'custom'
        control_library_model['control_library_version'] = 'testString'
        control_library_model['controls'] = [control_model]
        control_library_model['id'] = 'testString'
        control_library_model['account_id'] = 'testString'
        control_library_model['version_group_label'] = 'testString'
        control_library_model['latest'] = True
        control_library_model['created_by'] = 'testString'
        control_library_model['created_on'] = '2019-01-01T12:00:00Z'
        control_library_model['updated_by'] = 'testString'
        control_library_model['updated_on'] = '2019-01-01T12:00:00Z'
        control_library_model['hierarchy_enabled'] = True
        control_library_model['controls_count'] = 38
        control_library_model['control_parents_count'] = 38

        # Construct a json representation of a ControlLibraryCollection model
        control_library_collection_model_json = {}
        control_library_collection_model_json['limit'] = 50
        control_library_collection_model_json['total_count'] = 230
        control_library_collection_model_json['first'] = page_h_ref_first_model
        control_library_collection_model_json['next'] = page_h_ref_next_model
        control_library_collection_model_json['control_libraries'] = [control_library_model]

        # Construct a model instance of ControlLibraryCollection by calling from_dict on the json representation
        control_library_collection_model = ControlLibraryCollection.from_dict(control_library_collection_model_json)
        assert control_library_collection_model != False

        # Construct a model instance of ControlLibraryCollection by calling from_dict on the json representation
        control_library_collection_model_dict = ControlLibraryCollection.from_dict(control_library_collection_model_json).__dict__
        control_library_collection_model2 = ControlLibraryCollection(**control_library_collection_model_dict)

        # Verify the model instances are equivalent
        assert control_library_collection_model == control_library_collection_model2

        # Convert model instance back to dict and verify no loss of data
        control_library_collection_model_json2 = control_library_collection_model.to_dict()
        assert control_library_collection_model_json2 == control_library_collection_model_json


class TestModel_ControlPrototype:
    """
    Test Class for ControlPrototype
    """

    def test_control_prototype_serialization(self):
        """
        Test serialization/deserialization for ControlPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assessment_prototype_model = {}  # AssessmentPrototype
        assessment_prototype_model['assessment_id'] = 'testString'
        assessment_prototype_model['assessment_description'] = 'testString'

        control_specification_prototype_model = {}  # ControlSpecificationPrototype
        control_specification_prototype_model['component_id'] = 'testString'
        control_specification_prototype_model['environment'] = 'ibm-cloud'
        control_specification_prototype_model['control_specification_id'] = 'testString'
        control_specification_prototype_model['control_specification_description'] = 'testString'
        control_specification_prototype_model['assessments'] = [assessment_prototype_model]

        control_doc_model = {}  # ControlDoc
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        # Construct a json representation of a ControlPrototype model
        control_prototype_model_json = {}
        control_prototype_model_json['control_name'] = 'testString'
        control_prototype_model_json['control_description'] = 'testString'
        control_prototype_model_json['control_category'] = 'testString'
        control_prototype_model_json['control_requirement'] = True
        control_prototype_model_json['control_parent'] = 'testString'
        control_prototype_model_json['control_specifications'] = [control_specification_prototype_model]
        control_prototype_model_json['control_docs'] = control_doc_model
        control_prototype_model_json['status'] = 'testString'

        # Construct a model instance of ControlPrototype by calling from_dict on the json representation
        control_prototype_model = ControlPrototype.from_dict(control_prototype_model_json)
        assert control_prototype_model != False

        # Construct a model instance of ControlPrototype by calling from_dict on the json representation
        control_prototype_model_dict = ControlPrototype.from_dict(control_prototype_model_json).__dict__
        control_prototype_model2 = ControlPrototype(**control_prototype_model_dict)

        # Verify the model instances are equivalent
        assert control_prototype_model == control_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        control_prototype_model_json2 = control_prototype_model.to_dict()
        assert control_prototype_model_json2 == control_prototype_model_json


class TestModel_ControlSpecification:
    """
    Test Class for ControlSpecification
    """

    def test_control_specification_serialization(self):
        """
        Test serialization/deserialization for ControlSpecification
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        # Construct a json representation of a ControlSpecification model
        control_specification_model_json = {}
        control_specification_model_json['id'] = 'testString'
        control_specification_model_json['responsibility'] = 'testString'
        control_specification_model_json['component_id'] = 'testString'
        control_specification_model_json['component_name'] = 'testString'
        control_specification_model_json['component_type'] = 'testString'
        control_specification_model_json['environment'] = 'testString'
        control_specification_model_json['description'] = 'testString'
        control_specification_model_json['assessments_count'] = 38
        control_specification_model_json['assessments'] = [assessment_model]

        # Construct a model instance of ControlSpecification by calling from_dict on the json representation
        control_specification_model = ControlSpecification.from_dict(control_specification_model_json)
        assert control_specification_model != False

        # Construct a model instance of ControlSpecification by calling from_dict on the json representation
        control_specification_model_dict = ControlSpecification.from_dict(control_specification_model_json).__dict__
        control_specification_model2 = ControlSpecification(**control_specification_model_dict)

        # Verify the model instances are equivalent
        assert control_specification_model == control_specification_model2

        # Convert model instance back to dict and verify no loss of data
        control_specification_model_json2 = control_specification_model.to_dict()
        assert control_specification_model_json2 == control_specification_model_json


class TestModel_ControlSpecificationPrototype:
    """
    Test Class for ControlSpecificationPrototype
    """

    def test_control_specification_prototype_serialization(self):
        """
        Test serialization/deserialization for ControlSpecificationPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assessment_prototype_model = {}  # AssessmentPrototype
        assessment_prototype_model['assessment_id'] = 'testString'
        assessment_prototype_model['assessment_description'] = 'testString'

        # Construct a json representation of a ControlSpecificationPrototype model
        control_specification_prototype_model_json = {}
        control_specification_prototype_model_json['component_id'] = 'testString'
        control_specification_prototype_model_json['environment'] = 'ibm-cloud'
        control_specification_prototype_model_json['control_specification_id'] = 'testString'
        control_specification_prototype_model_json['control_specification_description'] = 'testString'
        control_specification_prototype_model_json['assessments'] = [assessment_prototype_model]

        # Construct a model instance of ControlSpecificationPrototype by calling from_dict on the json representation
        control_specification_prototype_model = ControlSpecificationPrototype.from_dict(control_specification_prototype_model_json)
        assert control_specification_prototype_model != False

        # Construct a model instance of ControlSpecificationPrototype by calling from_dict on the json representation
        control_specification_prototype_model_dict = ControlSpecificationPrototype.from_dict(control_specification_prototype_model_json).__dict__
        control_specification_prototype_model2 = ControlSpecificationPrototype(**control_specification_prototype_model_dict)

        # Verify the model instances are equivalent
        assert control_specification_prototype_model == control_specification_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        control_specification_prototype_model_json2 = control_specification_prototype_model.to_dict()
        assert control_specification_prototype_model_json2 == control_specification_prototype_model_json


class TestModel_ControlSpecificationWithStats:
    """
    Test Class for ControlSpecificationWithStats
    """

    def test_control_specification_with_stats_serialization(self):
        """
        Test serialization/deserialization for ControlSpecificationWithStats
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_with_stats_model = {}  # AssessmentWithStats
        assessment_with_stats_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_with_stats_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_with_stats_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_with_stats_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_with_stats_model['parameter_count'] = 1
        assessment_with_stats_model['parameters'] = [parameter_model]
        assessment_with_stats_model['total_count'] = 140
        assessment_with_stats_model['pass_count'] = 123
        assessment_with_stats_model['failure_count'] = 12
        assessment_with_stats_model['error_count'] = 5
        assessment_with_stats_model['completed_count'] = 135

        # Construct a json representation of a ControlSpecificationWithStats model
        control_specification_with_stats_model_json = {}
        control_specification_with_stats_model_json['control_specification_id'] = '18d32a4430e54c81a6668952609763b2'
        control_specification_with_stats_model_json['control_specification_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        control_specification_with_stats_model_json['component_id'] = 'cloud-object_storage'
        control_specification_with_stats_model_json['component_name'] = 'cloud-object_storage'
        control_specification_with_stats_model_json['environment'] = 'ibm cloud'
        control_specification_with_stats_model_json['responsibility'] = 'user'
        control_specification_with_stats_model_json['assessments'] = [assessment_with_stats_model]
        control_specification_with_stats_model_json['status'] = 'compliant'
        control_specification_with_stats_model_json['total_count'] = 150
        control_specification_with_stats_model_json['compliant_count'] = 130
        control_specification_with_stats_model_json['not_compliant_count'] = 5
        control_specification_with_stats_model_json['unable_to_perform_count'] = 5
        control_specification_with_stats_model_json['user_evaluation_required_count'] = 10
        control_specification_with_stats_model_json['not_applicable_count'] = 7

        # Construct a model instance of ControlSpecificationWithStats by calling from_dict on the json representation
        control_specification_with_stats_model = ControlSpecificationWithStats.from_dict(control_specification_with_stats_model_json)
        assert control_specification_with_stats_model != False

        # Construct a model instance of ControlSpecificationWithStats by calling from_dict on the json representation
        control_specification_with_stats_model_dict = ControlSpecificationWithStats.from_dict(control_specification_with_stats_model_json).__dict__
        control_specification_with_stats_model2 = ControlSpecificationWithStats(**control_specification_with_stats_model_dict)

        # Verify the model instances are equivalent
        assert control_specification_with_stats_model == control_specification_with_stats_model2

        # Convert model instance back to dict and verify no loss of data
        control_specification_with_stats_model_json2 = control_specification_with_stats_model.to_dict()
        assert control_specification_with_stats_model_json2 == control_specification_with_stats_model_json


class TestModel_ControlSummary:
    """
    Test Class for ControlSummary
    """

    def test_control_summary_serialization(self):
        """
        Test serialization/deserialization for ControlSummary
        """

        # Construct a json representation of a ControlSummary model
        control_summary_model_json = {}
        control_summary_model_json['id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        control_summary_model_json['control_name'] = 'ibm-cloud-rule'
        control_summary_model_json['control_description'] = 'Ensure security questions are registered by the account owner'

        # Construct a model instance of ControlSummary by calling from_dict on the json representation
        control_summary_model = ControlSummary.from_dict(control_summary_model_json)
        assert control_summary_model != False

        # Construct a model instance of ControlSummary by calling from_dict on the json representation
        control_summary_model_dict = ControlSummary.from_dict(control_summary_model_json).__dict__
        control_summary_model2 = ControlSummary(**control_summary_model_dict)

        # Verify the model instances are equivalent
        assert control_summary_model == control_summary_model2

        # Convert model instance back to dict and verify no loss of data
        control_summary_model_json2 = control_summary_model.to_dict()
        assert control_summary_model_json2 == control_summary_model_json


class TestModel_ControlWithStats:
    """
    Test Class for ControlWithStats
    """

    def test_control_with_stats_serialization(self):
        """
        Test serialization/deserialization for ControlWithStats
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_with_stats_model = {}  # AssessmentWithStats
        assessment_with_stats_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_with_stats_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_with_stats_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_with_stats_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_with_stats_model['parameter_count'] = 1
        assessment_with_stats_model['parameters'] = [parameter_model]
        assessment_with_stats_model['total_count'] = 140
        assessment_with_stats_model['pass_count'] = 123
        assessment_with_stats_model['failure_count'] = 12
        assessment_with_stats_model['error_count'] = 5
        assessment_with_stats_model['completed_count'] = 135

        control_specification_with_stats_model = {}  # ControlSpecificationWithStats
        control_specification_with_stats_model['control_specification_id'] = '18d32a4430e54c81a6668952609763b2'
        control_specification_with_stats_model['control_specification_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        control_specification_with_stats_model['component_id'] = 'cloud-object_storage'
        control_specification_with_stats_model['component_name'] = 'cloud-object_storage'
        control_specification_with_stats_model['environment'] = 'ibm cloud'
        control_specification_with_stats_model['responsibility'] = 'user'
        control_specification_with_stats_model['assessments'] = [assessment_with_stats_model]
        control_specification_with_stats_model['status'] = 'compliant'
        control_specification_with_stats_model['total_count'] = 150
        control_specification_with_stats_model['compliant_count'] = 130
        control_specification_with_stats_model['not_compliant_count'] = 5
        control_specification_with_stats_model['unable_to_perform_count'] = 5
        control_specification_with_stats_model['user_evaluation_required_count'] = 10
        control_specification_with_stats_model['not_applicable_count'] = 7

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        # Construct a json representation of a ControlWithStats model
        control_with_stats_model_json = {}
        control_with_stats_model_json['report_id'] = '6f1fdb98-c08b-41a8-a2f9-df10b51ff34a'
        control_with_stats_model_json['home_account_id'] = '2411ffdc16844b07b42521c3443f456d'
        control_with_stats_model_json['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        control_with_stats_model_json['control_library_id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        control_with_stats_model_json['control_library_version'] = 'v1.2.3'
        control_with_stats_model_json['control_name'] = 'Password Management'
        control_with_stats_model_json['control_description'] = 'Password Management'
        control_with_stats_model_json['control_category'] = 'Access Control'
        control_with_stats_model_json['control_specifications'] = [control_specification_with_stats_model]
        control_with_stats_model_json['resource_tags'] = tags_model
        control_with_stats_model_json['status'] = 'compliant'
        control_with_stats_model_json['total_count'] = 150
        control_with_stats_model_json['compliant_count'] = 130
        control_with_stats_model_json['not_compliant_count'] = 5
        control_with_stats_model_json['unable_to_perform_count'] = 5
        control_with_stats_model_json['user_evaluation_required_count'] = 10
        control_with_stats_model_json['not_applicable_count'] = 7

        # Construct a model instance of ControlWithStats by calling from_dict on the json representation
        control_with_stats_model = ControlWithStats.from_dict(control_with_stats_model_json)
        assert control_with_stats_model != False

        # Construct a model instance of ControlWithStats by calling from_dict on the json representation
        control_with_stats_model_dict = ControlWithStats.from_dict(control_with_stats_model_json).__dict__
        control_with_stats_model2 = ControlWithStats(**control_with_stats_model_dict)

        # Verify the model instances are equivalent
        assert control_with_stats_model == control_with_stats_model2

        # Convert model instance back to dict and verify no loss of data
        control_with_stats_model_json2 = control_with_stats_model.to_dict()
        assert control_with_stats_model_json2 == control_with_stats_model_json


class TestModel_CreateScanReport:
    """
    Test Class for CreateScanReport
    """

    def test_create_scan_report_serialization(self):
        """
        Test serialization/deserialization for CreateScanReport
        """

        # Construct a json representation of a CreateScanReport model
        create_scan_report_model_json = {}
        create_scan_report_model_json['id'] = 'testString'

        # Construct a model instance of CreateScanReport by calling from_dict on the json representation
        create_scan_report_model = CreateScanReport.from_dict(create_scan_report_model_json)
        assert create_scan_report_model != False

        # Construct a model instance of CreateScanReport by calling from_dict on the json representation
        create_scan_report_model_dict = CreateScanReport.from_dict(create_scan_report_model_json).__dict__
        create_scan_report_model2 = CreateScanReport(**create_scan_report_model_dict)

        # Verify the model instances are equivalent
        assert create_scan_report_model == create_scan_report_model2

        # Convert model instance back to dict and verify no loss of data
        create_scan_report_model_json2 = create_scan_report_model.to_dict()
        assert create_scan_report_model_json2 == create_scan_report_model_json


class TestModel_CreateScanResponse:
    """
    Test Class for CreateScanResponse
    """

    def test_create_scan_response_serialization(self):
        """
        Test serialization/deserialization for CreateScanResponse
        """

        # Construct a json representation of a CreateScanResponse model
        create_scan_response_model_json = {}
        create_scan_response_model_json['id'] = 'testString'
        create_scan_response_model_json['account_id'] = 'testString'
        create_scan_response_model_json['attachment_id'] = 'testString'
        create_scan_response_model_json['report_id'] = 'testString'
        create_scan_response_model_json['status'] = 'testString'
        create_scan_response_model_json['last_scan_time'] = '2019-01-01T12:00:00Z'
        create_scan_response_model_json['next_scan_time'] = '2019-01-01T12:00:00Z'
        create_scan_response_model_json['scan_type'] = 'testString'
        create_scan_response_model_json['occurence'] = 38

        # Construct a model instance of CreateScanResponse by calling from_dict on the json representation
        create_scan_response_model = CreateScanResponse.from_dict(create_scan_response_model_json)
        assert create_scan_response_model != False

        # Construct a model instance of CreateScanResponse by calling from_dict on the json representation
        create_scan_response_model_dict = CreateScanResponse.from_dict(create_scan_response_model_json).__dict__
        create_scan_response_model2 = CreateScanResponse(**create_scan_response_model_dict)

        # Verify the model instances are equivalent
        assert create_scan_response_model == create_scan_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_scan_response_model_json2 = create_scan_response_model.to_dict()
        assert create_scan_response_model_json2 == create_scan_response_model_json


class TestModel_Credential:
    """
    Test Class for Credential
    """

    def test_credential_serialization(self):
        """
        Test serialization/deserialization for Credential
        """

        # Construct dict forms of any model objects needed in order to build this model.

        account_model = {}  # Account
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        resource_model = {}  # Resource
        resource_model['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        resource_model['home_account_id'] = '2411ffdc16844b07b42521c3443f456d'
        resource_model['id'] = 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::'
        resource_model['resource_name'] = 'jeff\'s key'
        resource_model['account'] = account_model
        resource_model['component_id'] = 'cloud-object_storage'
        resource_model['component_name'] = 'cloud-object_storage'
        resource_model['environment'] = 'ibm cloud'
        resource_model['tags'] = tags_model
        resource_model['status'] = 'compliant'
        resource_model['total_count'] = 140
        resource_model['pass_count'] = 123
        resource_model['failure_count'] = 12
        resource_model['error_count'] = 5
        resource_model['skipped_count'] = 7
        resource_model['completed_count'] = 135
        resource_model['service_name'] = 'pm-20'
        resource_model['instance_crn'] = 'testString'

        # Construct a json representation of a Credential model
        credential_model_json = {}
        credential_model_json['secret_crn'] = 'testString'
        credential_model_json['resources'] = [resource_model]

        # Construct a model instance of Credential by calling from_dict on the json representation
        credential_model = Credential.from_dict(credential_model_json)
        assert credential_model != False

        # Construct a model instance of Credential by calling from_dict on the json representation
        credential_model_dict = Credential.from_dict(credential_model_json).__dict__
        credential_model2 = Credential(**credential_model_dict)

        # Verify the model instances are equivalent
        assert credential_model == credential_model2

        # Convert model instance back to dict and verify no loss of data
        credential_model_json2 = credential_model.to_dict()
        assert credential_model_json2 == credential_model_json


class TestModel_CredentialResponse:
    """
    Test Class for CredentialResponse
    """

    def test_credential_response_serialization(self):
        """
        Test serialization/deserialization for CredentialResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        account_model = {}  # Account
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        resource_model = {}  # Resource
        resource_model['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        resource_model['home_account_id'] = '2411ffdc16844b07b42521c3443f456d'
        resource_model['id'] = 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::'
        resource_model['resource_name'] = 'jeff\'s key'
        resource_model['account'] = account_model
        resource_model['component_id'] = 'cloud-object_storage'
        resource_model['component_name'] = 'cloud-object_storage'
        resource_model['environment'] = 'ibm cloud'
        resource_model['tags'] = tags_model
        resource_model['status'] = 'compliant'
        resource_model['total_count'] = 140
        resource_model['pass_count'] = 123
        resource_model['failure_count'] = 12
        resource_model['error_count'] = 5
        resource_model['skipped_count'] = 7
        resource_model['completed_count'] = 135
        resource_model['service_name'] = 'pm-20'
        resource_model['instance_crn'] = 'testString'

        # Construct a json representation of a CredentialResponse model
        credential_response_model_json = {}
        credential_response_model_json['type'] = 'iam_credentials'
        credential_response_model_json['secret_crn'] = 'testString'
        credential_response_model_json['secret_name'] = 'my secret'
        credential_response_model_json['resources'] = [resource_model]

        # Construct a model instance of CredentialResponse by calling from_dict on the json representation
        credential_response_model = CredentialResponse.from_dict(credential_response_model_json)
        assert credential_response_model != False

        # Construct a model instance of CredentialResponse by calling from_dict on the json representation
        credential_response_model_dict = CredentialResponse.from_dict(credential_response_model_json).__dict__
        credential_response_model2 = CredentialResponse(**credential_response_model_dict)

        # Verify the model instances are equivalent
        assert credential_response_model == credential_response_model2

        # Convert model instance back to dict and verify no loss of data
        credential_response_model_json2 = credential_response_model.to_dict()
        assert credential_response_model_json2 == credential_response_model_json


class TestModel_DateRange:
    """
    Test Class for DateRange
    """

    def test_date_range_serialization(self):
        """
        Test serialization/deserialization for DateRange
        """

        # Construct a json representation of a DateRange model
        date_range_model_json = {}
        date_range_model_json['start_date'] = '2025-02-28T05:42:58Z'
        date_range_model_json['end_date'] = '2025-02-28T05:42:58Z'

        # Construct a model instance of DateRange by calling from_dict on the json representation
        date_range_model = DateRange.from_dict(date_range_model_json)
        assert date_range_model != False

        # Construct a model instance of DateRange by calling from_dict on the json representation
        date_range_model_dict = DateRange.from_dict(date_range_model_json).__dict__
        date_range_model2 = DateRange(**date_range_model_dict)

        # Verify the model instances are equivalent
        assert date_range_model == date_range_model2

        # Convert model instance back to dict and verify no loss of data
        date_range_model_json2 = date_range_model.to_dict()
        assert date_range_model_json2 == date_range_model_json


class TestModel_DefaultParameters:
    """
    Test Class for DefaultParameters
    """

    def test_default_parameters_serialization(self):
        """
        Test serialization/deserialization for DefaultParameters
        """

        # Construct a json representation of a DefaultParameters model
        default_parameters_model_json = {}
        default_parameters_model_json['assessment_type'] = 'testString'
        default_parameters_model_json['assessment_id'] = 'testString'
        default_parameters_model_json['parameter_name'] = 'testString'
        default_parameters_model_json['parameter_default_value'] = 'testString'
        default_parameters_model_json['parameter_display_name'] = 'testString'
        default_parameters_model_json['parameter_type'] = 'testString'

        # Construct a model instance of DefaultParameters by calling from_dict on the json representation
        default_parameters_model = DefaultParameters.from_dict(default_parameters_model_json)
        assert default_parameters_model != False

        # Construct a model instance of DefaultParameters by calling from_dict on the json representation
        default_parameters_model_dict = DefaultParameters.from_dict(default_parameters_model_json).__dict__
        default_parameters_model2 = DefaultParameters(**default_parameters_model_dict)

        # Verify the model instances are equivalent
        assert default_parameters_model == default_parameters_model2

        # Convert model instance back to dict and verify no loss of data
        default_parameters_model_json2 = default_parameters_model.to_dict()
        assert default_parameters_model_json2 == default_parameters_model_json


class TestModel_DefaultParametersChanges:
    """
    Test Class for DefaultParametersChanges
    """

    def test_default_parameters_changes_serialization(self):
        """
        Test serialization/deserialization for DefaultParametersChanges
        """

        # Construct dict forms of any model objects needed in order to build this model.

        default_parameters_model = {}  # DefaultParameters
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'testString'

        default_parameters_difference_model = {}  # DefaultParametersDifference
        default_parameters_difference_model['current'] = default_parameters_model
        default_parameters_difference_model['latest'] = default_parameters_model

        # Construct a json representation of a DefaultParametersChanges model
        default_parameters_changes_model_json = {}
        default_parameters_changes_model_json['total_added'] = 38
        default_parameters_changes_model_json['total_removed'] = 38
        default_parameters_changes_model_json['total_updated'] = 38
        default_parameters_changes_model_json['added'] = [default_parameters_model]
        default_parameters_changes_model_json['removed'] = [default_parameters_model]
        default_parameters_changes_model_json['updated'] = [default_parameters_difference_model]

        # Construct a model instance of DefaultParametersChanges by calling from_dict on the json representation
        default_parameters_changes_model = DefaultParametersChanges.from_dict(default_parameters_changes_model_json)
        assert default_parameters_changes_model != False

        # Construct a model instance of DefaultParametersChanges by calling from_dict on the json representation
        default_parameters_changes_model_dict = DefaultParametersChanges.from_dict(default_parameters_changes_model_json).__dict__
        default_parameters_changes_model2 = DefaultParametersChanges(**default_parameters_changes_model_dict)

        # Verify the model instances are equivalent
        assert default_parameters_changes_model == default_parameters_changes_model2

        # Convert model instance back to dict and verify no loss of data
        default_parameters_changes_model_json2 = default_parameters_changes_model.to_dict()
        assert default_parameters_changes_model_json2 == default_parameters_changes_model_json


class TestModel_DefaultParametersDifference:
    """
    Test Class for DefaultParametersDifference
    """

    def test_default_parameters_difference_serialization(self):
        """
        Test serialization/deserialization for DefaultParametersDifference
        """

        # Construct dict forms of any model objects needed in order to build this model.

        default_parameters_model = {}  # DefaultParameters
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'testString'

        # Construct a json representation of a DefaultParametersDifference model
        default_parameters_difference_model_json = {}
        default_parameters_difference_model_json['current'] = default_parameters_model
        default_parameters_difference_model_json['latest'] = default_parameters_model

        # Construct a model instance of DefaultParametersDifference by calling from_dict on the json representation
        default_parameters_difference_model = DefaultParametersDifference.from_dict(default_parameters_difference_model_json)
        assert default_parameters_difference_model != False

        # Construct a model instance of DefaultParametersDifference by calling from_dict on the json representation
        default_parameters_difference_model_dict = DefaultParametersDifference.from_dict(default_parameters_difference_model_json).__dict__
        default_parameters_difference_model2 = DefaultParametersDifference(**default_parameters_difference_model_dict)

        # Verify the model instances are equivalent
        assert default_parameters_difference_model == default_parameters_difference_model2

        # Convert model instance back to dict and verify no loss of data
        default_parameters_difference_model_json2 = default_parameters_difference_model.to_dict()
        assert default_parameters_difference_model_json2 == default_parameters_difference_model_json


class TestModel_Endpoint:
    """
    Test Class for Endpoint
    """

    def test_endpoint_serialization(self):
        """
        Test serialization/deserialization for Endpoint
        """

        # Construct a json representation of a Endpoint model
        endpoint_model_json = {}
        endpoint_model_json['host'] = 'testString'
        endpoint_model_json['path'] = 'testString'
        endpoint_model_json['region'] = 'testString'
        endpoint_model_json['advisory_call_limit'] = 38

        # Construct a model instance of Endpoint by calling from_dict on the json representation
        endpoint_model = Endpoint.from_dict(endpoint_model_json)
        assert endpoint_model != False

        # Construct a model instance of Endpoint by calling from_dict on the json representation
        endpoint_model_dict = Endpoint.from_dict(endpoint_model_json).__dict__
        endpoint_model2 = Endpoint(**endpoint_model_dict)

        # Verify the model instances are equivalent
        assert endpoint_model == endpoint_model2

        # Convert model instance back to dict and verify no loss of data
        endpoint_model_json2 = endpoint_model.to_dict()
        assert endpoint_model_json2 == endpoint_model_json


class TestModel_EvalStats:
    """
    Test Class for EvalStats
    """

    def test_eval_stats_serialization(self):
        """
        Test serialization/deserialization for EvalStats
        """

        # Construct a json representation of a EvalStats model
        eval_stats_model_json = {}
        eval_stats_model_json['status'] = 'compliant'
        eval_stats_model_json['total_count'] = 140
        eval_stats_model_json['pass_count'] = 123
        eval_stats_model_json['failure_count'] = 12
        eval_stats_model_json['error_count'] = 5
        eval_stats_model_json['skipped_count'] = 7
        eval_stats_model_json['completed_count'] = 135

        # Construct a model instance of EvalStats by calling from_dict on the json representation
        eval_stats_model = EvalStats.from_dict(eval_stats_model_json)
        assert eval_stats_model != False

        # Construct a model instance of EvalStats by calling from_dict on the json representation
        eval_stats_model_dict = EvalStats.from_dict(eval_stats_model_json).__dict__
        eval_stats_model2 = EvalStats(**eval_stats_model_dict)

        # Verify the model instances are equivalent
        assert eval_stats_model == eval_stats_model2

        # Convert model instance back to dict and verify no loss of data
        eval_stats_model_json2 = eval_stats_model.to_dict()
        assert eval_stats_model_json2 == eval_stats_model_json


class TestModel_Evaluation:
    """
    Test Class for Evaluation
    """

    def test_evaluation_serialization(self):
        """
        Test serialization/deserialization for Evaluation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        target_info_model = {}  # TargetInfo
        target_info_model['id'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket'
        target_info_model['account_id'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        target_info_model['service_name'] = 'cloud-object-storage'
        target_info_model['service_display_name'] = 'cloud-object-storage'
        target_info_model['resource_crn'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket'
        target_info_model['resource_name'] = 'mybucket'
        target_info_model['tags'] = tags_model

        evaluation_property_model = {}  # EvaluationProperty
        evaluation_property_model['property'] = 'testString'
        evaluation_property_model['property_description'] = 'testString'
        evaluation_property_model['operator'] = 'string_equals'
        evaluation_property_model['expected_value'] = 'testString'
        evaluation_property_model['found_value'] = 'testString'

        evaluation_provider_info_model = {}  # EvaluationProviderInfo
        evaluation_provider_info_model['provider_type'] = 'testString'

        evaluation_details_model = {}  # EvaluationDetails
        evaluation_details_model['properties'] = [evaluation_property_model]
        evaluation_details_model['provider_info'] = evaluation_provider_info_model

        # Construct a json representation of a Evaluation model
        evaluation_model_json = {}
        evaluation_model_json['report_id'] = 'testString'
        evaluation_model_json['home_account_id'] = 'be200c80cabc456e91139e4152327456'
        evaluation_model_json['component_id'] = 'cloud-object_storage'
        evaluation_model_json['component_name'] = 'cloud-object_storage'
        evaluation_model_json['assessment'] = assessment_model
        evaluation_model_json['evaluate_time'] = '2022-06-30T11:03:44.630150782Z'
        evaluation_model_json['target'] = target_info_model
        evaluation_model_json['status'] = 'failure'
        evaluation_model_json['reason'] = 'One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met'
        evaluation_model_json['details'] = evaluation_details_model
        evaluation_model_json['evaluated_by'] = 'abc@ibm.com'

        # Construct a model instance of Evaluation by calling from_dict on the json representation
        evaluation_model = Evaluation.from_dict(evaluation_model_json)
        assert evaluation_model != False

        # Construct a model instance of Evaluation by calling from_dict on the json representation
        evaluation_model_dict = Evaluation.from_dict(evaluation_model_json).__dict__
        evaluation_model2 = Evaluation(**evaluation_model_dict)

        # Verify the model instances are equivalent
        assert evaluation_model == evaluation_model2

        # Convert model instance back to dict and verify no loss of data
        evaluation_model_json2 = evaluation_model.to_dict()
        assert evaluation_model_json2 == evaluation_model_json


class TestModel_EvaluationDetails:
    """
    Test Class for EvaluationDetails
    """

    def test_evaluation_details_serialization(self):
        """
        Test serialization/deserialization for EvaluationDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        evaluation_property_model = {}  # EvaluationProperty
        evaluation_property_model['property'] = 'testString'
        evaluation_property_model['property_description'] = 'testString'
        evaluation_property_model['operator'] = 'string_equals'
        evaluation_property_model['expected_value'] = 'testString'
        evaluation_property_model['found_value'] = 'testString'

        evaluation_provider_info_model = {}  # EvaluationProviderInfo
        evaluation_provider_info_model['provider_type'] = 'testString'

        # Construct a json representation of a EvaluationDetails model
        evaluation_details_model_json = {}
        evaluation_details_model_json['properties'] = [evaluation_property_model]
        evaluation_details_model_json['provider_info'] = evaluation_provider_info_model

        # Construct a model instance of EvaluationDetails by calling from_dict on the json representation
        evaluation_details_model = EvaluationDetails.from_dict(evaluation_details_model_json)
        assert evaluation_details_model != False

        # Construct a model instance of EvaluationDetails by calling from_dict on the json representation
        evaluation_details_model_dict = EvaluationDetails.from_dict(evaluation_details_model_json).__dict__
        evaluation_details_model2 = EvaluationDetails(**evaluation_details_model_dict)

        # Verify the model instances are equivalent
        assert evaluation_details_model == evaluation_details_model2

        # Convert model instance back to dict and verify no loss of data
        evaluation_details_model_json2 = evaluation_details_model.to_dict()
        assert evaluation_details_model_json2 == evaluation_details_model_json


class TestModel_EvaluationPage:
    """
    Test Class for EvaluationPage
    """

    def test_evaluation_page_serialization(self):
        """
        Test serialization/deserialization for EvaluationPage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_first_model = {}  # PageHRefFirst
        page_h_ref_first_model['href'] = 'testString'

        page_h_ref_next_model = {}  # PageHRefNext
        page_h_ref_next_model['href'] = 'testString'
        page_h_ref_next_model['start'] = 'testString'

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        target_info_model = {}  # TargetInfo
        target_info_model['id'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket'
        target_info_model['account_id'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        target_info_model['service_name'] = 'cloud-object-storage'
        target_info_model['service_display_name'] = 'cloud-object-storage'
        target_info_model['resource_crn'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket'
        target_info_model['resource_name'] = 'mybucket'
        target_info_model['tags'] = tags_model

        evaluation_property_model = {}  # EvaluationProperty
        evaluation_property_model['property'] = 'testString'
        evaluation_property_model['property_description'] = 'testString'
        evaluation_property_model['operator'] = 'string_equals'
        evaluation_property_model['expected_value'] = 'testString'
        evaluation_property_model['found_value'] = 'testString'

        evaluation_provider_info_model = {}  # EvaluationProviderInfo
        evaluation_provider_info_model['provider_type'] = 'testString'

        evaluation_details_model = {}  # EvaluationDetails
        evaluation_details_model['properties'] = [evaluation_property_model]
        evaluation_details_model['provider_info'] = evaluation_provider_info_model

        evaluation_model = {}  # Evaluation
        evaluation_model['report_id'] = 'testString'
        evaluation_model['home_account_id'] = 'be200c80cabc456e91139e4152327456'
        evaluation_model['component_id'] = 'cloud-object_storage'
        evaluation_model['component_name'] = 'cloud-object_storage'
        evaluation_model['assessment'] = assessment_model
        evaluation_model['evaluate_time'] = '2022-06-30T11:03:44.630150782Z'
        evaluation_model['target'] = target_info_model
        evaluation_model['status'] = 'failure'
        evaluation_model['reason'] = 'One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met'
        evaluation_model['details'] = evaluation_details_model
        evaluation_model['evaluated_by'] = 'abc@ibm.com'

        # Construct a json representation of a EvaluationPage model
        evaluation_page_model_json = {}
        evaluation_page_model_json['limit'] = 50
        evaluation_page_model_json['total_count'] = 230
        evaluation_page_model_json['first'] = page_h_ref_first_model
        evaluation_page_model_json['next'] = page_h_ref_next_model
        evaluation_page_model_json['report_id'] = 'testString'
        evaluation_page_model_json['home_account_id'] = 'testString'
        evaluation_page_model_json['evaluations'] = [evaluation_model]

        # Construct a model instance of EvaluationPage by calling from_dict on the json representation
        evaluation_page_model = EvaluationPage.from_dict(evaluation_page_model_json)
        assert evaluation_page_model != False

        # Construct a model instance of EvaluationPage by calling from_dict on the json representation
        evaluation_page_model_dict = EvaluationPage.from_dict(evaluation_page_model_json).__dict__
        evaluation_page_model2 = EvaluationPage(**evaluation_page_model_dict)

        # Verify the model instances are equivalent
        assert evaluation_page_model == evaluation_page_model2

        # Convert model instance back to dict and verify no loss of data
        evaluation_page_model_json2 = evaluation_page_model.to_dict()
        assert evaluation_page_model_json2 == evaluation_page_model_json


class TestModel_EvaluationProperty:
    """
    Test Class for EvaluationProperty
    """

    def test_evaluation_property_serialization(self):
        """
        Test serialization/deserialization for EvaluationProperty
        """

        # Construct a json representation of a EvaluationProperty model
        evaluation_property_model_json = {}
        evaluation_property_model_json['property'] = 'testString'
        evaluation_property_model_json['property_description'] = 'testString'
        evaluation_property_model_json['operator'] = 'string_equals'
        evaluation_property_model_json['expected_value'] = 'testString'
        evaluation_property_model_json['found_value'] = 'testString'

        # Construct a model instance of EvaluationProperty by calling from_dict on the json representation
        evaluation_property_model = EvaluationProperty.from_dict(evaluation_property_model_json)
        assert evaluation_property_model != False

        # Construct a model instance of EvaluationProperty by calling from_dict on the json representation
        evaluation_property_model_dict = EvaluationProperty.from_dict(evaluation_property_model_json).__dict__
        evaluation_property_model2 = EvaluationProperty(**evaluation_property_model_dict)

        # Verify the model instances are equivalent
        assert evaluation_property_model == evaluation_property_model2

        # Convert model instance back to dict and verify no loss of data
        evaluation_property_model_json2 = evaluation_property_model.to_dict()
        assert evaluation_property_model_json2 == evaluation_property_model_json


class TestModel_EvaluationProviderInfo:
    """
    Test Class for EvaluationProviderInfo
    """

    def test_evaluation_provider_info_serialization(self):
        """
        Test serialization/deserialization for EvaluationProviderInfo
        """

        # Construct a json representation of a EvaluationProviderInfo model
        evaluation_provider_info_model_json = {}
        evaluation_provider_info_model_json['provider_type'] = 'testString'

        # Construct a model instance of EvaluationProviderInfo by calling from_dict on the json representation
        evaluation_provider_info_model = EvaluationProviderInfo.from_dict(evaluation_provider_info_model_json)
        assert evaluation_provider_info_model != False

        # Construct a model instance of EvaluationProviderInfo by calling from_dict on the json representation
        evaluation_provider_info_model_dict = EvaluationProviderInfo.from_dict(evaluation_provider_info_model_json).__dict__
        evaluation_provider_info_model2 = EvaluationProviderInfo(**evaluation_provider_info_model_dict)

        # Verify the model instances are equivalent
        assert evaluation_provider_info_model == evaluation_provider_info_model2

        # Convert model instance back to dict and verify no loss of data
        evaluation_provider_info_model_json2 = evaluation_provider_info_model.to_dict()
        assert evaluation_provider_info_model_json2 == evaluation_provider_info_model_json


class TestModel_EventNotifications:
    """
    Test Class for EventNotifications
    """

    def test_event_notifications_serialization(self):
        """
        Test serialization/deserialization for EventNotifications
        """

        # Construct a json representation of a EventNotifications model
        event_notifications_model_json = {}
        event_notifications_model_json['instance_crn'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::'
        event_notifications_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        event_notifications_model_json['source_id'] = 'crn:v1:bluemix:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::'
        event_notifications_model_json['source_description'] = 'This source is used for integration with IBM Cloud Security and Compliance Center.'
        event_notifications_model_json['source_name'] = 'compliance'

        # Construct a model instance of EventNotifications by calling from_dict on the json representation
        event_notifications_model = EventNotifications.from_dict(event_notifications_model_json)
        assert event_notifications_model != False

        # Construct a model instance of EventNotifications by calling from_dict on the json representation
        event_notifications_model_dict = EventNotifications.from_dict(event_notifications_model_json).__dict__
        event_notifications_model2 = EventNotifications(**event_notifications_model_dict)

        # Verify the model instances are equivalent
        assert event_notifications_model == event_notifications_model2

        # Convert model instance back to dict and verify no loss of data
        event_notifications_model_json2 = event_notifications_model.to_dict()
        assert event_notifications_model_json2 == event_notifications_model_json


class TestModel_EventNotificationsPrototype:
    """
    Test Class for EventNotificationsPrototype
    """

    def test_event_notifications_prototype_serialization(self):
        """
        Test serialization/deserialization for EventNotificationsPrototype
        """

        # Construct a json representation of a EventNotificationsPrototype model
        event_notifications_prototype_model_json = {}
        event_notifications_prototype_model_json['instance_crn'] = 'testString'
        event_notifications_prototype_model_json['source_description'] = 'This source is used for integration with IBM Cloud Security and Compliance Center.'
        event_notifications_prototype_model_json['source_name'] = 'compliance'

        # Construct a model instance of EventNotificationsPrototype by calling from_dict on the json representation
        event_notifications_prototype_model = EventNotificationsPrototype.from_dict(event_notifications_prototype_model_json)
        assert event_notifications_prototype_model != False

        # Construct a model instance of EventNotificationsPrototype by calling from_dict on the json representation
        event_notifications_prototype_model_dict = EventNotificationsPrototype.from_dict(event_notifications_prototype_model_json).__dict__
        event_notifications_prototype_model2 = EventNotificationsPrototype(**event_notifications_prototype_model_dict)

        # Verify the model instances are equivalent
        assert event_notifications_prototype_model == event_notifications_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        event_notifications_prototype_model_json2 = event_notifications_prototype_model.to_dict()
        assert event_notifications_prototype_model_json2 == event_notifications_prototype_model_json


class TestModel_Import:
    """
    Test Class for Import
    """

    def test_import_serialization(self):
        """
        Test serialization/deserialization for Import
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_parameter_model = {}  # RuleParameter
        rule_parameter_model['name'] = 'testString'
        rule_parameter_model['display_name'] = 'testString'
        rule_parameter_model['description'] = 'testString'
        rule_parameter_model['type'] = 'string'

        # Construct a json representation of a Import model
        import_model_json = {}
        import_model_json['parameters'] = [rule_parameter_model]

        # Construct a model instance of Import by calling from_dict on the json representation
        import_model = Import.from_dict(import_model_json)
        assert import_model != False

        # Construct a model instance of Import by calling from_dict on the json representation
        import_model_dict = Import.from_dict(import_model_json).__dict__
        import_model2 = Import(**import_model_dict)

        # Verify the model instances are equivalent
        assert import_model == import_model2

        # Convert model instance back to dict and verify no loss of data
        import_model_json2 = import_model.to_dict()
        assert import_model_json2 == import_model_json


class TestModel_LabelType:
    """
    Test Class for LabelType
    """

    def test_label_type_serialization(self):
        """
        Test serialization/deserialization for LabelType
        """

        # Construct a json representation of a LabelType model
        label_type_model_json = {}
        label_type_model_json['text'] = '1 per instance'
        label_type_model_json['tip'] = 'Only 1 per instance'

        # Construct a model instance of LabelType by calling from_dict on the json representation
        label_type_model = LabelType.from_dict(label_type_model_json)
        assert label_type_model != False

        # Construct a model instance of LabelType by calling from_dict on the json representation
        label_type_model_dict = LabelType.from_dict(label_type_model_json).__dict__
        label_type_model2 = LabelType(**label_type_model_dict)

        # Verify the model instances are equivalent
        assert label_type_model == label_type_model2

        # Convert model instance back to dict and verify no loss of data
        label_type_model_json2 = label_type_model.to_dict()
        assert label_type_model_json2 == label_type_model_json


class TestModel_LastScan:
    """
    Test Class for LastScan
    """

    def test_last_scan_serialization(self):
        """
        Test serialization/deserialization for LastScan
        """

        # Construct a json representation of a LastScan model
        last_scan_model_json = {}
        last_scan_model_json['id'] = 'testString'
        last_scan_model_json['status'] = 'testString'
        last_scan_model_json['time'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of LastScan by calling from_dict on the json representation
        last_scan_model = LastScan.from_dict(last_scan_model_json)
        assert last_scan_model != False

        # Construct a model instance of LastScan by calling from_dict on the json representation
        last_scan_model_dict = LastScan.from_dict(last_scan_model_json).__dict__
        last_scan_model2 = LastScan(**last_scan_model_dict)

        # Verify the model instances are equivalent
        assert last_scan_model == last_scan_model2

        # Convert model instance back to dict and verify no loss of data
        last_scan_model_json2 = last_scan_model.to_dict()
        assert last_scan_model_json2 == last_scan_model_json


class TestModel_Link:
    """
    Test Class for Link
    """

    def test_link_serialization(self):
        """
        Test serialization/deserialization for Link
        """

        # Construct a json representation of a Link model
        link_model_json = {}
        link_model_json['description'] = 'testString'
        link_model_json['href'] = 'testString'

        # Construct a model instance of Link by calling from_dict on the json representation
        link_model = Link.from_dict(link_model_json)
        assert link_model != False

        # Construct a model instance of Link by calling from_dict on the json representation
        link_model_dict = Link.from_dict(link_model_json).__dict__
        link_model2 = Link(**link_model_dict)

        # Verify the model instances are equivalent
        assert link_model == link_model2

        # Convert model instance back to dict and verify no loss of data
        link_model_json2 = link_model.to_dict()
        assert link_model_json2 == link_model_json


class TestModel_ObjectStorage:
    """
    Test Class for ObjectStorage
    """

    def test_object_storage_serialization(self):
        """
        Test serialization/deserialization for ObjectStorage
        """

        # Construct a json representation of a ObjectStorage model
        object_storage_model_json = {}
        object_storage_model_json['instance_crn'] = 'testString'
        object_storage_model_json['bucket'] = 'testString'
        object_storage_model_json['bucket_location'] = 'testString'
        object_storage_model_json['bucket_endpoint'] = 'testString'
        object_storage_model_json['updated_on'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of ObjectStorage by calling from_dict on the json representation
        object_storage_model = ObjectStorage.from_dict(object_storage_model_json)
        assert object_storage_model != False

        # Construct a model instance of ObjectStorage by calling from_dict on the json representation
        object_storage_model_dict = ObjectStorage.from_dict(object_storage_model_json).__dict__
        object_storage_model2 = ObjectStorage(**object_storage_model_dict)

        # Verify the model instances are equivalent
        assert object_storage_model == object_storage_model2

        # Convert model instance back to dict and verify no loss of data
        object_storage_model_json2 = object_storage_model.to_dict()
        assert object_storage_model_json2 == object_storage_model_json


class TestModel_ObjectStoragePrototype:
    """
    Test Class for ObjectStoragePrototype
    """

    def test_object_storage_prototype_serialization(self):
        """
        Test serialization/deserialization for ObjectStoragePrototype
        """

        # Construct a json representation of a ObjectStoragePrototype model
        object_storage_prototype_model_json = {}
        object_storage_prototype_model_json['bucket'] = 'testString'
        object_storage_prototype_model_json['instance_crn'] = 'testString'

        # Construct a model instance of ObjectStoragePrototype by calling from_dict on the json representation
        object_storage_prototype_model = ObjectStoragePrototype.from_dict(object_storage_prototype_model_json)
        assert object_storage_prototype_model != False

        # Construct a model instance of ObjectStoragePrototype by calling from_dict on the json representation
        object_storage_prototype_model_dict = ObjectStoragePrototype.from_dict(object_storage_prototype_model_json).__dict__
        object_storage_prototype_model2 = ObjectStoragePrototype(**object_storage_prototype_model_dict)

        # Verify the model instances are equivalent
        assert object_storage_prototype_model == object_storage_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        object_storage_prototype_model_json2 = object_storage_prototype_model.to_dict()
        assert object_storage_prototype_model_json2 == object_storage_prototype_model_json


class TestModel_PageHRefFirst:
    """
    Test Class for PageHRefFirst
    """

    def test_page_h_ref_first_serialization(self):
        """
        Test serialization/deserialization for PageHRefFirst
        """

        # Construct a json representation of a PageHRefFirst model
        page_h_ref_first_model_json = {}
        page_h_ref_first_model_json['href'] = 'testString'

        # Construct a model instance of PageHRefFirst by calling from_dict on the json representation
        page_h_ref_first_model = PageHRefFirst.from_dict(page_h_ref_first_model_json)
        assert page_h_ref_first_model != False

        # Construct a model instance of PageHRefFirst by calling from_dict on the json representation
        page_h_ref_first_model_dict = PageHRefFirst.from_dict(page_h_ref_first_model_json).__dict__
        page_h_ref_first_model2 = PageHRefFirst(**page_h_ref_first_model_dict)

        # Verify the model instances are equivalent
        assert page_h_ref_first_model == page_h_ref_first_model2

        # Convert model instance back to dict and verify no loss of data
        page_h_ref_first_model_json2 = page_h_ref_first_model.to_dict()
        assert page_h_ref_first_model_json2 == page_h_ref_first_model_json


class TestModel_PageHRefNext:
    """
    Test Class for PageHRefNext
    """

    def test_page_h_ref_next_serialization(self):
        """
        Test serialization/deserialization for PageHRefNext
        """

        # Construct a json representation of a PageHRefNext model
        page_h_ref_next_model_json = {}
        page_h_ref_next_model_json['href'] = 'testString'
        page_h_ref_next_model_json['start'] = 'testString'

        # Construct a model instance of PageHRefNext by calling from_dict on the json representation
        page_h_ref_next_model = PageHRefNext.from_dict(page_h_ref_next_model_json)
        assert page_h_ref_next_model != False

        # Construct a model instance of PageHRefNext by calling from_dict on the json representation
        page_h_ref_next_model_dict = PageHRefNext.from_dict(page_h_ref_next_model_json).__dict__
        page_h_ref_next_model2 = PageHRefNext(**page_h_ref_next_model_dict)

        # Verify the model instances are equivalent
        assert page_h_ref_next_model == page_h_ref_next_model2

        # Convert model instance back to dict and verify no loss of data
        page_h_ref_next_model_json2 = page_h_ref_next_model.to_dict()
        assert page_h_ref_next_model_json2 == page_h_ref_next_model_json


class TestModel_Parameter:
    """
    Test Class for Parameter
    """

    def test_parameter_serialization(self):
        """
        Test serialization/deserialization for Parameter
        """

        # Construct a json representation of a Parameter model
        parameter_model_json = {}
        parameter_model_json['assessment_type'] = 'testString'
        parameter_model_json['assessment_id'] = 'testString'
        parameter_model_json['parameter_name'] = 'location'
        parameter_model_json['parameter_display_name'] = 'Location'
        parameter_model_json['parameter_type'] = 'string'
        parameter_model_json['parameter_value'] = 'testString'

        # Construct a model instance of Parameter by calling from_dict on the json representation
        parameter_model = Parameter.from_dict(parameter_model_json)
        assert parameter_model != False

        # Construct a model instance of Parameter by calling from_dict on the json representation
        parameter_model_dict = Parameter.from_dict(parameter_model_json).__dict__
        parameter_model2 = Parameter(**parameter_model_dict)

        # Verify the model instances are equivalent
        assert parameter_model == parameter_model2

        # Convert model instance back to dict and verify no loss of data
        parameter_model_json2 = parameter_model.to_dict()
        assert parameter_model_json2 == parameter_model_json


class TestModel_Profile:
    """
    Test Class for Profile
    """

    def test_profile_serialization(self):
        """
        Test serialization/deserialization for Profile
        """

        # Construct dict forms of any model objects needed in order to build this model.

        control_doc_model = {}  # ControlDoc
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        control_specification_model = {}  # ControlSpecification
        control_specification_model['id'] = 'testString'
        control_specification_model['responsibility'] = 'testString'
        control_specification_model['component_id'] = 'testString'
        control_specification_model['component_name'] = 'testString'
        control_specification_model['component_type'] = 'testString'
        control_specification_model['environment'] = 'testString'
        control_specification_model['description'] = 'testString'
        control_specification_model['assessments_count'] = 38
        control_specification_model['assessments'] = [assessment_model]

        profile_controls_model = {}  # ProfileControls
        profile_controls_model['control_requirement'] = True
        profile_controls_model['control_library_id'] = 'testString'
        profile_controls_model['control_id'] = 'testString'
        profile_controls_model['control_library_version'] = 'testString'
        profile_controls_model['control_name'] = 'testString'
        profile_controls_model['control_description'] = 'testString'
        profile_controls_model['control_severity'] = 'testString'
        profile_controls_model['control_category'] = 'testString'
        profile_controls_model['control_parent'] = 'testString'
        profile_controls_model['control_docs'] = control_doc_model
        profile_controls_model['control_specifications'] = [control_specification_model]

        default_parameters_model = {}  # DefaultParameters
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'testString'

        # Construct a json representation of a Profile model
        profile_model_json = {}
        profile_model_json['id'] = 'testString'
        profile_model_json['profile_name'] = 'testString'
        profile_model_json['instance_id'] = 'testString'
        profile_model_json['hierarchy_enabled'] = True
        profile_model_json['profile_description'] = 'testString'
        profile_model_json['profile_type'] = 'custom'
        profile_model_json['profile_version'] = 'testString'
        profile_model_json['version_group_label'] = 'testString'
        profile_model_json['latest'] = True
        profile_model_json['created_by'] = 'testString'
        profile_model_json['created_on'] = '2019-01-01T12:00:00Z'
        profile_model_json['updated_by'] = 'testString'
        profile_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        profile_model_json['controls_count'] = 38
        profile_model_json['attachments_count'] = 38
        profile_model_json['controls'] = [profile_controls_model]
        profile_model_json['default_parameters'] = [default_parameters_model]

        # Construct a model instance of Profile by calling from_dict on the json representation
        profile_model = Profile.from_dict(profile_model_json)
        assert profile_model != False

        # Construct a model instance of Profile by calling from_dict on the json representation
        profile_model_dict = Profile.from_dict(profile_model_json).__dict__
        profile_model2 = Profile(**profile_model_dict)

        # Verify the model instances are equivalent
        assert profile_model == profile_model2

        # Convert model instance back to dict and verify no loss of data
        profile_model_json2 = profile_model.to_dict()
        assert profile_model_json2 == profile_model_json


class TestModel_ProfileAttachment:
    """
    Test Class for ProfileAttachment
    """

    def test_profile_attachment_serialization(self):
        """
        Test serialization/deserialization for ProfileAttachment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        attachment_notifications_controls_model = {}  # AttachmentNotificationsControls
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = ['testString']

        attachment_notifications_model = {}  # AttachmentNotifications
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        multi_cloud_scope_payload_model = {}  # MultiCloudScopePayloadById
        multi_cloud_scope_payload_model['id'] = 'testString'

        date_range_model = {}  # DateRange
        date_range_model['start_date'] = '2025-02-28T05:42:58Z'
        date_range_model['end_date'] = '2025-02-28T05:42:58Z'

        last_scan_model = {}  # LastScan
        last_scan_model['id'] = 'testString'
        last_scan_model['status'] = 'testString'
        last_scan_model['time'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a ProfileAttachment model
        profile_attachment_model_json = {}
        profile_attachment_model_json['attachment_parameters'] = [parameter_model]
        profile_attachment_model_json['description'] = 'testString'
        profile_attachment_model_json['name'] = 'testString'
        profile_attachment_model_json['notifications'] = attachment_notifications_model
        profile_attachment_model_json['schedule'] = 'daily'
        profile_attachment_model_json['scope'] = [multi_cloud_scope_payload_model]
        profile_attachment_model_json['status'] = 'enabled'
        profile_attachment_model_json['data_selection_range'] = date_range_model
        profile_attachment_model_json['account_id'] = 'testString'
        profile_attachment_model_json['created_by'] = 'testString'
        profile_attachment_model_json['created_on'] = '2019-01-01T12:00:00Z'
        profile_attachment_model_json['id'] = 'testString'
        profile_attachment_model_json['instance_id'] = 'testString'
        profile_attachment_model_json['last_scan'] = last_scan_model
        profile_attachment_model_json['next_scan_time'] = '2019-01-01T12:00:00Z'
        profile_attachment_model_json['profile_id'] = 'testString'
        profile_attachment_model_json['updated_by'] = 'testString'
        profile_attachment_model_json['updated_on'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of ProfileAttachment by calling from_dict on the json representation
        profile_attachment_model = ProfileAttachment.from_dict(profile_attachment_model_json)
        assert profile_attachment_model != False

        # Construct a model instance of ProfileAttachment by calling from_dict on the json representation
        profile_attachment_model_dict = ProfileAttachment.from_dict(profile_attachment_model_json).__dict__
        profile_attachment_model2 = ProfileAttachment(**profile_attachment_model_dict)

        # Verify the model instances are equivalent
        assert profile_attachment_model == profile_attachment_model2

        # Convert model instance back to dict and verify no loss of data
        profile_attachment_model_json2 = profile_attachment_model.to_dict()
        assert profile_attachment_model_json2 == profile_attachment_model_json


class TestModel_ProfileAttachmentBase:
    """
    Test Class for ProfileAttachmentBase
    """

    def test_profile_attachment_base_serialization(self):
        """
        Test serialization/deserialization for ProfileAttachmentBase
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        attachment_notifications_controls_model = {}  # AttachmentNotificationsControls
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = ['testString']

        attachment_notifications_model = {}  # AttachmentNotifications
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        multi_cloud_scope_payload_model = {}  # MultiCloudScopePayloadById
        multi_cloud_scope_payload_model['id'] = 'testString'

        date_range_model = {}  # DateRange
        date_range_model['start_date'] = '2025-02-28T05:42:58Z'
        date_range_model['end_date'] = '2025-02-28T05:42:58Z'

        # Construct a json representation of a ProfileAttachmentBase model
        profile_attachment_base_model_json = {}
        profile_attachment_base_model_json['attachment_parameters'] = [parameter_model]
        profile_attachment_base_model_json['description'] = 'testString'
        profile_attachment_base_model_json['name'] = 'testString'
        profile_attachment_base_model_json['notifications'] = attachment_notifications_model
        profile_attachment_base_model_json['schedule'] = 'daily'
        profile_attachment_base_model_json['scope'] = [multi_cloud_scope_payload_model]
        profile_attachment_base_model_json['status'] = 'enabled'
        profile_attachment_base_model_json['data_selection_range'] = date_range_model

        # Construct a model instance of ProfileAttachmentBase by calling from_dict on the json representation
        profile_attachment_base_model = ProfileAttachmentBase.from_dict(profile_attachment_base_model_json)
        assert profile_attachment_base_model != False

        # Construct a model instance of ProfileAttachmentBase by calling from_dict on the json representation
        profile_attachment_base_model_dict = ProfileAttachmentBase.from_dict(profile_attachment_base_model_json).__dict__
        profile_attachment_base_model2 = ProfileAttachmentBase(**profile_attachment_base_model_dict)

        # Verify the model instances are equivalent
        assert profile_attachment_base_model == profile_attachment_base_model2

        # Convert model instance back to dict and verify no loss of data
        profile_attachment_base_model_json2 = profile_attachment_base_model.to_dict()
        assert profile_attachment_base_model_json2 == profile_attachment_base_model_json


class TestModel_ProfileAttachmentCollection:
    """
    Test Class for ProfileAttachmentCollection
    """

    def test_profile_attachment_collection_serialization(self):
        """
        Test serialization/deserialization for ProfileAttachmentCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_first_model = {}  # PageHRefFirst
        page_h_ref_first_model['href'] = 'testString'

        page_h_ref_next_model = {}  # PageHRefNext
        page_h_ref_next_model['href'] = 'testString'
        page_h_ref_next_model['start'] = 'testString'

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        attachment_notifications_controls_model = {}  # AttachmentNotificationsControls
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = ['testString']

        attachment_notifications_model = {}  # AttachmentNotifications
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        multi_cloud_scope_payload_model = {}  # MultiCloudScopePayloadById
        multi_cloud_scope_payload_model['id'] = 'testString'

        date_range_model = {}  # DateRange
        date_range_model['start_date'] = '2025-02-28T05:42:58Z'
        date_range_model['end_date'] = '2025-02-28T05:42:58Z'

        last_scan_model = {}  # LastScan
        last_scan_model['id'] = 'testString'
        last_scan_model['status'] = 'testString'
        last_scan_model['time'] = '2019-01-01T12:00:00Z'

        profile_attachment_model = {}  # ProfileAttachment
        profile_attachment_model['attachment_parameters'] = [parameter_model]
        profile_attachment_model['description'] = 'testString'
        profile_attachment_model['name'] = 'testString'
        profile_attachment_model['notifications'] = attachment_notifications_model
        profile_attachment_model['schedule'] = 'daily'
        profile_attachment_model['scope'] = [multi_cloud_scope_payload_model]
        profile_attachment_model['status'] = 'enabled'
        profile_attachment_model['data_selection_range'] = date_range_model
        profile_attachment_model['account_id'] = 'testString'
        profile_attachment_model['created_by'] = 'testString'
        profile_attachment_model['created_on'] = '2019-01-01T12:00:00Z'
        profile_attachment_model['id'] = 'testString'
        profile_attachment_model['instance_id'] = 'testString'
        profile_attachment_model['last_scan'] = last_scan_model
        profile_attachment_model['next_scan_time'] = '2019-01-01T12:00:00Z'
        profile_attachment_model['profile_id'] = 'testString'
        profile_attachment_model['updated_by'] = 'testString'
        profile_attachment_model['updated_on'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a ProfileAttachmentCollection model
        profile_attachment_collection_model_json = {}
        profile_attachment_collection_model_json['limit'] = 50
        profile_attachment_collection_model_json['total_count'] = 230
        profile_attachment_collection_model_json['first'] = page_h_ref_first_model
        profile_attachment_collection_model_json['next'] = page_h_ref_next_model
        profile_attachment_collection_model_json['attachments'] = [profile_attachment_model]

        # Construct a model instance of ProfileAttachmentCollection by calling from_dict on the json representation
        profile_attachment_collection_model = ProfileAttachmentCollection.from_dict(profile_attachment_collection_model_json)
        assert profile_attachment_collection_model != False

        # Construct a model instance of ProfileAttachmentCollection by calling from_dict on the json representation
        profile_attachment_collection_model_dict = ProfileAttachmentCollection.from_dict(profile_attachment_collection_model_json).__dict__
        profile_attachment_collection_model2 = ProfileAttachmentCollection(**profile_attachment_collection_model_dict)

        # Verify the model instances are equivalent
        assert profile_attachment_collection_model == profile_attachment_collection_model2

        # Convert model instance back to dict and verify no loss of data
        profile_attachment_collection_model_json2 = profile_attachment_collection_model.to_dict()
        assert profile_attachment_collection_model_json2 == profile_attachment_collection_model_json


class TestModel_ProfileAttachmentResponse:
    """
    Test Class for ProfileAttachmentResponse
    """

    def test_profile_attachment_response_serialization(self):
        """
        Test serialization/deserialization for ProfileAttachmentResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        attachment_notifications_controls_model = {}  # AttachmentNotificationsControls
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = ['testString']

        attachment_notifications_model = {}  # AttachmentNotifications
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        multi_cloud_scope_payload_model = {}  # MultiCloudScopePayloadById
        multi_cloud_scope_payload_model['id'] = 'testString'

        date_range_model = {}  # DateRange
        date_range_model['start_date'] = '2025-02-28T05:42:58Z'
        date_range_model['end_date'] = '2025-02-28T05:42:58Z'

        last_scan_model = {}  # LastScan
        last_scan_model['id'] = 'testString'
        last_scan_model['status'] = 'testString'
        last_scan_model['time'] = '2019-01-01T12:00:00Z'

        profile_attachment_model = {}  # ProfileAttachment
        profile_attachment_model['attachment_parameters'] = [parameter_model]
        profile_attachment_model['description'] = 'testString'
        profile_attachment_model['name'] = 'testString'
        profile_attachment_model['notifications'] = attachment_notifications_model
        profile_attachment_model['schedule'] = 'daily'
        profile_attachment_model['scope'] = [multi_cloud_scope_payload_model]
        profile_attachment_model['status'] = 'enabled'
        profile_attachment_model['data_selection_range'] = date_range_model
        profile_attachment_model['account_id'] = 'testString'
        profile_attachment_model['created_by'] = 'testString'
        profile_attachment_model['created_on'] = '2019-01-01T12:00:00Z'
        profile_attachment_model['id'] = 'testString'
        profile_attachment_model['instance_id'] = 'testString'
        profile_attachment_model['last_scan'] = last_scan_model
        profile_attachment_model['next_scan_time'] = '2019-01-01T12:00:00Z'
        profile_attachment_model['profile_id'] = 'testString'
        profile_attachment_model['updated_by'] = 'testString'
        profile_attachment_model['updated_on'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a ProfileAttachmentResponse model
        profile_attachment_response_model_json = {}
        profile_attachment_response_model_json['profile_id'] = 'testString'
        profile_attachment_response_model_json['attachments'] = [profile_attachment_model]

        # Construct a model instance of ProfileAttachmentResponse by calling from_dict on the json representation
        profile_attachment_response_model = ProfileAttachmentResponse.from_dict(profile_attachment_response_model_json)
        assert profile_attachment_response_model != False

        # Construct a model instance of ProfileAttachmentResponse by calling from_dict on the json representation
        profile_attachment_response_model_dict = ProfileAttachmentResponse.from_dict(profile_attachment_response_model_json).__dict__
        profile_attachment_response_model2 = ProfileAttachmentResponse(**profile_attachment_response_model_dict)

        # Verify the model instances are equivalent
        assert profile_attachment_response_model == profile_attachment_response_model2

        # Convert model instance back to dict and verify no loss of data
        profile_attachment_response_model_json2 = profile_attachment_response_model.to_dict()
        assert profile_attachment_response_model_json2 == profile_attachment_response_model_json


class TestModel_ProfileCollection:
    """
    Test Class for ProfileCollection
    """

    def test_profile_collection_serialization(self):
        """
        Test serialization/deserialization for ProfileCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_first_model = {}  # PageHRefFirst
        page_h_ref_first_model['href'] = 'testString'

        page_h_ref_next_model = {}  # PageHRefNext
        page_h_ref_next_model['href'] = 'testString'
        page_h_ref_next_model['start'] = 'testString'

        control_doc_model = {}  # ControlDoc
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        control_specification_model = {}  # ControlSpecification
        control_specification_model['id'] = 'testString'
        control_specification_model['responsibility'] = 'testString'
        control_specification_model['component_id'] = 'testString'
        control_specification_model['component_name'] = 'testString'
        control_specification_model['component_type'] = 'testString'
        control_specification_model['environment'] = 'testString'
        control_specification_model['description'] = 'testString'
        control_specification_model['assessments_count'] = 38
        control_specification_model['assessments'] = [assessment_model]

        profile_controls_model = {}  # ProfileControls
        profile_controls_model['control_requirement'] = True
        profile_controls_model['control_library_id'] = 'testString'
        profile_controls_model['control_id'] = 'testString'
        profile_controls_model['control_library_version'] = 'testString'
        profile_controls_model['control_name'] = 'testString'
        profile_controls_model['control_description'] = 'testString'
        profile_controls_model['control_severity'] = 'testString'
        profile_controls_model['control_category'] = 'testString'
        profile_controls_model['control_parent'] = 'testString'
        profile_controls_model['control_docs'] = control_doc_model
        profile_controls_model['control_specifications'] = [control_specification_model]

        default_parameters_model = {}  # DefaultParameters
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'testString'

        profile_model = {}  # Profile
        profile_model['id'] = 'testString'
        profile_model['profile_name'] = 'testString'
        profile_model['instance_id'] = 'testString'
        profile_model['hierarchy_enabled'] = True
        profile_model['profile_description'] = 'testString'
        profile_model['profile_type'] = 'custom'
        profile_model['profile_version'] = 'testString'
        profile_model['version_group_label'] = 'testString'
        profile_model['latest'] = True
        profile_model['created_by'] = 'testString'
        profile_model['created_on'] = '2019-01-01T12:00:00Z'
        profile_model['updated_by'] = 'testString'
        profile_model['updated_on'] = '2019-01-01T12:00:00Z'
        profile_model['controls_count'] = 38
        profile_model['attachments_count'] = 38
        profile_model['controls'] = [profile_controls_model]
        profile_model['default_parameters'] = [default_parameters_model]

        # Construct a json representation of a ProfileCollection model
        profile_collection_model_json = {}
        profile_collection_model_json['limit'] = 50
        profile_collection_model_json['total_count'] = 230
        profile_collection_model_json['first'] = page_h_ref_first_model
        profile_collection_model_json['next'] = page_h_ref_next_model
        profile_collection_model_json['profiles'] = [profile_model]

        # Construct a model instance of ProfileCollection by calling from_dict on the json representation
        profile_collection_model = ProfileCollection.from_dict(profile_collection_model_json)
        assert profile_collection_model != False

        # Construct a model instance of ProfileCollection by calling from_dict on the json representation
        profile_collection_model_dict = ProfileCollection.from_dict(profile_collection_model_json).__dict__
        profile_collection_model2 = ProfileCollection(**profile_collection_model_dict)

        # Verify the model instances are equivalent
        assert profile_collection_model == profile_collection_model2

        # Convert model instance back to dict and verify no loss of data
        profile_collection_model_json2 = profile_collection_model.to_dict()
        assert profile_collection_model_json2 == profile_collection_model_json


class TestModel_ProfileControls:
    """
    Test Class for ProfileControls
    """

    def test_profile_controls_serialization(self):
        """
        Test serialization/deserialization for ProfileControls
        """

        # Construct dict forms of any model objects needed in order to build this model.

        control_doc_model = {}  # ControlDoc
        control_doc_model['control_docs_id'] = 'testString'
        control_doc_model['control_docs_type'] = 'testString'

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_model]

        control_specification_model = {}  # ControlSpecification
        control_specification_model['id'] = 'testString'
        control_specification_model['responsibility'] = 'testString'
        control_specification_model['component_id'] = 'testString'
        control_specification_model['component_name'] = 'testString'
        control_specification_model['component_type'] = 'testString'
        control_specification_model['environment'] = 'testString'
        control_specification_model['description'] = 'testString'
        control_specification_model['assessments_count'] = 38
        control_specification_model['assessments'] = [assessment_model]

        # Construct a json representation of a ProfileControls model
        profile_controls_model_json = {}
        profile_controls_model_json['control_requirement'] = True
        profile_controls_model_json['control_library_id'] = 'testString'
        profile_controls_model_json['control_id'] = 'testString'
        profile_controls_model_json['control_library_version'] = 'testString'
        profile_controls_model_json['control_name'] = 'testString'
        profile_controls_model_json['control_description'] = 'testString'
        profile_controls_model_json['control_severity'] = 'testString'
        profile_controls_model_json['control_category'] = 'testString'
        profile_controls_model_json['control_parent'] = 'testString'
        profile_controls_model_json['control_docs'] = control_doc_model
        profile_controls_model_json['control_specifications'] = [control_specification_model]

        # Construct a model instance of ProfileControls by calling from_dict on the json representation
        profile_controls_model = ProfileControls.from_dict(profile_controls_model_json)
        assert profile_controls_model != False

        # Construct a model instance of ProfileControls by calling from_dict on the json representation
        profile_controls_model_dict = ProfileControls.from_dict(profile_controls_model_json).__dict__
        profile_controls_model2 = ProfileControls(**profile_controls_model_dict)

        # Verify the model instances are equivalent
        assert profile_controls_model == profile_controls_model2

        # Convert model instance back to dict and verify no loss of data
        profile_controls_model_json2 = profile_controls_model.to_dict()
        assert profile_controls_model_json2 == profile_controls_model_json


class TestModel_ProfileControlsPrototype:
    """
    Test Class for ProfileControlsPrototype
    """

    def test_profile_controls_prototype_serialization(self):
        """
        Test serialization/deserialization for ProfileControlsPrototype
        """

        # Construct a json representation of a ProfileControlsPrototype model
        profile_controls_prototype_model_json = {}
        profile_controls_prototype_model_json['control_library_id'] = 'testString'
        profile_controls_prototype_model_json['control_id'] = 'testString'

        # Construct a model instance of ProfileControlsPrototype by calling from_dict on the json representation
        profile_controls_prototype_model = ProfileControlsPrototype.from_dict(profile_controls_prototype_model_json)
        assert profile_controls_prototype_model != False

        # Construct a model instance of ProfileControlsPrototype by calling from_dict on the json representation
        profile_controls_prototype_model_dict = ProfileControlsPrototype.from_dict(profile_controls_prototype_model_json).__dict__
        profile_controls_prototype_model2 = ProfileControlsPrototype(**profile_controls_prototype_model_dict)

        # Verify the model instances are equivalent
        assert profile_controls_prototype_model == profile_controls_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        profile_controls_prototype_model_json2 = profile_controls_prototype_model.to_dict()
        assert profile_controls_prototype_model_json2 == profile_controls_prototype_model_json


class TestModel_ProfileDefaultParametersResponse:
    """
    Test Class for ProfileDefaultParametersResponse
    """

    def test_profile_default_parameters_response_serialization(self):
        """
        Test serialization/deserialization for ProfileDefaultParametersResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        default_parameters_model = {}  # DefaultParameters
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'testString'

        # Construct a json representation of a ProfileDefaultParametersResponse model
        profile_default_parameters_response_model_json = {}
        profile_default_parameters_response_model_json['id'] = 'testString'
        profile_default_parameters_response_model_json['default_parameters'] = [default_parameters_model]

        # Construct a model instance of ProfileDefaultParametersResponse by calling from_dict on the json representation
        profile_default_parameters_response_model = ProfileDefaultParametersResponse.from_dict(profile_default_parameters_response_model_json)
        assert profile_default_parameters_response_model != False

        # Construct a model instance of ProfileDefaultParametersResponse by calling from_dict on the json representation
        profile_default_parameters_response_model_dict = ProfileDefaultParametersResponse.from_dict(profile_default_parameters_response_model_json).__dict__
        profile_default_parameters_response_model2 = ProfileDefaultParametersResponse(**profile_default_parameters_response_model_dict)

        # Verify the model instances are equivalent
        assert profile_default_parameters_response_model == profile_default_parameters_response_model2

        # Convert model instance back to dict and verify no loss of data
        profile_default_parameters_response_model_json2 = profile_default_parameters_response_model.to_dict()
        assert profile_default_parameters_response_model_json2 == profile_default_parameters_response_model_json


class TestModel_ProfileInfo:
    """
    Test Class for ProfileInfo
    """

    def test_profile_info_serialization(self):
        """
        Test serialization/deserialization for ProfileInfo
        """

        # Construct a json representation of a ProfileInfo model
        profile_info_model_json = {}
        profile_info_model_json['id'] = '44a5-a292-32114fa73558'
        profile_info_model_json['name'] = 'IBM FS Cloud'
        profile_info_model_json['version'] = '0.1'

        # Construct a model instance of ProfileInfo by calling from_dict on the json representation
        profile_info_model = ProfileInfo.from_dict(profile_info_model_json)
        assert profile_info_model != False

        # Construct a model instance of ProfileInfo by calling from_dict on the json representation
        profile_info_model_dict = ProfileInfo.from_dict(profile_info_model_json).__dict__
        profile_info_model2 = ProfileInfo(**profile_info_model_dict)

        # Verify the model instances are equivalent
        assert profile_info_model == profile_info_model2

        # Convert model instance back to dict and verify no loss of data
        profile_info_model_json2 = profile_info_model.to_dict()
        assert profile_info_model_json2 == profile_info_model_json


class TestModel_ProviderType:
    """
    Test Class for ProviderType
    """

    def test_provider_type_serialization(self):
        """
        Test serialization/deserialization for ProviderType
        """

        # Construct dict forms of any model objects needed in order to build this model.

        label_type_model = {}  # LabelType
        label_type_model['text'] = '1 per instance'
        label_type_model['tip'] = 'Only 1 per instance'

        additional_property_model = {}  # AdditionalProperty
        additional_property_model['type'] = 'text'
        additional_property_model['display_name'] = 'Workload Protection Instance CRN'

        # Construct a json representation of a ProviderType model
        provider_type_model_json = {}
        provider_type_model_json['id'] = '7588190cce3c05ac8f7942ea597dafce'
        provider_type_model_json['type'] = 'workload-protection'
        provider_type_model_json['name'] = 'workload-protection'
        provider_type_model_json['description'] = 'Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.'
        provider_type_model_json['s2s_enabled'] = True
        provider_type_model_json['instance_limit'] = 1
        provider_type_model_json['mode'] = 'PULL'
        provider_type_model_json['data_type'] = 'com.sysdig.secure.results'
        provider_type_model_json['icon'] = 'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+'
        provider_type_model_json['label'] = label_type_model
        provider_type_model_json['attributes'] = {'key1': additional_property_model}
        provider_type_model_json['created_at'] = '2023-07-24T13:14:18.884000Z'
        provider_type_model_json['updated_at'] = '2023-07-24T13:14:18.884000Z'

        # Construct a model instance of ProviderType by calling from_dict on the json representation
        provider_type_model = ProviderType.from_dict(provider_type_model_json)
        assert provider_type_model != False

        # Construct a model instance of ProviderType by calling from_dict on the json representation
        provider_type_model_dict = ProviderType.from_dict(provider_type_model_json).__dict__
        provider_type_model2 = ProviderType(**provider_type_model_dict)

        # Verify the model instances are equivalent
        assert provider_type_model == provider_type_model2

        # Convert model instance back to dict and verify no loss of data
        provider_type_model_json2 = provider_type_model.to_dict()
        assert provider_type_model_json2 == provider_type_model_json


class TestModel_ProviderTypeCollection:
    """
    Test Class for ProviderTypeCollection
    """

    def test_provider_type_collection_serialization(self):
        """
        Test serialization/deserialization for ProviderTypeCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        label_type_model = {}  # LabelType
        label_type_model['text'] = '1 per instance'
        label_type_model['tip'] = 'Only 1 per instance'

        additional_property_model = {}  # AdditionalProperty
        additional_property_model['type'] = 'text'
        additional_property_model['display_name'] = 'Workload Protection Instance CRN'

        provider_type_model = {}  # ProviderType
        provider_type_model['id'] = '7588190cce3c05ac8f7942ea597dafce'
        provider_type_model['type'] = 'workload-protection'
        provider_type_model['name'] = 'workload-protection'
        provider_type_model['description'] = 'Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.'
        provider_type_model['s2s_enabled'] = True
        provider_type_model['instance_limit'] = 1
        provider_type_model['mode'] = 'PULL'
        provider_type_model['data_type'] = 'com.sysdig.secure.results'
        provider_type_model['icon'] = 'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+'
        provider_type_model['label'] = label_type_model
        provider_type_model['attributes'] = {'key1': additional_property_model}
        provider_type_model['created_at'] = '2023-07-24T13:14:18.884000Z'
        provider_type_model['updated_at'] = '2023-07-24T13:14:18.884000Z'

        # Construct a json representation of a ProviderTypeCollection model
        provider_type_collection_model_json = {}
        provider_type_collection_model_json['provider_types'] = [provider_type_model]

        # Construct a model instance of ProviderTypeCollection by calling from_dict on the json representation
        provider_type_collection_model = ProviderTypeCollection.from_dict(provider_type_collection_model_json)
        assert provider_type_collection_model != False

        # Construct a model instance of ProviderTypeCollection by calling from_dict on the json representation
        provider_type_collection_model_dict = ProviderTypeCollection.from_dict(provider_type_collection_model_json).__dict__
        provider_type_collection_model2 = ProviderTypeCollection(**provider_type_collection_model_dict)

        # Verify the model instances are equivalent
        assert provider_type_collection_model == provider_type_collection_model2

        # Convert model instance back to dict and verify no loss of data
        provider_type_collection_model_json2 = provider_type_collection_model.to_dict()
        assert provider_type_collection_model_json2 == provider_type_collection_model_json


class TestModel_ProviderTypeInstance:
    """
    Test Class for ProviderTypeInstance
    """

    def test_provider_type_instance_serialization(self):
        """
        Test serialization/deserialization for ProviderTypeInstance
        """

        # Construct a json representation of a ProviderTypeInstance model
        provider_type_instance_model_json = {}
        provider_type_instance_model_json['id'] = '7588190cce3c05ac8f7942ea597dafce'
        provider_type_instance_model_json['type'] = 'workload-protection'
        provider_type_instance_model_json['name'] = 'workload-protection-instance-1'
        provider_type_instance_model_json['attributes'] = {'wp_crn': 'crn:v1:staging:public:sysdig-secure:eu-gb:a/14q5SEnVIbwxzvP4AWPCjr2dJg5BAvPb:d1461d1ae-df1eee12fa81812e0-12-aa259::'}
        provider_type_instance_model_json['created_at'] = '2023-07-24T13:14:18.884000Z'
        provider_type_instance_model_json['updated_at'] = '2023-07-24T13:14:18.884000Z'

        # Construct a model instance of ProviderTypeInstance by calling from_dict on the json representation
        provider_type_instance_model = ProviderTypeInstance.from_dict(provider_type_instance_model_json)
        assert provider_type_instance_model != False

        # Construct a model instance of ProviderTypeInstance by calling from_dict on the json representation
        provider_type_instance_model_dict = ProviderTypeInstance.from_dict(provider_type_instance_model_json).__dict__
        provider_type_instance_model2 = ProviderTypeInstance(**provider_type_instance_model_dict)

        # Verify the model instances are equivalent
        assert provider_type_instance_model == provider_type_instance_model2

        # Convert model instance back to dict and verify no loss of data
        provider_type_instance_model_json2 = provider_type_instance_model.to_dict()
        assert provider_type_instance_model_json2 == provider_type_instance_model_json


class TestModel_ProviderTypeInstanceCollection:
    """
    Test Class for ProviderTypeInstanceCollection
    """

    def test_provider_type_instance_collection_serialization(self):
        """
        Test serialization/deserialization for ProviderTypeInstanceCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_type_instance_model = {}  # ProviderTypeInstance
        provider_type_instance_model['id'] = '7588190cce3c05ac8f7942ea597dafce'
        provider_type_instance_model['type'] = 'workload-protection'
        provider_type_instance_model['name'] = 'workload-protection-instance-1'
        provider_type_instance_model['attributes'] = {'wp_crn': 'crn:v1:staging:public:sysdig-secure:eu-gb:a/14q5SEnVIbwxzvP4AWPCjr2dJg5BAvPb:d1461d1ae-df1eee12fa81812e0-12-aa259::'}
        provider_type_instance_model['created_at'] = '2023-07-24T13:14:18.884000Z'
        provider_type_instance_model['updated_at'] = '2023-07-24T13:14:18.884000Z'

        # Construct a json representation of a ProviderTypeInstanceCollection model
        provider_type_instance_collection_model_json = {}
        provider_type_instance_collection_model_json['provider_type_instances'] = [provider_type_instance_model]

        # Construct a model instance of ProviderTypeInstanceCollection by calling from_dict on the json representation
        provider_type_instance_collection_model = ProviderTypeInstanceCollection.from_dict(provider_type_instance_collection_model_json)
        assert provider_type_instance_collection_model != False

        # Construct a model instance of ProviderTypeInstanceCollection by calling from_dict on the json representation
        provider_type_instance_collection_model_dict = ProviderTypeInstanceCollection.from_dict(provider_type_instance_collection_model_json).__dict__
        provider_type_instance_collection_model2 = ProviderTypeInstanceCollection(**provider_type_instance_collection_model_dict)

        # Verify the model instances are equivalent
        assert provider_type_instance_collection_model == provider_type_instance_collection_model2

        # Convert model instance back to dict and verify no loss of data
        provider_type_instance_collection_model_json2 = provider_type_instance_collection_model.to_dict()
        assert provider_type_instance_collection_model_json2 == provider_type_instance_collection_model_json


class TestModel_Report:
    """
    Test Class for Report
    """

    def test_report_serialization(self):
        """
        Test serialization/deserialization for Report
        """

        # Construct dict forms of any model objects needed in order to build this model.

        account_model = {}  # Account
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        profile_info_model = {}  # ProfileInfo
        profile_info_model['id'] = '44a5-a292-32114fa73558'
        profile_info_model['name'] = 'IBM FS Cloud'
        profile_info_model['version'] = '0.1'

        scope_id_model = {}  # ScopeID
        scope_id_model['id'] = '2411ffdc16844b07b42521c3443f456d'
        scope_id_model['type'] = 'account'

        scope_property_model = {}  # ScopePropertyScopeAny
        scope_property_model['name'] = 'testString'
        scope_property_model['value'] = 'testString'

        scope_model = {}  # Scope
        scope_model['id'] = 'testString'
        scope_model['name'] = 'testString'
        scope_model['description'] = 'testString'
        scope_model['environment'] = 'testString'
        scope_model['properties'] = [scope_property_model]
        scope_model['account_id'] = 'testString'
        scope_model['instance_id'] = 'testString'
        scope_model['created_by'] = 'testString'
        scope_model['created_on'] = '2019-01-01T12:00:00Z'
        scope_model['updated_by'] = 'testString'
        scope_model['updated_on'] = '2019-01-01T12:00:00Z'
        scope_model['attachment_count'] = 72.5

        attachment_notifications_controls_model = {}  # AttachmentNotificationsControls
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = ['testString']

        attachment_notifications_model = {}  # AttachmentNotifications
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        attachment_model = {}  # Attachment
        attachment_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        attachment_model['name'] = 'resource group - Default'
        attachment_model['description'] = 'Scoped to the Default resource group'
        attachment_model['schedule'] = 'daily'
        attachment_model['scope'] = 'testString'
        attachment_model['scopes'] = [scope_model]
        attachment_model['notifications'] = attachment_notifications_model

        control_summary_model = {}  # ControlSummary
        control_summary_model['id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        control_summary_model['control_name'] = 'ibm-cloud-rule'
        control_summary_model['control_description'] = 'Ensure security questions are registered by the account owner'

        compliance_stats_with_non_compliant_model = {}  # ComplianceStatsWithNonCompliant
        compliance_stats_with_non_compliant_model['status'] = 'compliant'
        compliance_stats_with_non_compliant_model['total_count'] = 150
        compliance_stats_with_non_compliant_model['compliant_count'] = 130
        compliance_stats_with_non_compliant_model['not_compliant_count'] = 5
        compliance_stats_with_non_compliant_model['unable_to_perform_count'] = 5
        compliance_stats_with_non_compliant_model['user_evaluation_required_count'] = 10
        compliance_stats_with_non_compliant_model['not_applicable_count'] = 7
        compliance_stats_with_non_compliant_model['not_compliant_controls'] = [control_summary_model]

        eval_stats_model = {}  # EvalStats
        eval_stats_model['status'] = 'compliant'
        eval_stats_model['total_count'] = 140
        eval_stats_model['pass_count'] = 123
        eval_stats_model['failure_count'] = 12
        eval_stats_model['error_count'] = 5
        eval_stats_model['skipped_count'] = 7
        eval_stats_model['completed_count'] = 135

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        report_scope_model = {}  # ReportScope
        report_scope_model['id'] = 'testString'
        report_scope_model['name'] = 'testString'
        report_scope_model['href'] = 'testString'
        report_scope_model['environment'] = 'testString'

        link_model = {}  # Link
        link_model['description'] = 'testString'
        link_model['href'] = 'testString'

        additional_details_model = {}  # AdditionalDetails
        additional_details_model['created_by'] = 'Security and Compliance Center'
        additional_details_model['labels'] = ['testString']
        additional_details_model['links'] = [link_model]

        # Construct a json representation of a Report model
        report_model_json = {}
        report_model_json['id'] = '44a5-a292-32114fa73558'
        report_model_json['type'] = 'scheduled'
        report_model_json['group_id'] = '55b6-b3A4-432250b84669'
        report_model_json['created_on'] = '2022-08-15T12:30:01Z'
        report_model_json['scan_time'] = '2022-08-15T12:30:01Z'
        report_model_json['cos_object'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7'
        report_model_json['instance_id'] = 'testString'
        report_model_json['account'] = account_model
        report_model_json['profile'] = profile_info_model
        report_model_json['scope'] = scope_id_model
        report_model_json['attachment'] = attachment_model
        report_model_json['controls_summary'] = compliance_stats_with_non_compliant_model
        report_model_json['evaluations_summary'] = eval_stats_model
        report_model_json['tags'] = tags_model
        report_model_json['scopes'] = [report_scope_model]
        report_model_json['additional_details'] = additional_details_model

        # Construct a model instance of Report by calling from_dict on the json representation
        report_model = Report.from_dict(report_model_json)
        assert report_model != False

        # Construct a model instance of Report by calling from_dict on the json representation
        report_model_dict = Report.from_dict(report_model_json).__dict__
        report_model2 = Report(**report_model_dict)

        # Verify the model instances are equivalent
        assert report_model == report_model2

        # Convert model instance back to dict and verify no loss of data
        report_model_json2 = report_model.to_dict()
        assert report_model_json2 == report_model_json


class TestModel_ReportCollection:
    """
    Test Class for ReportCollection
    """

    def test_report_collection_serialization(self):
        """
        Test serialization/deserialization for ReportCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_first_model = {}  # PageHRefFirst
        page_h_ref_first_model['href'] = 'testString'

        page_h_ref_next_model = {}  # PageHRefNext
        page_h_ref_next_model['href'] = 'testString'
        page_h_ref_next_model['start'] = 'testString'

        account_model = {}  # Account
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        profile_info_model = {}  # ProfileInfo
        profile_info_model['id'] = '44a5-a292-32114fa73558'
        profile_info_model['name'] = 'IBM FS Cloud'
        profile_info_model['version'] = '0.1'

        scope_id_model = {}  # ScopeID
        scope_id_model['id'] = '2411ffdc16844b07b42521c3443f456d'
        scope_id_model['type'] = 'account'

        scope_property_model = {}  # ScopePropertyScopeAny
        scope_property_model['name'] = 'testString'
        scope_property_model['value'] = 'testString'

        scope_model = {}  # Scope
        scope_model['id'] = 'testString'
        scope_model['name'] = 'testString'
        scope_model['description'] = 'testString'
        scope_model['environment'] = 'testString'
        scope_model['properties'] = [scope_property_model]
        scope_model['account_id'] = 'testString'
        scope_model['instance_id'] = 'testString'
        scope_model['created_by'] = 'testString'
        scope_model['created_on'] = '2019-01-01T12:00:00Z'
        scope_model['updated_by'] = 'testString'
        scope_model['updated_on'] = '2019-01-01T12:00:00Z'
        scope_model['attachment_count'] = 72.5

        attachment_notifications_controls_model = {}  # AttachmentNotificationsControls
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = ['testString']

        attachment_notifications_model = {}  # AttachmentNotifications
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        attachment_model = {}  # Attachment
        attachment_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        attachment_model['name'] = 'resource group - Default'
        attachment_model['description'] = 'Scoped to the Default resource group'
        attachment_model['schedule'] = 'daily'
        attachment_model['scope'] = 'testString'
        attachment_model['scopes'] = [scope_model]
        attachment_model['notifications'] = attachment_notifications_model

        control_summary_model = {}  # ControlSummary
        control_summary_model['id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        control_summary_model['control_name'] = 'ibm-cloud-rule'
        control_summary_model['control_description'] = 'Ensure security questions are registered by the account owner'

        compliance_stats_with_non_compliant_model = {}  # ComplianceStatsWithNonCompliant
        compliance_stats_with_non_compliant_model['status'] = 'compliant'
        compliance_stats_with_non_compliant_model['total_count'] = 150
        compliance_stats_with_non_compliant_model['compliant_count'] = 130
        compliance_stats_with_non_compliant_model['not_compliant_count'] = 5
        compliance_stats_with_non_compliant_model['unable_to_perform_count'] = 5
        compliance_stats_with_non_compliant_model['user_evaluation_required_count'] = 10
        compliance_stats_with_non_compliant_model['not_applicable_count'] = 7
        compliance_stats_with_non_compliant_model['not_compliant_controls'] = [control_summary_model]

        eval_stats_model = {}  # EvalStats
        eval_stats_model['status'] = 'compliant'
        eval_stats_model['total_count'] = 140
        eval_stats_model['pass_count'] = 123
        eval_stats_model['failure_count'] = 12
        eval_stats_model['error_count'] = 5
        eval_stats_model['skipped_count'] = 7
        eval_stats_model['completed_count'] = 135

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        report_scope_model = {}  # ReportScope
        report_scope_model['id'] = 'testString'
        report_scope_model['name'] = 'testString'
        report_scope_model['href'] = 'testString'
        report_scope_model['environment'] = 'testString'

        link_model = {}  # Link
        link_model['description'] = 'testString'
        link_model['href'] = 'testString'

        additional_details_model = {}  # AdditionalDetails
        additional_details_model['created_by'] = 'Security and Compliance Center'
        additional_details_model['labels'] = ['testString']
        additional_details_model['links'] = [link_model]

        report_model = {}  # Report
        report_model['id'] = '44a5-a292-32114fa73558'
        report_model['type'] = 'scheduled'
        report_model['group_id'] = '55b6-b3A4-432250b84669'
        report_model['created_on'] = '2022-08-15T12:30:01Z'
        report_model['scan_time'] = '2022-08-15T12:30:01Z'
        report_model['cos_object'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7'
        report_model['instance_id'] = 'testString'
        report_model['account'] = account_model
        report_model['profile'] = profile_info_model
        report_model['scope'] = scope_id_model
        report_model['attachment'] = attachment_model
        report_model['controls_summary'] = compliance_stats_with_non_compliant_model
        report_model['evaluations_summary'] = eval_stats_model
        report_model['tags'] = tags_model
        report_model['scopes'] = [report_scope_model]
        report_model['additional_details'] = additional_details_model

        # Construct a json representation of a ReportCollection model
        report_collection_model_json = {}
        report_collection_model_json['limit'] = 50
        report_collection_model_json['total_count'] = 230
        report_collection_model_json['first'] = page_h_ref_first_model
        report_collection_model_json['next'] = page_h_ref_next_model
        report_collection_model_json['home_account_id'] = 'testString'
        report_collection_model_json['reports'] = [report_model]

        # Construct a model instance of ReportCollection by calling from_dict on the json representation
        report_collection_model = ReportCollection.from_dict(report_collection_model_json)
        assert report_collection_model != False

        # Construct a model instance of ReportCollection by calling from_dict on the json representation
        report_collection_model_dict = ReportCollection.from_dict(report_collection_model_json).__dict__
        report_collection_model2 = ReportCollection(**report_collection_model_dict)

        # Verify the model instances are equivalent
        assert report_collection_model == report_collection_model2

        # Convert model instance back to dict and verify no loss of data
        report_collection_model_json2 = report_collection_model.to_dict()
        assert report_collection_model_json2 == report_collection_model_json


class TestModel_ReportControls:
    """
    Test Class for ReportControls
    """

    def test_report_controls_serialization(self):
        """
        Test serialization/deserialization for ReportControls
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['assessment_type'] = 'testString'
        parameter_model['assessment_id'] = 'testString'
        parameter_model['parameter_name'] = 'location'
        parameter_model['parameter_display_name'] = 'Location'
        parameter_model['parameter_type'] = 'string'
        parameter_model['parameter_value'] = 'testString'

        assessment_with_stats_model = {}  # AssessmentWithStats
        assessment_with_stats_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_with_stats_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_with_stats_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_with_stats_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_with_stats_model['parameter_count'] = 1
        assessment_with_stats_model['parameters'] = [parameter_model]
        assessment_with_stats_model['total_count'] = 140
        assessment_with_stats_model['pass_count'] = 123
        assessment_with_stats_model['failure_count'] = 12
        assessment_with_stats_model['error_count'] = 5
        assessment_with_stats_model['completed_count'] = 135

        control_specification_with_stats_model = {}  # ControlSpecificationWithStats
        control_specification_with_stats_model['control_specification_id'] = '18d32a4430e54c81a6668952609763b2'
        control_specification_with_stats_model['control_specification_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        control_specification_with_stats_model['component_id'] = 'cloud-object_storage'
        control_specification_with_stats_model['component_name'] = 'cloud-object_storage'
        control_specification_with_stats_model['environment'] = 'ibm cloud'
        control_specification_with_stats_model['responsibility'] = 'user'
        control_specification_with_stats_model['assessments'] = [assessment_with_stats_model]
        control_specification_with_stats_model['status'] = 'compliant'
        control_specification_with_stats_model['total_count'] = 150
        control_specification_with_stats_model['compliant_count'] = 130
        control_specification_with_stats_model['not_compliant_count'] = 5
        control_specification_with_stats_model['unable_to_perform_count'] = 5
        control_specification_with_stats_model['user_evaluation_required_count'] = 10
        control_specification_with_stats_model['not_applicable_count'] = 7

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        control_with_stats_model = {}  # ControlWithStats
        control_with_stats_model['report_id'] = '6f1fdb98-c08b-41a8-a2f9-df10b51ff34a'
        control_with_stats_model['home_account_id'] = '2411ffdc16844b07b42521c3443f456d'
        control_with_stats_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        control_with_stats_model['control_library_id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        control_with_stats_model['control_library_version'] = 'v1.2.3'
        control_with_stats_model['control_name'] = 'Password Management'
        control_with_stats_model['control_description'] = 'Password Management'
        control_with_stats_model['control_category'] = 'Access Control'
        control_with_stats_model['control_specifications'] = [control_specification_with_stats_model]
        control_with_stats_model['resource_tags'] = tags_model
        control_with_stats_model['status'] = 'compliant'
        control_with_stats_model['total_count'] = 150
        control_with_stats_model['compliant_count'] = 130
        control_with_stats_model['not_compliant_count'] = 5
        control_with_stats_model['unable_to_perform_count'] = 5
        control_with_stats_model['user_evaluation_required_count'] = 10
        control_with_stats_model['not_applicable_count'] = 7

        # Construct a json representation of a ReportControls model
        report_controls_model_json = {}
        report_controls_model_json['report_id'] = 'testString'
        report_controls_model_json['home_account_id'] = 'testString'
        report_controls_model_json['controls'] = [control_with_stats_model]

        # Construct a model instance of ReportControls by calling from_dict on the json representation
        report_controls_model = ReportControls.from_dict(report_controls_model_json)
        assert report_controls_model != False

        # Construct a model instance of ReportControls by calling from_dict on the json representation
        report_controls_model_dict = ReportControls.from_dict(report_controls_model_json).__dict__
        report_controls_model2 = ReportControls(**report_controls_model_dict)

        # Verify the model instances are equivalent
        assert report_controls_model == report_controls_model2

        # Convert model instance back to dict and verify no loss of data
        report_controls_model_json2 = report_controls_model.to_dict()
        assert report_controls_model_json2 == report_controls_model_json


class TestModel_ReportLatest:
    """
    Test Class for ReportLatest
    """

    def test_report_latest_serialization(self):
        """
        Test serialization/deserialization for ReportLatest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        compliance_stats_model = {}  # ComplianceStats
        compliance_stats_model['status'] = 'compliant'
        compliance_stats_model['total_count'] = 150
        compliance_stats_model['compliant_count'] = 130
        compliance_stats_model['not_compliant_count'] = 5
        compliance_stats_model['unable_to_perform_count'] = 5
        compliance_stats_model['user_evaluation_required_count'] = 10
        compliance_stats_model['not_applicable_count'] = 7

        eval_stats_model = {}  # EvalStats
        eval_stats_model['status'] = 'compliant'
        eval_stats_model['total_count'] = 140
        eval_stats_model['pass_count'] = 123
        eval_stats_model['failure_count'] = 12
        eval_stats_model['error_count'] = 5
        eval_stats_model['skipped_count'] = 7
        eval_stats_model['completed_count'] = 135

        compliance_score_model = {}  # ComplianceScore
        compliance_score_model['passed'] = 1
        compliance_score_model['total_count'] = 4
        compliance_score_model['percent'] = 25

        account_model = {}  # Account
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        profile_info_model = {}  # ProfileInfo
        profile_info_model['id'] = '44a5-a292-32114fa73558'
        profile_info_model['name'] = 'IBM FS Cloud'
        profile_info_model['version'] = '0.1'

        scope_id_model = {}  # ScopeID
        scope_id_model['id'] = '2411ffdc16844b07b42521c3443f456d'
        scope_id_model['type'] = 'account'

        scope_property_model = {}  # ScopePropertyScopeAny
        scope_property_model['name'] = 'testString'
        scope_property_model['value'] = 'testString'

        scope_model = {}  # Scope
        scope_model['id'] = 'testString'
        scope_model['name'] = 'testString'
        scope_model['description'] = 'testString'
        scope_model['environment'] = 'testString'
        scope_model['properties'] = [scope_property_model]
        scope_model['account_id'] = 'testString'
        scope_model['instance_id'] = 'testString'
        scope_model['created_by'] = 'testString'
        scope_model['created_on'] = '2019-01-01T12:00:00Z'
        scope_model['updated_by'] = 'testString'
        scope_model['updated_on'] = '2019-01-01T12:00:00Z'
        scope_model['attachment_count'] = 72.5

        attachment_notifications_controls_model = {}  # AttachmentNotificationsControls
        attachment_notifications_controls_model['threshold_limit'] = 15
        attachment_notifications_controls_model['failed_control_ids'] = ['testString']

        attachment_notifications_model = {}  # AttachmentNotifications
        attachment_notifications_model['enabled'] = True
        attachment_notifications_model['controls'] = attachment_notifications_controls_model

        attachment_model = {}  # Attachment
        attachment_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        attachment_model['name'] = 'resource group - Default'
        attachment_model['description'] = 'Scoped to the Default resource group'
        attachment_model['schedule'] = 'daily'
        attachment_model['scope'] = 'testString'
        attachment_model['scopes'] = [scope_model]
        attachment_model['notifications'] = attachment_notifications_model

        control_summary_model = {}  # ControlSummary
        control_summary_model['id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        control_summary_model['control_name'] = 'ibm-cloud-rule'
        control_summary_model['control_description'] = 'Ensure security questions are registered by the account owner'

        compliance_stats_with_non_compliant_model = {}  # ComplianceStatsWithNonCompliant
        compliance_stats_with_non_compliant_model['status'] = 'compliant'
        compliance_stats_with_non_compliant_model['total_count'] = 150
        compliance_stats_with_non_compliant_model['compliant_count'] = 130
        compliance_stats_with_non_compliant_model['not_compliant_count'] = 5
        compliance_stats_with_non_compliant_model['unable_to_perform_count'] = 5
        compliance_stats_with_non_compliant_model['user_evaluation_required_count'] = 10
        compliance_stats_with_non_compliant_model['not_applicable_count'] = 7
        compliance_stats_with_non_compliant_model['not_compliant_controls'] = [control_summary_model]

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        report_scope_model = {}  # ReportScope
        report_scope_model['id'] = 'testString'
        report_scope_model['name'] = 'testString'
        report_scope_model['href'] = 'testString'
        report_scope_model['environment'] = 'testString'

        link_model = {}  # Link
        link_model['description'] = 'testString'
        link_model['href'] = 'testString'

        additional_details_model = {}  # AdditionalDetails
        additional_details_model['created_by'] = 'Security and Compliance Center'
        additional_details_model['labels'] = ['testString']
        additional_details_model['links'] = [link_model]

        report_model = {}  # Report
        report_model['id'] = '44a5-a292-32114fa73558'
        report_model['type'] = 'scheduled'
        report_model['group_id'] = '55b6-b3A4-432250b84669'
        report_model['created_on'] = '2022-08-15T12:30:01Z'
        report_model['scan_time'] = '2022-08-15T12:30:01Z'
        report_model['cos_object'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7'
        report_model['instance_id'] = 'testString'
        report_model['account'] = account_model
        report_model['profile'] = profile_info_model
        report_model['scope'] = scope_id_model
        report_model['attachment'] = attachment_model
        report_model['controls_summary'] = compliance_stats_with_non_compliant_model
        report_model['evaluations_summary'] = eval_stats_model
        report_model['tags'] = tags_model
        report_model['scopes'] = [report_scope_model]
        report_model['additional_details'] = additional_details_model

        # Construct a json representation of a ReportLatest model
        report_latest_model_json = {}
        report_latest_model_json['home_account_id'] = 'testString'
        report_latest_model_json['controls_summary'] = compliance_stats_model
        report_latest_model_json['evaluations_summary'] = eval_stats_model
        report_latest_model_json['score'] = compliance_score_model
        report_latest_model_json['reports'] = [report_model]

        # Construct a model instance of ReportLatest by calling from_dict on the json representation
        report_latest_model = ReportLatest.from_dict(report_latest_model_json)
        assert report_latest_model != False

        # Construct a model instance of ReportLatest by calling from_dict on the json representation
        report_latest_model_dict = ReportLatest.from_dict(report_latest_model_json).__dict__
        report_latest_model2 = ReportLatest(**report_latest_model_dict)

        # Verify the model instances are equivalent
        assert report_latest_model == report_latest_model2

        # Convert model instance back to dict and verify no loss of data
        report_latest_model_json2 = report_latest_model.to_dict()
        assert report_latest_model_json2 == report_latest_model_json


class TestModel_ReportScope:
    """
    Test Class for ReportScope
    """

    def test_report_scope_serialization(self):
        """
        Test serialization/deserialization for ReportScope
        """

        # Construct a json representation of a ReportScope model
        report_scope_model_json = {}
        report_scope_model_json['id'] = 'testString'
        report_scope_model_json['name'] = 'testString'
        report_scope_model_json['href'] = 'testString'
        report_scope_model_json['environment'] = 'testString'

        # Construct a model instance of ReportScope by calling from_dict on the json representation
        report_scope_model = ReportScope.from_dict(report_scope_model_json)
        assert report_scope_model != False

        # Construct a model instance of ReportScope by calling from_dict on the json representation
        report_scope_model_dict = ReportScope.from_dict(report_scope_model_json).__dict__
        report_scope_model2 = ReportScope(**report_scope_model_dict)

        # Verify the model instances are equivalent
        assert report_scope_model == report_scope_model2

        # Convert model instance back to dict and verify no loss of data
        report_scope_model_json2 = report_scope_model.to_dict()
        assert report_scope_model_json2 == report_scope_model_json


class TestModel_ReportSummary:
    """
    Test Class for ReportSummary
    """

    def test_report_summary_serialization(self):
        """
        Test serialization/deserialization for ReportSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        account_model = {}  # Account
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        compliance_score_model = {}  # ComplianceScore
        compliance_score_model['passed'] = 1
        compliance_score_model['total_count'] = 4
        compliance_score_model['percent'] = 25

        eval_stats_model = {}  # EvalStats
        eval_stats_model['status'] = 'compliant'
        eval_stats_model['total_count'] = 140
        eval_stats_model['pass_count'] = 123
        eval_stats_model['failure_count'] = 12
        eval_stats_model['error_count'] = 5
        eval_stats_model['skipped_count'] = 7
        eval_stats_model['completed_count'] = 135

        compliance_stats_model = {}  # ComplianceStats
        compliance_stats_model['status'] = 'compliant'
        compliance_stats_model['total_count'] = 150
        compliance_stats_model['compliant_count'] = 130
        compliance_stats_model['not_compliant_count'] = 5
        compliance_stats_model['unable_to_perform_count'] = 5
        compliance_stats_model['user_evaluation_required_count'] = 10
        compliance_stats_model['not_applicable_count'] = 7

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        resource_summary_item_model = {}  # ResourceSummaryItem
        resource_summary_item_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        resource_summary_item_model['name'] = 'my-bucket'
        resource_summary_item_model['account'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        resource_summary_item_model['service'] = 'cloud-object-storage'
        resource_summary_item_model['service_display_name'] = 'cloud-object-storage'
        resource_summary_item_model['tags'] = tags_model
        resource_summary_item_model['status'] = 'compliant'
        resource_summary_item_model['total_count'] = 140
        resource_summary_item_model['pass_count'] = 123
        resource_summary_item_model['failure_count'] = 12
        resource_summary_item_model['error_count'] = 5
        resource_summary_item_model['skipped_count'] = 7
        resource_summary_item_model['completed_count'] = 135

        resource_summary_model = {}  # ResourceSummary
        resource_summary_model['status'] = 'compliant'
        resource_summary_model['total_count'] = 150
        resource_summary_model['compliant_count'] = 130
        resource_summary_model['not_compliant_count'] = 5
        resource_summary_model['unable_to_perform_count'] = 5
        resource_summary_model['user_evaluation_required_count'] = 10
        resource_summary_model['not_applicable_count'] = 7
        resource_summary_model['top_failed'] = [resource_summary_item_model]

        # Construct a json representation of a ReportSummary model
        report_summary_model_json = {}
        report_summary_model_json['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        report_summary_model_json['instance_id'] = '84644a08-31b6-4988-b504-49a46ca69ccd'
        report_summary_model_json['account'] = account_model
        report_summary_model_json['score'] = compliance_score_model
        report_summary_model_json['evaluations'] = eval_stats_model
        report_summary_model_json['controls'] = compliance_stats_model
        report_summary_model_json['resources'] = resource_summary_model

        # Construct a model instance of ReportSummary by calling from_dict on the json representation
        report_summary_model = ReportSummary.from_dict(report_summary_model_json)
        assert report_summary_model != False

        # Construct a model instance of ReportSummary by calling from_dict on the json representation
        report_summary_model_dict = ReportSummary.from_dict(report_summary_model_json).__dict__
        report_summary_model2 = ReportSummary(**report_summary_model_dict)

        # Verify the model instances are equivalent
        assert report_summary_model == report_summary_model2

        # Convert model instance back to dict and verify no loss of data
        report_summary_model_json2 = report_summary_model.to_dict()
        assert report_summary_model_json2 == report_summary_model_json


class TestModel_ReportTags:
    """
    Test Class for ReportTags
    """

    def test_report_tags_serialization(self):
        """
        Test serialization/deserialization for ReportTags
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        # Construct a json representation of a ReportTags model
        report_tags_model_json = {}
        report_tags_model_json['report_id'] = 'testString'
        report_tags_model_json['tags'] = tags_model

        # Construct a model instance of ReportTags by calling from_dict on the json representation
        report_tags_model = ReportTags.from_dict(report_tags_model_json)
        assert report_tags_model != False

        # Construct a model instance of ReportTags by calling from_dict on the json representation
        report_tags_model_dict = ReportTags.from_dict(report_tags_model_json).__dict__
        report_tags_model2 = ReportTags(**report_tags_model_dict)

        # Verify the model instances are equivalent
        assert report_tags_model == report_tags_model2

        # Convert model instance back to dict and verify no loss of data
        report_tags_model_json2 = report_tags_model.to_dict()
        assert report_tags_model_json2 == report_tags_model_json


class TestModel_ReportViolationDataPoint:
    """
    Test Class for ReportViolationDataPoint
    """

    def test_report_violation_data_point_serialization(self):
        """
        Test serialization/deserialization for ReportViolationDataPoint
        """

        # Construct dict forms of any model objects needed in order to build this model.

        compliance_stats_model = {}  # ComplianceStats
        compliance_stats_model['status'] = 'compliant'
        compliance_stats_model['total_count'] = 150
        compliance_stats_model['compliant_count'] = 130
        compliance_stats_model['not_compliant_count'] = 5
        compliance_stats_model['unable_to_perform_count'] = 5
        compliance_stats_model['user_evaluation_required_count'] = 10
        compliance_stats_model['not_applicable_count'] = 7

        # Construct a json representation of a ReportViolationDataPoint model
        report_violation_data_point_model_json = {}
        report_violation_data_point_model_json['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        report_violation_data_point_model_json['report_group_id'] = '55b6-b3A4-432250b84669'
        report_violation_data_point_model_json['scan_time'] = '2022-08-15T12:30:01Z'
        report_violation_data_point_model_json['controls_summary'] = compliance_stats_model

        # Construct a model instance of ReportViolationDataPoint by calling from_dict on the json representation
        report_violation_data_point_model = ReportViolationDataPoint.from_dict(report_violation_data_point_model_json)
        assert report_violation_data_point_model != False

        # Construct a model instance of ReportViolationDataPoint by calling from_dict on the json representation
        report_violation_data_point_model_dict = ReportViolationDataPoint.from_dict(report_violation_data_point_model_json).__dict__
        report_violation_data_point_model2 = ReportViolationDataPoint(**report_violation_data_point_model_dict)

        # Verify the model instances are equivalent
        assert report_violation_data_point_model == report_violation_data_point_model2

        # Convert model instance back to dict and verify no loss of data
        report_violation_data_point_model_json2 = report_violation_data_point_model.to_dict()
        assert report_violation_data_point_model_json2 == report_violation_data_point_model_json


class TestModel_ReportViolationsDrift:
    """
    Test Class for ReportViolationsDrift
    """

    def test_report_violations_drift_serialization(self):
        """
        Test serialization/deserialization for ReportViolationsDrift
        """

        # Construct dict forms of any model objects needed in order to build this model.

        compliance_stats_model = {}  # ComplianceStats
        compliance_stats_model['status'] = 'compliant'
        compliance_stats_model['total_count'] = 150
        compliance_stats_model['compliant_count'] = 130
        compliance_stats_model['not_compliant_count'] = 5
        compliance_stats_model['unable_to_perform_count'] = 5
        compliance_stats_model['user_evaluation_required_count'] = 10
        compliance_stats_model['not_applicable_count'] = 7

        report_violation_data_point_model = {}  # ReportViolationDataPoint
        report_violation_data_point_model['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        report_violation_data_point_model['report_group_id'] = '55b6-b3A4-432250b84669'
        report_violation_data_point_model['scan_time'] = '2022-08-15T12:30:01Z'
        report_violation_data_point_model['controls_summary'] = compliance_stats_model

        # Construct a json representation of a ReportViolationsDrift model
        report_violations_drift_model_json = {}
        report_violations_drift_model_json['home_account_id'] = 'testString'
        report_violations_drift_model_json['report_group_id'] = 'testString'
        report_violations_drift_model_json['data_points'] = [report_violation_data_point_model]

        # Construct a model instance of ReportViolationsDrift by calling from_dict on the json representation
        report_violations_drift_model = ReportViolationsDrift.from_dict(report_violations_drift_model_json)
        assert report_violations_drift_model != False

        # Construct a model instance of ReportViolationsDrift by calling from_dict on the json representation
        report_violations_drift_model_dict = ReportViolationsDrift.from_dict(report_violations_drift_model_json).__dict__
        report_violations_drift_model2 = ReportViolationsDrift(**report_violations_drift_model_dict)

        # Verify the model instances are equivalent
        assert report_violations_drift_model == report_violations_drift_model2

        # Convert model instance back to dict and verify no loss of data
        report_violations_drift_model_json2 = report_violations_drift_model.to_dict()
        assert report_violations_drift_model_json2 == report_violations_drift_model_json


class TestModel_Resource:
    """
    Test Class for Resource
    """

    def test_resource_serialization(self):
        """
        Test serialization/deserialization for Resource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        account_model = {}  # Account
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        # Construct a json representation of a Resource model
        resource_model_json = {}
        resource_model_json['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        resource_model_json['home_account_id'] = '2411ffdc16844b07b42521c3443f456d'
        resource_model_json['id'] = 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::'
        resource_model_json['resource_name'] = 'jeff\'s key'
        resource_model_json['account'] = account_model
        resource_model_json['component_id'] = 'cloud-object_storage'
        resource_model_json['component_name'] = 'cloud-object_storage'
        resource_model_json['environment'] = 'ibm cloud'
        resource_model_json['tags'] = tags_model
        resource_model_json['status'] = 'compliant'
        resource_model_json['total_count'] = 140
        resource_model_json['pass_count'] = 123
        resource_model_json['failure_count'] = 12
        resource_model_json['error_count'] = 5
        resource_model_json['skipped_count'] = 7
        resource_model_json['completed_count'] = 135
        resource_model_json['service_name'] = 'pm-20'
        resource_model_json['instance_crn'] = 'testString'

        # Construct a model instance of Resource by calling from_dict on the json representation
        resource_model = Resource.from_dict(resource_model_json)
        assert resource_model != False

        # Construct a model instance of Resource by calling from_dict on the json representation
        resource_model_dict = Resource.from_dict(resource_model_json).__dict__
        resource_model2 = Resource(**resource_model_dict)

        # Verify the model instances are equivalent
        assert resource_model == resource_model2

        # Convert model instance back to dict and verify no loss of data
        resource_model_json2 = resource_model.to_dict()
        assert resource_model_json2 == resource_model_json


class TestModel_ResourcePage:
    """
    Test Class for ResourcePage
    """

    def test_resource_page_serialization(self):
        """
        Test serialization/deserialization for ResourcePage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_first_model = {}  # PageHRefFirst
        page_h_ref_first_model['href'] = 'testString'

        page_h_ref_next_model = {}  # PageHRefNext
        page_h_ref_next_model['href'] = 'testString'
        page_h_ref_next_model['start'] = 'testString'

        account_model = {}  # Account
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        resource_model = {}  # Resource
        resource_model['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        resource_model['home_account_id'] = '2411ffdc16844b07b42521c3443f456d'
        resource_model['id'] = 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::'
        resource_model['resource_name'] = 'jeff\'s key'
        resource_model['account'] = account_model
        resource_model['component_id'] = 'cloud-object_storage'
        resource_model['component_name'] = 'cloud-object_storage'
        resource_model['environment'] = 'ibm cloud'
        resource_model['tags'] = tags_model
        resource_model['status'] = 'compliant'
        resource_model['total_count'] = 140
        resource_model['pass_count'] = 123
        resource_model['failure_count'] = 12
        resource_model['error_count'] = 5
        resource_model['skipped_count'] = 7
        resource_model['completed_count'] = 135
        resource_model['service_name'] = 'pm-20'
        resource_model['instance_crn'] = 'testString'

        # Construct a json representation of a ResourcePage model
        resource_page_model_json = {}
        resource_page_model_json['limit'] = 50
        resource_page_model_json['total_count'] = 230
        resource_page_model_json['first'] = page_h_ref_first_model
        resource_page_model_json['next'] = page_h_ref_next_model
        resource_page_model_json['report_id'] = 'testString'
        resource_page_model_json['home_account_id'] = 'testString'
        resource_page_model_json['resources'] = [resource_model]

        # Construct a model instance of ResourcePage by calling from_dict on the json representation
        resource_page_model = ResourcePage.from_dict(resource_page_model_json)
        assert resource_page_model != False

        # Construct a model instance of ResourcePage by calling from_dict on the json representation
        resource_page_model_dict = ResourcePage.from_dict(resource_page_model_json).__dict__
        resource_page_model2 = ResourcePage(**resource_page_model_dict)

        # Verify the model instances are equivalent
        assert resource_page_model == resource_page_model2

        # Convert model instance back to dict and verify no loss of data
        resource_page_model_json2 = resource_page_model.to_dict()
        assert resource_page_model_json2 == resource_page_model_json


class TestModel_ResourceSummary:
    """
    Test Class for ResourceSummary
    """

    def test_resource_summary_serialization(self):
        """
        Test serialization/deserialization for ResourceSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        resource_summary_item_model = {}  # ResourceSummaryItem
        resource_summary_item_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        resource_summary_item_model['name'] = 'my-bucket'
        resource_summary_item_model['account'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        resource_summary_item_model['service'] = 'cloud-object-storage'
        resource_summary_item_model['service_display_name'] = 'cloud-object-storage'
        resource_summary_item_model['tags'] = tags_model
        resource_summary_item_model['status'] = 'compliant'
        resource_summary_item_model['total_count'] = 140
        resource_summary_item_model['pass_count'] = 123
        resource_summary_item_model['failure_count'] = 12
        resource_summary_item_model['error_count'] = 5
        resource_summary_item_model['skipped_count'] = 7
        resource_summary_item_model['completed_count'] = 135

        # Construct a json representation of a ResourceSummary model
        resource_summary_model_json = {}
        resource_summary_model_json['status'] = 'compliant'
        resource_summary_model_json['total_count'] = 150
        resource_summary_model_json['compliant_count'] = 130
        resource_summary_model_json['not_compliant_count'] = 5
        resource_summary_model_json['unable_to_perform_count'] = 5
        resource_summary_model_json['user_evaluation_required_count'] = 10
        resource_summary_model_json['not_applicable_count'] = 7
        resource_summary_model_json['top_failed'] = [resource_summary_item_model]

        # Construct a model instance of ResourceSummary by calling from_dict on the json representation
        resource_summary_model = ResourceSummary.from_dict(resource_summary_model_json)
        assert resource_summary_model != False

        # Construct a model instance of ResourceSummary by calling from_dict on the json representation
        resource_summary_model_dict = ResourceSummary.from_dict(resource_summary_model_json).__dict__
        resource_summary_model2 = ResourceSummary(**resource_summary_model_dict)

        # Verify the model instances are equivalent
        assert resource_summary_model == resource_summary_model2

        # Convert model instance back to dict and verify no loss of data
        resource_summary_model_json2 = resource_summary_model.to_dict()
        assert resource_summary_model_json2 == resource_summary_model_json


class TestModel_ResourceSummaryItem:
    """
    Test Class for ResourceSummaryItem
    """

    def test_resource_summary_item_serialization(self):
        """
        Test serialization/deserialization for ResourceSummaryItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        # Construct a json representation of a ResourceSummaryItem model
        resource_summary_item_model_json = {}
        resource_summary_item_model_json['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        resource_summary_item_model_json['name'] = 'my-bucket'
        resource_summary_item_model_json['account'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        resource_summary_item_model_json['service'] = 'cloud-object-storage'
        resource_summary_item_model_json['service_display_name'] = 'cloud-object-storage'
        resource_summary_item_model_json['tags'] = tags_model
        resource_summary_item_model_json['status'] = 'compliant'
        resource_summary_item_model_json['total_count'] = 140
        resource_summary_item_model_json['pass_count'] = 123
        resource_summary_item_model_json['failure_count'] = 12
        resource_summary_item_model_json['error_count'] = 5
        resource_summary_item_model_json['skipped_count'] = 7
        resource_summary_item_model_json['completed_count'] = 135

        # Construct a model instance of ResourceSummaryItem by calling from_dict on the json representation
        resource_summary_item_model = ResourceSummaryItem.from_dict(resource_summary_item_model_json)
        assert resource_summary_item_model != False

        # Construct a model instance of ResourceSummaryItem by calling from_dict on the json representation
        resource_summary_item_model_dict = ResourceSummaryItem.from_dict(resource_summary_item_model_json).__dict__
        resource_summary_item_model2 = ResourceSummaryItem(**resource_summary_item_model_dict)

        # Verify the model instances are equivalent
        assert resource_summary_item_model == resource_summary_item_model2

        # Convert model instance back to dict and verify no loss of data
        resource_summary_item_model_json2 = resource_summary_item_model.to_dict()
        assert resource_summary_item_model_json2 == resource_summary_item_model_json


class TestModel_Rule:
    """
    Test Class for Rule
    """

    def test_rule_serialization(self):
        """
        Test serialization/deserialization for Rule
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_parameter_model = {}  # RuleParameter
        rule_parameter_model['name'] = 'testString'
        rule_parameter_model['display_name'] = 'testString'
        rule_parameter_model['description'] = 'testString'
        rule_parameter_model['type'] = 'string'

        import_model = {}  # Import
        import_model['parameters'] = [rule_parameter_model]

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_target_model = {}  # RuleTarget
        rule_target_model['service_name'] = 'testString'
        rule_target_model['service_display_name'] = 'testString'
        rule_target_model['resource_kind'] = 'testString'
        rule_target_model['additional_target_attributes'] = [additional_target_attribute_model]
        rule_target_model['ref'] = 'testString'

        required_config_model = {}  # RequiredConfigConditionBase
        required_config_model['description'] = 'testString'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        # Construct a json representation of a Rule model
        rule_model_json = {}
        rule_model_json['created_on'] = '2019-01-01T12:00:00Z'
        rule_model_json['created_by'] = 'testString'
        rule_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        rule_model_json['updated_by'] = 'testString'
        rule_model_json['id'] = 'testString'
        rule_model_json['account_id'] = 'testString'
        rule_model_json['description'] = 'testString'
        rule_model_json['type'] = 'user_defined'
        rule_model_json['version'] = 'testString'
        rule_model_json['import'] = import_model
        rule_model_json['target'] = rule_target_model
        rule_model_json['required_config'] = required_config_model
        rule_model_json['labels'] = ['testString']

        # Construct a model instance of Rule by calling from_dict on the json representation
        rule_model = Rule.from_dict(rule_model_json)
        assert rule_model != False

        # Construct a model instance of Rule by calling from_dict on the json representation
        rule_model_dict = Rule.from_dict(rule_model_json).__dict__
        rule_model2 = Rule(**rule_model_dict)

        # Verify the model instances are equivalent
        assert rule_model == rule_model2

        # Convert model instance back to dict and verify no loss of data
        rule_model_json2 = rule_model.to_dict()
        assert rule_model_json2 == rule_model_json


class TestModel_RuleCollection:
    """
    Test Class for RuleCollection
    """

    def test_rule_collection_serialization(self):
        """
        Test serialization/deserialization for RuleCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_first_model = {}  # PageHRefFirst
        page_h_ref_first_model['href'] = 'testString'

        page_h_ref_next_model = {}  # PageHRefNext
        page_h_ref_next_model['href'] = 'testString'
        page_h_ref_next_model['start'] = 'testString'

        rule_parameter_model = {}  # RuleParameter
        rule_parameter_model['name'] = 'testString'
        rule_parameter_model['display_name'] = 'testString'
        rule_parameter_model['description'] = 'testString'
        rule_parameter_model['type'] = 'string'

        import_model = {}  # Import
        import_model['parameters'] = [rule_parameter_model]

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_target_model = {}  # RuleTarget
        rule_target_model['service_name'] = 'testString'
        rule_target_model['service_display_name'] = 'testString'
        rule_target_model['resource_kind'] = 'testString'
        rule_target_model['additional_target_attributes'] = [additional_target_attribute_model]
        rule_target_model['ref'] = 'testString'

        required_config_model = {}  # RequiredConfigConditionBase
        required_config_model['description'] = 'testString'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        rule_model = {}  # Rule
        rule_model['created_on'] = '2019-01-01T12:00:00Z'
        rule_model['created_by'] = 'testString'
        rule_model['updated_on'] = '2019-01-01T12:00:00Z'
        rule_model['updated_by'] = 'testString'
        rule_model['id'] = 'testString'
        rule_model['account_id'] = 'testString'
        rule_model['description'] = 'testString'
        rule_model['type'] = 'user_defined'
        rule_model['version'] = 'testString'
        rule_model['import'] = import_model
        rule_model['target'] = rule_target_model
        rule_model['required_config'] = required_config_model
        rule_model['labels'] = ['testString']

        # Construct a json representation of a RuleCollection model
        rule_collection_model_json = {}
        rule_collection_model_json['limit'] = 50
        rule_collection_model_json['total_count'] = 230
        rule_collection_model_json['first'] = page_h_ref_first_model
        rule_collection_model_json['next'] = page_h_ref_next_model
        rule_collection_model_json['rules'] = [rule_model]

        # Construct a model instance of RuleCollection by calling from_dict on the json representation
        rule_collection_model = RuleCollection.from_dict(rule_collection_model_json)
        assert rule_collection_model != False

        # Construct a model instance of RuleCollection by calling from_dict on the json representation
        rule_collection_model_dict = RuleCollection.from_dict(rule_collection_model_json).__dict__
        rule_collection_model2 = RuleCollection(**rule_collection_model_dict)

        # Verify the model instances are equivalent
        assert rule_collection_model == rule_collection_model2

        # Convert model instance back to dict and verify no loss of data
        rule_collection_model_json2 = rule_collection_model.to_dict()
        assert rule_collection_model_json2 == rule_collection_model_json


class TestModel_RuleInfo:
    """
    Test Class for RuleInfo
    """

    def test_rule_info_serialization(self):
        """
        Test serialization/deserialization for RuleInfo
        """

        # Construct a json representation of a RuleInfo model
        rule_info_model_json = {}
        rule_info_model_json['id'] = 'rule-7b0560a4-df94-4629-bb76-680f3155ddda'
        rule_info_model_json['type'] = 'user_defined/system_defined'
        rule_info_model_json['description'] = 'rule'
        rule_info_model_json['version'] = '1.2.3'
        rule_info_model_json['account_id'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        rule_info_model_json['created_on'] = '2022-08-15T12:30:01Z'
        rule_info_model_json['created_by'] = 'IBMid-12345'
        rule_info_model_json['updated_on'] = '2022-08-15T12:30:01Z'
        rule_info_model_json['updated_by'] = 'IBMid-12345'
        rule_info_model_json['labels'] = ['testString']

        # Construct a model instance of RuleInfo by calling from_dict on the json representation
        rule_info_model = RuleInfo.from_dict(rule_info_model_json)
        assert rule_info_model != False

        # Construct a model instance of RuleInfo by calling from_dict on the json representation
        rule_info_model_dict = RuleInfo.from_dict(rule_info_model_json).__dict__
        rule_info_model2 = RuleInfo(**rule_info_model_dict)

        # Verify the model instances are equivalent
        assert rule_info_model == rule_info_model2

        # Convert model instance back to dict and verify no loss of data
        rule_info_model_json2 = rule_info_model.to_dict()
        assert rule_info_model_json2 == rule_info_model_json


class TestModel_RuleParameter:
    """
    Test Class for RuleParameter
    """

    def test_rule_parameter_serialization(self):
        """
        Test serialization/deserialization for RuleParameter
        """

        # Construct a json representation of a RuleParameter model
        rule_parameter_model_json = {}
        rule_parameter_model_json['name'] = 'testString'
        rule_parameter_model_json['display_name'] = 'testString'
        rule_parameter_model_json['description'] = 'testString'
        rule_parameter_model_json['type'] = 'string'

        # Construct a model instance of RuleParameter by calling from_dict on the json representation
        rule_parameter_model = RuleParameter.from_dict(rule_parameter_model_json)
        assert rule_parameter_model != False

        # Construct a model instance of RuleParameter by calling from_dict on the json representation
        rule_parameter_model_dict = RuleParameter.from_dict(rule_parameter_model_json).__dict__
        rule_parameter_model2 = RuleParameter(**rule_parameter_model_dict)

        # Verify the model instances are equivalent
        assert rule_parameter_model == rule_parameter_model2

        # Convert model instance back to dict and verify no loss of data
        rule_parameter_model_json2 = rule_parameter_model.to_dict()
        assert rule_parameter_model_json2 == rule_parameter_model_json


class TestModel_RuleProperty:
    """
    Test Class for RuleProperty
    """

    def test_rule_property_serialization(self):
        """
        Test serialization/deserialization for RuleProperty
        """

        # Construct a json representation of a RuleProperty model
        rule_property_model_json = {}
        rule_property_model_json['name'] = 'testString'
        rule_property_model_json['description'] = 'testString'
        rule_property_model_json['type'] = 'string'

        # Construct a model instance of RuleProperty by calling from_dict on the json representation
        rule_property_model = RuleProperty.from_dict(rule_property_model_json)
        assert rule_property_model != False

        # Construct a model instance of RuleProperty by calling from_dict on the json representation
        rule_property_model_dict = RuleProperty.from_dict(rule_property_model_json).__dict__
        rule_property_model2 = RuleProperty(**rule_property_model_dict)

        # Verify the model instances are equivalent
        assert rule_property_model == rule_property_model2

        # Convert model instance back to dict and verify no loss of data
        rule_property_model_json2 = rule_property_model.to_dict()
        assert rule_property_model_json2 == rule_property_model_json


class TestModel_RuleTarget:
    """
    Test Class for RuleTarget
    """

    def test_rule_target_serialization(self):
        """
        Test serialization/deserialization for RuleTarget
        """

        # Construct dict forms of any model objects needed in order to build this model.

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        # Construct a json representation of a RuleTarget model
        rule_target_model_json = {}
        rule_target_model_json['service_name'] = 'testString'
        rule_target_model_json['service_display_name'] = 'testString'
        rule_target_model_json['resource_kind'] = 'testString'
        rule_target_model_json['additional_target_attributes'] = [additional_target_attribute_model]
        rule_target_model_json['ref'] = 'testString'

        # Construct a model instance of RuleTarget by calling from_dict on the json representation
        rule_target_model = RuleTarget.from_dict(rule_target_model_json)
        assert rule_target_model != False

        # Construct a model instance of RuleTarget by calling from_dict on the json representation
        rule_target_model_dict = RuleTarget.from_dict(rule_target_model_json).__dict__
        rule_target_model2 = RuleTarget(**rule_target_model_dict)

        # Verify the model instances are equivalent
        assert rule_target_model == rule_target_model2

        # Convert model instance back to dict and verify no loss of data
        rule_target_model_json2 = rule_target_model.to_dict()
        assert rule_target_model_json2 == rule_target_model_json


class TestModel_RuleTargetPrototype:
    """
    Test Class for RuleTargetPrototype
    """

    def test_rule_target_prototype_serialization(self):
        """
        Test serialization/deserialization for RuleTargetPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        # Construct a json representation of a RuleTargetPrototype model
        rule_target_prototype_model_json = {}
        rule_target_prototype_model_json['service_name'] = 'testString'
        rule_target_prototype_model_json['resource_kind'] = 'testString'
        rule_target_prototype_model_json['additional_target_attributes'] = [additional_target_attribute_model]

        # Construct a model instance of RuleTargetPrototype by calling from_dict on the json representation
        rule_target_prototype_model = RuleTargetPrototype.from_dict(rule_target_prototype_model_json)
        assert rule_target_prototype_model != False

        # Construct a model instance of RuleTargetPrototype by calling from_dict on the json representation
        rule_target_prototype_model_dict = RuleTargetPrototype.from_dict(rule_target_prototype_model_json).__dict__
        rule_target_prototype_model2 = RuleTargetPrototype(**rule_target_prototype_model_dict)

        # Verify the model instances are equivalent
        assert rule_target_prototype_model == rule_target_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        rule_target_prototype_model_json2 = rule_target_prototype_model.to_dict()
        assert rule_target_prototype_model_json2 == rule_target_prototype_model_json


class TestModel_ScanReport:
    """
    Test Class for ScanReport
    """

    def test_scan_report_serialization(self):
        """
        Test serialization/deserialization for ScanReport
        """

        # Construct a json representation of a ScanReport model
        scan_report_model_json = {}
        scan_report_model_json['id'] = 'e44316e3-53bc-449b-a808-c16df680d462'
        scan_report_model_json['scan_id'] = '44a5-a292-32114fa73553'
        scan_report_model_json['instance_id'] = 'testString'
        scan_report_model_json['scope_id'] = '44a5-a292-32114fa73558'
        scan_report_model_json['subscope_id'] = '44a5-a292-32114fa73555'
        scan_report_model_json['status'] = 'completed'
        scan_report_model_json['created_on'] = '2024-05-08T12:30:01Z'
        scan_report_model_json['format'] = 'pdf'
        scan_report_model_json['href'] = 'testString'

        # Construct a model instance of ScanReport by calling from_dict on the json representation
        scan_report_model = ScanReport.from_dict(scan_report_model_json)
        assert scan_report_model != False

        # Construct a model instance of ScanReport by calling from_dict on the json representation
        scan_report_model_dict = ScanReport.from_dict(scan_report_model_json).__dict__
        scan_report_model2 = ScanReport(**scan_report_model_dict)

        # Verify the model instances are equivalent
        assert scan_report_model == scan_report_model2

        # Convert model instance back to dict and verify no loss of data
        scan_report_model_json2 = scan_report_model.to_dict()
        assert scan_report_model_json2 == scan_report_model_json


class TestModel_ScanReportCollection:
    """
    Test Class for ScanReportCollection
    """

    def test_scan_report_collection_serialization(self):
        """
        Test serialization/deserialization for ScanReportCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_first_model = {}  # PageHRefFirst
        page_h_ref_first_model['href'] = 'testString'

        page_h_ref_next_model = {}  # PageHRefNext
        page_h_ref_next_model['href'] = 'testString'
        page_h_ref_next_model['start'] = 'testString'

        scan_report_model = {}  # ScanReport
        scan_report_model['id'] = 'e44316e3-53bc-449b-a808-c16df680d462'
        scan_report_model['scan_id'] = '44a5-a292-32114fa73553'
        scan_report_model['instance_id'] = 'testString'
        scan_report_model['scope_id'] = '44a5-a292-32114fa73558'
        scan_report_model['subscope_id'] = '44a5-a292-32114fa73555'
        scan_report_model['status'] = 'completed'
        scan_report_model['created_on'] = '2024-05-08T12:30:01Z'
        scan_report_model['format'] = 'pdf'
        scan_report_model['href'] = 'testString'

        # Construct a json representation of a ScanReportCollection model
        scan_report_collection_model_json = {}
        scan_report_collection_model_json['limit'] = 50
        scan_report_collection_model_json['total_count'] = 230
        scan_report_collection_model_json['first'] = page_h_ref_first_model
        scan_report_collection_model_json['next'] = page_h_ref_next_model
        scan_report_collection_model_json['scope_id'] = '44a5-a292-32114fa73558'
        scan_report_collection_model_json['subscope_id'] = '44a5-a292-32114fa73555'
        scan_report_collection_model_json['scan_reports'] = [scan_report_model]

        # Construct a model instance of ScanReportCollection by calling from_dict on the json representation
        scan_report_collection_model = ScanReportCollection.from_dict(scan_report_collection_model_json)
        assert scan_report_collection_model != False

        # Construct a model instance of ScanReportCollection by calling from_dict on the json representation
        scan_report_collection_model_dict = ScanReportCollection.from_dict(scan_report_collection_model_json).__dict__
        scan_report_collection_model2 = ScanReportCollection(**scan_report_collection_model_dict)

        # Verify the model instances are equivalent
        assert scan_report_collection_model == scan_report_collection_model2

        # Convert model instance back to dict and verify no loss of data
        scan_report_collection_model_json2 = scan_report_collection_model.to_dict()
        assert scan_report_collection_model_json2 == scan_report_collection_model_json


class TestModel_Scope:
    """
    Test Class for Scope
    """

    def test_scope_serialization(self):
        """
        Test serialization/deserialization for Scope
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_property_model = {}  # ScopePropertyScopeAny
        scope_property_model['name'] = 'testString'
        scope_property_model['value'] = 'testString'

        # Construct a json representation of a Scope model
        scope_model_json = {}
        scope_model_json['id'] = 'testString'
        scope_model_json['name'] = 'testString'
        scope_model_json['description'] = 'testString'
        scope_model_json['environment'] = 'testString'
        scope_model_json['properties'] = [scope_property_model]
        scope_model_json['account_id'] = 'testString'
        scope_model_json['instance_id'] = 'testString'
        scope_model_json['created_by'] = 'testString'
        scope_model_json['created_on'] = '2019-01-01T12:00:00Z'
        scope_model_json['updated_by'] = 'testString'
        scope_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        scope_model_json['attachment_count'] = 72.5

        # Construct a model instance of Scope by calling from_dict on the json representation
        scope_model = Scope.from_dict(scope_model_json)
        assert scope_model != False

        # Construct a model instance of Scope by calling from_dict on the json representation
        scope_model_dict = Scope.from_dict(scope_model_json).__dict__
        scope_model2 = Scope(**scope_model_dict)

        # Verify the model instances are equivalent
        assert scope_model == scope_model2

        # Convert model instance back to dict and verify no loss of data
        scope_model_json2 = scope_model.to_dict()
        assert scope_model_json2 == scope_model_json


class TestModel_ScopeCollection:
    """
    Test Class for ScopeCollection
    """

    def test_scope_collection_serialization(self):
        """
        Test serialization/deserialization for ScopeCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_first_model = {}  # PageHRefFirst
        page_h_ref_first_model['href'] = 'testString'

        page_h_ref_next_model = {}  # PageHRefNext
        page_h_ref_next_model['href'] = 'testString'
        page_h_ref_next_model['start'] = 'testString'

        scope_property_model = {}  # ScopePropertyScopeAny
        scope_property_model['name'] = 'testString'
        scope_property_model['value'] = 'testString'

        scope_model = {}  # Scope
        scope_model['id'] = 'testString'
        scope_model['name'] = 'testString'
        scope_model['description'] = 'testString'
        scope_model['environment'] = 'testString'
        scope_model['properties'] = [scope_property_model]
        scope_model['account_id'] = 'testString'
        scope_model['instance_id'] = 'testString'
        scope_model['created_by'] = 'testString'
        scope_model['created_on'] = '2019-01-01T12:00:00Z'
        scope_model['updated_by'] = 'testString'
        scope_model['updated_on'] = '2019-01-01T12:00:00Z'
        scope_model['attachment_count'] = 72.5

        # Construct a json representation of a ScopeCollection model
        scope_collection_model_json = {}
        scope_collection_model_json['limit'] = 50
        scope_collection_model_json['total_count'] = 230
        scope_collection_model_json['first'] = page_h_ref_first_model
        scope_collection_model_json['next'] = page_h_ref_next_model
        scope_collection_model_json['scopes'] = [scope_model]

        # Construct a model instance of ScopeCollection by calling from_dict on the json representation
        scope_collection_model = ScopeCollection.from_dict(scope_collection_model_json)
        assert scope_collection_model != False

        # Construct a model instance of ScopeCollection by calling from_dict on the json representation
        scope_collection_model_dict = ScopeCollection.from_dict(scope_collection_model_json).__dict__
        scope_collection_model2 = ScopeCollection(**scope_collection_model_dict)

        # Verify the model instances are equivalent
        assert scope_collection_model == scope_collection_model2

        # Convert model instance back to dict and verify no loss of data
        scope_collection_model_json2 = scope_collection_model.to_dict()
        assert scope_collection_model_json2 == scope_collection_model_json


class TestModel_ScopeID:
    """
    Test Class for ScopeID
    """

    def test_scope_id_serialization(self):
        """
        Test serialization/deserialization for ScopeID
        """

        # Construct a json representation of a ScopeID model
        scope_id_model_json = {}
        scope_id_model_json['id'] = '2411ffdc16844b07b42521c3443f456d'
        scope_id_model_json['type'] = 'account'

        # Construct a model instance of ScopeID by calling from_dict on the json representation
        scope_id_model = ScopeID.from_dict(scope_id_model_json)
        assert scope_id_model != False

        # Construct a model instance of ScopeID by calling from_dict on the json representation
        scope_id_model_dict = ScopeID.from_dict(scope_id_model_json).__dict__
        scope_id_model2 = ScopeID(**scope_id_model_dict)

        # Verify the model instances are equivalent
        assert scope_id_model == scope_id_model2

        # Convert model instance back to dict and verify no loss of data
        scope_id_model_json2 = scope_id_model.to_dict()
        assert scope_id_model_json2 == scope_id_model_json


class TestModel_ScopePropertyExclusionItem:
    """
    Test Class for ScopePropertyExclusionItem
    """

    def test_scope_property_exclusion_item_serialization(self):
        """
        Test serialization/deserialization for ScopePropertyExclusionItem
        """

        # Construct a json representation of a ScopePropertyExclusionItem model
        scope_property_exclusion_item_model_json = {}
        scope_property_exclusion_item_model_json['scope_id'] = 'testString'
        scope_property_exclusion_item_model_json['scope_type'] = 'enterprise'

        # Construct a model instance of ScopePropertyExclusionItem by calling from_dict on the json representation
        scope_property_exclusion_item_model = ScopePropertyExclusionItem.from_dict(scope_property_exclusion_item_model_json)
        assert scope_property_exclusion_item_model != False

        # Construct a model instance of ScopePropertyExclusionItem by calling from_dict on the json representation
        scope_property_exclusion_item_model_dict = ScopePropertyExclusionItem.from_dict(scope_property_exclusion_item_model_json).__dict__
        scope_property_exclusion_item_model2 = ScopePropertyExclusionItem(**scope_property_exclusion_item_model_dict)

        # Verify the model instances are equivalent
        assert scope_property_exclusion_item_model == scope_property_exclusion_item_model2

        # Convert model instance back to dict and verify no loss of data
        scope_property_exclusion_item_model_json2 = scope_property_exclusion_item_model.to_dict()
        assert scope_property_exclusion_item_model_json2 == scope_property_exclusion_item_model_json


class TestModel_ScopePrototype:
    """
    Test Class for ScopePrototype
    """

    def test_scope_prototype_serialization(self):
        """
        Test serialization/deserialization for ScopePrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_property_model = {}  # ScopePropertyScopeAny
        scope_property_model['name'] = 'testString'
        scope_property_model['value'] = 'testString'

        # Construct a json representation of a ScopePrototype model
        scope_prototype_model_json = {}
        scope_prototype_model_json['name'] = 'testString'
        scope_prototype_model_json['description'] = 'testString'
        scope_prototype_model_json['environment'] = 'testString'
        scope_prototype_model_json['properties'] = [scope_property_model]

        # Construct a model instance of ScopePrototype by calling from_dict on the json representation
        scope_prototype_model = ScopePrototype.from_dict(scope_prototype_model_json)
        assert scope_prototype_model != False

        # Construct a model instance of ScopePrototype by calling from_dict on the json representation
        scope_prototype_model_dict = ScopePrototype.from_dict(scope_prototype_model_json).__dict__
        scope_prototype_model2 = ScopePrototype(**scope_prototype_model_dict)

        # Verify the model instances are equivalent
        assert scope_prototype_model == scope_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        scope_prototype_model_json2 = scope_prototype_model.to_dict()
        assert scope_prototype_model_json2 == scope_prototype_model_json


class TestModel_Service:
    """
    Test Class for Service
    """

    def test_service_serialization(self):
        """
        Test serialization/deserialization for Service
        """

        # Construct dict forms of any model objects needed in order to build this model.

        endpoint_model = {}  # Endpoint
        endpoint_model['host'] = 'testString'
        endpoint_model['path'] = 'testString'
        endpoint_model['region'] = 'testString'
        endpoint_model['advisory_call_limit'] = 38

        configuration_information_points_model = {}  # ConfigurationInformationPoints
        configuration_information_points_model['type'] = 'testString'
        configuration_information_points_model['endpoints'] = [endpoint_model]

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_property_model = {}  # RuleProperty
        rule_property_model['name'] = 'testString'
        rule_property_model['description'] = 'testString'
        rule_property_model['type'] = 'string'

        supported_configs_model = {}  # SupportedConfigs
        supported_configs_model['resource_kind'] = 'testString'
        supported_configs_model['additional_target_attributes'] = [additional_target_attribute_model]
        supported_configs_model['properties'] = [rule_property_model]
        supported_configs_model['description'] = 'testString'
        supported_configs_model['cip_requires_service_instance'] = True
        supported_configs_model['resource_group_support'] = True
        supported_configs_model['tagging_support'] = True
        supported_configs_model['inherit_tags'] = True

        # Construct a json representation of a Service model
        service_model_json = {}
        service_model_json['created_on'] = '2019-01-01T12:00:00Z'
        service_model_json['created_by'] = 'testString'
        service_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        service_model_json['updated_by'] = 'testString'
        service_model_json['service_name'] = 'testString'
        service_model_json['service_display_name'] = 'testString'
        service_model_json['description'] = 'testString'
        service_model_json['monitoring_enabled'] = True
        service_model_json['enforcement_enabled'] = True
        service_model_json['service_listing_enabled'] = True
        service_model_json['config_information_point'] = configuration_information_points_model
        service_model_json['supported_configs'] = [supported_configs_model]

        # Construct a model instance of Service by calling from_dict on the json representation
        service_model = Service.from_dict(service_model_json)
        assert service_model != False

        # Construct a model instance of Service by calling from_dict on the json representation
        service_model_dict = Service.from_dict(service_model_json).__dict__
        service_model2 = Service(**service_model_dict)

        # Verify the model instances are equivalent
        assert service_model == service_model2

        # Convert model instance back to dict and verify no loss of data
        service_model_json2 = service_model.to_dict()
        assert service_model_json2 == service_model_json


class TestModel_ServiceCollection:
    """
    Test Class for ServiceCollection
    """

    def test_service_collection_serialization(self):
        """
        Test serialization/deserialization for ServiceCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        endpoint_model = {}  # Endpoint
        endpoint_model['host'] = 'testString'
        endpoint_model['path'] = 'testString'
        endpoint_model['region'] = 'testString'
        endpoint_model['advisory_call_limit'] = 38

        configuration_information_points_model = {}  # ConfigurationInformationPoints
        configuration_information_points_model['type'] = 'testString'
        configuration_information_points_model['endpoints'] = [endpoint_model]

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_property_model = {}  # RuleProperty
        rule_property_model['name'] = 'testString'
        rule_property_model['description'] = 'testString'
        rule_property_model['type'] = 'string'

        supported_configs_model = {}  # SupportedConfigs
        supported_configs_model['resource_kind'] = 'testString'
        supported_configs_model['additional_target_attributes'] = [additional_target_attribute_model]
        supported_configs_model['properties'] = [rule_property_model]
        supported_configs_model['description'] = 'testString'
        supported_configs_model['cip_requires_service_instance'] = True
        supported_configs_model['resource_group_support'] = True
        supported_configs_model['tagging_support'] = True
        supported_configs_model['inherit_tags'] = True

        service_model = {}  # Service
        service_model['created_on'] = '2019-01-01T12:00:00Z'
        service_model['created_by'] = 'testString'
        service_model['updated_on'] = '2019-01-01T12:00:00Z'
        service_model['updated_by'] = 'testString'
        service_model['service_name'] = 'testString'
        service_model['service_display_name'] = 'testString'
        service_model['description'] = 'testString'
        service_model['monitoring_enabled'] = True
        service_model['enforcement_enabled'] = True
        service_model['service_listing_enabled'] = True
        service_model['config_information_point'] = configuration_information_points_model
        service_model['supported_configs'] = [supported_configs_model]

        # Construct a json representation of a ServiceCollection model
        service_collection_model_json = {}
        service_collection_model_json['services'] = [service_model]

        # Construct a model instance of ServiceCollection by calling from_dict on the json representation
        service_collection_model = ServiceCollection.from_dict(service_collection_model_json)
        assert service_collection_model != False

        # Construct a model instance of ServiceCollection by calling from_dict on the json representation
        service_collection_model_dict = ServiceCollection.from_dict(service_collection_model_json).__dict__
        service_collection_model2 = ServiceCollection(**service_collection_model_dict)

        # Verify the model instances are equivalent
        assert service_collection_model == service_collection_model2

        # Convert model instance back to dict and verify no loss of data
        service_collection_model_json2 = service_collection_model.to_dict()
        assert service_collection_model_json2 == service_collection_model_json


class TestModel_Settings:
    """
    Test Class for Settings
    """

    def test_settings_serialization(self):
        """
        Test serialization/deserialization for Settings
        """

        # Construct dict forms of any model objects needed in order to build this model.

        event_notifications_model = {}  # EventNotifications
        event_notifications_model['instance_crn'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::'
        event_notifications_model['updated_on'] = '2019-01-01T12:00:00Z'
        event_notifications_model['source_id'] = 'crn:v1:bluemix:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::'
        event_notifications_model['source_description'] = 'This source is used for integration with IBM Cloud Security and Compliance Center.'
        event_notifications_model['source_name'] = 'compliance'

        object_storage_model = {}  # ObjectStorage
        object_storage_model['instance_crn'] = 'testString'
        object_storage_model['bucket'] = 'testString'
        object_storage_model['bucket_location'] = 'testString'
        object_storage_model['bucket_endpoint'] = 'testString'
        object_storage_model['updated_on'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a Settings model
        settings_model_json = {}
        settings_model_json['event_notifications'] = event_notifications_model
        settings_model_json['object_storage'] = object_storage_model

        # Construct a model instance of Settings by calling from_dict on the json representation
        settings_model = Settings.from_dict(settings_model_json)
        assert settings_model != False

        # Construct a model instance of Settings by calling from_dict on the json representation
        settings_model_dict = Settings.from_dict(settings_model_json).__dict__
        settings_model2 = Settings(**settings_model_dict)

        # Verify the model instances are equivalent
        assert settings_model == settings_model2

        # Convert model instance back to dict and verify no loss of data
        settings_model_json2 = settings_model.to_dict()
        assert settings_model_json2 == settings_model_json


class TestModel_SubRule:
    """
    Test Class for SubRule
    """

    def test_sub_rule_serialization(self):
        """
        Test serialization/deserialization for SubRule
        """

        # Construct dict forms of any model objects needed in order to build this model.

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_target_model = {}  # RuleTarget
        rule_target_model['service_name'] = 'testString'
        rule_target_model['service_display_name'] = 'testString'
        rule_target_model['resource_kind'] = 'testString'
        rule_target_model['additional_target_attributes'] = [additional_target_attribute_model]
        rule_target_model['ref'] = 'testString'

        required_config_model = {}  # RequiredConfigConditionBase
        required_config_model['description'] = 'testString'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        # Construct a json representation of a SubRule model
        sub_rule_model_json = {}
        sub_rule_model_json['target'] = rule_target_model
        sub_rule_model_json['required_config'] = required_config_model

        # Construct a model instance of SubRule by calling from_dict on the json representation
        sub_rule_model = SubRule.from_dict(sub_rule_model_json)
        assert sub_rule_model != False

        # Construct a model instance of SubRule by calling from_dict on the json representation
        sub_rule_model_dict = SubRule.from_dict(sub_rule_model_json).__dict__
        sub_rule_model2 = SubRule(**sub_rule_model_dict)

        # Verify the model instances are equivalent
        assert sub_rule_model == sub_rule_model2

        # Convert model instance back to dict and verify no loss of data
        sub_rule_model_json2 = sub_rule_model.to_dict()
        assert sub_rule_model_json2 == sub_rule_model_json


class TestModel_SubScope:
    """
    Test Class for SubScope
    """

    def test_sub_scope_serialization(self):
        """
        Test serialization/deserialization for SubScope
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_property_model = {}  # ScopePropertyScopeAny
        scope_property_model['name'] = 'testString'
        scope_property_model['value'] = 'testString'

        # Construct a json representation of a SubScope model
        sub_scope_model_json = {}
        sub_scope_model_json['id'] = 'testString'
        sub_scope_model_json['name'] = 'testString'
        sub_scope_model_json['description'] = 'testString'
        sub_scope_model_json['environment'] = 'testString'
        sub_scope_model_json['properties'] = [scope_property_model]

        # Construct a model instance of SubScope by calling from_dict on the json representation
        sub_scope_model = SubScope.from_dict(sub_scope_model_json)
        assert sub_scope_model != False

        # Construct a model instance of SubScope by calling from_dict on the json representation
        sub_scope_model_dict = SubScope.from_dict(sub_scope_model_json).__dict__
        sub_scope_model2 = SubScope(**sub_scope_model_dict)

        # Verify the model instances are equivalent
        assert sub_scope_model == sub_scope_model2

        # Convert model instance back to dict and verify no loss of data
        sub_scope_model_json2 = sub_scope_model.to_dict()
        assert sub_scope_model_json2 == sub_scope_model_json


class TestModel_SubScopeCollection:
    """
    Test Class for SubScopeCollection
    """

    def test_sub_scope_collection_serialization(self):
        """
        Test serialization/deserialization for SubScopeCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_first_model = {}  # PageHRefFirst
        page_h_ref_first_model['href'] = 'testString'

        page_h_ref_next_model = {}  # PageHRefNext
        page_h_ref_next_model['href'] = 'testString'
        page_h_ref_next_model['start'] = 'testString'

        scope_property_model = {}  # ScopePropertyScopeAny
        scope_property_model['name'] = 'testString'
        scope_property_model['value'] = 'testString'

        sub_scope_model = {}  # SubScope
        sub_scope_model['id'] = 'testString'
        sub_scope_model['name'] = 'testString'
        sub_scope_model['description'] = 'testString'
        sub_scope_model['environment'] = 'testString'
        sub_scope_model['properties'] = [scope_property_model]

        # Construct a json representation of a SubScopeCollection model
        sub_scope_collection_model_json = {}
        sub_scope_collection_model_json['limit'] = 50
        sub_scope_collection_model_json['total_count'] = 230
        sub_scope_collection_model_json['first'] = page_h_ref_first_model
        sub_scope_collection_model_json['next'] = page_h_ref_next_model
        sub_scope_collection_model_json['subscopes'] = [sub_scope_model]

        # Construct a model instance of SubScopeCollection by calling from_dict on the json representation
        sub_scope_collection_model = SubScopeCollection.from_dict(sub_scope_collection_model_json)
        assert sub_scope_collection_model != False

        # Construct a model instance of SubScopeCollection by calling from_dict on the json representation
        sub_scope_collection_model_dict = SubScopeCollection.from_dict(sub_scope_collection_model_json).__dict__
        sub_scope_collection_model2 = SubScopeCollection(**sub_scope_collection_model_dict)

        # Verify the model instances are equivalent
        assert sub_scope_collection_model == sub_scope_collection_model2

        # Convert model instance back to dict and verify no loss of data
        sub_scope_collection_model_json2 = sub_scope_collection_model.to_dict()
        assert sub_scope_collection_model_json2 == sub_scope_collection_model_json


class TestModel_SubScopeResponse:
    """
    Test Class for SubScopeResponse
    """

    def test_sub_scope_response_serialization(self):
        """
        Test serialization/deserialization for SubScopeResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_property_model = {}  # ScopePropertyScopeAny
        scope_property_model['name'] = 'testString'
        scope_property_model['value'] = 'testString'

        sub_scope_model = {}  # SubScope
        sub_scope_model['id'] = 'testString'
        sub_scope_model['name'] = 'testString'
        sub_scope_model['description'] = 'testString'
        sub_scope_model['environment'] = 'testString'
        sub_scope_model['properties'] = [scope_property_model]

        # Construct a json representation of a SubScopeResponse model
        sub_scope_response_model_json = {}
        sub_scope_response_model_json['subscopes'] = [sub_scope_model]

        # Construct a model instance of SubScopeResponse by calling from_dict on the json representation
        sub_scope_response_model = SubScopeResponse.from_dict(sub_scope_response_model_json)
        assert sub_scope_response_model != False

        # Construct a model instance of SubScopeResponse by calling from_dict on the json representation
        sub_scope_response_model_dict = SubScopeResponse.from_dict(sub_scope_response_model_json).__dict__
        sub_scope_response_model2 = SubScopeResponse(**sub_scope_response_model_dict)

        # Verify the model instances are equivalent
        assert sub_scope_response_model == sub_scope_response_model2

        # Convert model instance back to dict and verify no loss of data
        sub_scope_response_model_json2 = sub_scope_response_model.to_dict()
        assert sub_scope_response_model_json2 == sub_scope_response_model_json


class TestModel_SupportedConfigs:
    """
    Test Class for SupportedConfigs
    """

    def test_supported_configs_serialization(self):
        """
        Test serialization/deserialization for SupportedConfigs
        """

        # Construct dict forms of any model objects needed in order to build this model.

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_property_model = {}  # RuleProperty
        rule_property_model['name'] = 'testString'
        rule_property_model['description'] = 'testString'
        rule_property_model['type'] = 'string'

        # Construct a json representation of a SupportedConfigs model
        supported_configs_model_json = {}
        supported_configs_model_json['resource_kind'] = 'testString'
        supported_configs_model_json['additional_target_attributes'] = [additional_target_attribute_model]
        supported_configs_model_json['properties'] = [rule_property_model]
        supported_configs_model_json['description'] = 'testString'
        supported_configs_model_json['cip_requires_service_instance'] = True
        supported_configs_model_json['resource_group_support'] = True
        supported_configs_model_json['tagging_support'] = True
        supported_configs_model_json['inherit_tags'] = True

        # Construct a model instance of SupportedConfigs by calling from_dict on the json representation
        supported_configs_model = SupportedConfigs.from_dict(supported_configs_model_json)
        assert supported_configs_model != False

        # Construct a model instance of SupportedConfigs by calling from_dict on the json representation
        supported_configs_model_dict = SupportedConfigs.from_dict(supported_configs_model_json).__dict__
        supported_configs_model2 = SupportedConfigs(**supported_configs_model_dict)

        # Verify the model instances are equivalent
        assert supported_configs_model == supported_configs_model2

        # Convert model instance back to dict and verify no loss of data
        supported_configs_model_json2 = supported_configs_model.to_dict()
        assert supported_configs_model_json2 == supported_configs_model_json


class TestModel_Tags:
    """
    Test Class for Tags
    """

    def test_tags_serialization(self):
        """
        Test serialization/deserialization for Tags
        """

        # Construct a json representation of a Tags model
        tags_model_json = {}
        tags_model_json['user'] = ['testString']
        tags_model_json['access'] = ['testString']
        tags_model_json['service'] = ['testString']

        # Construct a model instance of Tags by calling from_dict on the json representation
        tags_model = Tags.from_dict(tags_model_json)
        assert tags_model != False

        # Construct a model instance of Tags by calling from_dict on the json representation
        tags_model_dict = Tags.from_dict(tags_model_json).__dict__
        tags_model2 = Tags(**tags_model_dict)

        # Verify the model instances are equivalent
        assert tags_model == tags_model2

        # Convert model instance back to dict and verify no loss of data
        tags_model_json2 = tags_model.to_dict()
        assert tags_model_json2 == tags_model_json


class TestModel_Target:
    """
    Test Class for Target
    """

    def test_target_serialization(self):
        """
        Test serialization/deserialization for Target
        """

        # Construct dict forms of any model objects needed in order to build this model.

        account_model = {}  # Account
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        resource_model = {}  # Resource
        resource_model['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        resource_model['home_account_id'] = '2411ffdc16844b07b42521c3443f456d'
        resource_model['id'] = 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::'
        resource_model['resource_name'] = 'jeff\'s key'
        resource_model['account'] = account_model
        resource_model['component_id'] = 'cloud-object_storage'
        resource_model['component_name'] = 'cloud-object_storage'
        resource_model['environment'] = 'ibm cloud'
        resource_model['tags'] = tags_model
        resource_model['status'] = 'compliant'
        resource_model['total_count'] = 140
        resource_model['pass_count'] = 123
        resource_model['failure_count'] = 12
        resource_model['error_count'] = 5
        resource_model['skipped_count'] = 7
        resource_model['completed_count'] = 135
        resource_model['service_name'] = 'pm-20'
        resource_model['instance_crn'] = 'testString'

        credential_response_model = {}  # CredentialResponse
        credential_response_model['type'] = 'iam_credentials'
        credential_response_model['secret_crn'] = 'testString'
        credential_response_model['secret_name'] = 'my secret'
        credential_response_model['resources'] = [resource_model]

        # Construct a json representation of a Target model
        target_model_json = {}
        target_model_json['id'] = 'a2366444-ad87-40b1-81d0-476df1cc1f18'
        target_model_json['account_id'] = 'be200c80cabc456e91139e4152327823'
        target_model_json['trusted_profile_id'] = 'Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3'
        target_model_json['name'] = 'Target Account-A'
        target_model_json['credentials'] = [credential_response_model]
        target_model_json['created_by'] = 'IBMid-270007EPPC'
        target_model_json['created_on'] = '2024-02-07T05:42:58Z'
        target_model_json['updated_by'] = 'IBMid-270007EPPC'
        target_model_json['updated_on'] = '2024-02-07T05:42:58Z'

        # Construct a model instance of Target by calling from_dict on the json representation
        target_model = Target.from_dict(target_model_json)
        assert target_model != False

        # Construct a model instance of Target by calling from_dict on the json representation
        target_model_dict = Target.from_dict(target_model_json).__dict__
        target_model2 = Target(**target_model_dict)

        # Verify the model instances are equivalent
        assert target_model == target_model2

        # Convert model instance back to dict and verify no loss of data
        target_model_json2 = target_model.to_dict()
        assert target_model_json2 == target_model_json


class TestModel_TargetCollection:
    """
    Test Class for TargetCollection
    """

    def test_target_collection_serialization(self):
        """
        Test serialization/deserialization for TargetCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_first_model = {}  # PageHRefFirst
        page_h_ref_first_model['href'] = 'testString'

        page_h_ref_next_model = {}  # PageHRefNext
        page_h_ref_next_model['href'] = 'testString'
        page_h_ref_next_model['start'] = 'testString'

        account_model = {}  # Account
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        resource_model = {}  # Resource
        resource_model['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        resource_model['home_account_id'] = '2411ffdc16844b07b42521c3443f456d'
        resource_model['id'] = 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::'
        resource_model['resource_name'] = 'jeff\'s key'
        resource_model['account'] = account_model
        resource_model['component_id'] = 'cloud-object_storage'
        resource_model['component_name'] = 'cloud-object_storage'
        resource_model['environment'] = 'ibm cloud'
        resource_model['tags'] = tags_model
        resource_model['status'] = 'compliant'
        resource_model['total_count'] = 140
        resource_model['pass_count'] = 123
        resource_model['failure_count'] = 12
        resource_model['error_count'] = 5
        resource_model['skipped_count'] = 7
        resource_model['completed_count'] = 135
        resource_model['service_name'] = 'pm-20'
        resource_model['instance_crn'] = 'testString'

        credential_response_model = {}  # CredentialResponse
        credential_response_model['type'] = 'iam_credentials'
        credential_response_model['secret_crn'] = 'testString'
        credential_response_model['secret_name'] = 'my secret'
        credential_response_model['resources'] = [resource_model]

        target_model = {}  # Target
        target_model['id'] = 'a2366444-ad87-40b1-81d0-476df1cc1f18'
        target_model['account_id'] = 'be200c80cabc456e91139e4152327823'
        target_model['trusted_profile_id'] = 'Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3'
        target_model['name'] = 'Target Account-A'
        target_model['credentials'] = [credential_response_model]
        target_model['created_by'] = 'IBMid-270007EPPC'
        target_model['created_on'] = '2024-02-07T05:42:58Z'
        target_model['updated_by'] = 'IBMid-270007EPPC'
        target_model['updated_on'] = '2024-02-07T05:42:58Z'

        # Construct a json representation of a TargetCollection model
        target_collection_model_json = {}
        target_collection_model_json['limit'] = 50
        target_collection_model_json['total_count'] = 230
        target_collection_model_json['first'] = page_h_ref_first_model
        target_collection_model_json['next'] = page_h_ref_next_model
        target_collection_model_json['targets'] = [target_model]

        # Construct a model instance of TargetCollection by calling from_dict on the json representation
        target_collection_model = TargetCollection.from_dict(target_collection_model_json)
        assert target_collection_model != False

        # Construct a model instance of TargetCollection by calling from_dict on the json representation
        target_collection_model_dict = TargetCollection.from_dict(target_collection_model_json).__dict__
        target_collection_model2 = TargetCollection(**target_collection_model_dict)

        # Verify the model instances are equivalent
        assert target_collection_model == target_collection_model2

        # Convert model instance back to dict and verify no loss of data
        target_collection_model_json2 = target_collection_model.to_dict()
        assert target_collection_model_json2 == target_collection_model_json


class TestModel_TargetInfo:
    """
    Test Class for TargetInfo
    """

    def test_target_info_serialization(self):
        """
        Test serialization/deserialization for TargetInfo
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        # Construct a json representation of a TargetInfo model
        target_info_model_json = {}
        target_info_model_json['id'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket'
        target_info_model_json['account_id'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        target_info_model_json['service_name'] = 'cloud-object-storage'
        target_info_model_json['service_display_name'] = 'cloud-object-storage'
        target_info_model_json['resource_crn'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket'
        target_info_model_json['resource_name'] = 'mybucket'
        target_info_model_json['tags'] = tags_model

        # Construct a model instance of TargetInfo by calling from_dict on the json representation
        target_info_model = TargetInfo.from_dict(target_info_model_json)
        assert target_info_model != False

        # Construct a model instance of TargetInfo by calling from_dict on the json representation
        target_info_model_dict = TargetInfo.from_dict(target_info_model_json).__dict__
        target_info_model2 = TargetInfo(**target_info_model_dict)

        # Verify the model instances are equivalent
        assert target_info_model == target_info_model2

        # Convert model instance back to dict and verify no loss of data
        target_info_model_json2 = target_info_model.to_dict()
        assert target_info_model_json2 == target_info_model_json


class TestModel_TestEvent:
    """
    Test Class for TestEvent
    """

    def test_test_event_serialization(self):
        """
        Test serialization/deserialization for TestEvent
        """

        # Construct a json representation of a TestEvent model
        test_event_model_json = {}
        test_event_model_json['success'] = True

        # Construct a model instance of TestEvent by calling from_dict on the json representation
        test_event_model = TestEvent.from_dict(test_event_model_json)
        assert test_event_model != False

        # Construct a model instance of TestEvent by calling from_dict on the json representation
        test_event_model_dict = TestEvent.from_dict(test_event_model_json).__dict__
        test_event_model2 = TestEvent(**test_event_model_dict)

        # Verify the model instances are equivalent
        assert test_event_model == test_event_model2

        # Convert model instance back to dict and verify no loss of data
        test_event_model_json2 = test_event_model.to_dict()
        assert test_event_model_json2 == test_event_model_json


class TestModel_ConditionItemConditionBase:
    """
    Test Class for ConditionItemConditionBase
    """

    def test_condition_item_condition_base_serialization(self):
        """
        Test serialization/deserialization for ConditionItemConditionBase
        """

        # Construct a json representation of a ConditionItemConditionBase model
        condition_item_condition_base_model_json = {}
        condition_item_condition_base_model_json['description'] = 'testString'
        condition_item_condition_base_model_json['property'] = 'testString'
        condition_item_condition_base_model_json['operator'] = 'string_equals'
        condition_item_condition_base_model_json['value'] = 'testString'

        # Construct a model instance of ConditionItemConditionBase by calling from_dict on the json representation
        condition_item_condition_base_model = ConditionItemConditionBase.from_dict(condition_item_condition_base_model_json)
        assert condition_item_condition_base_model != False

        # Construct a model instance of ConditionItemConditionBase by calling from_dict on the json representation
        condition_item_condition_base_model_dict = ConditionItemConditionBase.from_dict(condition_item_condition_base_model_json).__dict__
        condition_item_condition_base_model2 = ConditionItemConditionBase(**condition_item_condition_base_model_dict)

        # Verify the model instances are equivalent
        assert condition_item_condition_base_model == condition_item_condition_base_model2

        # Convert model instance back to dict and verify no loss of data
        condition_item_condition_base_model_json2 = condition_item_condition_base_model.to_dict()
        assert condition_item_condition_base_model_json2 == condition_item_condition_base_model_json


class TestModel_MultiCloudScopePayloadById:
    """
    Test Class for MultiCloudScopePayloadById
    """

    def test_multi_cloud_scope_payload_by_id_serialization(self):
        """
        Test serialization/deserialization for MultiCloudScopePayloadById
        """

        # Construct a json representation of a MultiCloudScopePayloadById model
        multi_cloud_scope_payload_by_id_model_json = {}
        multi_cloud_scope_payload_by_id_model_json['id'] = 'testString'

        # Construct a model instance of MultiCloudScopePayloadById by calling from_dict on the json representation
        multi_cloud_scope_payload_by_id_model = MultiCloudScopePayloadById.from_dict(multi_cloud_scope_payload_by_id_model_json)
        assert multi_cloud_scope_payload_by_id_model != False

        # Construct a model instance of MultiCloudScopePayloadById by calling from_dict on the json representation
        multi_cloud_scope_payload_by_id_model_dict = MultiCloudScopePayloadById.from_dict(multi_cloud_scope_payload_by_id_model_json).__dict__
        multi_cloud_scope_payload_by_id_model2 = MultiCloudScopePayloadById(**multi_cloud_scope_payload_by_id_model_dict)

        # Verify the model instances are equivalent
        assert multi_cloud_scope_payload_by_id_model == multi_cloud_scope_payload_by_id_model2

        # Convert model instance back to dict and verify no loss of data
        multi_cloud_scope_payload_by_id_model_json2 = multi_cloud_scope_payload_by_id_model.to_dict()
        assert multi_cloud_scope_payload_by_id_model_json2 == multi_cloud_scope_payload_by_id_model_json


class TestModel_MultiCloudScopePayloadByProperties:
    """
    Test Class for MultiCloudScopePayloadByProperties
    """

    def test_multi_cloud_scope_payload_by_properties_serialization(self):
        """
        Test serialization/deserialization for MultiCloudScopePayloadByProperties
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_property_model = {}  # ScopePropertyScopeAny
        scope_property_model['name'] = 'testString'
        scope_property_model['value'] = 'testString'

        # Construct a json representation of a MultiCloudScopePayloadByProperties model
        multi_cloud_scope_payload_by_properties_model_json = {}
        multi_cloud_scope_payload_by_properties_model_json['description'] = 'testString'
        multi_cloud_scope_payload_by_properties_model_json['environment'] = 'testString'
        multi_cloud_scope_payload_by_properties_model_json['properties'] = [scope_property_model]

        # Construct a model instance of MultiCloudScopePayloadByProperties by calling from_dict on the json representation
        multi_cloud_scope_payload_by_properties_model = MultiCloudScopePayloadByProperties.from_dict(multi_cloud_scope_payload_by_properties_model_json)
        assert multi_cloud_scope_payload_by_properties_model != False

        # Construct a model instance of MultiCloudScopePayloadByProperties by calling from_dict on the json representation
        multi_cloud_scope_payload_by_properties_model_dict = MultiCloudScopePayloadByProperties.from_dict(multi_cloud_scope_payload_by_properties_model_json).__dict__
        multi_cloud_scope_payload_by_properties_model2 = MultiCloudScopePayloadByProperties(**multi_cloud_scope_payload_by_properties_model_dict)

        # Verify the model instances are equivalent
        assert multi_cloud_scope_payload_by_properties_model == multi_cloud_scope_payload_by_properties_model2

        # Convert model instance back to dict and verify no loss of data
        multi_cloud_scope_payload_by_properties_model_json2 = multi_cloud_scope_payload_by_properties_model.to_dict()
        assert multi_cloud_scope_payload_by_properties_model_json2 == multi_cloud_scope_payload_by_properties_model_json


class TestModel_RequiredConfigConditionBase:
    """
    Test Class for RequiredConfigConditionBase
    """

    def test_required_config_condition_base_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigConditionBase
        """

        # Construct a json representation of a RequiredConfigConditionBase model
        required_config_condition_base_model_json = {}
        required_config_condition_base_model_json['description'] = 'testString'
        required_config_condition_base_model_json['property'] = 'testString'
        required_config_condition_base_model_json['operator'] = 'string_equals'
        required_config_condition_base_model_json['value'] = 'testString'

        # Construct a model instance of RequiredConfigConditionBase by calling from_dict on the json representation
        required_config_condition_base_model = RequiredConfigConditionBase.from_dict(required_config_condition_base_model_json)
        assert required_config_condition_base_model != False

        # Construct a model instance of RequiredConfigConditionBase by calling from_dict on the json representation
        required_config_condition_base_model_dict = RequiredConfigConditionBase.from_dict(required_config_condition_base_model_json).__dict__
        required_config_condition_base_model2 = RequiredConfigConditionBase(**required_config_condition_base_model_dict)

        # Verify the model instances are equivalent
        assert required_config_condition_base_model == required_config_condition_base_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_condition_base_model_json2 = required_config_condition_base_model.to_dict()
        assert required_config_condition_base_model_json2 == required_config_condition_base_model_json


class TestModel_ScopePropertyExclusions:
    """
    Test Class for ScopePropertyExclusions
    """

    def test_scope_property_exclusions_serialization(self):
        """
        Test serialization/deserialization for ScopePropertyExclusions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_property_exclusion_item_model = {}  # ScopePropertyExclusionItem
        scope_property_exclusion_item_model['scope_id'] = 'testString'
        scope_property_exclusion_item_model['scope_type'] = 'enterprise'

        # Construct a json representation of a ScopePropertyExclusions model
        scope_property_exclusions_model_json = {}
        scope_property_exclusions_model_json['name'] = 'exclusions'
        scope_property_exclusions_model_json['value'] = [scope_property_exclusion_item_model]

        # Construct a model instance of ScopePropertyExclusions by calling from_dict on the json representation
        scope_property_exclusions_model = ScopePropertyExclusions.from_dict(scope_property_exclusions_model_json)
        assert scope_property_exclusions_model != False

        # Construct a model instance of ScopePropertyExclusions by calling from_dict on the json representation
        scope_property_exclusions_model_dict = ScopePropertyExclusions.from_dict(scope_property_exclusions_model_json).__dict__
        scope_property_exclusions_model2 = ScopePropertyExclusions(**scope_property_exclusions_model_dict)

        # Verify the model instances are equivalent
        assert scope_property_exclusions_model == scope_property_exclusions_model2

        # Convert model instance back to dict and verify no loss of data
        scope_property_exclusions_model_json2 = scope_property_exclusions_model.to_dict()
        assert scope_property_exclusions_model_json2 == scope_property_exclusions_model_json


class TestModel_ScopePropertyScopeAny:
    """
    Test Class for ScopePropertyScopeAny
    """

    def test_scope_property_scope_any_serialization(self):
        """
        Test serialization/deserialization for ScopePropertyScopeAny
        """

        # Construct a json representation of a ScopePropertyScopeAny model
        scope_property_scope_any_model_json = {}
        scope_property_scope_any_model_json['name'] = 'testString'
        scope_property_scope_any_model_json['value'] = 'testString'

        # Construct a model instance of ScopePropertyScopeAny by calling from_dict on the json representation
        scope_property_scope_any_model = ScopePropertyScopeAny.from_dict(scope_property_scope_any_model_json)
        assert scope_property_scope_any_model != False

        # Construct a model instance of ScopePropertyScopeAny by calling from_dict on the json representation
        scope_property_scope_any_model_dict = ScopePropertyScopeAny.from_dict(scope_property_scope_any_model_json).__dict__
        scope_property_scope_any_model2 = ScopePropertyScopeAny(**scope_property_scope_any_model_dict)

        # Verify the model instances are equivalent
        assert scope_property_scope_any_model == scope_property_scope_any_model2

        # Convert model instance back to dict and verify no loss of data
        scope_property_scope_any_model_json2 = scope_property_scope_any_model.to_dict()
        assert scope_property_scope_any_model_json2 == scope_property_scope_any_model_json


class TestModel_ScopePropertyScopeId:
    """
    Test Class for ScopePropertyScopeId
    """

    def test_scope_property_scope_id_serialization(self):
        """
        Test serialization/deserialization for ScopePropertyScopeId
        """

        # Construct a json representation of a ScopePropertyScopeId model
        scope_property_scope_id_model_json = {}
        scope_property_scope_id_model_json['name'] = 'scope_id'
        scope_property_scope_id_model_json['value'] = 'testString'

        # Construct a model instance of ScopePropertyScopeId by calling from_dict on the json representation
        scope_property_scope_id_model = ScopePropertyScopeId.from_dict(scope_property_scope_id_model_json)
        assert scope_property_scope_id_model != False

        # Construct a model instance of ScopePropertyScopeId by calling from_dict on the json representation
        scope_property_scope_id_model_dict = ScopePropertyScopeId.from_dict(scope_property_scope_id_model_json).__dict__
        scope_property_scope_id_model2 = ScopePropertyScopeId(**scope_property_scope_id_model_dict)

        # Verify the model instances are equivalent
        assert scope_property_scope_id_model == scope_property_scope_id_model2

        # Convert model instance back to dict and verify no loss of data
        scope_property_scope_id_model_json2 = scope_property_scope_id_model.to_dict()
        assert scope_property_scope_id_model_json2 == scope_property_scope_id_model_json


class TestModel_ScopePropertyScopeType:
    """
    Test Class for ScopePropertyScopeType
    """

    def test_scope_property_scope_type_serialization(self):
        """
        Test serialization/deserialization for ScopePropertyScopeType
        """

        # Construct a json representation of a ScopePropertyScopeType model
        scope_property_scope_type_model_json = {}
        scope_property_scope_type_model_json['name'] = 'scope_type'
        scope_property_scope_type_model_json['value'] = 'account'

        # Construct a model instance of ScopePropertyScopeType by calling from_dict on the json representation
        scope_property_scope_type_model = ScopePropertyScopeType.from_dict(scope_property_scope_type_model_json)
        assert scope_property_scope_type_model != False

        # Construct a model instance of ScopePropertyScopeType by calling from_dict on the json representation
        scope_property_scope_type_model_dict = ScopePropertyScopeType.from_dict(scope_property_scope_type_model_json).__dict__
        scope_property_scope_type_model2 = ScopePropertyScopeType(**scope_property_scope_type_model_dict)

        # Verify the model instances are equivalent
        assert scope_property_scope_type_model == scope_property_scope_type_model2

        # Convert model instance back to dict and verify no loss of data
        scope_property_scope_type_model_json2 = scope_property_scope_type_model.to_dict()
        assert scope_property_scope_type_model_json2 == scope_property_scope_type_model_json


class TestModel_ConditionItemConditionListConditionListConditionAnd:
    """
    Test Class for ConditionItemConditionListConditionListConditionAnd
    """

    def test_condition_item_condition_list_condition_list_condition_and_serialization(self):
        """
        Test serialization/deserialization for ConditionItemConditionListConditionListConditionAnd
        """

        # Construct dict forms of any model objects needed in order to build this model.

        condition_item_model = {}  # ConditionItemConditionBase
        condition_item_model['description'] = 'testString'
        condition_item_model['property'] = 'testString'
        condition_item_model['operator'] = 'string_equals'
        condition_item_model['value'] = 'testString'

        # Construct a json representation of a ConditionItemConditionListConditionListConditionAnd model
        condition_item_condition_list_condition_list_condition_and_model_json = {}
        condition_item_condition_list_condition_list_condition_and_model_json['description'] = 'testString'
        condition_item_condition_list_condition_list_condition_and_model_json['and'] = [condition_item_model]

        # Construct a model instance of ConditionItemConditionListConditionListConditionAnd by calling from_dict on the json representation
        condition_item_condition_list_condition_list_condition_and_model = ConditionItemConditionListConditionListConditionAnd.from_dict(condition_item_condition_list_condition_list_condition_and_model_json)
        assert condition_item_condition_list_condition_list_condition_and_model != False

        # Construct a model instance of ConditionItemConditionListConditionListConditionAnd by calling from_dict on the json representation
        condition_item_condition_list_condition_list_condition_and_model_dict = ConditionItemConditionListConditionListConditionAnd.from_dict(condition_item_condition_list_condition_list_condition_and_model_json).__dict__
        condition_item_condition_list_condition_list_condition_and_model2 = ConditionItemConditionListConditionListConditionAnd(**condition_item_condition_list_condition_list_condition_and_model_dict)

        # Verify the model instances are equivalent
        assert condition_item_condition_list_condition_list_condition_and_model == condition_item_condition_list_condition_list_condition_and_model2

        # Convert model instance back to dict and verify no loss of data
        condition_item_condition_list_condition_list_condition_and_model_json2 = condition_item_condition_list_condition_list_condition_and_model.to_dict()
        assert condition_item_condition_list_condition_list_condition_and_model_json2 == condition_item_condition_list_condition_list_condition_and_model_json


class TestModel_ConditionItemConditionListConditionListConditionOr:
    """
    Test Class for ConditionItemConditionListConditionListConditionOr
    """

    def test_condition_item_condition_list_condition_list_condition_or_serialization(self):
        """
        Test serialization/deserialization for ConditionItemConditionListConditionListConditionOr
        """

        # Construct dict forms of any model objects needed in order to build this model.

        condition_item_model = {}  # ConditionItemConditionBase
        condition_item_model['description'] = 'testString'
        condition_item_model['property'] = 'testString'
        condition_item_model['operator'] = 'string_equals'
        condition_item_model['value'] = 'testString'

        # Construct a json representation of a ConditionItemConditionListConditionListConditionOr model
        condition_item_condition_list_condition_list_condition_or_model_json = {}
        condition_item_condition_list_condition_list_condition_or_model_json['description'] = 'testString'
        condition_item_condition_list_condition_list_condition_or_model_json['or'] = [condition_item_model]

        # Construct a model instance of ConditionItemConditionListConditionListConditionOr by calling from_dict on the json representation
        condition_item_condition_list_condition_list_condition_or_model = ConditionItemConditionListConditionListConditionOr.from_dict(condition_item_condition_list_condition_list_condition_or_model_json)
        assert condition_item_condition_list_condition_list_condition_or_model != False

        # Construct a model instance of ConditionItemConditionListConditionListConditionOr by calling from_dict on the json representation
        condition_item_condition_list_condition_list_condition_or_model_dict = ConditionItemConditionListConditionListConditionOr.from_dict(condition_item_condition_list_condition_list_condition_or_model_json).__dict__
        condition_item_condition_list_condition_list_condition_or_model2 = ConditionItemConditionListConditionListConditionOr(**condition_item_condition_list_condition_list_condition_or_model_dict)

        # Verify the model instances are equivalent
        assert condition_item_condition_list_condition_list_condition_or_model == condition_item_condition_list_condition_list_condition_or_model2

        # Convert model instance back to dict and verify no loss of data
        condition_item_condition_list_condition_list_condition_or_model_json2 = condition_item_condition_list_condition_list_condition_or_model.to_dict()
        assert condition_item_condition_list_condition_list_condition_or_model_json2 == condition_item_condition_list_condition_list_condition_or_model_json


class TestModel_ConditionItemConditionSubRuleConditionSubRuleConditionAll:
    """
    Test Class for ConditionItemConditionSubRuleConditionSubRuleConditionAll
    """

    def test_condition_item_condition_sub_rule_condition_sub_rule_condition_all_serialization(self):
        """
        Test serialization/deserialization for ConditionItemConditionSubRuleConditionSubRuleConditionAll
        """

        # Construct dict forms of any model objects needed in order to build this model.

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_target_model = {}  # RuleTarget
        rule_target_model['service_name'] = 'testString'
        rule_target_model['service_display_name'] = 'testString'
        rule_target_model['resource_kind'] = 'testString'
        rule_target_model['additional_target_attributes'] = [additional_target_attribute_model]
        rule_target_model['ref'] = 'testString'

        required_config_model = {}  # RequiredConfigConditionBase
        required_config_model['description'] = 'testString'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        sub_rule_model = {}  # SubRule
        sub_rule_model['target'] = rule_target_model
        sub_rule_model['required_config'] = required_config_model

        # Construct a json representation of a ConditionItemConditionSubRuleConditionSubRuleConditionAll model
        condition_item_condition_sub_rule_condition_sub_rule_condition_all_model_json = {}
        condition_item_condition_sub_rule_condition_sub_rule_condition_all_model_json['all'] = sub_rule_model

        # Construct a model instance of ConditionItemConditionSubRuleConditionSubRuleConditionAll by calling from_dict on the json representation
        condition_item_condition_sub_rule_condition_sub_rule_condition_all_model = ConditionItemConditionSubRuleConditionSubRuleConditionAll.from_dict(condition_item_condition_sub_rule_condition_sub_rule_condition_all_model_json)
        assert condition_item_condition_sub_rule_condition_sub_rule_condition_all_model != False

        # Construct a model instance of ConditionItemConditionSubRuleConditionSubRuleConditionAll by calling from_dict on the json representation
        condition_item_condition_sub_rule_condition_sub_rule_condition_all_model_dict = ConditionItemConditionSubRuleConditionSubRuleConditionAll.from_dict(condition_item_condition_sub_rule_condition_sub_rule_condition_all_model_json).__dict__
        condition_item_condition_sub_rule_condition_sub_rule_condition_all_model2 = ConditionItemConditionSubRuleConditionSubRuleConditionAll(**condition_item_condition_sub_rule_condition_sub_rule_condition_all_model_dict)

        # Verify the model instances are equivalent
        assert condition_item_condition_sub_rule_condition_sub_rule_condition_all_model == condition_item_condition_sub_rule_condition_sub_rule_condition_all_model2

        # Convert model instance back to dict and verify no loss of data
        condition_item_condition_sub_rule_condition_sub_rule_condition_all_model_json2 = condition_item_condition_sub_rule_condition_sub_rule_condition_all_model.to_dict()
        assert condition_item_condition_sub_rule_condition_sub_rule_condition_all_model_json2 == condition_item_condition_sub_rule_condition_sub_rule_condition_all_model_json


class TestModel_ConditionItemConditionSubRuleConditionSubRuleConditionAllIf:
    """
    Test Class for ConditionItemConditionSubRuleConditionSubRuleConditionAllIf
    """

    def test_condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_serialization(self):
        """
        Test serialization/deserialization for ConditionItemConditionSubRuleConditionSubRuleConditionAllIf
        """

        # Construct dict forms of any model objects needed in order to build this model.

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_target_model = {}  # RuleTarget
        rule_target_model['service_name'] = 'testString'
        rule_target_model['service_display_name'] = 'testString'
        rule_target_model['resource_kind'] = 'testString'
        rule_target_model['additional_target_attributes'] = [additional_target_attribute_model]
        rule_target_model['ref'] = 'testString'

        required_config_model = {}  # RequiredConfigConditionBase
        required_config_model['description'] = 'testString'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        sub_rule_model = {}  # SubRule
        sub_rule_model['target'] = rule_target_model
        sub_rule_model['required_config'] = required_config_model

        # Construct a json representation of a ConditionItemConditionSubRuleConditionSubRuleConditionAllIf model
        condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model_json = {}
        condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model_json['all_ifexists'] = sub_rule_model

        # Construct a model instance of ConditionItemConditionSubRuleConditionSubRuleConditionAllIf by calling from_dict on the json representation
        condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model = ConditionItemConditionSubRuleConditionSubRuleConditionAllIf.from_dict(condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model_json)
        assert condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model != False

        # Construct a model instance of ConditionItemConditionSubRuleConditionSubRuleConditionAllIf by calling from_dict on the json representation
        condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model_dict = ConditionItemConditionSubRuleConditionSubRuleConditionAllIf.from_dict(condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model_json).__dict__
        condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model2 = ConditionItemConditionSubRuleConditionSubRuleConditionAllIf(**condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model_dict)

        # Verify the model instances are equivalent
        assert condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model == condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model2

        # Convert model instance back to dict and verify no loss of data
        condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model_json2 = condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model.to_dict()
        assert condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model_json2 == condition_item_condition_sub_rule_condition_sub_rule_condition_all_if_model_json


class TestModel_ConditionItemConditionSubRuleConditionSubRuleConditionAny:
    """
    Test Class for ConditionItemConditionSubRuleConditionSubRuleConditionAny
    """

    def test_condition_item_condition_sub_rule_condition_sub_rule_condition_any_serialization(self):
        """
        Test serialization/deserialization for ConditionItemConditionSubRuleConditionSubRuleConditionAny
        """

        # Construct dict forms of any model objects needed in order to build this model.

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_target_model = {}  # RuleTarget
        rule_target_model['service_name'] = 'testString'
        rule_target_model['service_display_name'] = 'testString'
        rule_target_model['resource_kind'] = 'testString'
        rule_target_model['additional_target_attributes'] = [additional_target_attribute_model]
        rule_target_model['ref'] = 'testString'

        required_config_model = {}  # RequiredConfigConditionBase
        required_config_model['description'] = 'testString'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        sub_rule_model = {}  # SubRule
        sub_rule_model['target'] = rule_target_model
        sub_rule_model['required_config'] = required_config_model

        # Construct a json representation of a ConditionItemConditionSubRuleConditionSubRuleConditionAny model
        condition_item_condition_sub_rule_condition_sub_rule_condition_any_model_json = {}
        condition_item_condition_sub_rule_condition_sub_rule_condition_any_model_json['any'] = sub_rule_model

        # Construct a model instance of ConditionItemConditionSubRuleConditionSubRuleConditionAny by calling from_dict on the json representation
        condition_item_condition_sub_rule_condition_sub_rule_condition_any_model = ConditionItemConditionSubRuleConditionSubRuleConditionAny.from_dict(condition_item_condition_sub_rule_condition_sub_rule_condition_any_model_json)
        assert condition_item_condition_sub_rule_condition_sub_rule_condition_any_model != False

        # Construct a model instance of ConditionItemConditionSubRuleConditionSubRuleConditionAny by calling from_dict on the json representation
        condition_item_condition_sub_rule_condition_sub_rule_condition_any_model_dict = ConditionItemConditionSubRuleConditionSubRuleConditionAny.from_dict(condition_item_condition_sub_rule_condition_sub_rule_condition_any_model_json).__dict__
        condition_item_condition_sub_rule_condition_sub_rule_condition_any_model2 = ConditionItemConditionSubRuleConditionSubRuleConditionAny(**condition_item_condition_sub_rule_condition_sub_rule_condition_any_model_dict)

        # Verify the model instances are equivalent
        assert condition_item_condition_sub_rule_condition_sub_rule_condition_any_model == condition_item_condition_sub_rule_condition_sub_rule_condition_any_model2

        # Convert model instance back to dict and verify no loss of data
        condition_item_condition_sub_rule_condition_sub_rule_condition_any_model_json2 = condition_item_condition_sub_rule_condition_sub_rule_condition_any_model.to_dict()
        assert condition_item_condition_sub_rule_condition_sub_rule_condition_any_model_json2 == condition_item_condition_sub_rule_condition_sub_rule_condition_any_model_json


class TestModel_ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf:
    """
    Test Class for ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf
    """

    def test_condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_serialization(self):
        """
        Test serialization/deserialization for ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf
        """

        # Construct dict forms of any model objects needed in order to build this model.

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_target_model = {}  # RuleTarget
        rule_target_model['service_name'] = 'testString'
        rule_target_model['service_display_name'] = 'testString'
        rule_target_model['resource_kind'] = 'testString'
        rule_target_model['additional_target_attributes'] = [additional_target_attribute_model]
        rule_target_model['ref'] = 'testString'

        required_config_model = {}  # RequiredConfigConditionBase
        required_config_model['description'] = 'testString'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        sub_rule_model = {}  # SubRule
        sub_rule_model['target'] = rule_target_model
        sub_rule_model['required_config'] = required_config_model

        # Construct a json representation of a ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf model
        condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model_json = {}
        condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model_json['any_ifexists'] = sub_rule_model

        # Construct a model instance of ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf by calling from_dict on the json representation
        condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model = ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf.from_dict(condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model_json)
        assert condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model != False

        # Construct a model instance of ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf by calling from_dict on the json representation
        condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model_dict = ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf.from_dict(condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model_json).__dict__
        condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model2 = ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf(**condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model_dict)

        # Verify the model instances are equivalent
        assert condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model == condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model2

        # Convert model instance back to dict and verify no loss of data
        condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model_json2 = condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model.to_dict()
        assert condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model_json2 == condition_item_condition_sub_rule_condition_sub_rule_condition_any_if_model_json


class TestModel_RequiredConfigConditionListConditionListConditionAnd:
    """
    Test Class for RequiredConfigConditionListConditionListConditionAnd
    """

    def test_required_config_condition_list_condition_list_condition_and_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigConditionListConditionListConditionAnd
        """

        # Construct dict forms of any model objects needed in order to build this model.

        condition_item_model = {}  # ConditionItemConditionBase
        condition_item_model['description'] = 'testString'
        condition_item_model['property'] = 'testString'
        condition_item_model['operator'] = 'string_equals'
        condition_item_model['value'] = 'testString'

        # Construct a json representation of a RequiredConfigConditionListConditionListConditionAnd model
        required_config_condition_list_condition_list_condition_and_model_json = {}
        required_config_condition_list_condition_list_condition_and_model_json['description'] = 'testString'
        required_config_condition_list_condition_list_condition_and_model_json['and'] = [condition_item_model]

        # Construct a model instance of RequiredConfigConditionListConditionListConditionAnd by calling from_dict on the json representation
        required_config_condition_list_condition_list_condition_and_model = RequiredConfigConditionListConditionListConditionAnd.from_dict(required_config_condition_list_condition_list_condition_and_model_json)
        assert required_config_condition_list_condition_list_condition_and_model != False

        # Construct a model instance of RequiredConfigConditionListConditionListConditionAnd by calling from_dict on the json representation
        required_config_condition_list_condition_list_condition_and_model_dict = RequiredConfigConditionListConditionListConditionAnd.from_dict(required_config_condition_list_condition_list_condition_and_model_json).__dict__
        required_config_condition_list_condition_list_condition_and_model2 = RequiredConfigConditionListConditionListConditionAnd(**required_config_condition_list_condition_list_condition_and_model_dict)

        # Verify the model instances are equivalent
        assert required_config_condition_list_condition_list_condition_and_model == required_config_condition_list_condition_list_condition_and_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_condition_list_condition_list_condition_and_model_json2 = required_config_condition_list_condition_list_condition_and_model.to_dict()
        assert required_config_condition_list_condition_list_condition_and_model_json2 == required_config_condition_list_condition_list_condition_and_model_json


class TestModel_RequiredConfigConditionListConditionListConditionOr:
    """
    Test Class for RequiredConfigConditionListConditionListConditionOr
    """

    def test_required_config_condition_list_condition_list_condition_or_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigConditionListConditionListConditionOr
        """

        # Construct dict forms of any model objects needed in order to build this model.

        condition_item_model = {}  # ConditionItemConditionBase
        condition_item_model['description'] = 'testString'
        condition_item_model['property'] = 'testString'
        condition_item_model['operator'] = 'string_equals'
        condition_item_model['value'] = 'testString'

        # Construct a json representation of a RequiredConfigConditionListConditionListConditionOr model
        required_config_condition_list_condition_list_condition_or_model_json = {}
        required_config_condition_list_condition_list_condition_or_model_json['description'] = 'testString'
        required_config_condition_list_condition_list_condition_or_model_json['or'] = [condition_item_model]

        # Construct a model instance of RequiredConfigConditionListConditionListConditionOr by calling from_dict on the json representation
        required_config_condition_list_condition_list_condition_or_model = RequiredConfigConditionListConditionListConditionOr.from_dict(required_config_condition_list_condition_list_condition_or_model_json)
        assert required_config_condition_list_condition_list_condition_or_model != False

        # Construct a model instance of RequiredConfigConditionListConditionListConditionOr by calling from_dict on the json representation
        required_config_condition_list_condition_list_condition_or_model_dict = RequiredConfigConditionListConditionListConditionOr.from_dict(required_config_condition_list_condition_list_condition_or_model_json).__dict__
        required_config_condition_list_condition_list_condition_or_model2 = RequiredConfigConditionListConditionListConditionOr(**required_config_condition_list_condition_list_condition_or_model_dict)

        # Verify the model instances are equivalent
        assert required_config_condition_list_condition_list_condition_or_model == required_config_condition_list_condition_list_condition_or_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_condition_list_condition_list_condition_or_model_json2 = required_config_condition_list_condition_list_condition_or_model.to_dict()
        assert required_config_condition_list_condition_list_condition_or_model_json2 == required_config_condition_list_condition_list_condition_or_model_json


class TestModel_RequiredConfigConditionSubRuleConditionSubRuleConditionAll:
    """
    Test Class for RequiredConfigConditionSubRuleConditionSubRuleConditionAll
    """

    def test_required_config_condition_sub_rule_condition_sub_rule_condition_all_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigConditionSubRuleConditionSubRuleConditionAll
        """

        # Construct dict forms of any model objects needed in order to build this model.

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_target_model = {}  # RuleTarget
        rule_target_model['service_name'] = 'testString'
        rule_target_model['service_display_name'] = 'testString'
        rule_target_model['resource_kind'] = 'testString'
        rule_target_model['additional_target_attributes'] = [additional_target_attribute_model]
        rule_target_model['ref'] = 'testString'

        required_config_model = {}  # RequiredConfigConditionBase
        required_config_model['description'] = 'testString'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        sub_rule_model = {}  # SubRule
        sub_rule_model['target'] = rule_target_model
        sub_rule_model['required_config'] = required_config_model

        # Construct a json representation of a RequiredConfigConditionSubRuleConditionSubRuleConditionAll model
        required_config_condition_sub_rule_condition_sub_rule_condition_all_model_json = {}
        required_config_condition_sub_rule_condition_sub_rule_condition_all_model_json['all'] = sub_rule_model

        # Construct a model instance of RequiredConfigConditionSubRuleConditionSubRuleConditionAll by calling from_dict on the json representation
        required_config_condition_sub_rule_condition_sub_rule_condition_all_model = RequiredConfigConditionSubRuleConditionSubRuleConditionAll.from_dict(required_config_condition_sub_rule_condition_sub_rule_condition_all_model_json)
        assert required_config_condition_sub_rule_condition_sub_rule_condition_all_model != False

        # Construct a model instance of RequiredConfigConditionSubRuleConditionSubRuleConditionAll by calling from_dict on the json representation
        required_config_condition_sub_rule_condition_sub_rule_condition_all_model_dict = RequiredConfigConditionSubRuleConditionSubRuleConditionAll.from_dict(required_config_condition_sub_rule_condition_sub_rule_condition_all_model_json).__dict__
        required_config_condition_sub_rule_condition_sub_rule_condition_all_model2 = RequiredConfigConditionSubRuleConditionSubRuleConditionAll(**required_config_condition_sub_rule_condition_sub_rule_condition_all_model_dict)

        # Verify the model instances are equivalent
        assert required_config_condition_sub_rule_condition_sub_rule_condition_all_model == required_config_condition_sub_rule_condition_sub_rule_condition_all_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_condition_sub_rule_condition_sub_rule_condition_all_model_json2 = required_config_condition_sub_rule_condition_sub_rule_condition_all_model.to_dict()
        assert required_config_condition_sub_rule_condition_sub_rule_condition_all_model_json2 == required_config_condition_sub_rule_condition_sub_rule_condition_all_model_json


class TestModel_RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf:
    """
    Test Class for RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf
    """

    def test_required_config_condition_sub_rule_condition_sub_rule_condition_all_if_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf
        """

        # Construct dict forms of any model objects needed in order to build this model.

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_target_model = {}  # RuleTarget
        rule_target_model['service_name'] = 'testString'
        rule_target_model['service_display_name'] = 'testString'
        rule_target_model['resource_kind'] = 'testString'
        rule_target_model['additional_target_attributes'] = [additional_target_attribute_model]
        rule_target_model['ref'] = 'testString'

        required_config_model = {}  # RequiredConfigConditionBase
        required_config_model['description'] = 'testString'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        sub_rule_model = {}  # SubRule
        sub_rule_model['target'] = rule_target_model
        sub_rule_model['required_config'] = required_config_model

        # Construct a json representation of a RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf model
        required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model_json = {}
        required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model_json['all_ifexists'] = sub_rule_model

        # Construct a model instance of RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf by calling from_dict on the json representation
        required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model = RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf.from_dict(required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model_json)
        assert required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model != False

        # Construct a model instance of RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf by calling from_dict on the json representation
        required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model_dict = RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf.from_dict(required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model_json).__dict__
        required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model2 = RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf(**required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model_dict)

        # Verify the model instances are equivalent
        assert required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model == required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model_json2 = required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model.to_dict()
        assert required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model_json2 == required_config_condition_sub_rule_condition_sub_rule_condition_all_if_model_json


class TestModel_RequiredConfigConditionSubRuleConditionSubRuleConditionAny:
    """
    Test Class for RequiredConfigConditionSubRuleConditionSubRuleConditionAny
    """

    def test_required_config_condition_sub_rule_condition_sub_rule_condition_any_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigConditionSubRuleConditionSubRuleConditionAny
        """

        # Construct dict forms of any model objects needed in order to build this model.

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_target_model = {}  # RuleTarget
        rule_target_model['service_name'] = 'testString'
        rule_target_model['service_display_name'] = 'testString'
        rule_target_model['resource_kind'] = 'testString'
        rule_target_model['additional_target_attributes'] = [additional_target_attribute_model]
        rule_target_model['ref'] = 'testString'

        required_config_model = {}  # RequiredConfigConditionBase
        required_config_model['description'] = 'testString'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        sub_rule_model = {}  # SubRule
        sub_rule_model['target'] = rule_target_model
        sub_rule_model['required_config'] = required_config_model

        # Construct a json representation of a RequiredConfigConditionSubRuleConditionSubRuleConditionAny model
        required_config_condition_sub_rule_condition_sub_rule_condition_any_model_json = {}
        required_config_condition_sub_rule_condition_sub_rule_condition_any_model_json['any'] = sub_rule_model

        # Construct a model instance of RequiredConfigConditionSubRuleConditionSubRuleConditionAny by calling from_dict on the json representation
        required_config_condition_sub_rule_condition_sub_rule_condition_any_model = RequiredConfigConditionSubRuleConditionSubRuleConditionAny.from_dict(required_config_condition_sub_rule_condition_sub_rule_condition_any_model_json)
        assert required_config_condition_sub_rule_condition_sub_rule_condition_any_model != False

        # Construct a model instance of RequiredConfigConditionSubRuleConditionSubRuleConditionAny by calling from_dict on the json representation
        required_config_condition_sub_rule_condition_sub_rule_condition_any_model_dict = RequiredConfigConditionSubRuleConditionSubRuleConditionAny.from_dict(required_config_condition_sub_rule_condition_sub_rule_condition_any_model_json).__dict__
        required_config_condition_sub_rule_condition_sub_rule_condition_any_model2 = RequiredConfigConditionSubRuleConditionSubRuleConditionAny(**required_config_condition_sub_rule_condition_sub_rule_condition_any_model_dict)

        # Verify the model instances are equivalent
        assert required_config_condition_sub_rule_condition_sub_rule_condition_any_model == required_config_condition_sub_rule_condition_sub_rule_condition_any_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_condition_sub_rule_condition_sub_rule_condition_any_model_json2 = required_config_condition_sub_rule_condition_sub_rule_condition_any_model.to_dict()
        assert required_config_condition_sub_rule_condition_sub_rule_condition_any_model_json2 == required_config_condition_sub_rule_condition_sub_rule_condition_any_model_json


class TestModel_RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf:
    """
    Test Class for RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf
    """

    def test_required_config_condition_sub_rule_condition_sub_rule_condition_any_if_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf
        """

        # Construct dict forms of any model objects needed in order to build this model.

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'testString'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'testString'

        rule_target_model = {}  # RuleTarget
        rule_target_model['service_name'] = 'testString'
        rule_target_model['service_display_name'] = 'testString'
        rule_target_model['resource_kind'] = 'testString'
        rule_target_model['additional_target_attributes'] = [additional_target_attribute_model]
        rule_target_model['ref'] = 'testString'

        required_config_model = {}  # RequiredConfigConditionBase
        required_config_model['description'] = 'testString'
        required_config_model['property'] = 'testString'
        required_config_model['operator'] = 'string_equals'
        required_config_model['value'] = 'testString'

        sub_rule_model = {}  # SubRule
        sub_rule_model['target'] = rule_target_model
        sub_rule_model['required_config'] = required_config_model

        # Construct a json representation of a RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf model
        required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model_json = {}
        required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model_json['any_ifexists'] = sub_rule_model

        # Construct a model instance of RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf by calling from_dict on the json representation
        required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model = RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf.from_dict(required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model_json)
        assert required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model != False

        # Construct a model instance of RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf by calling from_dict on the json representation
        required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model_dict = RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf.from_dict(required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model_json).__dict__
        required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model2 = RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf(**required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model_dict)

        # Verify the model instances are equivalent
        assert required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model == required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model_json2 = required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model.to_dict()
        assert required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model_json2 == required_config_condition_sub_rule_condition_sub_rule_condition_any_if_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
