# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
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

_base_url = 'https://us-south.compliance.cloud.ibm.com/instances/instance_id/v3'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


def test_parameterized_url():
    """
    Test formatting the parameterized service URL with the default variable values.
    """
    default_formatted_url = 'https://us-south.compliance.cloud.ibm.com/instances/instance_id/v3'
    assert SecurityAndComplianceCenterApiV3.construct_service_url() == default_formatted_url


##############################################################################
# Start of Service: Settings
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
        url = preprocess_url('/settings')
        mock_response = '{"event_notifications": {"instance_crn": "crn:v1:staging:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::", "updated_on": "2019-01-01T12:00:00.000Z", "source_id": "crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::", "source_description": "This source is used for integration with IBM Cloud Security and Compliance Center.", "source_name": "compliance"}, "object_storage": {"instance_crn": "instance_crn", "bucket": "bucket", "bucket_location": "bucket_location", "bucket_endpoint": "bucket_endpoint", "updated_on": "2019-01-01T12:00:00.000Z"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_correlation_id = '1a2b3c4d-5e6f-4a7b-8c9d-e0f1a2b3c4d5'
        x_request_id = 'testString'

        # Invoke method
        response = _service.get_settings(
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
    def test_get_settings_required_params(self):
        """
        test_get_settings_required_params()
        """
        # Set up mock
        url = preprocess_url('/settings')
        mock_response = '{"event_notifications": {"instance_crn": "crn:v1:staging:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::", "updated_on": "2019-01-01T12:00:00.000Z", "source_id": "crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::", "source_description": "This source is used for integration with IBM Cloud Security and Compliance Center.", "source_name": "compliance"}, "object_storage": {"instance_crn": "instance_crn", "bucket": "bucket", "bucket_location": "bucket_location", "bucket_endpoint": "bucket_endpoint", "updated_on": "2019-01-01T12:00:00.000Z"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_settings()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_settings_required_params_with_retries(self):
        # Enable retries and run test_get_settings_required_params.
        _service.enable_retries()
        self.test_get_settings_required_params()

        # Disable retries and run test_get_settings_required_params.
        _service.disable_retries()
        self.test_get_settings_required_params()


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
        url = preprocess_url('/settings')
        mock_response = '{"event_notifications": {"instance_crn": "crn:v1:staging:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::", "updated_on": "2019-01-01T12:00:00.000Z", "source_id": "crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::", "source_description": "This source is used for integration with IBM Cloud Security and Compliance Center.", "source_name": "compliance"}, "object_storage": {"instance_crn": "instance_crn", "bucket": "bucket", "bucket_location": "bucket_location", "bucket_endpoint": "bucket_endpoint", "updated_on": "2019-01-01T12:00:00.000Z"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a EventNotifications model
        event_notifications_model = {}
        event_notifications_model['instance_crn'] = 'crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::'
        event_notifications_model['updated_on'] = '2019-01-01T12:00:00Z'
        event_notifications_model['source_id'] = 'crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::'
        event_notifications_model['source_description'] = 'This source is used for integration with IBM Cloud Security and Compliance Center.'
        event_notifications_model['source_name'] = 'compliance'

        # Construct a dict representation of a ObjectStorage model
        object_storage_model = {}
        object_storage_model['instance_crn'] = 'crn:v1:staging:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::'
        object_storage_model['bucket'] = 'px-scan-results'
        object_storage_model['bucket_location'] = 'us-south'
        object_storage_model['bucket_endpoint'] = 'testString'
        object_storage_model['updated_on'] = '2019-01-01T12:00:00Z'

        # Set up parameter values
        event_notifications = event_notifications_model
        object_storage = object_storage_model
        x_correlation_id = '1a2b3c4d-5e6f-4a7b-8c9d-e0f1a2b3c4d5'
        x_request_id = 'testString'

        # Invoke method
        response = _service.update_settings(
            event_notifications=event_notifications,
            object_storage=object_storage,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['event_notifications'] == event_notifications_model
        assert req_body['object_storage'] == object_storage_model

    def test_update_settings_all_params_with_retries(self):
        # Enable retries and run test_update_settings_all_params.
        _service.enable_retries()
        self.test_update_settings_all_params()

        # Disable retries and run test_update_settings_all_params.
        _service.disable_retries()
        self.test_update_settings_all_params()

    @responses.activate
    def test_update_settings_required_params(self):
        """
        test_update_settings_required_params()
        """
        # Set up mock
        url = preprocess_url('/settings')
        mock_response = '{"event_notifications": {"instance_crn": "crn:v1:staging:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::", "updated_on": "2019-01-01T12:00:00.000Z", "source_id": "crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::", "source_description": "This source is used for integration with IBM Cloud Security and Compliance Center.", "source_name": "compliance"}, "object_storage": {"instance_crn": "instance_crn", "bucket": "bucket", "bucket_location": "bucket_location", "bucket_endpoint": "bucket_endpoint", "updated_on": "2019-01-01T12:00:00.000Z"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a EventNotifications model
        event_notifications_model = {}
        event_notifications_model['instance_crn'] = 'crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::'
        event_notifications_model['updated_on'] = '2019-01-01T12:00:00Z'
        event_notifications_model['source_id'] = 'crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::'
        event_notifications_model['source_description'] = 'This source is used for integration with IBM Cloud Security and Compliance Center.'
        event_notifications_model['source_name'] = 'compliance'

        # Construct a dict representation of a ObjectStorage model
        object_storage_model = {}
        object_storage_model['instance_crn'] = 'crn:v1:staging:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::'
        object_storage_model['bucket'] = 'px-scan-results'
        object_storage_model['bucket_location'] = 'us-south'
        object_storage_model['bucket_endpoint'] = 'testString'
        object_storage_model['updated_on'] = '2019-01-01T12:00:00Z'

        # Set up parameter values
        event_notifications = event_notifications_model
        object_storage = object_storage_model

        # Invoke method
        response = _service.update_settings(
            event_notifications=event_notifications,
            object_storage=object_storage,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['event_notifications'] == event_notifications_model
        assert req_body['object_storage'] == object_storage_model

    def test_update_settings_required_params_with_retries(self):
        # Enable retries and run test_update_settings_required_params.
        _service.enable_retries()
        self.test_update_settings_required_params()

        # Disable retries and run test_update_settings_required_params.
        _service.disable_retries()
        self.test_update_settings_required_params()


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
        url = preprocess_url('/test_event')
        mock_response = '{"success": false}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        x_correlation_id = '1a2b3c4d-5e6f-4a7b-8c9d-e0f1a2b3c4d5'
        x_request_id = 'testString'

        # Invoke method
        response = _service.post_test_event(
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
    def test_post_test_event_required_params(self):
        """
        test_post_test_event_required_params()
        """
        # Set up mock
        url = preprocess_url('/test_event')
        mock_response = '{"success": false}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Invoke method
        response = _service.post_test_event()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_post_test_event_required_params_with_retries(self):
        # Enable retries and run test_post_test_event_required_params.
        _service.enable_retries()
        self.test_post_test_event_required_params()

        # Disable retries and run test_post_test_event_required_params.
        _service.disable_retries()
        self.test_post_test_event_required_params()


# endregion
##############################################################################
# End of Service: Settings
##############################################################################

##############################################################################
# Start of Service: ControlLibraries
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
        url = preprocess_url('/control_libraries')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "control_libraries": [{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "control_library_type", "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_correlation_id = 'testString'
        x_request_id = 'testString'
        limit = 50
        control_library_type = 'custom'
        start = 'testString'

        # Invoke method
        response = _service.list_control_libraries(
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            limit=limit,
            control_library_type=control_library_type,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'control_library_type={}'.format(control_library_type) in query_string
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
        url = preprocess_url('/control_libraries')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "control_libraries": [{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "control_library_type", "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_control_libraries()

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
    def test_list_control_libraries_with_pager_get_next(self):
        """
        test_list_control_libraries_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/control_libraries')
        mock_response1 = '{"next":{"start":"1"},"control_libraries":[{"id":"id","account_id":"account_id","control_library_name":"control_library_name","control_library_description":"control_library_description","control_library_type":"control_library_type","created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","version_group_label":"version_group_label","control_library_version":"control_library_version","latest":true,"controls_count":14}],"total_count":2,"limit":1}'
        mock_response2 = '{"control_libraries":[{"id":"id","account_id":"account_id","control_library_name":"control_library_name","control_library_description":"control_library_description","control_library_type":"control_library_type","created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","version_group_label":"version_group_label","control_library_version":"control_library_version","latest":true,"controls_count":14}],"total_count":2,"limit":1}'
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
            x_correlation_id='testString',
            x_request_id='testString',
            limit=50,
            control_library_type='custom',
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
        url = preprocess_url('/control_libraries')
        mock_response1 = '{"next":{"start":"1"},"control_libraries":[{"id":"id","account_id":"account_id","control_library_name":"control_library_name","control_library_description":"control_library_description","control_library_type":"control_library_type","created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","version_group_label":"version_group_label","control_library_version":"control_library_version","latest":true,"controls_count":14}],"total_count":2,"limit":1}'
        mock_response2 = '{"control_libraries":[{"id":"id","account_id":"account_id","control_library_name":"control_library_name","control_library_description":"control_library_description","control_library_type":"control_library_type","created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","version_group_label":"version_group_label","control_library_version":"control_library_version","latest":true,"controls_count":14}],"total_count":2,"limit":1}'
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
            x_correlation_id='testString',
            x_request_id='testString',
            limit=50,
            control_library_type='custom',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateCustomControlLibrary:
    """
    Test Class for create_custom_control_library
    """

    @responses.activate
    def test_create_custom_control_library_all_params(self):
        """
        create_custom_control_library()
        """
        # Set up mock
        url = preprocess_url('/control_libraries')
        mock_response = '{"id": "f3517159-889e-4781-819a-89d89b747c85", "account_id": "130003ea8bfa43c5aacea07a86da3000", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "control_library_version": "control_library_version", "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "latest": true, "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21, "controls": [{"control_name": "control_name", "control_id": "1fa45e17-9322-4e6c-bbd6-1c51db08e790", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_tags": ["control_tags"], "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_requirement": false, "status": "enabled"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'session_invalidation_in_seconds'
        parameter_info_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        parameter_info_model['parameter_type'] = 'numeric'
        parameter_info_model['parameter_value'] = 'public'

        # Construct a dict representation of a Implementation model
        implementation_model = {}
        implementation_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        implementation_model['assessment_method'] = 'ibm-cloud-rule'
        implementation_model['assessment_type'] = 'automated'
        implementation_model['assessment_description'] = 'Check that there is an Activity Tracker event route defined to collect global events generated by IBM Cloud services'
        implementation_model['parameter_count'] = 38
        implementation_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {}
        control_specifications_model['control_specification_id'] = '5c7d6f88-a92f-4734-9b49-bd22b0900184'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'iam-identity'
        control_specifications_model['componenet_name'] = 'testString'
        control_specifications_model['environment'] = 'ibm-cloud'
        control_specifications_model['control_specification_description'] = 'IBM cloud'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_model]

        # Construct a dict representation of a ControlDocs model
        control_docs_model = {}
        control_docs_model['control_docs_id'] = 'sc-7'
        control_docs_model['control_docs_type'] = 'ibm-cloud'

        # Construct a dict representation of a ControlsInControlLib model
        controls_in_control_lib_model = {}
        controls_in_control_lib_model['control_name'] = 'SC-7'
        controls_in_control_lib_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'
        controls_in_control_lib_model['control_description'] = 'Boundary Protection'
        controls_in_control_lib_model['control_category'] = 'System and Communications Protection'
        controls_in_control_lib_model['control_parent'] = 'testString'
        controls_in_control_lib_model['control_tags'] = ['1fa45e17-9322-4e6c-bbd6-1c51db08e790']
        controls_in_control_lib_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_model['control_docs'] = control_docs_model
        controls_in_control_lib_model['control_requirement'] = True
        controls_in_control_lib_model['status'] = 'enabled'

        # Set up parameter values
        control_library_name = 'IBM Cloud for Financial Services'
        control_library_description = 'IBM Cloud for Financial Services'
        control_library_type = 'custom'
        controls = [controls_in_control_lib_model]
        version_group_label = '33fc7b80-0fa5-4f16-bbba-1f293f660f0d'
        control_library_version = '1.0.0'
        latest = True
        controls_count = 38
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.create_custom_control_library(
            control_library_name,
            control_library_description,
            control_library_type,
            controls,
            version_group_label=version_group_label,
            control_library_version=control_library_version,
            latest=latest,
            controls_count=controls_count,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['control_library_name'] == 'IBM Cloud for Financial Services'
        assert req_body['control_library_description'] == 'IBM Cloud for Financial Services'
        assert req_body['control_library_type'] == 'custom'
        assert req_body['controls'] == [controls_in_control_lib_model]
        assert req_body['version_group_label'] == '33fc7b80-0fa5-4f16-bbba-1f293f660f0d'
        assert req_body['control_library_version'] == '1.0.0'
        assert req_body['latest'] == True
        assert req_body['controls_count'] == 38

    def test_create_custom_control_library_all_params_with_retries(self):
        # Enable retries and run test_create_custom_control_library_all_params.
        _service.enable_retries()
        self.test_create_custom_control_library_all_params()

        # Disable retries and run test_create_custom_control_library_all_params.
        _service.disable_retries()
        self.test_create_custom_control_library_all_params()

    @responses.activate
    def test_create_custom_control_library_required_params(self):
        """
        test_create_custom_control_library_required_params()
        """
        # Set up mock
        url = preprocess_url('/control_libraries')
        mock_response = '{"id": "f3517159-889e-4781-819a-89d89b747c85", "account_id": "130003ea8bfa43c5aacea07a86da3000", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "control_library_version": "control_library_version", "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "latest": true, "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21, "controls": [{"control_name": "control_name", "control_id": "1fa45e17-9322-4e6c-bbd6-1c51db08e790", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_tags": ["control_tags"], "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_requirement": false, "status": "enabled"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'session_invalidation_in_seconds'
        parameter_info_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        parameter_info_model['parameter_type'] = 'numeric'
        parameter_info_model['parameter_value'] = 'public'

        # Construct a dict representation of a Implementation model
        implementation_model = {}
        implementation_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        implementation_model['assessment_method'] = 'ibm-cloud-rule'
        implementation_model['assessment_type'] = 'automated'
        implementation_model['assessment_description'] = 'Check that there is an Activity Tracker event route defined to collect global events generated by IBM Cloud services'
        implementation_model['parameter_count'] = 38
        implementation_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {}
        control_specifications_model['control_specification_id'] = '5c7d6f88-a92f-4734-9b49-bd22b0900184'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'iam-identity'
        control_specifications_model['componenet_name'] = 'testString'
        control_specifications_model['environment'] = 'ibm-cloud'
        control_specifications_model['control_specification_description'] = 'IBM cloud'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_model]

        # Construct a dict representation of a ControlDocs model
        control_docs_model = {}
        control_docs_model['control_docs_id'] = 'sc-7'
        control_docs_model['control_docs_type'] = 'ibm-cloud'

        # Construct a dict representation of a ControlsInControlLib model
        controls_in_control_lib_model = {}
        controls_in_control_lib_model['control_name'] = 'SC-7'
        controls_in_control_lib_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'
        controls_in_control_lib_model['control_description'] = 'Boundary Protection'
        controls_in_control_lib_model['control_category'] = 'System and Communications Protection'
        controls_in_control_lib_model['control_parent'] = 'testString'
        controls_in_control_lib_model['control_tags'] = ['1fa45e17-9322-4e6c-bbd6-1c51db08e790']
        controls_in_control_lib_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_model['control_docs'] = control_docs_model
        controls_in_control_lib_model['control_requirement'] = True
        controls_in_control_lib_model['status'] = 'enabled'

        # Set up parameter values
        control_library_name = 'IBM Cloud for Financial Services'
        control_library_description = 'IBM Cloud for Financial Services'
        control_library_type = 'custom'
        controls = [controls_in_control_lib_model]
        version_group_label = '33fc7b80-0fa5-4f16-bbba-1f293f660f0d'
        control_library_version = '1.0.0'
        latest = True
        controls_count = 38

        # Invoke method
        response = _service.create_custom_control_library(
            control_library_name,
            control_library_description,
            control_library_type,
            controls,
            version_group_label=version_group_label,
            control_library_version=control_library_version,
            latest=latest,
            controls_count=controls_count,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['control_library_name'] == 'IBM Cloud for Financial Services'
        assert req_body['control_library_description'] == 'IBM Cloud for Financial Services'
        assert req_body['control_library_type'] == 'custom'
        assert req_body['controls'] == [controls_in_control_lib_model]
        assert req_body['version_group_label'] == '33fc7b80-0fa5-4f16-bbba-1f293f660f0d'
        assert req_body['control_library_version'] == '1.0.0'
        assert req_body['latest'] == True
        assert req_body['controls_count'] == 38

    def test_create_custom_control_library_required_params_with_retries(self):
        # Enable retries and run test_create_custom_control_library_required_params.
        _service.enable_retries()
        self.test_create_custom_control_library_required_params()

        # Disable retries and run test_create_custom_control_library_required_params.
        _service.disable_retries()
        self.test_create_custom_control_library_required_params()

    @responses.activate
    def test_create_custom_control_library_value_error(self):
        """
        test_create_custom_control_library_value_error()
        """
        # Set up mock
        url = preprocess_url('/control_libraries')
        mock_response = '{"id": "f3517159-889e-4781-819a-89d89b747c85", "account_id": "130003ea8bfa43c5aacea07a86da3000", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "control_library_version": "control_library_version", "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "latest": true, "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21, "controls": [{"control_name": "control_name", "control_id": "1fa45e17-9322-4e6c-bbd6-1c51db08e790", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_tags": ["control_tags"], "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_requirement": false, "status": "enabled"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'session_invalidation_in_seconds'
        parameter_info_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        parameter_info_model['parameter_type'] = 'numeric'
        parameter_info_model['parameter_value'] = 'public'

        # Construct a dict representation of a Implementation model
        implementation_model = {}
        implementation_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        implementation_model['assessment_method'] = 'ibm-cloud-rule'
        implementation_model['assessment_type'] = 'automated'
        implementation_model['assessment_description'] = 'Check that there is an Activity Tracker event route defined to collect global events generated by IBM Cloud services'
        implementation_model['parameter_count'] = 38
        implementation_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {}
        control_specifications_model['control_specification_id'] = '5c7d6f88-a92f-4734-9b49-bd22b0900184'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'iam-identity'
        control_specifications_model['componenet_name'] = 'testString'
        control_specifications_model['environment'] = 'ibm-cloud'
        control_specifications_model['control_specification_description'] = 'IBM cloud'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_model]

        # Construct a dict representation of a ControlDocs model
        control_docs_model = {}
        control_docs_model['control_docs_id'] = 'sc-7'
        control_docs_model['control_docs_type'] = 'ibm-cloud'

        # Construct a dict representation of a ControlsInControlLib model
        controls_in_control_lib_model = {}
        controls_in_control_lib_model['control_name'] = 'SC-7'
        controls_in_control_lib_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'
        controls_in_control_lib_model['control_description'] = 'Boundary Protection'
        controls_in_control_lib_model['control_category'] = 'System and Communications Protection'
        controls_in_control_lib_model['control_parent'] = 'testString'
        controls_in_control_lib_model['control_tags'] = ['1fa45e17-9322-4e6c-bbd6-1c51db08e790']
        controls_in_control_lib_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_model['control_docs'] = control_docs_model
        controls_in_control_lib_model['control_requirement'] = True
        controls_in_control_lib_model['status'] = 'enabled'

        # Set up parameter values
        control_library_name = 'IBM Cloud for Financial Services'
        control_library_description = 'IBM Cloud for Financial Services'
        control_library_type = 'custom'
        controls = [controls_in_control_lib_model]
        version_group_label = '33fc7b80-0fa5-4f16-bbba-1f293f660f0d'
        control_library_version = '1.0.0'
        latest = True
        controls_count = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "control_library_name": control_library_name,
            "control_library_description": control_library_description,
            "control_library_type": control_library_type,
            "controls": controls,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_custom_control_library(**req_copy)

    def test_create_custom_control_library_value_error_with_retries(self):
        # Enable retries and run test_create_custom_control_library_value_error.
        _service.enable_retries()
        self.test_create_custom_control_library_value_error()

        # Disable retries and run test_create_custom_control_library_value_error.
        _service.disable_retries()
        self.test_create_custom_control_library_value_error()


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
        url = preprocess_url('/control_libraries/testString')
        mock_response = '{"deleted": "deleted"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        control_libraries_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.delete_custom_control_library(
            control_libraries_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

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
        url = preprocess_url('/control_libraries/testString')
        mock_response = '{"deleted": "deleted"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        control_libraries_id = 'testString'

        # Invoke method
        response = _service.delete_custom_control_library(
            control_libraries_id,
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
        url = preprocess_url('/control_libraries/testString')
        mock_response = '{"deleted": "deleted"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        control_libraries_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "control_libraries_id": control_libraries_id,
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
        url = preprocess_url('/control_libraries/testString')
        mock_response = '{"id": "f3517159-889e-4781-819a-89d89b747c85", "account_id": "130003ea8bfa43c5aacea07a86da3000", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "control_library_version": "control_library_version", "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "latest": true, "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21, "controls": [{"control_name": "control_name", "control_id": "1fa45e17-9322-4e6c-bbd6-1c51db08e790", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_tags": ["control_tags"], "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_requirement": false, "status": "enabled"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        control_libraries_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.get_control_library(
            control_libraries_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

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
        url = preprocess_url('/control_libraries/testString')
        mock_response = '{"id": "f3517159-889e-4781-819a-89d89b747c85", "account_id": "130003ea8bfa43c5aacea07a86da3000", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "control_library_version": "control_library_version", "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "latest": true, "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21, "controls": [{"control_name": "control_name", "control_id": "1fa45e17-9322-4e6c-bbd6-1c51db08e790", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_tags": ["control_tags"], "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_requirement": false, "status": "enabled"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        control_libraries_id = 'testString'

        # Invoke method
        response = _service.get_control_library(
            control_libraries_id,
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
        url = preprocess_url('/control_libraries/testString')
        mock_response = '{"id": "f3517159-889e-4781-819a-89d89b747c85", "account_id": "130003ea8bfa43c5aacea07a86da3000", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "control_library_version": "control_library_version", "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "latest": true, "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21, "controls": [{"control_name": "control_name", "control_id": "1fa45e17-9322-4e6c-bbd6-1c51db08e790", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_tags": ["control_tags"], "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_requirement": false, "status": "enabled"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        control_libraries_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "control_libraries_id": control_libraries_id,
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
        url = preprocess_url('/control_libraries/testString')
        mock_response = '{"id": "f3517159-889e-4781-819a-89d89b747c85", "account_id": "130003ea8bfa43c5aacea07a86da3000", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "control_library_version": "control_library_version", "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "latest": true, "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21, "controls": [{"control_name": "control_name", "control_id": "1fa45e17-9322-4e6c-bbd6-1c51db08e790", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_tags": ["control_tags"], "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_requirement": false, "status": "enabled"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'session_invalidation_in_seconds'
        parameter_info_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        parameter_info_model['parameter_type'] = 'numeric'
        parameter_info_model['parameter_value'] = 'public'

        # Construct a dict representation of a Implementation model
        implementation_model = {}
        implementation_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        implementation_model['assessment_method'] = 'ibm-cloud-rule'
        implementation_model['assessment_type'] = 'automated'
        implementation_model['assessment_description'] = 'Check that there is an Activity Tracker event route defined to collect global events generated by IBM Cloud services'
        implementation_model['parameter_count'] = 38
        implementation_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {}
        control_specifications_model['control_specification_id'] = '5c7d6f88-a92f-4734-9b49-bd22b0900184'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'iam-identity'
        control_specifications_model['componenet_name'] = 'testString'
        control_specifications_model['environment'] = 'ibm-cloud'
        control_specifications_model['control_specification_description'] = 'IBM cloud'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_model]

        # Construct a dict representation of a ControlDocs model
        control_docs_model = {}
        control_docs_model['control_docs_id'] = 'sc-7'
        control_docs_model['control_docs_type'] = 'ibm-cloud'

        # Construct a dict representation of a ControlsInControlLib model
        controls_in_control_lib_model = {}
        controls_in_control_lib_model['control_name'] = 'SC-7'
        controls_in_control_lib_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'
        controls_in_control_lib_model['control_description'] = 'Boundary Protection'
        controls_in_control_lib_model['control_category'] = 'System and Communications Protection'
        controls_in_control_lib_model['control_parent'] = 'testString'
        controls_in_control_lib_model['control_tags'] = ['1fa45e17-9322-4e6c-bbd6-1c51db08e790']
        controls_in_control_lib_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_model['control_docs'] = control_docs_model
        controls_in_control_lib_model['control_requirement'] = True
        controls_in_control_lib_model['status'] = 'enabled'

        # Set up parameter values
        control_libraries_id = 'testString'
        id = 'testString'
        account_id = 'testString'
        control_library_name = 'IBM Cloud for Financial Services'
        control_library_description = 'IBM Cloud for Financial Services'
        control_library_type = 'custom'
        version_group_label = 'testString'
        control_library_version = '1.1.0'
        created_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        created_by = 'testString'
        updated_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        updated_by = 'testString'
        latest = True
        hierarchy_enabled = True
        controls_count = 38
        control_parents_count = 38
        controls = [controls_in_control_lib_model]
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.replace_custom_control_library(
            control_libraries_id,
            id=id,
            account_id=account_id,
            control_library_name=control_library_name,
            control_library_description=control_library_description,
            control_library_type=control_library_type,
            version_group_label=version_group_label,
            control_library_version=control_library_version,
            created_on=created_on,
            created_by=created_by,
            updated_on=updated_on,
            updated_by=updated_by,
            latest=latest,
            hierarchy_enabled=hierarchy_enabled,
            controls_count=controls_count,
            control_parents_count=control_parents_count,
            controls=controls,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['control_library_name'] == 'IBM Cloud for Financial Services'
        assert req_body['control_library_description'] == 'IBM Cloud for Financial Services'
        assert req_body['control_library_type'] == 'custom'
        assert req_body['version_group_label'] == 'testString'
        assert req_body['control_library_version'] == '1.1.0'
        assert req_body['created_on'] == '2019-01-01T12:00:00Z'
        assert req_body['created_by'] == 'testString'
        assert req_body['updated_on'] == '2019-01-01T12:00:00Z'
        assert req_body['updated_by'] == 'testString'
        assert req_body['latest'] == True
        assert req_body['hierarchy_enabled'] == True
        assert req_body['controls_count'] == 38
        assert req_body['control_parents_count'] == 38
        assert req_body['controls'] == [controls_in_control_lib_model]

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
        url = preprocess_url('/control_libraries/testString')
        mock_response = '{"id": "f3517159-889e-4781-819a-89d89b747c85", "account_id": "130003ea8bfa43c5aacea07a86da3000", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "control_library_version": "control_library_version", "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "latest": true, "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21, "controls": [{"control_name": "control_name", "control_id": "1fa45e17-9322-4e6c-bbd6-1c51db08e790", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_tags": ["control_tags"], "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_requirement": false, "status": "enabled"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'session_invalidation_in_seconds'
        parameter_info_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        parameter_info_model['parameter_type'] = 'numeric'
        parameter_info_model['parameter_value'] = 'public'

        # Construct a dict representation of a Implementation model
        implementation_model = {}
        implementation_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        implementation_model['assessment_method'] = 'ibm-cloud-rule'
        implementation_model['assessment_type'] = 'automated'
        implementation_model['assessment_description'] = 'Check that there is an Activity Tracker event route defined to collect global events generated by IBM Cloud services'
        implementation_model['parameter_count'] = 38
        implementation_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {}
        control_specifications_model['control_specification_id'] = '5c7d6f88-a92f-4734-9b49-bd22b0900184'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'iam-identity'
        control_specifications_model['componenet_name'] = 'testString'
        control_specifications_model['environment'] = 'ibm-cloud'
        control_specifications_model['control_specification_description'] = 'IBM cloud'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_model]

        # Construct a dict representation of a ControlDocs model
        control_docs_model = {}
        control_docs_model['control_docs_id'] = 'sc-7'
        control_docs_model['control_docs_type'] = 'ibm-cloud'

        # Construct a dict representation of a ControlsInControlLib model
        controls_in_control_lib_model = {}
        controls_in_control_lib_model['control_name'] = 'SC-7'
        controls_in_control_lib_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'
        controls_in_control_lib_model['control_description'] = 'Boundary Protection'
        controls_in_control_lib_model['control_category'] = 'System and Communications Protection'
        controls_in_control_lib_model['control_parent'] = 'testString'
        controls_in_control_lib_model['control_tags'] = ['1fa45e17-9322-4e6c-bbd6-1c51db08e790']
        controls_in_control_lib_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_model['control_docs'] = control_docs_model
        controls_in_control_lib_model['control_requirement'] = True
        controls_in_control_lib_model['status'] = 'enabled'

        # Set up parameter values
        control_libraries_id = 'testString'
        id = 'testString'
        account_id = 'testString'
        control_library_name = 'IBM Cloud for Financial Services'
        control_library_description = 'IBM Cloud for Financial Services'
        control_library_type = 'custom'
        version_group_label = 'testString'
        control_library_version = '1.1.0'
        created_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        created_by = 'testString'
        updated_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        updated_by = 'testString'
        latest = True
        hierarchy_enabled = True
        controls_count = 38
        control_parents_count = 38
        controls = [controls_in_control_lib_model]

        # Invoke method
        response = _service.replace_custom_control_library(
            control_libraries_id,
            id=id,
            account_id=account_id,
            control_library_name=control_library_name,
            control_library_description=control_library_description,
            control_library_type=control_library_type,
            version_group_label=version_group_label,
            control_library_version=control_library_version,
            created_on=created_on,
            created_by=created_by,
            updated_on=updated_on,
            updated_by=updated_by,
            latest=latest,
            hierarchy_enabled=hierarchy_enabled,
            controls_count=controls_count,
            control_parents_count=control_parents_count,
            controls=controls,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['control_library_name'] == 'IBM Cloud for Financial Services'
        assert req_body['control_library_description'] == 'IBM Cloud for Financial Services'
        assert req_body['control_library_type'] == 'custom'
        assert req_body['version_group_label'] == 'testString'
        assert req_body['control_library_version'] == '1.1.0'
        assert req_body['created_on'] == '2019-01-01T12:00:00Z'
        assert req_body['created_by'] == 'testString'
        assert req_body['updated_on'] == '2019-01-01T12:00:00Z'
        assert req_body['updated_by'] == 'testString'
        assert req_body['latest'] == True
        assert req_body['hierarchy_enabled'] == True
        assert req_body['controls_count'] == 38
        assert req_body['control_parents_count'] == 38
        assert req_body['controls'] == [controls_in_control_lib_model]

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
        url = preprocess_url('/control_libraries/testString')
        mock_response = '{"id": "f3517159-889e-4781-819a-89d89b747c85", "account_id": "130003ea8bfa43c5aacea07a86da3000", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "control_library_version": "control_library_version", "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "latest": true, "hierarchy_enabled": false, "controls_count": 14, "control_parents_count": 21, "controls": [{"control_name": "control_name", "control_id": "1fa45e17-9322-4e6c-bbd6-1c51db08e790", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_tags": ["control_tags"], "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_requirement": false, "status": "enabled"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'session_invalidation_in_seconds'
        parameter_info_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        parameter_info_model['parameter_type'] = 'numeric'
        parameter_info_model['parameter_value'] = 'public'

        # Construct a dict representation of a Implementation model
        implementation_model = {}
        implementation_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        implementation_model['assessment_method'] = 'ibm-cloud-rule'
        implementation_model['assessment_type'] = 'automated'
        implementation_model['assessment_description'] = 'Check that there is an Activity Tracker event route defined to collect global events generated by IBM Cloud services'
        implementation_model['parameter_count'] = 38
        implementation_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {}
        control_specifications_model['control_specification_id'] = '5c7d6f88-a92f-4734-9b49-bd22b0900184'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'iam-identity'
        control_specifications_model['componenet_name'] = 'testString'
        control_specifications_model['environment'] = 'ibm-cloud'
        control_specifications_model['control_specification_description'] = 'IBM cloud'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_model]

        # Construct a dict representation of a ControlDocs model
        control_docs_model = {}
        control_docs_model['control_docs_id'] = 'sc-7'
        control_docs_model['control_docs_type'] = 'ibm-cloud'

        # Construct a dict representation of a ControlsInControlLib model
        controls_in_control_lib_model = {}
        controls_in_control_lib_model['control_name'] = 'SC-7'
        controls_in_control_lib_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'
        controls_in_control_lib_model['control_description'] = 'Boundary Protection'
        controls_in_control_lib_model['control_category'] = 'System and Communications Protection'
        controls_in_control_lib_model['control_parent'] = 'testString'
        controls_in_control_lib_model['control_tags'] = ['1fa45e17-9322-4e6c-bbd6-1c51db08e790']
        controls_in_control_lib_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_model['control_docs'] = control_docs_model
        controls_in_control_lib_model['control_requirement'] = True
        controls_in_control_lib_model['status'] = 'enabled'

        # Set up parameter values
        control_libraries_id = 'testString'
        id = 'testString'
        account_id = 'testString'
        control_library_name = 'IBM Cloud for Financial Services'
        control_library_description = 'IBM Cloud for Financial Services'
        control_library_type = 'custom'
        version_group_label = 'testString'
        control_library_version = '1.1.0'
        created_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        created_by = 'testString'
        updated_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        updated_by = 'testString'
        latest = True
        hierarchy_enabled = True
        controls_count = 38
        control_parents_count = 38
        controls = [controls_in_control_lib_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "control_libraries_id": control_libraries_id,
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


# endregion
##############################################################################
# End of Service: ControlLibraries
##############################################################################

##############################################################################
# Start of Service: Profiles
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
        url = preprocess_url('/profiles')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "profiles": [{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_correlation_id = 'testString'
        x_request_id = 'testString'
        limit = 50
        profile_type = 'custom'
        start = 'testString'

        # Invoke method
        response = _service.list_profiles(
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            limit=limit,
            profile_type=profile_type,
            start=start,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'profile_type={}'.format(profile_type) in query_string
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
        url = preprocess_url('/profiles')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "profiles": [{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "attachments_count": 17}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_profiles()

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
    def test_list_profiles_with_pager_get_next(self):
        """
        test_list_profiles_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/profiles')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"profiles":[{"id":"id","profile_name":"profile_name","profile_description":"profile_description","profile_type":"profile_type","profile_version":"profile_version","version_group_label":"version_group_label","latest":true,"created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","controls_count":14,"attachments_count":17}]}'
        mock_response2 = '{"total_count":2,"limit":1,"profiles":[{"id":"id","profile_name":"profile_name","profile_description":"profile_description","profile_type":"profile_type","profile_version":"profile_version","version_group_label":"version_group_label","latest":true,"created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","controls_count":14,"attachments_count":17}]}'
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
            x_correlation_id='testString',
            x_request_id='testString',
            limit=10,
            profile_type='custom',
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
        url = preprocess_url('/profiles')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"profiles":[{"id":"id","profile_name":"profile_name","profile_description":"profile_description","profile_type":"profile_type","profile_version":"profile_version","version_group_label":"version_group_label","latest":true,"created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","controls_count":14,"attachments_count":17}]}'
        mock_response2 = '{"total_count":2,"limit":1,"profiles":[{"id":"id","profile_name":"profile_name","profile_description":"profile_description","profile_type":"profile_type","profile_version":"profile_version","version_group_label":"version_group_label","latest":true,"created_by":"created_by","created_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","updated_on":"2019-01-01T12:00:00.000Z","controls_count":14,"attachments_count":17}]}'
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
            x_correlation_id='testString',
            x_request_id='testString',
            limit=10,
            profile_type='custom',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


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
        url = preprocess_url('/profiles')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "predefined", "profile_version": "profile_version", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "instance_id": "instance_id", "latest": true, "hierarchy_enabled": false, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "control_parents_count": 21, "attachments_count": 17, "controls": [{"control_library_id": "e98a56ff-dc24-41d4-9875-1e188e2da6cd", "control_id": "5C453578-E9A1-421E-AD0F-C6AFCDD67CCF", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_requirement": false, "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications_count": 28, "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProfileControlsPrototype model
        profile_controls_prototype_model = {}
        profile_controls_prototype_model['control_library_id'] = 'e98a56ff-dc24-41d4-9875-1e188e2da6cd'
        profile_controls_prototype_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'

        # Construct a dict representation of a DefaultParametersPrototype model
        default_parameters_prototype_model = {}
        default_parameters_prototype_model['assessment_type'] = 'Automated'
        default_parameters_prototype_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        default_parameters_prototype_model['parameter_name'] = 'session_invalidation_in_seconds'
        default_parameters_prototype_model['parameter_default_value'] = '120'
        default_parameters_prototype_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        default_parameters_prototype_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profile_name = 'test_profile1'
        profile_description = 'test_description1'
        profile_type = 'custom'
        controls = [profile_controls_prototype_model]
        default_parameters = [default_parameters_prototype_model]
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.create_profile(
            profile_name,
            profile_description,
            profile_type,
            controls,
            default_parameters,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['profile_name'] == 'test_profile1'
        assert req_body['profile_description'] == 'test_description1'
        assert req_body['profile_type'] == 'custom'
        assert req_body['controls'] == [profile_controls_prototype_model]
        assert req_body['default_parameters'] == [default_parameters_prototype_model]

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
        url = preprocess_url('/profiles')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "predefined", "profile_version": "profile_version", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "instance_id": "instance_id", "latest": true, "hierarchy_enabled": false, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "control_parents_count": 21, "attachments_count": 17, "controls": [{"control_library_id": "e98a56ff-dc24-41d4-9875-1e188e2da6cd", "control_id": "5C453578-E9A1-421E-AD0F-C6AFCDD67CCF", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_requirement": false, "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications_count": 28, "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProfileControlsPrototype model
        profile_controls_prototype_model = {}
        profile_controls_prototype_model['control_library_id'] = 'e98a56ff-dc24-41d4-9875-1e188e2da6cd'
        profile_controls_prototype_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'

        # Construct a dict representation of a DefaultParametersPrototype model
        default_parameters_prototype_model = {}
        default_parameters_prototype_model['assessment_type'] = 'Automated'
        default_parameters_prototype_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        default_parameters_prototype_model['parameter_name'] = 'session_invalidation_in_seconds'
        default_parameters_prototype_model['parameter_default_value'] = '120'
        default_parameters_prototype_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        default_parameters_prototype_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profile_name = 'test_profile1'
        profile_description = 'test_description1'
        profile_type = 'custom'
        controls = [profile_controls_prototype_model]
        default_parameters = [default_parameters_prototype_model]

        # Invoke method
        response = _service.create_profile(
            profile_name,
            profile_description,
            profile_type,
            controls,
            default_parameters,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['profile_name'] == 'test_profile1'
        assert req_body['profile_description'] == 'test_description1'
        assert req_body['profile_type'] == 'custom'
        assert req_body['controls'] == [profile_controls_prototype_model]
        assert req_body['default_parameters'] == [default_parameters_prototype_model]

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
        url = preprocess_url('/profiles')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "predefined", "profile_version": "profile_version", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "instance_id": "instance_id", "latest": true, "hierarchy_enabled": false, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "control_parents_count": 21, "attachments_count": 17, "controls": [{"control_library_id": "e98a56ff-dc24-41d4-9875-1e188e2da6cd", "control_id": "5C453578-E9A1-421E-AD0F-C6AFCDD67CCF", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_requirement": false, "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications_count": 28, "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProfileControlsPrototype model
        profile_controls_prototype_model = {}
        profile_controls_prototype_model['control_library_id'] = 'e98a56ff-dc24-41d4-9875-1e188e2da6cd'
        profile_controls_prototype_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'

        # Construct a dict representation of a DefaultParametersPrototype model
        default_parameters_prototype_model = {}
        default_parameters_prototype_model['assessment_type'] = 'Automated'
        default_parameters_prototype_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        default_parameters_prototype_model['parameter_name'] = 'session_invalidation_in_seconds'
        default_parameters_prototype_model['parameter_default_value'] = '120'
        default_parameters_prototype_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        default_parameters_prototype_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profile_name = 'test_profile1'
        profile_description = 'test_description1'
        profile_type = 'custom'
        controls = [profile_controls_prototype_model]
        default_parameters = [default_parameters_prototype_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profile_name": profile_name,
            "profile_description": profile_description,
            "profile_type": profile_type,
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
        url = preprocess_url('/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "predefined", "profile_version": "profile_version", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "instance_id": "instance_id", "latest": true, "hierarchy_enabled": false, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "control_parents_count": 21, "attachments_count": 17, "controls": [{"control_library_id": "e98a56ff-dc24-41d4-9875-1e188e2da6cd", "control_id": "5C453578-E9A1-421E-AD0F-C6AFCDD67CCF", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_requirement": false, "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications_count": 28, "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.delete_custom_profile(
            profiles_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

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
        url = preprocess_url('/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "predefined", "profile_version": "profile_version", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "instance_id": "instance_id", "latest": true, "hierarchy_enabled": false, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "control_parents_count": 21, "attachments_count": 17, "controls": [{"control_library_id": "e98a56ff-dc24-41d4-9875-1e188e2da6cd", "control_id": "5C453578-E9A1-421E-AD0F-C6AFCDD67CCF", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_requirement": false, "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications_count": 28, "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'

        # Invoke method
        response = _service.delete_custom_profile(
            profiles_id,
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
        url = preprocess_url('/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "predefined", "profile_version": "profile_version", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "instance_id": "instance_id", "latest": true, "hierarchy_enabled": false, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "control_parents_count": 21, "attachments_count": 17, "controls": [{"control_library_id": "e98a56ff-dc24-41d4-9875-1e188e2da6cd", "control_id": "5C453578-E9A1-421E-AD0F-C6AFCDD67CCF", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_requirement": false, "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications_count": 28, "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
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
        url = preprocess_url('/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "predefined", "profile_version": "profile_version", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "instance_id": "instance_id", "latest": true, "hierarchy_enabled": false, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "control_parents_count": 21, "attachments_count": 17, "controls": [{"control_library_id": "e98a56ff-dc24-41d4-9875-1e188e2da6cd", "control_id": "5C453578-E9A1-421E-AD0F-C6AFCDD67CCF", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_requirement": false, "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications_count": 28, "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.get_profile(
            profiles_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

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
        url = preprocess_url('/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "predefined", "profile_version": "profile_version", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "instance_id": "instance_id", "latest": true, "hierarchy_enabled": false, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "control_parents_count": 21, "attachments_count": 17, "controls": [{"control_library_id": "e98a56ff-dc24-41d4-9875-1e188e2da6cd", "control_id": "5C453578-E9A1-421E-AD0F-C6AFCDD67CCF", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_requirement": false, "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications_count": 28, "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'

        # Invoke method
        response = _service.get_profile(
            profiles_id,
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
        url = preprocess_url('/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "predefined", "profile_version": "profile_version", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "instance_id": "instance_id", "latest": true, "hierarchy_enabled": false, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "control_parents_count": 21, "attachments_count": 17, "controls": [{"control_library_id": "e98a56ff-dc24-41d4-9875-1e188e2da6cd", "control_id": "5C453578-E9A1-421E-AD0F-C6AFCDD67CCF", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_requirement": false, "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications_count": 28, "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
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
        url = preprocess_url('/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "predefined", "profile_version": "profile_version", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "instance_id": "instance_id", "latest": true, "hierarchy_enabled": false, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "control_parents_count": 21, "attachments_count": 17, "controls": [{"control_library_id": "e98a56ff-dc24-41d4-9875-1e188e2da6cd", "control_id": "5C453578-E9A1-421E-AD0F-C6AFCDD67CCF", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_requirement": false, "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications_count": 28, "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileControlsPrototype model
        profile_controls_prototype_model = {}
        profile_controls_prototype_model['control_library_id'] = 'e98a56ff-dc24-41d4-9875-1e188e2da6cd'
        profile_controls_prototype_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'

        # Construct a dict representation of a DefaultParametersPrototype model
        default_parameters_prototype_model = {}
        default_parameters_prototype_model['assessment_type'] = 'Automated'
        default_parameters_prototype_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        default_parameters_prototype_model['parameter_name'] = 'session_invalidation_in_seconds'
        default_parameters_prototype_model['parameter_default_value'] = '120'
        default_parameters_prototype_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        default_parameters_prototype_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        profile_name = 'test_profile1'
        profile_description = 'test_description1'
        profile_type = 'custom'
        controls = [profile_controls_prototype_model]
        default_parameters = [default_parameters_prototype_model]
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.replace_profile(
            profiles_id,
            profile_name,
            profile_description,
            profile_type,
            controls,
            default_parameters,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['profile_name'] == 'test_profile1'
        assert req_body['profile_description'] == 'test_description1'
        assert req_body['profile_type'] == 'custom'
        assert req_body['controls'] == [profile_controls_prototype_model]
        assert req_body['default_parameters'] == [default_parameters_prototype_model]

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
        url = preprocess_url('/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "predefined", "profile_version": "profile_version", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "instance_id": "instance_id", "latest": true, "hierarchy_enabled": false, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "control_parents_count": 21, "attachments_count": 17, "controls": [{"control_library_id": "e98a56ff-dc24-41d4-9875-1e188e2da6cd", "control_id": "5C453578-E9A1-421E-AD0F-C6AFCDD67CCF", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_requirement": false, "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications_count": 28, "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileControlsPrototype model
        profile_controls_prototype_model = {}
        profile_controls_prototype_model['control_library_id'] = 'e98a56ff-dc24-41d4-9875-1e188e2da6cd'
        profile_controls_prototype_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'

        # Construct a dict representation of a DefaultParametersPrototype model
        default_parameters_prototype_model = {}
        default_parameters_prototype_model['assessment_type'] = 'Automated'
        default_parameters_prototype_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        default_parameters_prototype_model['parameter_name'] = 'session_invalidation_in_seconds'
        default_parameters_prototype_model['parameter_default_value'] = '120'
        default_parameters_prototype_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        default_parameters_prototype_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        profile_name = 'test_profile1'
        profile_description = 'test_description1'
        profile_type = 'custom'
        controls = [profile_controls_prototype_model]
        default_parameters = [default_parameters_prototype_model]

        # Invoke method
        response = _service.replace_profile(
            profiles_id,
            profile_name,
            profile_description,
            profile_type,
            controls,
            default_parameters,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['profile_name'] == 'test_profile1'
        assert req_body['profile_description'] == 'test_description1'
        assert req_body['profile_type'] == 'custom'
        assert req_body['controls'] == [profile_controls_prototype_model]
        assert req_body['default_parameters'] == [default_parameters_prototype_model]

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
        url = preprocess_url('/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "predefined", "profile_version": "profile_version", "version_group_label": "e0923045-f00d-44de-b49b-6f1f0e8033cc", "instance_id": "instance_id", "latest": true, "hierarchy_enabled": false, "created_by": "created_by", "created_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "updated_on": "2019-01-01T12:00:00.000Z", "controls_count": 14, "control_parents_count": 21, "attachments_count": 17, "controls": [{"control_library_id": "e98a56ff-dc24-41d4-9875-1e188e2da6cd", "control_id": "5C453578-E9A1-421E-AD0F-C6AFCDD67CCF", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_requirement": false, "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications_count": 28, "control_specifications": [{"control_specification_id": "f3517159-889e-4781-819a-89d89b747c85", "responsibility": "user", "component_id": "f3517159-889e-4781-819a-89d89b747c85", "componenet_name": "componenet_name", "environment": "environment", "control_specification_description": "control_specification_description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileControlsPrototype model
        profile_controls_prototype_model = {}
        profile_controls_prototype_model['control_library_id'] = 'e98a56ff-dc24-41d4-9875-1e188e2da6cd'
        profile_controls_prototype_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'

        # Construct a dict representation of a DefaultParametersPrototype model
        default_parameters_prototype_model = {}
        default_parameters_prototype_model['assessment_type'] = 'Automated'
        default_parameters_prototype_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        default_parameters_prototype_model['parameter_name'] = 'session_invalidation_in_seconds'
        default_parameters_prototype_model['parameter_default_value'] = '120'
        default_parameters_prototype_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        default_parameters_prototype_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        profile_name = 'test_profile1'
        profile_description = 'test_description1'
        profile_type = 'custom'
        controls = [profile_controls_prototype_model]
        default_parameters = [default_parameters_prototype_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "profile_name": profile_name,
            "profile_description": profile_description,
            "profile_type": profile_type,
            "controls": controls,
            "default_parameters": default_parameters,
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


# endregion
##############################################################################
# End of Service: Profiles
##############################################################################

##############################################################################
# Start of Service: Rules
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
        url = preprocess_url('/rules')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "rules": [{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "value"}]}, "required_config": {"description": "description", "and": [{"description": "description"}]}, "labels": ["labels"]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_correlation_id = 'testString'
        x_request_id = 'testString'
        type = 'system_defined'
        search = 'testString'
        service_name = 'testString'

        # Invoke method
        response = _service.list_rules(
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            type=type,
            search=search,
            service_name=service_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'type={}'.format(type) in query_string
        assert 'search={}'.format(search) in query_string
        assert 'service_name={}'.format(service_name) in query_string

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
        url = preprocess_url('/rules')
        mock_response = '{"limit": 50, "total_count": 230, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "rules": [{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "value"}]}, "required_config": {"description": "description", "and": [{"description": "description"}]}, "labels": ["labels"]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_rules()

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
        url = preprocess_url('/rules')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "value"}]}, "required_config": {"description": "description", "and": [{"description": "description"}]}, "labels": ["labels"]}'
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

        # Construct a dict representation of a Target model
        target_model = {}
        target_model['service_name'] = 'cloud-object-storage'
        target_model['service_display_name'] = 'testString'
        target_model['resource_kind'] = 'bucket'
        target_model['additional_target_attributes'] = [additional_target_attribute_model]

        # Construct a dict representation of a RequiredConfigItemsRequiredConfigBase model
        required_config_items_model = {}
        required_config_items_model['description'] = 'testString'
        required_config_items_model['property'] = 'hard_quota'
        required_config_items_model['operator'] = 'num_equals'
        required_config_items_model['value'] = '${hard_quota}'

        # Construct a dict representation of a RequiredConfigRequiredConfigAnd model
        required_config_model = {}
        required_config_model['description'] = 'The Cloud Object Storage rule.'
        required_config_model['and'] = [required_config_items_model]

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['name'] = 'hard_quota'
        parameter_model['display_name'] = 'The Cloud Object Storage bucket quota.'
        parameter_model['description'] = 'The maximum bytes that are allocated to the Cloud Object Storage bucket.'
        parameter_model['type'] = 'numeric'

        # Construct a dict representation of a Import model
        import_model = {}
        import_model['parameters'] = [parameter_model]

        # Set up parameter values
        description = 'Example rule'
        target = target_model
        required_config = required_config_model
        type = 'user_defined'
        version = '1.0.0'
        import_ = import_model
        labels = []
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.create_rule(
            description,
            target,
            required_config,
            type=type,
            version=version,
            import_=import_,
            labels=labels,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'Example rule'
        assert req_body['target'] == target_model
        assert req_body['required_config'] == required_config_model
        assert req_body['type'] == 'user_defined'
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
    def test_create_rule_required_params(self):
        """
        test_create_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/rules')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "value"}]}, "required_config": {"description": "description", "and": [{"description": "description"}]}, "labels": ["labels"]}'
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

        # Construct a dict representation of a Target model
        target_model = {}
        target_model['service_name'] = 'cloud-object-storage'
        target_model['service_display_name'] = 'testString'
        target_model['resource_kind'] = 'bucket'
        target_model['additional_target_attributes'] = [additional_target_attribute_model]

        # Construct a dict representation of a RequiredConfigItemsRequiredConfigBase model
        required_config_items_model = {}
        required_config_items_model['description'] = 'testString'
        required_config_items_model['property'] = 'hard_quota'
        required_config_items_model['operator'] = 'num_equals'
        required_config_items_model['value'] = '${hard_quota}'

        # Construct a dict representation of a RequiredConfigRequiredConfigAnd model
        required_config_model = {}
        required_config_model['description'] = 'The Cloud Object Storage rule.'
        required_config_model['and'] = [required_config_items_model]

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['name'] = 'hard_quota'
        parameter_model['display_name'] = 'The Cloud Object Storage bucket quota.'
        parameter_model['description'] = 'The maximum bytes that are allocated to the Cloud Object Storage bucket.'
        parameter_model['type'] = 'numeric'

        # Construct a dict representation of a Import model
        import_model = {}
        import_model['parameters'] = [parameter_model]

        # Set up parameter values
        description = 'Example rule'
        target = target_model
        required_config = required_config_model
        type = 'user_defined'
        version = '1.0.0'
        import_ = import_model
        labels = []

        # Invoke method
        response = _service.create_rule(
            description,
            target,
            required_config,
            type=type,
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
        assert req_body['target'] == target_model
        assert req_body['required_config'] == required_config_model
        assert req_body['type'] == 'user_defined'
        assert req_body['version'] == '1.0.0'
        assert req_body['import'] == import_model
        assert req_body['labels'] == []

    def test_create_rule_required_params_with_retries(self):
        # Enable retries and run test_create_rule_required_params.
        _service.enable_retries()
        self.test_create_rule_required_params()

        # Disable retries and run test_create_rule_required_params.
        _service.disable_retries()
        self.test_create_rule_required_params()

    @responses.activate
    def test_create_rule_value_error(self):
        """
        test_create_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/rules')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "value"}]}, "required_config": {"description": "description", "and": [{"description": "description"}]}, "labels": ["labels"]}'
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

        # Construct a dict representation of a Target model
        target_model = {}
        target_model['service_name'] = 'cloud-object-storage'
        target_model['service_display_name'] = 'testString'
        target_model['resource_kind'] = 'bucket'
        target_model['additional_target_attributes'] = [additional_target_attribute_model]

        # Construct a dict representation of a RequiredConfigItemsRequiredConfigBase model
        required_config_items_model = {}
        required_config_items_model['description'] = 'testString'
        required_config_items_model['property'] = 'hard_quota'
        required_config_items_model['operator'] = 'num_equals'
        required_config_items_model['value'] = '${hard_quota}'

        # Construct a dict representation of a RequiredConfigRequiredConfigAnd model
        required_config_model = {}
        required_config_model['description'] = 'The Cloud Object Storage rule.'
        required_config_model['and'] = [required_config_items_model]

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['name'] = 'hard_quota'
        parameter_model['display_name'] = 'The Cloud Object Storage bucket quota.'
        parameter_model['description'] = 'The maximum bytes that are allocated to the Cloud Object Storage bucket.'
        parameter_model['type'] = 'numeric'

        # Construct a dict representation of a Import model
        import_model = {}
        import_model['parameters'] = [parameter_model]

        # Set up parameter values
        description = 'Example rule'
        target = target_model
        required_config = required_config_model
        type = 'user_defined'
        version = '1.0.0'
        import_ = import_model
        labels = []

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = preprocess_url('/rules/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        rule_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.delete_rule(
            rule_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
    def test_delete_rule_required_params(self):
        """
        test_delete_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/rules/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = _service.delete_rule(
            rule_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_rule_required_params_with_retries(self):
        # Enable retries and run test_delete_rule_required_params.
        _service.enable_retries()
        self.test_delete_rule_required_params()

        # Disable retries and run test_delete_rule_required_params.
        _service.disable_retries()
        self.test_delete_rule_required_params()

    @responses.activate
    def test_delete_rule_value_error(self):
        """
        test_delete_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/rules/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = preprocess_url('/rules/testString')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "value"}]}, "required_config": {"description": "description", "and": [{"description": "description"}]}, "labels": ["labels"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        rule_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.get_rule(
            rule_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
    def test_get_rule_required_params(self):
        """
        test_get_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/rules/testString')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "value"}]}, "required_config": {"description": "description", "and": [{"description": "description"}]}, "labels": ["labels"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = _service.get_rule(
            rule_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_rule_required_params_with_retries(self):
        # Enable retries and run test_get_rule_required_params.
        _service.enable_retries()
        self.test_get_rule_required_params()

        # Disable retries and run test_get_rule_required_params.
        _service.disable_retries()
        self.test_get_rule_required_params()

    @responses.activate
    def test_get_rule_value_error(self):
        """
        test_get_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/rules/testString')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "value"}]}, "required_config": {"description": "description", "and": [{"description": "description"}]}, "labels": ["labels"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = preprocess_url('/rules/testString')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "value"}]}, "required_config": {"description": "description", "and": [{"description": "description"}]}, "labels": ["labels"]}'
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

        # Construct a dict representation of a Target model
        target_model = {}
        target_model['service_name'] = 'cloud-object-storage'
        target_model['service_display_name'] = 'Cloud Object Storage'
        target_model['resource_kind'] = 'bucket'
        target_model['additional_target_attributes'] = [additional_target_attribute_model]

        # Construct a dict representation of a RequiredConfigItemsRequiredConfigBase model
        required_config_items_model = {}
        required_config_items_model['description'] = 'testString'
        required_config_items_model['property'] = 'hard_quota'
        required_config_items_model['operator'] = 'num_equals'
        required_config_items_model['value'] = '${hard_quota}'

        # Construct a dict representation of a RequiredConfigRequiredConfigAnd model
        required_config_model = {}
        required_config_model['description'] = 'The Cloud Object Storage rule.'
        required_config_model['and'] = [required_config_items_model]

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['name'] = 'hard_quota'
        parameter_model['display_name'] = 'The Cloud Object Storage bucket quota.'
        parameter_model['description'] = 'The maximum bytes that are allocated to the Cloud Object Storage bucket.'
        parameter_model['type'] = 'numeric'

        # Construct a dict representation of a Import model
        import_model = {}
        import_model['parameters'] = [parameter_model]

        # Set up parameter values
        rule_id = 'testString'
        if_match = 'testString'
        description = 'Example rule'
        target = target_model
        required_config = required_config_model
        type = 'user_defined'
        version = '1.0.1'
        import_ = import_model
        labels = []
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.replace_rule(
            rule_id,
            if_match,
            description,
            target,
            required_config,
            type=type,
            version=version,
            import_=import_,
            labels=labels,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'Example rule'
        assert req_body['target'] == target_model
        assert req_body['required_config'] == required_config_model
        assert req_body['type'] == 'user_defined'
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
    def test_replace_rule_required_params(self):
        """
        test_replace_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/rules/testString')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "value"}]}, "required_config": {"description": "description", "and": [{"description": "description"}]}, "labels": ["labels"]}'
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

        # Construct a dict representation of a Target model
        target_model = {}
        target_model['service_name'] = 'cloud-object-storage'
        target_model['service_display_name'] = 'Cloud Object Storage'
        target_model['resource_kind'] = 'bucket'
        target_model['additional_target_attributes'] = [additional_target_attribute_model]

        # Construct a dict representation of a RequiredConfigItemsRequiredConfigBase model
        required_config_items_model = {}
        required_config_items_model['description'] = 'testString'
        required_config_items_model['property'] = 'hard_quota'
        required_config_items_model['operator'] = 'num_equals'
        required_config_items_model['value'] = '${hard_quota}'

        # Construct a dict representation of a RequiredConfigRequiredConfigAnd model
        required_config_model = {}
        required_config_model['description'] = 'The Cloud Object Storage rule.'
        required_config_model['and'] = [required_config_items_model]

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['name'] = 'hard_quota'
        parameter_model['display_name'] = 'The Cloud Object Storage bucket quota.'
        parameter_model['description'] = 'The maximum bytes that are allocated to the Cloud Object Storage bucket.'
        parameter_model['type'] = 'numeric'

        # Construct a dict representation of a Import model
        import_model = {}
        import_model['parameters'] = [parameter_model]

        # Set up parameter values
        rule_id = 'testString'
        if_match = 'testString'
        description = 'Example rule'
        target = target_model
        required_config = required_config_model
        type = 'user_defined'
        version = '1.0.1'
        import_ = import_model
        labels = []

        # Invoke method
        response = _service.replace_rule(
            rule_id,
            if_match,
            description,
            target,
            required_config,
            type=type,
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
        assert req_body['target'] == target_model
        assert req_body['required_config'] == required_config_model
        assert req_body['type'] == 'user_defined'
        assert req_body['version'] == '1.0.1'
        assert req_body['import'] == import_model
        assert req_body['labels'] == []

    def test_replace_rule_required_params_with_retries(self):
        # Enable retries and run test_replace_rule_required_params.
        _service.enable_retries()
        self.test_replace_rule_required_params()

        # Disable retries and run test_replace_rule_required_params.
        _service.disable_retries()
        self.test_replace_rule_required_params()

    @responses.activate
    def test_replace_rule_value_error(self):
        """
        test_replace_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/rules/testString')
        mock_response = '{"created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "id": "id", "account_id": "account_id", "description": "description", "type": "user_defined", "version": "version", "import": {"parameters": [{"name": "name", "display_name": "display_name", "description": "description", "type": "string"}]}, "target": {"service_name": "service_name", "service_display_name": "service_display_name", "resource_kind": "resource_kind", "additional_target_attributes": [{"name": "name", "operator": "string_equals", "value": "value"}]}, "required_config": {"description": "description", "and": [{"description": "description"}]}, "labels": ["labels"]}'
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

        # Construct a dict representation of a Target model
        target_model = {}
        target_model['service_name'] = 'cloud-object-storage'
        target_model['service_display_name'] = 'Cloud Object Storage'
        target_model['resource_kind'] = 'bucket'
        target_model['additional_target_attributes'] = [additional_target_attribute_model]

        # Construct a dict representation of a RequiredConfigItemsRequiredConfigBase model
        required_config_items_model = {}
        required_config_items_model['description'] = 'testString'
        required_config_items_model['property'] = 'hard_quota'
        required_config_items_model['operator'] = 'num_equals'
        required_config_items_model['value'] = '${hard_quota}'

        # Construct a dict representation of a RequiredConfigRequiredConfigAnd model
        required_config_model = {}
        required_config_model['description'] = 'The Cloud Object Storage rule.'
        required_config_model['and'] = [required_config_items_model]

        # Construct a dict representation of a Parameter model
        parameter_model = {}
        parameter_model['name'] = 'hard_quota'
        parameter_model['display_name'] = 'The Cloud Object Storage bucket quota.'
        parameter_model['description'] = 'The maximum bytes that are allocated to the Cloud Object Storage bucket.'
        parameter_model['type'] = 'numeric'

        # Construct a dict representation of a Import model
        import_model = {}
        import_model['parameters'] = [parameter_model]

        # Set up parameter values
        rule_id = 'testString'
        if_match = 'testString'
        description = 'Example rule'
        target = target_model
        required_config = required_config_model
        type = 'user_defined'
        version = '1.0.1'
        import_ = import_model
        labels = []

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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


# endregion
##############################################################################
# End of Service: Rules
##############################################################################

##############################################################################
# Start of Service: Attachments
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


class TestListAttachments:
    """
    Test Class for list_attachments
    """

    @responses.activate
    def test_list_attachments_all_params(self):
        """
        list_attachments()
        """
        # Set up mock
        url = preprocess_url('/profiles/testString/attachments')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "attachments": [{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_attachments(
            profiles_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_attachments_all_params_with_retries(self):
        # Enable retries and run test_list_attachments_all_params.
        _service.enable_retries()
        self.test_list_attachments_all_params()

        # Disable retries and run test_list_attachments_all_params.
        _service.disable_retries()
        self.test_list_attachments_all_params()

    @responses.activate
    def test_list_attachments_required_params(self):
        """
        test_list_attachments_required_params()
        """
        # Set up mock
        url = preprocess_url('/profiles/testString/attachments')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "attachments": [{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'

        # Invoke method
        response = _service.list_attachments(
            profiles_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_attachments_required_params_with_retries(self):
        # Enable retries and run test_list_attachments_required_params.
        _service.enable_retries()
        self.test_list_attachments_required_params()

        # Disable retries and run test_list_attachments_required_params.
        _service.disable_retries()
        self.test_list_attachments_required_params()

    @responses.activate
    def test_list_attachments_value_error(self):
        """
        test_list_attachments_value_error()
        """
        # Set up mock
        url = preprocess_url('/profiles/testString/attachments')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "attachments": [{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_attachments(**req_copy)

    def test_list_attachments_value_error_with_retries(self):
        # Enable retries and run test_list_attachments_value_error.
        _service.enable_retries()
        self.test_list_attachments_value_error()

        # Disable retries and run test_list_attachments_value_error.
        _service.disable_retries()
        self.test_list_attachments_value_error()

    @responses.activate
    def test_list_attachments_with_pager_get_next(self):
        """
        test_list_attachments_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/profiles/testString/attachments')
        mock_response1 = '{"next":{"start":"1"},"attachments":[{"id":"130003ea8bfa43c5aacea07a86da3000","profile_id":"7ec45986-54fc-4b66-a303-d9577b078c65","account_id":"130003ea8bfa43c5aacea07a86da3000","instance_id":"edf9524f-406c-412c-acbb-ee371a5cabda","scope":[{"environment":"environment","properties":[{"name":"name","value":"value"}]}],"created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","status":"enabled","schedule":"daily","notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}},"attachment_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"parameter_name","parameter_value":"parameter_value","parameter_display_name":"parameter_display_name","parameter_type":"string"}],"last_scan":{"id":"e8a39d25-0051-4328-8462-988ad321f49a","status":"in_progress","time":"2019-01-01T12:00:00.000Z"},"next_scan_time":"2019-01-01T12:00:00.000Z","name":"account-130003ea8bfa43c5aacea07a86da3000","description":"Test description"}],"total_count":2,"limit":1}'
        mock_response2 = '{"attachments":[{"id":"130003ea8bfa43c5aacea07a86da3000","profile_id":"7ec45986-54fc-4b66-a303-d9577b078c65","account_id":"130003ea8bfa43c5aacea07a86da3000","instance_id":"edf9524f-406c-412c-acbb-ee371a5cabda","scope":[{"environment":"environment","properties":[{"name":"name","value":"value"}]}],"created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","status":"enabled","schedule":"daily","notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}},"attachment_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"parameter_name","parameter_value":"parameter_value","parameter_display_name":"parameter_display_name","parameter_type":"string"}],"last_scan":{"id":"e8a39d25-0051-4328-8462-988ad321f49a","status":"in_progress","time":"2019-01-01T12:00:00.000Z"},"next_scan_time":"2019-01-01T12:00:00.000Z","name":"account-130003ea8bfa43c5aacea07a86da3000","description":"Test description"}],"total_count":2,"limit":1}'
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
        pager = AttachmentsPager(
            client=_service,
            profiles_id='testString',
            x_correlation_id='testString',
            x_request_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_attachments_with_pager_get_all(self):
        """
        test_list_attachments_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/profiles/testString/attachments')
        mock_response1 = '{"next":{"start":"1"},"attachments":[{"id":"130003ea8bfa43c5aacea07a86da3000","profile_id":"7ec45986-54fc-4b66-a303-d9577b078c65","account_id":"130003ea8bfa43c5aacea07a86da3000","instance_id":"edf9524f-406c-412c-acbb-ee371a5cabda","scope":[{"environment":"environment","properties":[{"name":"name","value":"value"}]}],"created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","status":"enabled","schedule":"daily","notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}},"attachment_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"parameter_name","parameter_value":"parameter_value","parameter_display_name":"parameter_display_name","parameter_type":"string"}],"last_scan":{"id":"e8a39d25-0051-4328-8462-988ad321f49a","status":"in_progress","time":"2019-01-01T12:00:00.000Z"},"next_scan_time":"2019-01-01T12:00:00.000Z","name":"account-130003ea8bfa43c5aacea07a86da3000","description":"Test description"}],"total_count":2,"limit":1}'
        mock_response2 = '{"attachments":[{"id":"130003ea8bfa43c5aacea07a86da3000","profile_id":"7ec45986-54fc-4b66-a303-d9577b078c65","account_id":"130003ea8bfa43c5aacea07a86da3000","instance_id":"edf9524f-406c-412c-acbb-ee371a5cabda","scope":[{"environment":"environment","properties":[{"name":"name","value":"value"}]}],"created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","status":"enabled","schedule":"daily","notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}},"attachment_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"parameter_name","parameter_value":"parameter_value","parameter_display_name":"parameter_display_name","parameter_type":"string"}],"last_scan":{"id":"e8a39d25-0051-4328-8462-988ad321f49a","status":"in_progress","time":"2019-01-01T12:00:00.000Z"},"next_scan_time":"2019-01-01T12:00:00.000Z","name":"account-130003ea8bfa43c5aacea07a86da3000","description":"Test description"}],"total_count":2,"limit":1}'
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
        pager = AttachmentsPager(
            client=_service,
            profiles_id='testString',
            x_correlation_id='testString',
            x_request_id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateAttachment:
    """
    Test Class for create_attachment
    """

    @responses.activate
    def test_create_attachment_all_params(self):
        """
        create_attachment()
        """
        # Set up mock
        url = preprocess_url('/profiles/testString/attachments')
        mock_response = '{"profile_id": "profile_id", "attachments": [{"id": "130003ea8bfa43c5aacea07a86da3000", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a PropertyItem model
        property_item_model = {}
        property_item_model['name'] = 'scope_id'
        property_item_model['value'] = 'cg3335893hh1428692d6747cf300yeb5'

        # Construct a dict representation of a MultiCloudScope model
        multi_cloud_scope_model = {}
        multi_cloud_scope_model['environment'] = 'ibm-cloud'
        multi_cloud_scope_model['properties'] = [property_item_model]

        # Construct a dict representation of a FailedControls model
        failed_controls_model = {}
        failed_controls_model['threshold_limit'] = 15
        failed_controls_model['failed_control_ids'] = []

        # Construct a dict representation of a AttachmentsNotificationsPrototype model
        attachments_notifications_prototype_model = {}
        attachments_notifications_prototype_model['enabled'] = False
        attachments_notifications_prototype_model['controls'] = failed_controls_model

        # Construct a dict representation of a AttachmentParameterPrototype model
        attachment_parameter_prototype_model = {}
        attachment_parameter_prototype_model['assessment_type'] = 'Automated'
        attachment_parameter_prototype_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        attachment_parameter_prototype_model['parameter_name'] = 'session_invalidation_in_seconds'
        attachment_parameter_prototype_model['parameter_value'] = '120'
        attachment_parameter_prototype_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        attachment_parameter_prototype_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a AttachmentsPrototype model
        attachments_prototype_model = {}
        attachments_prototype_model['id'] = '130003ea8bfa43c5aacea07a86da3000'
        attachments_prototype_model['name'] = 'account-0d8c3805dfea40aa8ad02265a18eb12b'
        attachments_prototype_model['description'] = 'Test description'
        attachments_prototype_model['scope'] = [multi_cloud_scope_model]
        attachments_prototype_model['status'] = 'enabled'
        attachments_prototype_model['schedule'] = 'every_30_days'
        attachments_prototype_model['notifications'] = attachments_notifications_prototype_model
        attachments_prototype_model['attachment_parameters'] = [attachment_parameter_prototype_model]

        # Set up parameter values
        profiles_id = 'testString'
        attachments = [attachments_prototype_model]
        profile_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.create_attachment(
            profiles_id,
            attachments,
            profile_id=profile_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachments'] == [attachments_prototype_model]
        assert req_body['profile_id'] == 'testString'

    def test_create_attachment_all_params_with_retries(self):
        # Enable retries and run test_create_attachment_all_params.
        _service.enable_retries()
        self.test_create_attachment_all_params()

        # Disable retries and run test_create_attachment_all_params.
        _service.disable_retries()
        self.test_create_attachment_all_params()

    @responses.activate
    def test_create_attachment_required_params(self):
        """
        test_create_attachment_required_params()
        """
        # Set up mock
        url = preprocess_url('/profiles/testString/attachments')
        mock_response = '{"profile_id": "profile_id", "attachments": [{"id": "130003ea8bfa43c5aacea07a86da3000", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a PropertyItem model
        property_item_model = {}
        property_item_model['name'] = 'scope_id'
        property_item_model['value'] = 'cg3335893hh1428692d6747cf300yeb5'

        # Construct a dict representation of a MultiCloudScope model
        multi_cloud_scope_model = {}
        multi_cloud_scope_model['environment'] = 'ibm-cloud'
        multi_cloud_scope_model['properties'] = [property_item_model]

        # Construct a dict representation of a FailedControls model
        failed_controls_model = {}
        failed_controls_model['threshold_limit'] = 15
        failed_controls_model['failed_control_ids'] = []

        # Construct a dict representation of a AttachmentsNotificationsPrototype model
        attachments_notifications_prototype_model = {}
        attachments_notifications_prototype_model['enabled'] = False
        attachments_notifications_prototype_model['controls'] = failed_controls_model

        # Construct a dict representation of a AttachmentParameterPrototype model
        attachment_parameter_prototype_model = {}
        attachment_parameter_prototype_model['assessment_type'] = 'Automated'
        attachment_parameter_prototype_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        attachment_parameter_prototype_model['parameter_name'] = 'session_invalidation_in_seconds'
        attachment_parameter_prototype_model['parameter_value'] = '120'
        attachment_parameter_prototype_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        attachment_parameter_prototype_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a AttachmentsPrototype model
        attachments_prototype_model = {}
        attachments_prototype_model['id'] = '130003ea8bfa43c5aacea07a86da3000'
        attachments_prototype_model['name'] = 'account-0d8c3805dfea40aa8ad02265a18eb12b'
        attachments_prototype_model['description'] = 'Test description'
        attachments_prototype_model['scope'] = [multi_cloud_scope_model]
        attachments_prototype_model['status'] = 'enabled'
        attachments_prototype_model['schedule'] = 'every_30_days'
        attachments_prototype_model['notifications'] = attachments_notifications_prototype_model
        attachments_prototype_model['attachment_parameters'] = [attachment_parameter_prototype_model]

        # Set up parameter values
        profiles_id = 'testString'
        attachments = [attachments_prototype_model]
        profile_id = 'testString'

        # Invoke method
        response = _service.create_attachment(
            profiles_id,
            attachments,
            profile_id=profile_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachments'] == [attachments_prototype_model]
        assert req_body['profile_id'] == 'testString'

    def test_create_attachment_required_params_with_retries(self):
        # Enable retries and run test_create_attachment_required_params.
        _service.enable_retries()
        self.test_create_attachment_required_params()

        # Disable retries and run test_create_attachment_required_params.
        _service.disable_retries()
        self.test_create_attachment_required_params()

    @responses.activate
    def test_create_attachment_value_error(self):
        """
        test_create_attachment_value_error()
        """
        # Set up mock
        url = preprocess_url('/profiles/testString/attachments')
        mock_response = '{"profile_id": "profile_id", "attachments": [{"id": "130003ea8bfa43c5aacea07a86da3000", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a PropertyItem model
        property_item_model = {}
        property_item_model['name'] = 'scope_id'
        property_item_model['value'] = 'cg3335893hh1428692d6747cf300yeb5'

        # Construct a dict representation of a MultiCloudScope model
        multi_cloud_scope_model = {}
        multi_cloud_scope_model['environment'] = 'ibm-cloud'
        multi_cloud_scope_model['properties'] = [property_item_model]

        # Construct a dict representation of a FailedControls model
        failed_controls_model = {}
        failed_controls_model['threshold_limit'] = 15
        failed_controls_model['failed_control_ids'] = []

        # Construct a dict representation of a AttachmentsNotificationsPrototype model
        attachments_notifications_prototype_model = {}
        attachments_notifications_prototype_model['enabled'] = False
        attachments_notifications_prototype_model['controls'] = failed_controls_model

        # Construct a dict representation of a AttachmentParameterPrototype model
        attachment_parameter_prototype_model = {}
        attachment_parameter_prototype_model['assessment_type'] = 'Automated'
        attachment_parameter_prototype_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        attachment_parameter_prototype_model['parameter_name'] = 'session_invalidation_in_seconds'
        attachment_parameter_prototype_model['parameter_value'] = '120'
        attachment_parameter_prototype_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        attachment_parameter_prototype_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a AttachmentsPrototype model
        attachments_prototype_model = {}
        attachments_prototype_model['id'] = '130003ea8bfa43c5aacea07a86da3000'
        attachments_prototype_model['name'] = 'account-0d8c3805dfea40aa8ad02265a18eb12b'
        attachments_prototype_model['description'] = 'Test description'
        attachments_prototype_model['scope'] = [multi_cloud_scope_model]
        attachments_prototype_model['status'] = 'enabled'
        attachments_prototype_model['schedule'] = 'every_30_days'
        attachments_prototype_model['notifications'] = attachments_notifications_prototype_model
        attachments_prototype_model['attachment_parameters'] = [attachment_parameter_prototype_model]

        # Set up parameter values
        profiles_id = 'testString'
        attachments = [attachments_prototype_model]
        profile_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "attachments": attachments,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_attachment(**req_copy)

    def test_create_attachment_value_error_with_retries(self):
        # Enable retries and run test_create_attachment_value_error.
        _service.enable_retries()
        self.test_create_attachment_value_error()

        # Disable retries and run test_create_attachment_value_error.
        _service.disable_retries()
        self.test_create_attachment_value_error()


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
        url = preprocess_url('/profiles/testString/attachments/testString')
        mock_response = '{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        attachment_id = 'testString'
        profiles_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.delete_profile_attachment(
            attachment_id,
            profiles_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

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
        url = preprocess_url('/profiles/testString/attachments/testString')
        mock_response = '{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        attachment_id = 'testString'
        profiles_id = 'testString'

        # Invoke method
        response = _service.delete_profile_attachment(
            attachment_id,
            profiles_id,
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
        url = preprocess_url('/profiles/testString/attachments/testString')
        mock_response = '{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        attachment_id = 'testString'
        profiles_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "attachment_id": attachment_id,
            "profiles_id": profiles_id,
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
        url = preprocess_url('/profiles/testString/attachments/testString')
        mock_response = '{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        attachment_id = 'testString'
        profiles_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.get_profile_attachment(
            attachment_id,
            profiles_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

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
        url = preprocess_url('/profiles/testString/attachments/testString')
        mock_response = '{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        attachment_id = 'testString'
        profiles_id = 'testString'

        # Invoke method
        response = _service.get_profile_attachment(
            attachment_id,
            profiles_id,
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
        url = preprocess_url('/profiles/testString/attachments/testString')
        mock_response = '{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        attachment_id = 'testString'
        profiles_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "attachment_id": attachment_id,
            "profiles_id": profiles_id,
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
        url = preprocess_url('/profiles/testString/attachments/testString')
        mock_response = '{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a PropertyItem model
        property_item_model = {}
        property_item_model['name'] = 'scope_id'
        property_item_model['value'] = 'cg3335893hh1428692d6747cf300yeb5'

        # Construct a dict representation of a MultiCloudScope model
        multi_cloud_scope_model = {}
        multi_cloud_scope_model['environment'] = 'ibm-cloud'
        multi_cloud_scope_model['properties'] = [property_item_model]

        # Construct a dict representation of a FailedControls model
        failed_controls_model = {}
        failed_controls_model['threshold_limit'] = 15
        failed_controls_model['failed_control_ids'] = []

        # Construct a dict representation of a AttachmentsNotificationsPrototype model
        attachments_notifications_prototype_model = {}
        attachments_notifications_prototype_model['enabled'] = False
        attachments_notifications_prototype_model['controls'] = failed_controls_model

        # Construct a dict representation of a AttachmentParameterPrototype model
        attachment_parameter_prototype_model = {}
        attachment_parameter_prototype_model['assessment_type'] = 'Automated'
        attachment_parameter_prototype_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        attachment_parameter_prototype_model['parameter_name'] = 'session_invalidation_in_seconds'
        attachment_parameter_prototype_model['parameter_value'] = '120'
        attachment_parameter_prototype_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        attachment_parameter_prototype_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a LastScan model
        last_scan_model = {}
        last_scan_model['id'] = 'e8a39d25-0051-4328-8462-988ad321f49a'
        last_scan_model['status'] = 'in_progress'
        last_scan_model['time'] = '2019-01-01T12:00:00Z'

        # Set up parameter values
        attachment_id = 'testString'
        profiles_id = 'testString'
        id = 'testString'
        profile_id = 'testString'
        account_id = 'testString'
        instance_id = 'testString'
        scope = [multi_cloud_scope_model]
        created_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        created_by = 'testString'
        updated_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        updated_by = 'testString'
        status = 'enabled'
        schedule = 'every_30_days'
        notifications = attachments_notifications_prototype_model
        attachment_parameters = [attachment_parameter_prototype_model]
        last_scan = last_scan_model
        next_scan_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        name = 'account-0d8c3805dfea40aa8ad02265a18eb12b'
        description = 'Test description'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.replace_profile_attachment(
            attachment_id,
            profiles_id,
            id=id,
            profile_id=profile_id,
            account_id=account_id,
            instance_id=instance_id,
            scope=scope,
            created_on=created_on,
            created_by=created_by,
            updated_on=updated_on,
            updated_by=updated_by,
            status=status,
            schedule=schedule,
            notifications=notifications,
            attachment_parameters=attachment_parameters,
            last_scan=last_scan,
            next_scan_time=next_scan_time,
            name=name,
            description=description,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['profile_id'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['instance_id'] == 'testString'
        assert req_body['scope'] == [multi_cloud_scope_model]
        assert req_body['created_on'] == '2019-01-01T12:00:00Z'
        assert req_body['created_by'] == 'testString'
        assert req_body['updated_on'] == '2019-01-01T12:00:00Z'
        assert req_body['updated_by'] == 'testString'
        assert req_body['status'] == 'enabled'
        assert req_body['schedule'] == 'every_30_days'
        assert req_body['notifications'] == attachments_notifications_prototype_model
        assert req_body['attachment_parameters'] == [attachment_parameter_prototype_model]
        assert req_body['last_scan'] == last_scan_model
        assert req_body['next_scan_time'] == '2019-01-01T12:00:00Z'
        assert req_body['name'] == 'account-0d8c3805dfea40aa8ad02265a18eb12b'
        assert req_body['description'] == 'Test description'

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
        url = preprocess_url('/profiles/testString/attachments/testString')
        mock_response = '{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a PropertyItem model
        property_item_model = {}
        property_item_model['name'] = 'scope_id'
        property_item_model['value'] = 'cg3335893hh1428692d6747cf300yeb5'

        # Construct a dict representation of a MultiCloudScope model
        multi_cloud_scope_model = {}
        multi_cloud_scope_model['environment'] = 'ibm-cloud'
        multi_cloud_scope_model['properties'] = [property_item_model]

        # Construct a dict representation of a FailedControls model
        failed_controls_model = {}
        failed_controls_model['threshold_limit'] = 15
        failed_controls_model['failed_control_ids'] = []

        # Construct a dict representation of a AttachmentsNotificationsPrototype model
        attachments_notifications_prototype_model = {}
        attachments_notifications_prototype_model['enabled'] = False
        attachments_notifications_prototype_model['controls'] = failed_controls_model

        # Construct a dict representation of a AttachmentParameterPrototype model
        attachment_parameter_prototype_model = {}
        attachment_parameter_prototype_model['assessment_type'] = 'Automated'
        attachment_parameter_prototype_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        attachment_parameter_prototype_model['parameter_name'] = 'session_invalidation_in_seconds'
        attachment_parameter_prototype_model['parameter_value'] = '120'
        attachment_parameter_prototype_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        attachment_parameter_prototype_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a LastScan model
        last_scan_model = {}
        last_scan_model['id'] = 'e8a39d25-0051-4328-8462-988ad321f49a'
        last_scan_model['status'] = 'in_progress'
        last_scan_model['time'] = '2019-01-01T12:00:00Z'

        # Set up parameter values
        attachment_id = 'testString'
        profiles_id = 'testString'
        id = 'testString'
        profile_id = 'testString'
        account_id = 'testString'
        instance_id = 'testString'
        scope = [multi_cloud_scope_model]
        created_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        created_by = 'testString'
        updated_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        updated_by = 'testString'
        status = 'enabled'
        schedule = 'every_30_days'
        notifications = attachments_notifications_prototype_model
        attachment_parameters = [attachment_parameter_prototype_model]
        last_scan = last_scan_model
        next_scan_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        name = 'account-0d8c3805dfea40aa8ad02265a18eb12b'
        description = 'Test description'

        # Invoke method
        response = _service.replace_profile_attachment(
            attachment_id,
            profiles_id,
            id=id,
            profile_id=profile_id,
            account_id=account_id,
            instance_id=instance_id,
            scope=scope,
            created_on=created_on,
            created_by=created_by,
            updated_on=updated_on,
            updated_by=updated_by,
            status=status,
            schedule=schedule,
            notifications=notifications,
            attachment_parameters=attachment_parameters,
            last_scan=last_scan,
            next_scan_time=next_scan_time,
            name=name,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['profile_id'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['instance_id'] == 'testString'
        assert req_body['scope'] == [multi_cloud_scope_model]
        assert req_body['created_on'] == '2019-01-01T12:00:00Z'
        assert req_body['created_by'] == 'testString'
        assert req_body['updated_on'] == '2019-01-01T12:00:00Z'
        assert req_body['updated_by'] == 'testString'
        assert req_body['status'] == 'enabled'
        assert req_body['schedule'] == 'every_30_days'
        assert req_body['notifications'] == attachments_notifications_prototype_model
        assert req_body['attachment_parameters'] == [attachment_parameter_prototype_model]
        assert req_body['last_scan'] == last_scan_model
        assert req_body['next_scan_time'] == '2019-01-01T12:00:00Z'
        assert req_body['name'] == 'account-0d8c3805dfea40aa8ad02265a18eb12b'
        assert req_body['description'] == 'Test description'

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
        url = preprocess_url('/profiles/testString/attachments/testString')
        mock_response = '{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a PropertyItem model
        property_item_model = {}
        property_item_model['name'] = 'scope_id'
        property_item_model['value'] = 'cg3335893hh1428692d6747cf300yeb5'

        # Construct a dict representation of a MultiCloudScope model
        multi_cloud_scope_model = {}
        multi_cloud_scope_model['environment'] = 'ibm-cloud'
        multi_cloud_scope_model['properties'] = [property_item_model]

        # Construct a dict representation of a FailedControls model
        failed_controls_model = {}
        failed_controls_model['threshold_limit'] = 15
        failed_controls_model['failed_control_ids'] = []

        # Construct a dict representation of a AttachmentsNotificationsPrototype model
        attachments_notifications_prototype_model = {}
        attachments_notifications_prototype_model['enabled'] = False
        attachments_notifications_prototype_model['controls'] = failed_controls_model

        # Construct a dict representation of a AttachmentParameterPrototype model
        attachment_parameter_prototype_model = {}
        attachment_parameter_prototype_model['assessment_type'] = 'Automated'
        attachment_parameter_prototype_model['assessment_id'] = 'rule-a637949b-7e51-46c4-afd4-b96619001bf1'
        attachment_parameter_prototype_model['parameter_name'] = 'session_invalidation_in_seconds'
        attachment_parameter_prototype_model['parameter_value'] = '120'
        attachment_parameter_prototype_model['parameter_display_name'] = 'Sign out due to inactivity in seconds'
        attachment_parameter_prototype_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a LastScan model
        last_scan_model = {}
        last_scan_model['id'] = 'e8a39d25-0051-4328-8462-988ad321f49a'
        last_scan_model['status'] = 'in_progress'
        last_scan_model['time'] = '2019-01-01T12:00:00Z'

        # Set up parameter values
        attachment_id = 'testString'
        profiles_id = 'testString'
        id = 'testString'
        profile_id = 'testString'
        account_id = 'testString'
        instance_id = 'testString'
        scope = [multi_cloud_scope_model]
        created_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        created_by = 'testString'
        updated_on = string_to_datetime('2019-01-01T12:00:00.000Z')
        updated_by = 'testString'
        status = 'enabled'
        schedule = 'every_30_days'
        notifications = attachments_notifications_prototype_model
        attachment_parameters = [attachment_parameter_prototype_model]
        last_scan = last_scan_model
        next_scan_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        name = 'account-0d8c3805dfea40aa8ad02265a18eb12b'
        description = 'Test description'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "attachment_id": attachment_id,
            "profiles_id": profiles_id,
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
        url = preprocess_url('/scans')
        mock_response = '{"id": "id", "account_id": "account_id", "attachment_id": "attachment_id", "report_id": "report_id", "status": "completed", "last_scan_time": "last_scan_time", "next_scan_time": "next_scan_time", "scan_type": "ondemand", "occurence": 9}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        attachment_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.create_scan(
            attachment_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachment_id'] == 'testString'

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
        url = preprocess_url('/scans')
        mock_response = '{"id": "id", "account_id": "account_id", "attachment_id": "attachment_id", "report_id": "report_id", "status": "completed", "last_scan_time": "last_scan_time", "next_scan_time": "next_scan_time", "scan_type": "ondemand", "occurence": 9}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        attachment_id = 'testString'

        # Invoke method
        response = _service.create_scan(
            attachment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachment_id'] == 'testString'

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
        url = preprocess_url('/scans')
        mock_response = '{"id": "id", "account_id": "account_id", "attachment_id": "attachment_id", "report_id": "report_id", "status": "completed", "last_scan_time": "last_scan_time", "next_scan_time": "next_scan_time", "scan_type": "ondemand", "occurence": 9}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        attachment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "attachment_id": attachment_id,
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


class TestListAttachmentsAccount:
    """
    Test Class for list_attachments_account
    """

    @responses.activate
    def test_list_attachments_account_all_params(self):
        """
        list_attachments_account()
        """
        # Set up mock
        url = preprocess_url('/attachments')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "attachments": [{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_correlation_id = 'testString'
        x_request_id = 'testString'
        limit = 50
        start = 'testString'

        # Invoke method
        response = _service.list_attachments_account(
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_attachments_account_all_params_with_retries(self):
        # Enable retries and run test_list_attachments_account_all_params.
        _service.enable_retries()
        self.test_list_attachments_account_all_params()

        # Disable retries and run test_list_attachments_account_all_params.
        _service.disable_retries()
        self.test_list_attachments_account_all_params()

    @responses.activate
    def test_list_attachments_account_required_params(self):
        """
        test_list_attachments_account_required_params()
        """
        # Set up mock
        url = preprocess_url('/attachments')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "attachments": [{"id": "130003ea8bfa43c5aacea07a86da3000", "profile_id": "7ec45986-54fc-4b66-a303-d9577b078c65", "account_id": "130003ea8bfa43c5aacea07a86da3000", "instance_id": "edf9524f-406c-412c-acbb-ee371a5cabda", "scope": [{"environment": "environment", "properties": [{"name": "name", "value": "value"}]}], "created_on": "2019-01-01T12:00:00.000Z", "created_by": "created_by", "updated_on": "2019-01-01T12:00:00.000Z", "updated_by": "updated_by", "status": "enabled", "schedule": "daily", "notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}}, "attachment_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_value": "parameter_value", "parameter_display_name": "parameter_display_name", "parameter_type": "string"}], "last_scan": {"id": "e8a39d25-0051-4328-8462-988ad321f49a", "status": "in_progress", "time": "2019-01-01T12:00:00.000Z"}, "next_scan_time": "2019-01-01T12:00:00.000Z", "name": "account-130003ea8bfa43c5aacea07a86da3000", "description": "Test description"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_attachments_account()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_attachments_account_required_params_with_retries(self):
        # Enable retries and run test_list_attachments_account_required_params.
        _service.enable_retries()
        self.test_list_attachments_account_required_params()

        # Disable retries and run test_list_attachments_account_required_params.
        _service.disable_retries()
        self.test_list_attachments_account_required_params()

    @responses.activate
    def test_list_attachments_account_with_pager_get_next(self):
        """
        test_list_attachments_account_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/attachments')
        mock_response1 = '{"next":{"start":"1"},"attachments":[{"id":"130003ea8bfa43c5aacea07a86da3000","profile_id":"7ec45986-54fc-4b66-a303-d9577b078c65","account_id":"130003ea8bfa43c5aacea07a86da3000","instance_id":"edf9524f-406c-412c-acbb-ee371a5cabda","scope":[{"environment":"environment","properties":[{"name":"name","value":"value"}]}],"created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","status":"enabled","schedule":"daily","notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}},"attachment_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"parameter_name","parameter_value":"parameter_value","parameter_display_name":"parameter_display_name","parameter_type":"string"}],"last_scan":{"id":"e8a39d25-0051-4328-8462-988ad321f49a","status":"in_progress","time":"2019-01-01T12:00:00.000Z"},"next_scan_time":"2019-01-01T12:00:00.000Z","name":"account-130003ea8bfa43c5aacea07a86da3000","description":"Test description"}],"total_count":2,"limit":1}'
        mock_response2 = '{"attachments":[{"id":"130003ea8bfa43c5aacea07a86da3000","profile_id":"7ec45986-54fc-4b66-a303-d9577b078c65","account_id":"130003ea8bfa43c5aacea07a86da3000","instance_id":"edf9524f-406c-412c-acbb-ee371a5cabda","scope":[{"environment":"environment","properties":[{"name":"name","value":"value"}]}],"created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","status":"enabled","schedule":"daily","notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}},"attachment_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"parameter_name","parameter_value":"parameter_value","parameter_display_name":"parameter_display_name","parameter_type":"string"}],"last_scan":{"id":"e8a39d25-0051-4328-8462-988ad321f49a","status":"in_progress","time":"2019-01-01T12:00:00.000Z"},"next_scan_time":"2019-01-01T12:00:00.000Z","name":"account-130003ea8bfa43c5aacea07a86da3000","description":"Test description"}],"total_count":2,"limit":1}'
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
        pager = AttachmentsAccountPager(
            client=_service,
            x_correlation_id='testString',
            x_request_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_attachments_account_with_pager_get_all(self):
        """
        test_list_attachments_account_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/attachments')
        mock_response1 = '{"next":{"start":"1"},"attachments":[{"id":"130003ea8bfa43c5aacea07a86da3000","profile_id":"7ec45986-54fc-4b66-a303-d9577b078c65","account_id":"130003ea8bfa43c5aacea07a86da3000","instance_id":"edf9524f-406c-412c-acbb-ee371a5cabda","scope":[{"environment":"environment","properties":[{"name":"name","value":"value"}]}],"created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","status":"enabled","schedule":"daily","notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}},"attachment_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"parameter_name","parameter_value":"parameter_value","parameter_display_name":"parameter_display_name","parameter_type":"string"}],"last_scan":{"id":"e8a39d25-0051-4328-8462-988ad321f49a","status":"in_progress","time":"2019-01-01T12:00:00.000Z"},"next_scan_time":"2019-01-01T12:00:00.000Z","name":"account-130003ea8bfa43c5aacea07a86da3000","description":"Test description"}],"total_count":2,"limit":1}'
        mock_response2 = '{"attachments":[{"id":"130003ea8bfa43c5aacea07a86da3000","profile_id":"7ec45986-54fc-4b66-a303-d9577b078c65","account_id":"130003ea8bfa43c5aacea07a86da3000","instance_id":"edf9524f-406c-412c-acbb-ee371a5cabda","scope":[{"environment":"environment","properties":[{"name":"name","value":"value"}]}],"created_on":"2019-01-01T12:00:00.000Z","created_by":"created_by","updated_on":"2019-01-01T12:00:00.000Z","updated_by":"updated_by","status":"enabled","schedule":"daily","notifications":{"enabled":false,"controls":{"threshold_limit":15,"failed_control_ids":["5C453578-E9A1-421E-AD0F-C6AFCDD67CCF"]}},"attachment_parameters":[{"assessment_type":"assessment_type","assessment_id":"assessment_id","parameter_name":"parameter_name","parameter_value":"parameter_value","parameter_display_name":"parameter_display_name","parameter_type":"string"}],"last_scan":{"id":"e8a39d25-0051-4328-8462-988ad321f49a","status":"in_progress","time":"2019-01-01T12:00:00.000Z"},"next_scan_time":"2019-01-01T12:00:00.000Z","name":"account-130003ea8bfa43c5aacea07a86da3000","description":"Test description"}],"total_count":2,"limit":1}'
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
        pager = AttachmentsAccountPager(
            client=_service,
            x_correlation_id='testString',
            x_request_id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


# endregion
##############################################################################
# End of Service: Attachments
##############################################################################

##############################################################################
# Start of Service: Reports
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
        url = preprocess_url('/reports/latest')
        mock_response = '{"home_account_id": "home_account_id", "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}, "score": {"passed": 1, "total_count": 4, "percent": 25}, "reports": [{"id": "44a5-a292-32114fa73558", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "type": "scheduled", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "84644a08-31b6-4988-b504-49a46ca69ccd", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": [{"id": "ca0941aa-b7e2-43a3-9794-1b3d322474d9", "environment": "ibm-cloud", "properties": [{"name": "scope_id", "value": "18d32a4430e54c81a6668952609763b2"}]}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_correlation_id = 'testString'
        x_request_id = 'testString'
        sort = 'profile_name'

        # Invoke method
        response = _service.get_latest_reports(
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
        url = preprocess_url('/reports/latest')
        mock_response = '{"home_account_id": "home_account_id", "controls_summary": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}, "evaluations_summary": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}, "score": {"passed": 1, "total_count": 4, "percent": 25}, "reports": [{"id": "44a5-a292-32114fa73558", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "type": "scheduled", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "84644a08-31b6-4988-b504-49a46ca69ccd", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": [{"id": "ca0941aa-b7e2-43a3-9794-1b3d322474d9", "environment": "ibm-cloud", "properties": [{"name": "scope_id", "value": "18d32a4430e54c81a6668952609763b2"}]}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_latest_reports()

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
        url = preprocess_url('/reports')
        mock_response = '{"total_count": 230, "limit": 50, "start": "start", "first": {"href": "href"}, "next": {"href": "href"}, "home_account_id": "home_account_id", "reports": [{"id": "44a5-a292-32114fa73558", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "type": "scheduled", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "84644a08-31b6-4988-b504-49a46ca69ccd", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": [{"id": "ca0941aa-b7e2-43a3-9794-1b3d322474d9", "environment": "ibm-cloud", "properties": [{"name": "scope_id", "value": "18d32a4430e54c81a6668952609763b2"}]}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_correlation_id = 'testString'
        x_request_id = 'testString'
        attachment_id = 'testString'
        group_id = 'testString'
        profile_id = 'testString'
        type = 'scheduled'
        start = 'testString'
        limit = 50
        sort = 'profile_name'

        # Invoke method
        response = _service.list_reports(
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            attachment_id=attachment_id,
            group_id=group_id,
            profile_id=profile_id,
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
        assert 'attachment_id={}'.format(attachment_id) in query_string
        assert 'group_id={}'.format(group_id) in query_string
        assert 'profile_id={}'.format(profile_id) in query_string
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
        url = preprocess_url('/reports')
        mock_response = '{"total_count": 230, "limit": 50, "start": "start", "first": {"href": "href"}, "next": {"href": "href"}, "home_account_id": "home_account_id", "reports": [{"id": "44a5-a292-32114fa73558", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "type": "scheduled", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "84644a08-31b6-4988-b504-49a46ca69ccd", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": [{"id": "ca0941aa-b7e2-43a3-9794-1b3d322474d9", "environment": "ibm-cloud", "properties": [{"name": "scope_id", "value": "18d32a4430e54c81a6668952609763b2"}]}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_reports()

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
    def test_list_reports_with_pager_get_next(self):
        """
        test_list_reports_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/reports')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?start=1"},"reports":[{"id":"44a5-a292-32114fa73558","group_id":"55b6-b3A4-432250b84669","created_on":"2022-08-15T12:30:01Z","scan_time":"2022-08-15T12:30:01Z","type":"scheduled","cos_object":"crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7","instance_id":"84644a08-31b6-4988-b504-49a46ca69ccd","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"profile":{"id":"44a5-a292-32114fa73558","name":"IBM FS Cloud","version":"0.1"},"attachment":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"resource group - Default","description":"Scoped to the Default resource group","schedule":"daily","scope":[{"id":"ca0941aa-b7e2-43a3-9794-1b3d322474d9","environment":"ibm-cloud","properties":[{"name":"scope_id","value":"18d32a4430e54c81a6668952609763b2"}]}]}}],"total_count":2,"limit":1}'
        mock_response2 = '{"reports":[{"id":"44a5-a292-32114fa73558","group_id":"55b6-b3A4-432250b84669","created_on":"2022-08-15T12:30:01Z","scan_time":"2022-08-15T12:30:01Z","type":"scheduled","cos_object":"crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7","instance_id":"84644a08-31b6-4988-b504-49a46ca69ccd","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"profile":{"id":"44a5-a292-32114fa73558","name":"IBM FS Cloud","version":"0.1"},"attachment":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"resource group - Default","description":"Scoped to the Default resource group","schedule":"daily","scope":[{"id":"ca0941aa-b7e2-43a3-9794-1b3d322474d9","environment":"ibm-cloud","properties":[{"name":"scope_id","value":"18d32a4430e54c81a6668952609763b2"}]}]}}],"total_count":2,"limit":1}'
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
            x_correlation_id='testString',
            x_request_id='testString',
            attachment_id='testString',
            group_id='testString',
            profile_id='testString',
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
        url = preprocess_url('/reports')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?start=1"},"reports":[{"id":"44a5-a292-32114fa73558","group_id":"55b6-b3A4-432250b84669","created_on":"2022-08-15T12:30:01Z","scan_time":"2022-08-15T12:30:01Z","type":"scheduled","cos_object":"crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7","instance_id":"84644a08-31b6-4988-b504-49a46ca69ccd","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"profile":{"id":"44a5-a292-32114fa73558","name":"IBM FS Cloud","version":"0.1"},"attachment":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"resource group - Default","description":"Scoped to the Default resource group","schedule":"daily","scope":[{"id":"ca0941aa-b7e2-43a3-9794-1b3d322474d9","environment":"ibm-cloud","properties":[{"name":"scope_id","value":"18d32a4430e54c81a6668952609763b2"}]}]}}],"total_count":2,"limit":1}'
        mock_response2 = '{"reports":[{"id":"44a5-a292-32114fa73558","group_id":"55b6-b3A4-432250b84669","created_on":"2022-08-15T12:30:01Z","scan_time":"2022-08-15T12:30:01Z","type":"scheduled","cos_object":"crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7","instance_id":"84644a08-31b6-4988-b504-49a46ca69ccd","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"profile":{"id":"44a5-a292-32114fa73558","name":"IBM FS Cloud","version":"0.1"},"attachment":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"resource group - Default","description":"Scoped to the Default resource group","schedule":"daily","scope":[{"id":"ca0941aa-b7e2-43a3-9794-1b3d322474d9","environment":"ibm-cloud","properties":[{"name":"scope_id","value":"18d32a4430e54c81a6668952609763b2"}]}]}}],"total_count":2,"limit":1}'
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
            x_correlation_id='testString',
            x_request_id='testString',
            attachment_id='testString',
            group_id='testString',
            profile_id='testString',
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
        url = preprocess_url('/reports/testString')
        mock_response = '{"id": "44a5-a292-32114fa73558", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "type": "scheduled", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "84644a08-31b6-4988-b504-49a46ca69ccd", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": [{"id": "ca0941aa-b7e2-43a3-9794-1b3d322474d9", "environment": "ibm-cloud", "properties": [{"name": "scope_id", "value": "18d32a4430e54c81a6668952609763b2"}]}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.get_report(
            report_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

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
        url = preprocess_url('/reports/testString')
        mock_response = '{"id": "44a5-a292-32114fa73558", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "type": "scheduled", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "84644a08-31b6-4988-b504-49a46ca69ccd", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": [{"id": "ca0941aa-b7e2-43a3-9794-1b3d322474d9", "environment": "ibm-cloud", "properties": [{"name": "scope_id", "value": "18d32a4430e54c81a6668952609763b2"}]}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Invoke method
        response = _service.get_report(
            report_id,
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
        url = preprocess_url('/reports/testString')
        mock_response = '{"id": "44a5-a292-32114fa73558", "group_id": "55b6-b3A4-432250b84669", "created_on": "2022-08-15T12:30:01Z", "scan_time": "2022-08-15T12:30:01Z", "type": "scheduled", "cos_object": "crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7", "instance_id": "84644a08-31b6-4988-b504-49a46ca69ccd", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "profile": {"id": "44a5-a292-32114fa73558", "name": "IBM FS Cloud", "version": "0.1"}, "attachment": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "resource group - Default", "description": "Scoped to the Default resource group", "schedule": "daily", "scope": [{"id": "ca0941aa-b7e2-43a3-9794-1b3d322474d9", "environment": "ibm-cloud", "properties": [{"name": "scope_id", "value": "18d32a4430e54c81a6668952609763b2"}]}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "report_id": report_id,
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
        url = preprocess_url('/reports/testString/summary')
        mock_response = '{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "isntance_id": "84644a08-31b6-4988-b504-49a46ca69ccd", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "score": {"passed": 1, "total_count": 4, "percent": 25}, "controls": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}, "evaluations": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}, "resources": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "top_failed": [{"name": "my-bucket", "id": "531fc3e28bfc43c5a2cea07786d93f5c", "service": "cloud-object-storage", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "account": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.get_report_summary(
            report_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
    def test_get_report_summary_required_params(self):
        """
        test_get_report_summary_required_params()
        """
        # Set up mock
        url = preprocess_url('/reports/testString/summary')
        mock_response = '{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "isntance_id": "84644a08-31b6-4988-b504-49a46ca69ccd", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "score": {"passed": 1, "total_count": 4, "percent": 25}, "controls": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}, "evaluations": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}, "resources": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "top_failed": [{"name": "my-bucket", "id": "531fc3e28bfc43c5a2cea07786d93f5c", "service": "cloud-object-storage", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "account": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Invoke method
        response = _service.get_report_summary(
            report_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_report_summary_required_params_with_retries(self):
        # Enable retries and run test_get_report_summary_required_params.
        _service.enable_retries()
        self.test_get_report_summary_required_params()

        # Disable retries and run test_get_report_summary_required_params.
        _service.disable_retries()
        self.test_get_report_summary_required_params()

    @responses.activate
    def test_get_report_summary_value_error(self):
        """
        test_get_report_summary_value_error()
        """
        # Set up mock
        url = preprocess_url('/reports/testString/summary')
        mock_response = '{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "isntance_id": "84644a08-31b6-4988-b504-49a46ca69ccd", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "score": {"passed": 1, "total_count": 4, "percent": 25}, "controls": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}, "evaluations": {"status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}, "resources": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "top_failed": [{"name": "my-bucket", "id": "531fc3e28bfc43c5a2cea07786d93f5c", "service": "cloud-object-storage", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}, "account": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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


class TestGetReportEvaluation:
    """
    Test Class for get_report_evaluation
    """

    @responses.activate
    def test_get_report_evaluation_all_params(self):
        """
        get_report_evaluation()
        """
        # Set up mock
        url = preprocess_url('/reports/testString/download')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/csv',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'
        exclude_summary = True

        # Invoke method
        response = _service.get_report_evaluation(
            report_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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

    def test_get_report_evaluation_all_params_with_retries(self):
        # Enable retries and run test_get_report_evaluation_all_params.
        _service.enable_retries()
        self.test_get_report_evaluation_all_params()

        # Disable retries and run test_get_report_evaluation_all_params.
        _service.disable_retries()
        self.test_get_report_evaluation_all_params()

    @responses.activate
    def test_get_report_evaluation_required_params(self):
        """
        test_get_report_evaluation_required_params()
        """
        # Set up mock
        url = preprocess_url('/reports/testString/download')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/csv',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Invoke method
        response = _service.get_report_evaluation(
            report_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_report_evaluation_required_params_with_retries(self):
        # Enable retries and run test_get_report_evaluation_required_params.
        _service.enable_retries()
        self.test_get_report_evaluation_required_params()

        # Disable retries and run test_get_report_evaluation_required_params.
        _service.disable_retries()
        self.test_get_report_evaluation_required_params()

    @responses.activate
    def test_get_report_evaluation_value_error(self):
        """
        test_get_report_evaluation_value_error()
        """
        # Set up mock
        url = preprocess_url('/reports/testString/download')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/csv',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "report_id": report_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_report_evaluation(**req_copy)

    def test_get_report_evaluation_value_error_with_retries(self):
        # Enable retries and run test_get_report_evaluation_value_error.
        _service.enable_retries()
        self.test_get_report_evaluation_value_error()

        # Disable retries and run test_get_report_evaluation_value_error.
        _service.disable_retries()
        self.test_get_report_evaluation_value_error()


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
        url = preprocess_url('/reports/testString/controls')
        mock_response = '{"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "home_account_id": "home_account_id", "report_id": "report_id", "controls": [{"id": "531fc3e28bfc43c5a2cea07786d93f5c", "control_library_id": "531fc3e28bfc43c5a2cea07786d93f5c", "control_library_version": "v1.2.3", "control_name": "Password Management", "control_description": "Password Management", "control_category": "Access Control", "control_path": "AC-2(a)", "control_specifications": [{"control_specification_id": "18d32a4430e54c81a6668952609763b2", "component_id": "cloud-object_storage", "control_specification_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "environment": "ibm cloud", "responsibility": "user", "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}], "status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}], "status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'
        control_id = 'testString'
        control_name = 'testString'
        control_description = 'testString'
        control_category = 'testString'
        status = 'compliant'
        sort = 'control_name'

        # Invoke method
        response = _service.get_report_controls(
            report_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            control_id=control_id,
            control_name=control_name,
            control_description=control_description,
            control_category=control_category,
            status=status,
            sort=sort,
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
        url = preprocess_url('/reports/testString/controls')
        mock_response = '{"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "home_account_id": "home_account_id", "report_id": "report_id", "controls": [{"id": "531fc3e28bfc43c5a2cea07786d93f5c", "control_library_id": "531fc3e28bfc43c5a2cea07786d93f5c", "control_library_version": "v1.2.3", "control_name": "Password Management", "control_description": "Password Management", "control_category": "Access Control", "control_path": "AC-2(a)", "control_specifications": [{"control_specification_id": "18d32a4430e54c81a6668952609763b2", "component_id": "cloud-object_storage", "control_specification_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "environment": "ibm cloud", "responsibility": "user", "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}], "status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}], "status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Invoke method
        response = _service.get_report_controls(
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
        url = preprocess_url('/reports/testString/controls')
        mock_response = '{"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10, "home_account_id": "home_account_id", "report_id": "report_id", "controls": [{"id": "531fc3e28bfc43c5a2cea07786d93f5c", "control_library_id": "531fc3e28bfc43c5a2cea07786d93f5c", "control_library_version": "v1.2.3", "control_name": "Password Management", "control_description": "Password Management", "control_category": "Access Control", "control_path": "AC-2(a)", "control_specifications": [{"control_specification_id": "18d32a4430e54c81a6668952609763b2", "component_id": "cloud-object_storage", "control_specification_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "environment": "ibm cloud", "responsibility": "user", "assessments": [{"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}], "status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}], "status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = preprocess_url('/reports/testString/rules/rule-8d444f8c-fd1d-48de-bcaa-f43732568761')
        mock_response = '{"id": "rule-7b0560a4-df94-4629-bb76-680f3155ddda", "type": "user_defined/system_defined", "description": "rule", "version": "1.2.3", "account_id": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "created_on": "2022-08-15T12:30:01Z", "created_by": "IBMid-12345", "updated_on": "2022-08-15T12:30:01Z", "updated_by": "IBMid-12345", "labels": ["labels"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        rule_id = 'rule-8d444f8c-fd1d-48de-bcaa-f43732568761'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.get_report_rule(
            report_id,
            rule_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
    def test_get_report_rule_required_params(self):
        """
        test_get_report_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/reports/testString/rules/rule-8d444f8c-fd1d-48de-bcaa-f43732568761')
        mock_response = '{"id": "rule-7b0560a4-df94-4629-bb76-680f3155ddda", "type": "user_defined/system_defined", "description": "rule", "version": "1.2.3", "account_id": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "created_on": "2022-08-15T12:30:01Z", "created_by": "IBMid-12345", "updated_on": "2022-08-15T12:30:01Z", "updated_by": "IBMid-12345", "labels": ["labels"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        rule_id = 'rule-8d444f8c-fd1d-48de-bcaa-f43732568761'

        # Invoke method
        response = _service.get_report_rule(
            report_id,
            rule_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_report_rule_required_params_with_retries(self):
        # Enable retries and run test_get_report_rule_required_params.
        _service.enable_retries()
        self.test_get_report_rule_required_params()

        # Disable retries and run test_get_report_rule_required_params.
        _service.disable_retries()
        self.test_get_report_rule_required_params()

    @responses.activate
    def test_get_report_rule_value_error(self):
        """
        test_get_report_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/reports/testString/rules/rule-8d444f8c-fd1d-48de-bcaa-f43732568761')
        mock_response = '{"id": "rule-7b0560a4-df94-4629-bb76-680f3155ddda", "type": "user_defined/system_defined", "description": "rule", "version": "1.2.3", "account_id": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "created_on": "2022-08-15T12:30:01Z", "created_by": "IBMid-12345", "updated_on": "2022-08-15T12:30:01Z", "updated_by": "IBMid-12345", "labels": ["labels"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        rule_id = 'rule-8d444f8c-fd1d-48de-bcaa-f43732568761'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = preprocess_url('/reports/testString/evaluations')
        mock_response = '{"total_count": 230, "limit": 50, "start": "start", "first": {"href": "href"}, "next": {"href": "href"}, "home_account_id": "home_account_id", "report_id": "report_id", "evaluations": [{"home_account_id": "be200c80cabc456e91139e4152327456", "report_id": "44a5-a292-32114fa73558", "control_id": "28016c95-b389-447f-8a05-eabe1ad7fd24", "component_id": "cloud-object_storage", "assessment": {"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}, "evaluate_time": "2022-06-30T11:03:44.630150782Z", "target": {"id": "crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket", "account_id": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "resource_crn": "crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket", "resource_name": "mybucket", "service_name": "cloud-object-storage"}, "status": "failure", "reason": "One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met", "details": {"properties": [{"property": "allowed_network", "property_description": "A description for this property", "operator": "string_equals", "expected_value": "anyValue", "found_value": "anyValue"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'
        assessment_id = 'testString'
        component_id = 'testString'
        target_id = 'testString'
        target_name = 'testString'
        status = 'failure'
        start = 'testString'
        limit = 50

        # Invoke method
        response = _service.list_report_evaluations(
            report_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            assessment_id=assessment_id,
            component_id=component_id,
            target_id=target_id,
            target_name=target_name,
            status=status,
            start=start,
            limit=limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'assessment_id={}'.format(assessment_id) in query_string
        assert 'component_id={}'.format(component_id) in query_string
        assert 'target_id={}'.format(target_id) in query_string
        assert 'target_name={}'.format(target_name) in query_string
        assert 'status={}'.format(status) in query_string
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string

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
        url = preprocess_url('/reports/testString/evaluations')
        mock_response = '{"total_count": 230, "limit": 50, "start": "start", "first": {"href": "href"}, "next": {"href": "href"}, "home_account_id": "home_account_id", "report_id": "report_id", "evaluations": [{"home_account_id": "be200c80cabc456e91139e4152327456", "report_id": "44a5-a292-32114fa73558", "control_id": "28016c95-b389-447f-8a05-eabe1ad7fd24", "component_id": "cloud-object_storage", "assessment": {"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}, "evaluate_time": "2022-06-30T11:03:44.630150782Z", "target": {"id": "crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket", "account_id": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "resource_crn": "crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket", "resource_name": "mybucket", "service_name": "cloud-object-storage"}, "status": "failure", "reason": "One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met", "details": {"properties": [{"property": "allowed_network", "property_description": "A description for this property", "operator": "string_equals", "expected_value": "anyValue", "found_value": "anyValue"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Invoke method
        response = _service.list_report_evaluations(
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
        url = preprocess_url('/reports/testString/evaluations')
        mock_response = '{"total_count": 230, "limit": 50, "start": "start", "first": {"href": "href"}, "next": {"href": "href"}, "home_account_id": "home_account_id", "report_id": "report_id", "evaluations": [{"home_account_id": "be200c80cabc456e91139e4152327456", "report_id": "44a5-a292-32114fa73558", "control_id": "28016c95-b389-447f-8a05-eabe1ad7fd24", "component_id": "cloud-object_storage", "assessment": {"assessment_id": "382c2b06-e6b2-43ee-b189-c1c7743b67ee", "assessment_type": "ibm-cloud-rule", "assessment_method": "ibm-cloud-rule", "assessment_description": "Check whether Cloud Object Storage is accessible only by using private endpoints", "parameter_count": 1, "parameters": [{"parameter_name": "location", "parameter_display_name": "Location", "parameter_type": "string", "parameter_value": "anyValue"}]}, "evaluate_time": "2022-06-30T11:03:44.630150782Z", "target": {"id": "crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket", "account_id": "59bcbfa6ea2f006b4ed7094c1a08dcdd", "resource_crn": "crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket", "resource_name": "mybucket", "service_name": "cloud-object-storage"}, "status": "failure", "reason": "One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met", "details": {"properties": [{"property": "allowed_network", "property_description": "A description for this property", "operator": "string_equals", "expected_value": "anyValue", "found_value": "anyValue"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = preprocess_url('/reports/testString/evaluations')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?start=1"},"evaluations":[{"home_account_id":"be200c80cabc456e91139e4152327456","report_id":"44a5-a292-32114fa73558","control_id":"28016c95-b389-447f-8a05-eabe1ad7fd24","component_id":"cloud-object_storage","assessment":{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]},"evaluate_time":"2022-06-30T11:03:44.630150782Z","target":{"id":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","account_id":"59bcbfa6ea2f006b4ed7094c1a08dcdd","resource_crn":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","resource_name":"mybucket","service_name":"cloud-object-storage"},"status":"failure","reason":"One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met","details":{"properties":[{"property":"allowed_network","property_description":"A description for this property","operator":"string_equals","expected_value":"anyValue","found_value":"anyValue"}]}}],"total_count":2,"limit":1}'
        mock_response2 = '{"evaluations":[{"home_account_id":"be200c80cabc456e91139e4152327456","report_id":"44a5-a292-32114fa73558","control_id":"28016c95-b389-447f-8a05-eabe1ad7fd24","component_id":"cloud-object_storage","assessment":{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]},"evaluate_time":"2022-06-30T11:03:44.630150782Z","target":{"id":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","account_id":"59bcbfa6ea2f006b4ed7094c1a08dcdd","resource_crn":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","resource_name":"mybucket","service_name":"cloud-object-storage"},"status":"failure","reason":"One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met","details":{"properties":[{"property":"allowed_network","property_description":"A description for this property","operator":"string_equals","expected_value":"anyValue","found_value":"anyValue"}]}}],"total_count":2,"limit":1}'
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
            report_id='testString',
            x_correlation_id='testString',
            x_request_id='testString',
            assessment_id='testString',
            component_id='testString',
            target_id='testString',
            target_name='testString',
            status='failure',
            limit=10,
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
        url = preprocess_url('/reports/testString/evaluations')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?start=1"},"evaluations":[{"home_account_id":"be200c80cabc456e91139e4152327456","report_id":"44a5-a292-32114fa73558","control_id":"28016c95-b389-447f-8a05-eabe1ad7fd24","component_id":"cloud-object_storage","assessment":{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]},"evaluate_time":"2022-06-30T11:03:44.630150782Z","target":{"id":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","account_id":"59bcbfa6ea2f006b4ed7094c1a08dcdd","resource_crn":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","resource_name":"mybucket","service_name":"cloud-object-storage"},"status":"failure","reason":"One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met","details":{"properties":[{"property":"allowed_network","property_description":"A description for this property","operator":"string_equals","expected_value":"anyValue","found_value":"anyValue"}]}}],"total_count":2,"limit":1}'
        mock_response2 = '{"evaluations":[{"home_account_id":"be200c80cabc456e91139e4152327456","report_id":"44a5-a292-32114fa73558","control_id":"28016c95-b389-447f-8a05-eabe1ad7fd24","component_id":"cloud-object_storage","assessment":{"assessment_id":"382c2b06-e6b2-43ee-b189-c1c7743b67ee","assessment_type":"ibm-cloud-rule","assessment_method":"ibm-cloud-rule","assessment_description":"Check whether Cloud Object Storage is accessible only by using private endpoints","parameter_count":1,"parameters":[{"parameter_name":"location","parameter_display_name":"Location","parameter_type":"string","parameter_value":"anyValue"}]},"evaluate_time":"2022-06-30T11:03:44.630150782Z","target":{"id":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","account_id":"59bcbfa6ea2f006b4ed7094c1a08dcdd","resource_crn":"crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket","resource_name":"mybucket","service_name":"cloud-object-storage"},"status":"failure","reason":"One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met","details":{"properties":[{"property":"allowed_network","property_description":"A description for this property","operator":"string_equals","expected_value":"anyValue","found_value":"anyValue"}]}}],"total_count":2,"limit":1}'
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
            report_id='testString',
            x_correlation_id='testString',
            x_request_id='testString',
            assessment_id='testString',
            component_id='testString',
            target_id='testString',
            target_name='testString',
            status='failure',
            limit=10,
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
        url = preprocess_url('/reports/testString/resources')
        mock_response = '{"total_count": 230, "limit": 50, "start": "start", "first": {"href": "href"}, "next": {"href": "href"}, "home_account_id": "home_account_id", "report_id": "report_id", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "component_id": "cloud-object_storage", "environment": "ibm cloud", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'
        id = 'testString'
        resource_name = 'testString'
        account_id = 'testString'
        component_id = 'testString'
        status = 'compliant'
        sort = 'account_id'
        start = 'testString'
        limit = 50

        # Invoke method
        response = _service.list_report_resources(
            report_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            id=id,
            resource_name=resource_name,
            account_id=account_id,
            component_id=component_id,
            status=status,
            sort=sort,
            start=start,
            limit=limit,
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
        url = preprocess_url('/reports/testString/resources')
        mock_response = '{"total_count": 230, "limit": 50, "start": "start", "first": {"href": "href"}, "next": {"href": "href"}, "home_account_id": "home_account_id", "report_id": "report_id", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "component_id": "cloud-object_storage", "environment": "ibm cloud", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Invoke method
        response = _service.list_report_resources(
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
        url = preprocess_url('/reports/testString/resources')
        mock_response = '{"total_count": 230, "limit": 50, "start": "start", "first": {"href": "href"}, "next": {"href": "href"}, "home_account_id": "home_account_id", "report_id": "report_id", "resources": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "id": "crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::", "resource_name": "jeff\'s key", "component_id": "cloud-object_storage", "environment": "ibm cloud", "account": {"id": "531fc3e28bfc43c5a2cea07786d93f5c", "name": "NIST", "type": "account_type"}, "status": "compliant", "total_count": 140, "pass_count": 123, "failure_count": 12, "error_count": 5, "completed_count": 135}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = preprocess_url('/reports/testString/resources')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?start=1"},"total_count":2,"limit":1,"resources":[{"report_id":"30b434b3-cb08-4845-af10-7a8fc682b6a8","id":"crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::","resource_name":"jeff\'s key","component_id":"cloud-object_storage","environment":"ibm cloud","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"status":"compliant","total_count":140,"pass_count":123,"failure_count":12,"error_count":5,"completed_count":135}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"report_id":"30b434b3-cb08-4845-af10-7a8fc682b6a8","id":"crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::","resource_name":"jeff\'s key","component_id":"cloud-object_storage","environment":"ibm cloud","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"status":"compliant","total_count":140,"pass_count":123,"failure_count":12,"error_count":5,"completed_count":135}]}'
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
            report_id='testString',
            x_correlation_id='testString',
            x_request_id='testString',
            id='testString',
            resource_name='testString',
            account_id='testString',
            component_id='testString',
            status='compliant',
            sort='account_id',
            limit=10,
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
        url = preprocess_url('/reports/testString/resources')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?start=1"},"total_count":2,"limit":1,"resources":[{"report_id":"30b434b3-cb08-4845-af10-7a8fc682b6a8","id":"crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::","resource_name":"jeff\'s key","component_id":"cloud-object_storage","environment":"ibm cloud","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"status":"compliant","total_count":140,"pass_count":123,"failure_count":12,"error_count":5,"completed_count":135}]}'
        mock_response2 = '{"total_count":2,"limit":1,"resources":[{"report_id":"30b434b3-cb08-4845-af10-7a8fc682b6a8","id":"crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::","resource_name":"jeff\'s key","component_id":"cloud-object_storage","environment":"ibm cloud","account":{"id":"531fc3e28bfc43c5a2cea07786d93f5c","name":"NIST","type":"account_type"},"status":"compliant","total_count":140,"pass_count":123,"failure_count":12,"error_count":5,"completed_count":135}]}'
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
            report_id='testString',
            x_correlation_id='testString',
            x_request_id='testString',
            id='testString',
            resource_name='testString',
            account_id='testString',
            component_id='testString',
            status='compliant',
            sort='account_id',
            limit=10,
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
        url = preprocess_url('/reports/testString/tags')
        mock_response = '{"report_id": "report_id", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.get_report_tags(
            report_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
    def test_get_report_tags_required_params(self):
        """
        test_get_report_tags_required_params()
        """
        # Set up mock
        url = preprocess_url('/reports/testString/tags')
        mock_response = '{"report_id": "report_id", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Invoke method
        response = _service.get_report_tags(
            report_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_report_tags_required_params_with_retries(self):
        # Enable retries and run test_get_report_tags_required_params.
        _service.enable_retries()
        self.test_get_report_tags_required_params()

        # Disable retries and run test_get_report_tags_required_params.
        _service.disable_retries()
        self.test_get_report_tags_required_params()

    @responses.activate
    def test_get_report_tags_value_error(self):
        """
        test_get_report_tags_value_error()
        """
        # Set up mock
        url = preprocess_url('/reports/testString/tags')
        mock_response = '{"report_id": "report_id", "tags": {"user": ["user"], "access": ["access"], "service": ["service"]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = preprocess_url('/reports/testString/violations_drift')
        mock_response = '{"home_account_id": "home_account_id", "report_id": "report_id", "data_points": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "report_group_id": "55b6-b3A4-432250b84669", "scan_time": "2022-08-15T12:30:01Z", "controls": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'
        scan_time_duration = 0

        # Invoke method
        response = _service.get_report_violations_drift(
            report_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            scan_time_duration=scan_time_duration,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'scan_time_duration={}'.format(scan_time_duration) in query_string

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
        url = preprocess_url('/reports/testString/violations_drift')
        mock_response = '{"home_account_id": "home_account_id", "report_id": "report_id", "data_points": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "report_group_id": "55b6-b3A4-432250b84669", "scan_time": "2022-08-15T12:30:01Z", "controls": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Invoke method
        response = _service.get_report_violations_drift(
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
        url = preprocess_url('/reports/testString/violations_drift')
        mock_response = '{"home_account_id": "home_account_id", "report_id": "report_id", "data_points": [{"report_id": "30b434b3-cb08-4845-af10-7a8fc682b6a8", "report_group_id": "55b6-b3A4-432250b84669", "scan_time": "2022-08-15T12:30:01Z", "controls": {"status": "compliant", "total_count": 150, "compliant_count": 130, "not_compliant_count": 5, "unable_to_perform_count": 5, "user_evaluation_required_count": 10}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        report_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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


# endregion
##############################################################################
# End of Service: Reports
##############################################################################

##############################################################################
# Start of Service: ProviderTypes
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
        url = preprocess_url('/provider_types')
        mock_response = '{"provider_types": [{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection", "description": "Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.", "s2s_enabled": true, "instance_limit": 1, "mode": "PULL", "data_type": "com.sysdig.secure.results", "icon": "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+", "label": {"text": "1 per instance", "tip": "Only 1 per instance"}, "attributes": {"mapKey": {"type": "text", "display_name": "Workload Protection Instance CRN"}}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.list_provider_types(
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
    def test_list_provider_types_required_params(self):
        """
        test_list_provider_types_required_params()
        """
        # Set up mock
        url = preprocess_url('/provider_types')
        mock_response = '{"provider_types": [{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection", "description": "Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.", "s2s_enabled": true, "instance_limit": 1, "mode": "PULL", "data_type": "com.sysdig.secure.results", "icon": "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+", "label": {"text": "1 per instance", "tip": "Only 1 per instance"}, "attributes": {"mapKey": {"type": "text", "display_name": "Workload Protection Instance CRN"}}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_provider_types()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_provider_types_required_params_with_retries(self):
        # Enable retries and run test_list_provider_types_required_params.
        _service.enable_retries()
        self.test_list_provider_types_required_params()

        # Disable retries and run test_list_provider_types_required_params.
        _service.disable_retries()
        self.test_list_provider_types_required_params()


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
        url = preprocess_url('/provider_types/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection", "description": "Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.", "s2s_enabled": true, "instance_limit": 1, "mode": "PULL", "data_type": "com.sysdig.secure.results", "icon": "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+", "label": {"text": "1 per instance", "tip": "Only 1 per instance"}, "attributes": {"mapKey": {"type": "text", "display_name": "Workload Protection Instance CRN"}}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.get_provider_type_by_id(
            provider_type_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
    def test_get_provider_type_by_id_required_params(self):
        """
        test_get_provider_type_by_id_required_params()
        """
        # Set up mock
        url = preprocess_url('/provider_types/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection", "description": "Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.", "s2s_enabled": true, "instance_limit": 1, "mode": "PULL", "data_type": "com.sysdig.secure.results", "icon": "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+", "label": {"text": "1 per instance", "tip": "Only 1 per instance"}, "attributes": {"mapKey": {"type": "text", "display_name": "Workload Protection Instance CRN"}}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        provider_type_id = 'testString'

        # Invoke method
        response = _service.get_provider_type_by_id(
            provider_type_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_provider_type_by_id_required_params_with_retries(self):
        # Enable retries and run test_get_provider_type_by_id_required_params.
        _service.enable_retries()
        self.test_get_provider_type_by_id_required_params()

        # Disable retries and run test_get_provider_type_by_id_required_params.
        _service.disable_retries()
        self.test_get_provider_type_by_id_required_params()

    @responses.activate
    def test_get_provider_type_by_id_value_error(self):
        """
        test_get_provider_type_by_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/provider_types/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection", "description": "Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.", "s2s_enabled": true, "instance_limit": 1, "mode": "PULL", "data_type": "com.sysdig.secure.results", "icon": "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+", "label": {"text": "1 per instance", "tip": "Only 1 per instance"}, "attributes": {"mapKey": {"type": "text", "display_name": "Workload Protection Instance CRN"}}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        provider_type_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
# End of Service: ProviderTypes
##############################################################################

##############################################################################
# Start of Service: ProviderTypeInstances
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
        url = preprocess_url('/provider_types/testString/provider_type_instances')
        mock_response = '{"provider_type_instances": [{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.list_provider_type_instances(
            provider_type_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
    def test_list_provider_type_instances_required_params(self):
        """
        test_list_provider_type_instances_required_params()
        """
        # Set up mock
        url = preprocess_url('/provider_types/testString/provider_type_instances')
        mock_response = '{"provider_type_instances": [{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        provider_type_id = 'testString'

        # Invoke method
        response = _service.list_provider_type_instances(
            provider_type_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_provider_type_instances_required_params_with_retries(self):
        # Enable retries and run test_list_provider_type_instances_required_params.
        _service.enable_retries()
        self.test_list_provider_type_instances_required_params()

        # Disable retries and run test_list_provider_type_instances_required_params.
        _service.disable_retries()
        self.test_list_provider_type_instances_required_params()

    @responses.activate
    def test_list_provider_type_instances_value_error(self):
        """
        test_list_provider_type_instances_value_error()
        """
        # Set up mock
        url = preprocess_url('/provider_types/testString/provider_type_instances')
        mock_response = '{"provider_type_instances": [{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        provider_type_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = preprocess_url('/provider_types/testString/provider_type_instances')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        name = 'workload-protection-instance-1'
        attributes = {'anyKey': 'anyValue'}
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.create_provider_type_instance(
            provider_type_id,
            name=name,
            attributes=attributes,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'workload-protection-instance-1'
        assert req_body['attributes'] == {'anyKey': 'anyValue'}

    def test_create_provider_type_instance_all_params_with_retries(self):
        # Enable retries and run test_create_provider_type_instance_all_params.
        _service.enable_retries()
        self.test_create_provider_type_instance_all_params()

        # Disable retries and run test_create_provider_type_instance_all_params.
        _service.disable_retries()
        self.test_create_provider_type_instance_all_params()

    @responses.activate
    def test_create_provider_type_instance_required_params(self):
        """
        test_create_provider_type_instance_required_params()
        """
        # Set up mock
        url = preprocess_url('/provider_types/testString/provider_type_instances')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        name = 'workload-protection-instance-1'
        attributes = {'anyKey': 'anyValue'}

        # Invoke method
        response = _service.create_provider_type_instance(
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
        assert req_body['attributes'] == {'anyKey': 'anyValue'}

    def test_create_provider_type_instance_required_params_with_retries(self):
        # Enable retries and run test_create_provider_type_instance_required_params.
        _service.enable_retries()
        self.test_create_provider_type_instance_required_params()

        # Disable retries and run test_create_provider_type_instance_required_params.
        _service.disable_retries()
        self.test_create_provider_type_instance_required_params()

    @responses.activate
    def test_create_provider_type_instance_value_error(self):
        """
        test_create_provider_type_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/provider_types/testString/provider_type_instances')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        name = 'workload-protection-instance-1'
        attributes = {'anyKey': 'anyValue'}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = preprocess_url('/provider_types/testString/provider_type_instances/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        provider_type_instance_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.delete_provider_type_instance(
            provider_type_id,
            provider_type_instance_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
    def test_delete_provider_type_instance_required_params(self):
        """
        test_delete_provider_type_instance_required_params()
        """
        # Set up mock
        url = preprocess_url('/provider_types/testString/provider_type_instances/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        provider_type_instance_id = 'testString'

        # Invoke method
        response = _service.delete_provider_type_instance(
            provider_type_id,
            provider_type_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_provider_type_instance_required_params_with_retries(self):
        # Enable retries and run test_delete_provider_type_instance_required_params.
        _service.enable_retries()
        self.test_delete_provider_type_instance_required_params()

        # Disable retries and run test_delete_provider_type_instance_required_params.
        _service.disable_retries()
        self.test_delete_provider_type_instance_required_params()

    @responses.activate
    def test_delete_provider_type_instance_value_error(self):
        """
        test_delete_provider_type_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/provider_types/testString/provider_type_instances/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        provider_type_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = preprocess_url('/provider_types/testString/provider_type_instances/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        provider_type_instance_id = 'testString'
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.get_provider_type_instance(
            provider_type_id,
            provider_type_instance_id,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
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
    def test_get_provider_type_instance_required_params(self):
        """
        test_get_provider_type_instance_required_params()
        """
        # Set up mock
        url = preprocess_url('/provider_types/testString/provider_type_instances/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        provider_type_instance_id = 'testString'

        # Invoke method
        response = _service.get_provider_type_instance(
            provider_type_id,
            provider_type_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_provider_type_instance_required_params_with_retries(self):
        # Enable retries and run test_get_provider_type_instance_required_params.
        _service.enable_retries()
        self.test_get_provider_type_instance_required_params()

        # Disable retries and run test_get_provider_type_instance_required_params.
        _service.disable_retries()
        self.test_get_provider_type_instance_required_params()

    @responses.activate
    def test_get_provider_type_instance_value_error(self):
        """
        test_get_provider_type_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/provider_types/testString/provider_type_instances/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        provider_type_instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = preprocess_url('/provider_types/testString/provider_type_instances/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        provider_type_instance_id = 'testString'
        name = 'workload-protection-instance-1'
        attributes = {'anyKey': 'anyValue'}
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.update_provider_type_instance(
            provider_type_id,
            provider_type_instance_id,
            name=name,
            attributes=attributes,
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'workload-protection-instance-1'
        assert req_body['attributes'] == {'anyKey': 'anyValue'}

    def test_update_provider_type_instance_all_params_with_retries(self):
        # Enable retries and run test_update_provider_type_instance_all_params.
        _service.enable_retries()
        self.test_update_provider_type_instance_all_params()

        # Disable retries and run test_update_provider_type_instance_all_params.
        _service.disable_retries()
        self.test_update_provider_type_instance_all_params()

    @responses.activate
    def test_update_provider_type_instance_required_params(self):
        """
        test_update_provider_type_instance_required_params()
        """
        # Set up mock
        url = preprocess_url('/provider_types/testString/provider_type_instances/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        provider_type_instance_id = 'testString'
        name = 'workload-protection-instance-1'
        attributes = {'anyKey': 'anyValue'}

        # Invoke method
        response = _service.update_provider_type_instance(
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
        assert req_body['attributes'] == {'anyKey': 'anyValue'}

    def test_update_provider_type_instance_required_params_with_retries(self):
        # Enable retries and run test_update_provider_type_instance_required_params.
        _service.enable_retries()
        self.test_update_provider_type_instance_required_params()

        # Disable retries and run test_update_provider_type_instance_required_params.
        _service.disable_retries()
        self.test_update_provider_type_instance_required_params()

    @responses.activate
    def test_update_provider_type_instance_value_error(self):
        """
        test_update_provider_type_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/provider_types/testString/provider_type_instances/testString')
        mock_response = '{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        provider_type_id = 'testString'
        provider_type_instance_id = 'testString'
        name = 'workload-protection-instance-1'
        attributes = {'anyKey': 'anyValue'}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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


class TestGetProviderTypesInstances:
    """
    Test Class for get_provider_types_instances
    """

    @responses.activate
    def test_get_provider_types_instances_all_params(self):
        """
        get_provider_types_instances()
        """
        # Set up mock
        url = preprocess_url('/provider_types_instances')
        mock_response = '{"provider_types_instances": [{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        x_correlation_id = 'testString'
        x_request_id = 'testString'

        # Invoke method
        response = _service.get_provider_types_instances(
            x_correlation_id=x_correlation_id,
            x_request_id=x_request_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_provider_types_instances_all_params_with_retries(self):
        # Enable retries and run test_get_provider_types_instances_all_params.
        _service.enable_retries()
        self.test_get_provider_types_instances_all_params()

        # Disable retries and run test_get_provider_types_instances_all_params.
        _service.disable_retries()
        self.test_get_provider_types_instances_all_params()

    @responses.activate
    def test_get_provider_types_instances_required_params(self):
        """
        test_get_provider_types_instances_required_params()
        """
        # Set up mock
        url = preprocess_url('/provider_types_instances')
        mock_response = '{"provider_types_instances": [{"id": "7588190cce3c05ac8f7942ea597dafce", "type": "workload-protection", "name": "workload-protection-instance-1", "attributes": {"anyKey": "anyValue"}, "created_at": "2023-07-24T13:14:18.884Z", "updated_at": "2023-07-24T13:14:18.884Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_provider_types_instances()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_provider_types_instances_required_params_with_retries(self):
        # Enable retries and run test_get_provider_types_instances_required_params.
        _service.enable_retries()
        self.test_get_provider_types_instances_required_params()

        # Disable retries and run test_get_provider_types_instances_required_params.
        _service.disable_retries()
        self.test_get_provider_types_instances_required_params()


# endregion
##############################################################################
# End of Service: ProviderTypeInstances
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

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'location'
        parameter_info_model['parameter_display_name'] = 'Location'
        parameter_info_model['parameter_type'] = 'string'
        parameter_info_model['parameter_value'] = 'public'

        # Construct a json representation of a Assessment model
        assessment_model_json = {}
        assessment_model_json['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model_json['assessment_type'] = 'ibm-cloud-rule'
        assessment_model_json['assessment_method'] = 'ibm-cloud-rule'
        assessment_model_json['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model_json['parameter_count'] = 1
        assessment_model_json['parameters'] = [parameter_info_model]

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


class TestModel_Attachment:
    """
    Test Class for Attachment
    """

    def test_attachment_serialization(self):
        """
        Test serialization/deserialization for Attachment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_property_model = {}  # ScopeProperty
        scope_property_model['name'] = 'scope_id'
        scope_property_model['value'] = '18d32a4430e54c81a6668952609763b2'

        attachment_scope_model = {}  # AttachmentScope
        attachment_scope_model['id'] = 'ca0941aa-b7e2-43a3-9794-1b3d322474d9'
        attachment_scope_model['environment'] = 'ibm-cloud'
        attachment_scope_model['properties'] = [scope_property_model]

        # Construct a json representation of a Attachment model
        attachment_model_json = {}
        attachment_model_json['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        attachment_model_json['name'] = 'resource group - Default'
        attachment_model_json['description'] = 'Scoped to the Default resource group'
        attachment_model_json['schedule'] = 'daily'
        attachment_model_json['scope'] = [attachment_scope_model]

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


class TestModel_AttachmentCollection:
    """
    Test Class for AttachmentCollection
    """

    def test_attachment_collection_serialization(self):
        """
        Test serialization/deserialization for AttachmentCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        paginated_collection_first_model = {}  # PaginatedCollectionFirst
        paginated_collection_first_model['href'] = 'href'

        paginated_collection_next_model = {}  # PaginatedCollectionNext
        paginated_collection_next_model['href'] = 'href'
        paginated_collection_next_model['start'] = 'start'

        property_item_model = {}  # PropertyItem
        property_item_model['name'] = 'name'
        property_item_model['value'] = 'value'

        multi_cloud_scope_model = {}  # MultiCloudScope
        multi_cloud_scope_model['environment'] = 'environment'
        multi_cloud_scope_model['properties'] = [property_item_model]

        failed_controls_model = {}  # FailedControls
        failed_controls_model['threshold_limit'] = 0
        failed_controls_model['failed_control_ids'] = ['5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF']

        attachments_notifications_prototype_model = {}  # AttachmentsNotificationsPrototype
        attachments_notifications_prototype_model['enabled'] = True
        attachments_notifications_prototype_model['controls'] = failed_controls_model

        attachment_parameter_prototype_model = {}  # AttachmentParameterPrototype
        attachment_parameter_prototype_model['assessment_type'] = 'assessment_type'
        attachment_parameter_prototype_model['assessment_id'] = 'assessment_id'
        attachment_parameter_prototype_model['parameter_name'] = 'parameter_name'
        attachment_parameter_prototype_model['parameter_value'] = 'parameter_value'
        attachment_parameter_prototype_model['parameter_display_name'] = 'parameter_display_name'
        attachment_parameter_prototype_model['parameter_type'] = 'string'

        last_scan_model = {}  # LastScan
        last_scan_model['id'] = 'e8a39d25-0051-4328-8462-988ad321f49a'
        last_scan_model['status'] = 'in_progress'
        last_scan_model['time'] = '2000-01-23T04:56:07Z'

        attachment_item_model = {}  # AttachmentItem
        attachment_item_model['id'] = '130003ea8bfa43c5aacea07a86da3000'
        attachment_item_model['profile_id'] = '7ec45986-54fc-4b66-a303-d9577b078c65'
        attachment_item_model['account_id'] = '130003ea8bfa43c5aacea07a86da3000'
        attachment_item_model['instance_id'] = 'edf9524f-406c-412c-acbb-ee371a5cabda'
        attachment_item_model['scope'] = [multi_cloud_scope_model]
        attachment_item_model['created_on'] = '2000-01-23T04:56:07Z'
        attachment_item_model['created_by'] = 'created_by'
        attachment_item_model['updated_on'] = '2000-01-23T04:56:07Z'
        attachment_item_model['updated_by'] = 'updated_by'
        attachment_item_model['status'] = 'enabled'
        attachment_item_model['schedule'] = 'daily'
        attachment_item_model['notifications'] = attachments_notifications_prototype_model
        attachment_item_model['attachment_parameters'] = [attachment_parameter_prototype_model]
        attachment_item_model['last_scan'] = last_scan_model
        attachment_item_model['next_scan_time'] = '2000-01-23T04:56:07Z'
        attachment_item_model['name'] = 'account-130003ea8bfa43c5aacea07a86da3000'
        attachment_item_model['description'] = 'Test description'

        # Construct a json representation of a AttachmentCollection model
        attachment_collection_model_json = {}
        attachment_collection_model_json['total_count'] = 1
        attachment_collection_model_json['limit'] = 20
        attachment_collection_model_json['first'] = paginated_collection_first_model
        attachment_collection_model_json['next'] = paginated_collection_next_model
        attachment_collection_model_json['attachments'] = [attachment_item_model]

        # Construct a model instance of AttachmentCollection by calling from_dict on the json representation
        attachment_collection_model = AttachmentCollection.from_dict(attachment_collection_model_json)
        assert attachment_collection_model != False

        # Construct a model instance of AttachmentCollection by calling from_dict on the json representation
        attachment_collection_model_dict = AttachmentCollection.from_dict(attachment_collection_model_json).__dict__
        attachment_collection_model2 = AttachmentCollection(**attachment_collection_model_dict)

        # Verify the model instances are equivalent
        assert attachment_collection_model == attachment_collection_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_collection_model_json2 = attachment_collection_model.to_dict()
        assert attachment_collection_model_json2 == attachment_collection_model_json


class TestModel_AttachmentItem:
    """
    Test Class for AttachmentItem
    """

    def test_attachment_item_serialization(self):
        """
        Test serialization/deserialization for AttachmentItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        property_item_model = {}  # PropertyItem
        property_item_model['name'] = 'name'
        property_item_model['value'] = 'value'

        multi_cloud_scope_model = {}  # MultiCloudScope
        multi_cloud_scope_model['environment'] = 'environment'
        multi_cloud_scope_model['properties'] = [property_item_model]

        failed_controls_model = {}  # FailedControls
        failed_controls_model['threshold_limit'] = 0
        failed_controls_model['failed_control_ids'] = ['5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF']

        attachments_notifications_prototype_model = {}  # AttachmentsNotificationsPrototype
        attachments_notifications_prototype_model['enabled'] = True
        attachments_notifications_prototype_model['controls'] = failed_controls_model

        attachment_parameter_prototype_model = {}  # AttachmentParameterPrototype
        attachment_parameter_prototype_model['assessment_type'] = 'assessment_type'
        attachment_parameter_prototype_model['assessment_id'] = 'assessment_id'
        attachment_parameter_prototype_model['parameter_name'] = 'parameter_name'
        attachment_parameter_prototype_model['parameter_value'] = 'parameter_value'
        attachment_parameter_prototype_model['parameter_display_name'] = 'parameter_display_name'
        attachment_parameter_prototype_model['parameter_type'] = 'string'

        last_scan_model = {}  # LastScan
        last_scan_model['id'] = 'e8a39d25-0051-4328-8462-988ad321f49a'
        last_scan_model['status'] = 'in_progress'
        last_scan_model['time'] = '2000-01-23T04:56:07Z'

        # Construct a json representation of a AttachmentItem model
        attachment_item_model_json = {}
        attachment_item_model_json['id'] = '130003ea8bfa43c5aacea07a86da3000'
        attachment_item_model_json['profile_id'] = '7ec45986-54fc-4b66-a303-d9577b078c65'
        attachment_item_model_json['account_id'] = '130003ea8bfa43c5aacea07a86da3000'
        attachment_item_model_json['instance_id'] = 'edf9524f-406c-412c-acbb-ee371a5cabda'
        attachment_item_model_json['scope'] = [multi_cloud_scope_model]
        attachment_item_model_json['created_on'] = '2019-01-01T12:00:00Z'
        attachment_item_model_json['created_by'] = 'testString'
        attachment_item_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        attachment_item_model_json['updated_by'] = 'testString'
        attachment_item_model_json['status'] = 'enabled'
        attachment_item_model_json['schedule'] = 'daily'
        attachment_item_model_json['notifications'] = attachments_notifications_prototype_model
        attachment_item_model_json['attachment_parameters'] = [attachment_parameter_prototype_model]
        attachment_item_model_json['last_scan'] = last_scan_model
        attachment_item_model_json['next_scan_time'] = '2019-01-01T12:00:00Z'
        attachment_item_model_json['name'] = 'account-130003ea8bfa43c5aacea07a86da3000'
        attachment_item_model_json['description'] = 'Test description'

        # Construct a model instance of AttachmentItem by calling from_dict on the json representation
        attachment_item_model = AttachmentItem.from_dict(attachment_item_model_json)
        assert attachment_item_model != False

        # Construct a model instance of AttachmentItem by calling from_dict on the json representation
        attachment_item_model_dict = AttachmentItem.from_dict(attachment_item_model_json).__dict__
        attachment_item_model2 = AttachmentItem(**attachment_item_model_dict)

        # Verify the model instances are equivalent
        assert attachment_item_model == attachment_item_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_item_model_json2 = attachment_item_model.to_dict()
        assert attachment_item_model_json2 == attachment_item_model_json


class TestModel_AttachmentParameterPrototype:
    """
    Test Class for AttachmentParameterPrototype
    """

    def test_attachment_parameter_prototype_serialization(self):
        """
        Test serialization/deserialization for AttachmentParameterPrototype
        """

        # Construct a json representation of a AttachmentParameterPrototype model
        attachment_parameter_prototype_model_json = {}
        attachment_parameter_prototype_model_json['assessment_type'] = 'testString'
        attachment_parameter_prototype_model_json['assessment_id'] = 'testString'
        attachment_parameter_prototype_model_json['parameter_name'] = 'testString'
        attachment_parameter_prototype_model_json['parameter_value'] = 'testString'
        attachment_parameter_prototype_model_json['parameter_display_name'] = 'testString'
        attachment_parameter_prototype_model_json['parameter_type'] = 'string'

        # Construct a model instance of AttachmentParameterPrototype by calling from_dict on the json representation
        attachment_parameter_prototype_model = AttachmentParameterPrototype.from_dict(attachment_parameter_prototype_model_json)
        assert attachment_parameter_prototype_model != False

        # Construct a model instance of AttachmentParameterPrototype by calling from_dict on the json representation
        attachment_parameter_prototype_model_dict = AttachmentParameterPrototype.from_dict(attachment_parameter_prototype_model_json).__dict__
        attachment_parameter_prototype_model2 = AttachmentParameterPrototype(**attachment_parameter_prototype_model_dict)

        # Verify the model instances are equivalent
        assert attachment_parameter_prototype_model == attachment_parameter_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_parameter_prototype_model_json2 = attachment_parameter_prototype_model.to_dict()
        assert attachment_parameter_prototype_model_json2 == attachment_parameter_prototype_model_json


class TestModel_AttachmentPrototype:
    """
    Test Class for AttachmentPrototype
    """

    def test_attachment_prototype_serialization(self):
        """
        Test serialization/deserialization for AttachmentPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        property_item_model = {}  # PropertyItem
        property_item_model['name'] = 'name'
        property_item_model['value'] = 'value'

        multi_cloud_scope_model = {}  # MultiCloudScope
        multi_cloud_scope_model['environment'] = 'environment'
        multi_cloud_scope_model['properties'] = [property_item_model]

        failed_controls_model = {}  # FailedControls
        failed_controls_model['threshold_limit'] = 0
        failed_controls_model['failed_control_ids'] = ['5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF']

        attachments_notifications_prototype_model = {}  # AttachmentsNotificationsPrototype
        attachments_notifications_prototype_model['enabled'] = True
        attachments_notifications_prototype_model['controls'] = failed_controls_model

        attachment_parameter_prototype_model = {}  # AttachmentParameterPrototype
        attachment_parameter_prototype_model['assessment_type'] = 'assessment_type'
        attachment_parameter_prototype_model['assessment_id'] = 'assessment_id'
        attachment_parameter_prototype_model['parameter_name'] = 'parameter_name'
        attachment_parameter_prototype_model['parameter_value'] = 'parameter_value'
        attachment_parameter_prototype_model['parameter_display_name'] = 'parameter_display_name'
        attachment_parameter_prototype_model['parameter_type'] = 'string'

        attachments_prototype_model = {}  # AttachmentsPrototype
        attachments_prototype_model['id'] = '130003ea8bfa43c5aacea07a86da3000'
        attachments_prototype_model['name'] = 'account-130003ea8bfa43c5aacea07a86da3000'
        attachments_prototype_model['description'] = 'Test description'
        attachments_prototype_model['scope'] = [multi_cloud_scope_model]
        attachments_prototype_model['status'] = 'enabled'
        attachments_prototype_model['schedule'] = 'daily'
        attachments_prototype_model['notifications'] = attachments_notifications_prototype_model
        attachments_prototype_model['attachment_parameters'] = [attachment_parameter_prototype_model]

        # Construct a json representation of a AttachmentPrototype model
        attachment_prototype_model_json = {}
        attachment_prototype_model_json['profile_id'] = 'testString'
        attachment_prototype_model_json['attachments'] = [attachments_prototype_model]

        # Construct a model instance of AttachmentPrototype by calling from_dict on the json representation
        attachment_prototype_model = AttachmentPrototype.from_dict(attachment_prototype_model_json)
        assert attachment_prototype_model != False

        # Construct a model instance of AttachmentPrototype by calling from_dict on the json representation
        attachment_prototype_model_dict = AttachmentPrototype.from_dict(attachment_prototype_model_json).__dict__
        attachment_prototype_model2 = AttachmentPrototype(**attachment_prototype_model_dict)

        # Verify the model instances are equivalent
        assert attachment_prototype_model == attachment_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_prototype_model_json2 = attachment_prototype_model.to_dict()
        assert attachment_prototype_model_json2 == attachment_prototype_model_json


class TestModel_AttachmentScope:
    """
    Test Class for AttachmentScope
    """

    def test_attachment_scope_serialization(self):
        """
        Test serialization/deserialization for AttachmentScope
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_property_model = {}  # ScopeProperty
        scope_property_model['name'] = 'scope_id'
        scope_property_model['value'] = '18d32a4430e54c81a6668952609763b2'

        # Construct a json representation of a AttachmentScope model
        attachment_scope_model_json = {}
        attachment_scope_model_json['id'] = 'ca0941aa-b7e2-43a3-9794-1b3d322474d9'
        attachment_scope_model_json['environment'] = 'ibm-cloud'
        attachment_scope_model_json['properties'] = [scope_property_model]

        # Construct a model instance of AttachmentScope by calling from_dict on the json representation
        attachment_scope_model = AttachmentScope.from_dict(attachment_scope_model_json)
        assert attachment_scope_model != False

        # Construct a model instance of AttachmentScope by calling from_dict on the json representation
        attachment_scope_model_dict = AttachmentScope.from_dict(attachment_scope_model_json).__dict__
        attachment_scope_model2 = AttachmentScope(**attachment_scope_model_dict)

        # Verify the model instances are equivalent
        assert attachment_scope_model == attachment_scope_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_scope_model_json2 = attachment_scope_model.to_dict()
        assert attachment_scope_model_json2 == attachment_scope_model_json


class TestModel_AttachmentsNotificationsPrototype:
    """
    Test Class for AttachmentsNotificationsPrototype
    """

    def test_attachments_notifications_prototype_serialization(self):
        """
        Test serialization/deserialization for AttachmentsNotificationsPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        failed_controls_model = {}  # FailedControls
        failed_controls_model['threshold_limit'] = 0
        failed_controls_model['failed_control_ids'] = ['5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF']

        # Construct a json representation of a AttachmentsNotificationsPrototype model
        attachments_notifications_prototype_model_json = {}
        attachments_notifications_prototype_model_json['enabled'] = True
        attachments_notifications_prototype_model_json['controls'] = failed_controls_model

        # Construct a model instance of AttachmentsNotificationsPrototype by calling from_dict on the json representation
        attachments_notifications_prototype_model = AttachmentsNotificationsPrototype.from_dict(attachments_notifications_prototype_model_json)
        assert attachments_notifications_prototype_model != False

        # Construct a model instance of AttachmentsNotificationsPrototype by calling from_dict on the json representation
        attachments_notifications_prototype_model_dict = AttachmentsNotificationsPrototype.from_dict(attachments_notifications_prototype_model_json).__dict__
        attachments_notifications_prototype_model2 = AttachmentsNotificationsPrototype(**attachments_notifications_prototype_model_dict)

        # Verify the model instances are equivalent
        assert attachments_notifications_prototype_model == attachments_notifications_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        attachments_notifications_prototype_model_json2 = attachments_notifications_prototype_model.to_dict()
        assert attachments_notifications_prototype_model_json2 == attachments_notifications_prototype_model_json


class TestModel_AttachmentsPrototype:
    """
    Test Class for AttachmentsPrototype
    """

    def test_attachments_prototype_serialization(self):
        """
        Test serialization/deserialization for AttachmentsPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        property_item_model = {}  # PropertyItem
        property_item_model['name'] = 'name'
        property_item_model['value'] = 'value'

        multi_cloud_scope_model = {}  # MultiCloudScope
        multi_cloud_scope_model['environment'] = 'environment'
        multi_cloud_scope_model['properties'] = [property_item_model]

        failed_controls_model = {}  # FailedControls
        failed_controls_model['threshold_limit'] = 0
        failed_controls_model['failed_control_ids'] = ['5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF', '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF']

        attachments_notifications_prototype_model = {}  # AttachmentsNotificationsPrototype
        attachments_notifications_prototype_model['enabled'] = True
        attachments_notifications_prototype_model['controls'] = failed_controls_model

        attachment_parameter_prototype_model = {}  # AttachmentParameterPrototype
        attachment_parameter_prototype_model['assessment_type'] = 'assessment_type'
        attachment_parameter_prototype_model['assessment_id'] = 'assessment_id'
        attachment_parameter_prototype_model['parameter_name'] = 'parameter_name'
        attachment_parameter_prototype_model['parameter_value'] = 'parameter_value'
        attachment_parameter_prototype_model['parameter_display_name'] = 'parameter_display_name'
        attachment_parameter_prototype_model['parameter_type'] = 'string'

        # Construct a json representation of a AttachmentsPrototype model
        attachments_prototype_model_json = {}
        attachments_prototype_model_json['id'] = '130003ea8bfa43c5aacea07a86da3000'
        attachments_prototype_model_json['name'] = 'account-130003ea8bfa43c5aacea07a86da3000'
        attachments_prototype_model_json['description'] = 'Test description'
        attachments_prototype_model_json['scope'] = [multi_cloud_scope_model]
        attachments_prototype_model_json['status'] = 'enabled'
        attachments_prototype_model_json['schedule'] = 'daily'
        attachments_prototype_model_json['notifications'] = attachments_notifications_prototype_model
        attachments_prototype_model_json['attachment_parameters'] = [attachment_parameter_prototype_model]

        # Construct a model instance of AttachmentsPrototype by calling from_dict on the json representation
        attachments_prototype_model = AttachmentsPrototype.from_dict(attachments_prototype_model_json)
        assert attachments_prototype_model != False

        # Construct a model instance of AttachmentsPrototype by calling from_dict on the json representation
        attachments_prototype_model_dict = AttachmentsPrototype.from_dict(attachments_prototype_model_json).__dict__
        attachments_prototype_model2 = AttachmentsPrototype(**attachments_prototype_model_dict)

        # Verify the model instances are equivalent
        assert attachments_prototype_model == attachments_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        attachments_prototype_model_json2 = attachments_prototype_model.to_dict()
        assert attachments_prototype_model_json2 == attachments_prototype_model_json


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


class TestModel_ControlDocs:
    """
    Test Class for ControlDocs
    """

    def test_control_docs_serialization(self):
        """
        Test serialization/deserialization for ControlDocs
        """

        # Construct a json representation of a ControlDocs model
        control_docs_model_json = {}
        control_docs_model_json['control_docs_id'] = 'testString'
        control_docs_model_json['control_docs_type'] = 'testString'

        # Construct a model instance of ControlDocs by calling from_dict on the json representation
        control_docs_model = ControlDocs.from_dict(control_docs_model_json)
        assert control_docs_model != False

        # Construct a model instance of ControlDocs by calling from_dict on the json representation
        control_docs_model_dict = ControlDocs.from_dict(control_docs_model_json).__dict__
        control_docs_model2 = ControlDocs(**control_docs_model_dict)

        # Verify the model instances are equivalent
        assert control_docs_model == control_docs_model2

        # Convert model instance back to dict and verify no loss of data
        control_docs_model_json2 = control_docs_model.to_dict()
        assert control_docs_model_json2 == control_docs_model_json


class TestModel_ControlLibrary:
    """
    Test Class for ControlLibrary
    """

    def test_control_library_serialization(self):
        """
        Test serialization/deserialization for ControlLibrary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'parameter_name'
        parameter_info_model['parameter_display_name'] = 'parameter_display_name'
        parameter_info_model['parameter_type'] = 'string'
        parameter_info_model['parameter_value'] = 'public'

        implementation_model = {}  # Implementation
        implementation_model['assessment_id'] = 'assessment_id'
        implementation_model['assessment_method'] = 'assessment_method'
        implementation_model['assessment_type'] = 'assessment_type'
        implementation_model['assessment_description'] = 'assessment_description'
        implementation_model['parameter_count'] = 5
        implementation_model['parameters'] = [parameter_info_model]

        control_specifications_model = {}  # ControlSpecifications
        control_specifications_model['control_specification_id'] = 'f3517159-889e-4781-819a-89d89b747c85'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'f3517159-889e-4781-819a-89d89b747c85'
        control_specifications_model['componenet_name'] = 'componenet_name'
        control_specifications_model['environment'] = 'environment'
        control_specifications_model['control_specification_description'] = 'control_specification_description'
        control_specifications_model['assessments_count'] = 1
        control_specifications_model['assessments'] = [implementation_model]

        control_docs_model = {}  # ControlDocs
        control_docs_model['control_docs_id'] = 'control_docs_id'
        control_docs_model['control_docs_type'] = 'control_docs_type'

        controls_in_control_lib_model = {}  # ControlsInControlLib
        controls_in_control_lib_model['control_name'] = 'control_name'
        controls_in_control_lib_model['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'
        controls_in_control_lib_model['control_description'] = 'control_description'
        controls_in_control_lib_model['control_category'] = 'control_category'
        controls_in_control_lib_model['control_parent'] = 'control_parent'
        controls_in_control_lib_model['control_tags'] = ['control_tags', 'control_tags', 'control_tags', 'control_tags', 'control_tags']
        controls_in_control_lib_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_model['control_docs'] = control_docs_model
        controls_in_control_lib_model['control_requirement'] = True
        controls_in_control_lib_model['status'] = 'enabled'

        # Construct a json representation of a ControlLibrary model
        control_library_model_json = {}
        control_library_model_json['id'] = 'f3517159-889e-4781-819a-89d89b747c85'
        control_library_model_json['account_id'] = '130003ea8bfa43c5aacea07a86da3000'
        control_library_model_json['control_library_name'] = 'testString'
        control_library_model_json['control_library_description'] = 'testString'
        control_library_model_json['control_library_type'] = 'predefined'
        control_library_model_json['version_group_label'] = 'e0923045-f00d-44de-b49b-6f1f0e8033cc'
        control_library_model_json['control_library_version'] = 'testString'
        control_library_model_json['created_on'] = '2019-01-01T12:00:00Z'
        control_library_model_json['created_by'] = 'testString'
        control_library_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        control_library_model_json['updated_by'] = 'testString'
        control_library_model_json['latest'] = True
        control_library_model_json['hierarchy_enabled'] = True
        control_library_model_json['controls_count'] = 38
        control_library_model_json['control_parents_count'] = 38
        control_library_model_json['controls'] = [controls_in_control_lib_model]

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

        paginated_collection_first_model = {}  # PaginatedCollectionFirst
        paginated_collection_first_model['href'] = 'href'

        paginated_collection_next_model = {}  # PaginatedCollectionNext
        paginated_collection_next_model['href'] = 'href'
        paginated_collection_next_model['start'] = 'start'

        control_library_item_model = {}  # ControlLibraryItem
        control_library_item_model['id'] = 'id'
        control_library_item_model['account_id'] = 'account_id'
        control_library_item_model['control_library_name'] = 'control_library_name'
        control_library_item_model['control_library_description'] = 'control_library_description'
        control_library_item_model['control_library_type'] = 'control_library_type'
        control_library_item_model['created_on'] = '2000-01-23T04:56:07Z'
        control_library_item_model['created_by'] = 'created_by'
        control_library_item_model['updated_on'] = '2000-01-23T04:56:07Z'
        control_library_item_model['updated_by'] = 'updated_by'
        control_library_item_model['version_group_label'] = 'version_group_label'
        control_library_item_model['control_library_version'] = 'control_library_version'
        control_library_item_model['latest'] = True
        control_library_item_model['controls_count'] = 0

        # Construct a json representation of a ControlLibraryCollection model
        control_library_collection_model_json = {}
        control_library_collection_model_json['total_count'] = 1
        control_library_collection_model_json['limit'] = 20
        control_library_collection_model_json['first'] = paginated_collection_first_model
        control_library_collection_model_json['next'] = paginated_collection_next_model
        control_library_collection_model_json['control_libraries'] = [control_library_item_model]

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


class TestModel_ControlLibraryDelete:
    """
    Test Class for ControlLibraryDelete
    """

    def test_control_library_delete_serialization(self):
        """
        Test serialization/deserialization for ControlLibraryDelete
        """

        # Construct a json representation of a ControlLibraryDelete model
        control_library_delete_model_json = {}
        control_library_delete_model_json['deleted'] = 'testString'

        # Construct a model instance of ControlLibraryDelete by calling from_dict on the json representation
        control_library_delete_model = ControlLibraryDelete.from_dict(control_library_delete_model_json)
        assert control_library_delete_model != False

        # Construct a model instance of ControlLibraryDelete by calling from_dict on the json representation
        control_library_delete_model_dict = ControlLibraryDelete.from_dict(control_library_delete_model_json).__dict__
        control_library_delete_model2 = ControlLibraryDelete(**control_library_delete_model_dict)

        # Verify the model instances are equivalent
        assert control_library_delete_model == control_library_delete_model2

        # Convert model instance back to dict and verify no loss of data
        control_library_delete_model_json2 = control_library_delete_model.to_dict()
        assert control_library_delete_model_json2 == control_library_delete_model_json


class TestModel_ControlLibraryItem:
    """
    Test Class for ControlLibraryItem
    """

    def test_control_library_item_serialization(self):
        """
        Test serialization/deserialization for ControlLibraryItem
        """

        # Construct a json representation of a ControlLibraryItem model
        control_library_item_model_json = {}
        control_library_item_model_json['id'] = 'testString'
        control_library_item_model_json['account_id'] = 'testString'
        control_library_item_model_json['control_library_name'] = 'testString'
        control_library_item_model_json['control_library_description'] = 'testString'
        control_library_item_model_json['control_library_type'] = 'testString'
        control_library_item_model_json['created_on'] = '2019-01-01T12:00:00Z'
        control_library_item_model_json['created_by'] = 'testString'
        control_library_item_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        control_library_item_model_json['updated_by'] = 'testString'
        control_library_item_model_json['version_group_label'] = 'testString'
        control_library_item_model_json['control_library_version'] = 'testString'
        control_library_item_model_json['latest'] = True
        control_library_item_model_json['controls_count'] = 38

        # Construct a model instance of ControlLibraryItem by calling from_dict on the json representation
        control_library_item_model = ControlLibraryItem.from_dict(control_library_item_model_json)
        assert control_library_item_model != False

        # Construct a model instance of ControlLibraryItem by calling from_dict on the json representation
        control_library_item_model_dict = ControlLibraryItem.from_dict(control_library_item_model_json).__dict__
        control_library_item_model2 = ControlLibraryItem(**control_library_item_model_dict)

        # Verify the model instances are equivalent
        assert control_library_item_model == control_library_item_model2

        # Convert model instance back to dict and verify no loss of data
        control_library_item_model_json2 = control_library_item_model.to_dict()
        assert control_library_item_model_json2 == control_library_item_model_json


class TestModel_ControlSpecificationWithStats:
    """
    Test Class for ControlSpecificationWithStats
    """

    def test_control_specification_with_stats_serialization(self):
        """
        Test serialization/deserialization for ControlSpecificationWithStats
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'location'
        parameter_info_model['parameter_display_name'] = 'Location'
        parameter_info_model['parameter_type'] = 'string'
        parameter_info_model['parameter_value'] = 'public'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_info_model]

        # Construct a json representation of a ControlSpecificationWithStats model
        control_specification_with_stats_model_json = {}
        control_specification_with_stats_model_json['control_specification_id'] = '18d32a4430e54c81a6668952609763b2'
        control_specification_with_stats_model_json['component_id'] = 'cloud-object_storage'
        control_specification_with_stats_model_json['control_specification_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        control_specification_with_stats_model_json['environment'] = 'ibm cloud'
        control_specification_with_stats_model_json['responsibility'] = 'user'
        control_specification_with_stats_model_json['assessments'] = [assessment_model]
        control_specification_with_stats_model_json['status'] = 'compliant'
        control_specification_with_stats_model_json['total_count'] = 150
        control_specification_with_stats_model_json['compliant_count'] = 130
        control_specification_with_stats_model_json['not_compliant_count'] = 5
        control_specification_with_stats_model_json['unable_to_perform_count'] = 5
        control_specification_with_stats_model_json['user_evaluation_required_count'] = 10

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


class TestModel_ControlSpecifications:
    """
    Test Class for ControlSpecifications
    """

    def test_control_specifications_serialization(self):
        """
        Test serialization/deserialization for ControlSpecifications
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'parameter_name'
        parameter_info_model['parameter_display_name'] = 'parameter_display_name'
        parameter_info_model['parameter_type'] = 'string'
        parameter_info_model['parameter_value'] = 'public'

        implementation_model = {}  # Implementation
        implementation_model['assessment_id'] = 'assessment_id'
        implementation_model['assessment_method'] = 'assessment_method'
        implementation_model['assessment_type'] = 'assessment_type'
        implementation_model['assessment_description'] = 'assessment_description'
        implementation_model['parameter_count'] = 5
        implementation_model['parameters'] = [parameter_info_model]

        # Construct a json representation of a ControlSpecifications model
        control_specifications_model_json = {}
        control_specifications_model_json['control_specification_id'] = 'f3517159-889e-4781-819a-89d89b747c85'
        control_specifications_model_json['responsibility'] = 'user'
        control_specifications_model_json['component_id'] = 'f3517159-889e-4781-819a-89d89b747c85'
        control_specifications_model_json['componenet_name'] = 'testString'
        control_specifications_model_json['environment'] = 'testString'
        control_specifications_model_json['control_specification_description'] = 'testString'
        control_specifications_model_json['assessments_count'] = 38
        control_specifications_model_json['assessments'] = [implementation_model]

        # Construct a model instance of ControlSpecifications by calling from_dict on the json representation
        control_specifications_model = ControlSpecifications.from_dict(control_specifications_model_json)
        assert control_specifications_model != False

        # Construct a model instance of ControlSpecifications by calling from_dict on the json representation
        control_specifications_model_dict = ControlSpecifications.from_dict(control_specifications_model_json).__dict__
        control_specifications_model2 = ControlSpecifications(**control_specifications_model_dict)

        # Verify the model instances are equivalent
        assert control_specifications_model == control_specifications_model2

        # Convert model instance back to dict and verify no loss of data
        control_specifications_model_json2 = control_specifications_model.to_dict()
        assert control_specifications_model_json2 == control_specifications_model_json


class TestModel_ControlWithStats:
    """
    Test Class for ControlWithStats
    """

    def test_control_with_stats_serialization(self):
        """
        Test serialization/deserialization for ControlWithStats
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'location'
        parameter_info_model['parameter_display_name'] = 'Location'
        parameter_info_model['parameter_type'] = 'string'
        parameter_info_model['parameter_value'] = 'public'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_info_model]

        control_specification_with_stats_model = {}  # ControlSpecificationWithStats
        control_specification_with_stats_model['control_specification_id'] = '18d32a4430e54c81a6668952609763b2'
        control_specification_with_stats_model['component_id'] = 'cloud-object_storage'
        control_specification_with_stats_model['control_specification_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        control_specification_with_stats_model['environment'] = 'ibm cloud'
        control_specification_with_stats_model['responsibility'] = 'user'
        control_specification_with_stats_model['assessments'] = [assessment_model]
        control_specification_with_stats_model['status'] = 'compliant'
        control_specification_with_stats_model['total_count'] = 150
        control_specification_with_stats_model['compliant_count'] = 130
        control_specification_with_stats_model['not_compliant_count'] = 5
        control_specification_with_stats_model['unable_to_perform_count'] = 5
        control_specification_with_stats_model['user_evaluation_required_count'] = 10

        # Construct a json representation of a ControlWithStats model
        control_with_stats_model_json = {}
        control_with_stats_model_json['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        control_with_stats_model_json['control_library_id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        control_with_stats_model_json['control_library_version'] = 'v1.2.3'
        control_with_stats_model_json['control_name'] = 'Password Management'
        control_with_stats_model_json['control_description'] = 'Password Management'
        control_with_stats_model_json['control_category'] = 'Access Control'
        control_with_stats_model_json['control_path'] = 'AC-2(a)'
        control_with_stats_model_json['control_specifications'] = [control_specification_with_stats_model]
        control_with_stats_model_json['status'] = 'compliant'
        control_with_stats_model_json['total_count'] = 150
        control_with_stats_model_json['compliant_count'] = 130
        control_with_stats_model_json['not_compliant_count'] = 5
        control_with_stats_model_json['unable_to_perform_count'] = 5
        control_with_stats_model_json['user_evaluation_required_count'] = 10

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


class TestModel_ControlsInControlLib:
    """
    Test Class for ControlsInControlLib
    """

    def test_controls_in_control_lib_serialization(self):
        """
        Test serialization/deserialization for ControlsInControlLib
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'parameter_name'
        parameter_info_model['parameter_display_name'] = 'parameter_display_name'
        parameter_info_model['parameter_type'] = 'string'
        parameter_info_model['parameter_value'] = 'public'

        implementation_model = {}  # Implementation
        implementation_model['assessment_id'] = 'assessment_id'
        implementation_model['assessment_method'] = 'assessment_method'
        implementation_model['assessment_type'] = 'assessment_type'
        implementation_model['assessment_description'] = 'assessment_description'
        implementation_model['parameter_count'] = 5
        implementation_model['parameters'] = [parameter_info_model]

        control_specifications_model = {}  # ControlSpecifications
        control_specifications_model['control_specification_id'] = 'f3517159-889e-4781-819a-89d89b747c85'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'f3517159-889e-4781-819a-89d89b747c85'
        control_specifications_model['componenet_name'] = 'componenet_name'
        control_specifications_model['environment'] = 'environment'
        control_specifications_model['control_specification_description'] = 'control_specification_description'
        control_specifications_model['assessments_count'] = 1
        control_specifications_model['assessments'] = [implementation_model]

        control_docs_model = {}  # ControlDocs
        control_docs_model['control_docs_id'] = 'control_docs_id'
        control_docs_model['control_docs_type'] = 'control_docs_type'

        # Construct a json representation of a ControlsInControlLib model
        controls_in_control_lib_model_json = {}
        controls_in_control_lib_model_json['control_name'] = 'testString'
        controls_in_control_lib_model_json['control_id'] = '1fa45e17-9322-4e6c-bbd6-1c51db08e790'
        controls_in_control_lib_model_json['control_description'] = 'testString'
        controls_in_control_lib_model_json['control_category'] = 'testString'
        controls_in_control_lib_model_json['control_parent'] = 'testString'
        controls_in_control_lib_model_json['control_tags'] = ['testString']
        controls_in_control_lib_model_json['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_model_json['control_docs'] = control_docs_model
        controls_in_control_lib_model_json['control_requirement'] = True
        controls_in_control_lib_model_json['status'] = 'enabled'

        # Construct a model instance of ControlsInControlLib by calling from_dict on the json representation
        controls_in_control_lib_model = ControlsInControlLib.from_dict(controls_in_control_lib_model_json)
        assert controls_in_control_lib_model != False

        # Construct a model instance of ControlsInControlLib by calling from_dict on the json representation
        controls_in_control_lib_model_dict = ControlsInControlLib.from_dict(controls_in_control_lib_model_json).__dict__
        controls_in_control_lib_model2 = ControlsInControlLib(**controls_in_control_lib_model_dict)

        # Verify the model instances are equivalent
        assert controls_in_control_lib_model == controls_in_control_lib_model2

        # Convert model instance back to dict and verify no loss of data
        controls_in_control_lib_model_json2 = controls_in_control_lib_model.to_dict()
        assert controls_in_control_lib_model_json2 == controls_in_control_lib_model_json


class TestModel_DefaultParametersPrototype:
    """
    Test Class for DefaultParametersPrototype
    """

    def test_default_parameters_prototype_serialization(self):
        """
        Test serialization/deserialization for DefaultParametersPrototype
        """

        # Construct a json representation of a DefaultParametersPrototype model
        default_parameters_prototype_model_json = {}
        default_parameters_prototype_model_json['assessment_type'] = 'testString'
        default_parameters_prototype_model_json['assessment_id'] = 'testString'
        default_parameters_prototype_model_json['parameter_name'] = 'testString'
        default_parameters_prototype_model_json['parameter_default_value'] = 'testString'
        default_parameters_prototype_model_json['parameter_display_name'] = 'testString'
        default_parameters_prototype_model_json['parameter_type'] = 'string'

        # Construct a model instance of DefaultParametersPrototype by calling from_dict on the json representation
        default_parameters_prototype_model = DefaultParametersPrototype.from_dict(default_parameters_prototype_model_json)
        assert default_parameters_prototype_model != False

        # Construct a model instance of DefaultParametersPrototype by calling from_dict on the json representation
        default_parameters_prototype_model_dict = DefaultParametersPrototype.from_dict(default_parameters_prototype_model_json).__dict__
        default_parameters_prototype_model2 = DefaultParametersPrototype(**default_parameters_prototype_model_dict)

        # Verify the model instances are equivalent
        assert default_parameters_prototype_model == default_parameters_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        default_parameters_prototype_model_json2 = default_parameters_prototype_model.to_dict()
        assert default_parameters_prototype_model_json2 == default_parameters_prototype_model_json


class TestModel_EvalDetails:
    """
    Test Class for EvalDetails
    """

    def test_eval_details_serialization(self):
        """
        Test serialization/deserialization for EvalDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        property_model = {}  # Property
        property_model['property'] = 'allowed_network'
        property_model['property_description'] = 'A description for this property'
        property_model['operator'] = 'string_equals'
        property_model['expected_value'] = 'public'
        property_model['found_value'] = 'public'

        # Construct a json representation of a EvalDetails model
        eval_details_model_json = {}
        eval_details_model_json['properties'] = [property_model]

        # Construct a model instance of EvalDetails by calling from_dict on the json representation
        eval_details_model = EvalDetails.from_dict(eval_details_model_json)
        assert eval_details_model != False

        # Construct a model instance of EvalDetails by calling from_dict on the json representation
        eval_details_model_dict = EvalDetails.from_dict(eval_details_model_json).__dict__
        eval_details_model2 = EvalDetails(**eval_details_model_dict)

        # Verify the model instances are equivalent
        assert eval_details_model == eval_details_model2

        # Convert model instance back to dict and verify no loss of data
        eval_details_model_json2 = eval_details_model.to_dict()
        assert eval_details_model_json2 == eval_details_model_json


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

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'location'
        parameter_info_model['parameter_display_name'] = 'Location'
        parameter_info_model['parameter_type'] = 'string'
        parameter_info_model['parameter_value'] = 'public'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_info_model]

        target_info_model = {}  # TargetInfo
        target_info_model['id'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket'
        target_info_model['account_id'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        target_info_model['resource_crn'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket'
        target_info_model['resource_name'] = 'mybucket'
        target_info_model['service_name'] = 'cloud-object-storage'

        property_model = {}  # Property
        property_model['property'] = 'allowed_network'
        property_model['property_description'] = 'A description for this property'
        property_model['operator'] = 'string_equals'
        property_model['expected_value'] = 'public'
        property_model['found_value'] = 'public'

        eval_details_model = {}  # EvalDetails
        eval_details_model['properties'] = [property_model]

        # Construct a json representation of a Evaluation model
        evaluation_model_json = {}
        evaluation_model_json['home_account_id'] = 'be200c80cabc456e91139e4152327456'
        evaluation_model_json['report_id'] = '44a5-a292-32114fa73558'
        evaluation_model_json['control_id'] = '28016c95-b389-447f-8a05-eabe1ad7fd24'
        evaluation_model_json['component_id'] = 'cloud-object_storage'
        evaluation_model_json['assessment'] = assessment_model
        evaluation_model_json['evaluate_time'] = '2022-06-30T11:03:44.630150782Z'
        evaluation_model_json['target'] = target_info_model
        evaluation_model_json['status'] = 'failure'
        evaluation_model_json['reason'] = 'One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met'
        evaluation_model_json['details'] = eval_details_model

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


class TestModel_EvaluationPage:
    """
    Test Class for EvaluationPage
    """

    def test_evaluation_page_serialization(self):
        """
        Test serialization/deserialization for EvaluationPage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_model = {}  # PageHRef
        page_h_ref_model['href'] = 'testString'

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'location'
        parameter_info_model['parameter_display_name'] = 'Location'
        parameter_info_model['parameter_type'] = 'string'
        parameter_info_model['parameter_value'] = 'public'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_info_model]

        target_info_model = {}  # TargetInfo
        target_info_model['id'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket'
        target_info_model['account_id'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        target_info_model['resource_crn'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket'
        target_info_model['resource_name'] = 'mybucket'
        target_info_model['service_name'] = 'cloud-object-storage'

        property_model = {}  # Property
        property_model['property'] = 'allowed_network'
        property_model['property_description'] = 'A description for this property'
        property_model['operator'] = 'string_equals'
        property_model['expected_value'] = 'public'
        property_model['found_value'] = 'public'

        eval_details_model = {}  # EvalDetails
        eval_details_model['properties'] = [property_model]

        evaluation_model = {}  # Evaluation
        evaluation_model['home_account_id'] = 'be200c80cabc456e91139e4152327456'
        evaluation_model['report_id'] = '44a5-a292-32114fa73558'
        evaluation_model['control_id'] = '28016c95-b389-447f-8a05-eabe1ad7fd24'
        evaluation_model['component_id'] = 'cloud-object_storage'
        evaluation_model['assessment'] = assessment_model
        evaluation_model['evaluate_time'] = '2022-06-30T11:03:44.630150782Z'
        evaluation_model['target'] = target_info_model
        evaluation_model['status'] = 'failure'
        evaluation_model['reason'] = 'One or more conditions in rule rule-7b0560a4-df94-4629-bb76-680f3155ddda were not met'
        evaluation_model['details'] = eval_details_model

        # Construct a json representation of a EvaluationPage model
        evaluation_page_model_json = {}
        evaluation_page_model_json['total_count'] = 230
        evaluation_page_model_json['limit'] = 50
        evaluation_page_model_json['start'] = 'testString'
        evaluation_page_model_json['first'] = page_h_ref_model
        evaluation_page_model_json['next'] = page_h_ref_model
        evaluation_page_model_json['home_account_id'] = 'testString'
        evaluation_page_model_json['report_id'] = 'testString'
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
        event_notifications_model_json['instance_crn'] = 'crn:v1:staging:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::'
        event_notifications_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        event_notifications_model_json['source_id'] = 'crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::'
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


class TestModel_FailedControls:
    """
    Test Class for FailedControls
    """

    def test_failed_controls_serialization(self):
        """
        Test serialization/deserialization for FailedControls
        """

        # Construct a json representation of a FailedControls model
        failed_controls_model_json = {}
        failed_controls_model_json['threshold_limit'] = 38
        failed_controls_model_json['failed_control_ids'] = ['5C453578-E9A1-421E-AD0F-C6AFCDD67CCF']

        # Construct a model instance of FailedControls by calling from_dict on the json representation
        failed_controls_model = FailedControls.from_dict(failed_controls_model_json)
        assert failed_controls_model != False

        # Construct a model instance of FailedControls by calling from_dict on the json representation
        failed_controls_model_dict = FailedControls.from_dict(failed_controls_model_json).__dict__
        failed_controls_model2 = FailedControls(**failed_controls_model_dict)

        # Verify the model instances are equivalent
        assert failed_controls_model == failed_controls_model2

        # Convert model instance back to dict and verify no loss of data
        failed_controls_model_json2 = failed_controls_model.to_dict()
        assert failed_controls_model_json2 == failed_controls_model_json


class TestModel_Implementation:
    """
    Test Class for Implementation
    """

    def test_implementation_serialization(self):
        """
        Test serialization/deserialization for Implementation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'parameter_name'
        parameter_info_model['parameter_display_name'] = 'parameter_display_name'
        parameter_info_model['parameter_type'] = 'string'
        parameter_info_model['parameter_value'] = 'public'

        # Construct a json representation of a Implementation model
        implementation_model_json = {}
        implementation_model_json['assessment_id'] = 'testString'
        implementation_model_json['assessment_method'] = 'testString'
        implementation_model_json['assessment_type'] = 'testString'
        implementation_model_json['assessment_description'] = 'testString'
        implementation_model_json['parameter_count'] = 38
        implementation_model_json['parameters'] = [parameter_info_model]

        # Construct a model instance of Implementation by calling from_dict on the json representation
        implementation_model = Implementation.from_dict(implementation_model_json)
        assert implementation_model != False

        # Construct a model instance of Implementation by calling from_dict on the json representation
        implementation_model_dict = Implementation.from_dict(implementation_model_json).__dict__
        implementation_model2 = Implementation(**implementation_model_dict)

        # Verify the model instances are equivalent
        assert implementation_model == implementation_model2

        # Convert model instance back to dict and verify no loss of data
        implementation_model_json2 = implementation_model.to_dict()
        assert implementation_model_json2 == implementation_model_json


class TestModel_Import:
    """
    Test Class for Import
    """

    def test_import_serialization(self):
        """
        Test serialization/deserialization for Import
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_model = {}  # Parameter
        parameter_model['name'] = 'name'
        parameter_model['display_name'] = 'display_name'
        parameter_model['description'] = 'description'
        parameter_model['type'] = 'string'

        # Construct a json representation of a Import model
        import_model_json = {}
        import_model_json['parameters'] = [parameter_model]

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
        last_scan_model_json['id'] = 'e8a39d25-0051-4328-8462-988ad321f49a'
        last_scan_model_json['status'] = 'in_progress'
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


class TestModel_MultiCloudScope:
    """
    Test Class for MultiCloudScope
    """

    def test_multi_cloud_scope_serialization(self):
        """
        Test serialization/deserialization for MultiCloudScope
        """

        # Construct dict forms of any model objects needed in order to build this model.

        property_item_model = {}  # PropertyItem
        property_item_model['name'] = 'name'
        property_item_model['value'] = 'value'

        # Construct a json representation of a MultiCloudScope model
        multi_cloud_scope_model_json = {}
        multi_cloud_scope_model_json['environment'] = 'testString'
        multi_cloud_scope_model_json['properties'] = [property_item_model]

        # Construct a model instance of MultiCloudScope by calling from_dict on the json representation
        multi_cloud_scope_model = MultiCloudScope.from_dict(multi_cloud_scope_model_json)
        assert multi_cloud_scope_model != False

        # Construct a model instance of MultiCloudScope by calling from_dict on the json representation
        multi_cloud_scope_model_dict = MultiCloudScope.from_dict(multi_cloud_scope_model_json).__dict__
        multi_cloud_scope_model2 = MultiCloudScope(**multi_cloud_scope_model_dict)

        # Verify the model instances are equivalent
        assert multi_cloud_scope_model == multi_cloud_scope_model2

        # Convert model instance back to dict and verify no loss of data
        multi_cloud_scope_model_json2 = multi_cloud_scope_model.to_dict()
        assert multi_cloud_scope_model_json2 == multi_cloud_scope_model_json


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


class TestModel_PageHRef:
    """
    Test Class for PageHRef
    """

    def test_page_h_ref_serialization(self):
        """
        Test serialization/deserialization for PageHRef
        """

        # Construct a json representation of a PageHRef model
        page_h_ref_model_json = {}
        page_h_ref_model_json['href'] = 'testString'

        # Construct a model instance of PageHRef by calling from_dict on the json representation
        page_h_ref_model = PageHRef.from_dict(page_h_ref_model_json)
        assert page_h_ref_model != False

        # Construct a model instance of PageHRef by calling from_dict on the json representation
        page_h_ref_model_dict = PageHRef.from_dict(page_h_ref_model_json).__dict__
        page_h_ref_model2 = PageHRef(**page_h_ref_model_dict)

        # Verify the model instances are equivalent
        assert page_h_ref_model == page_h_ref_model2

        # Convert model instance back to dict and verify no loss of data
        page_h_ref_model_json2 = page_h_ref_model.to_dict()
        assert page_h_ref_model_json2 == page_h_ref_model_json


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


class TestModel_PaginatedCollectionFirst:
    """
    Test Class for PaginatedCollectionFirst
    """

    def test_paginated_collection_first_serialization(self):
        """
        Test serialization/deserialization for PaginatedCollectionFirst
        """

        # Construct a json representation of a PaginatedCollectionFirst model
        paginated_collection_first_model_json = {}
        paginated_collection_first_model_json['href'] = 'testString'

        # Construct a model instance of PaginatedCollectionFirst by calling from_dict on the json representation
        paginated_collection_first_model = PaginatedCollectionFirst.from_dict(paginated_collection_first_model_json)
        assert paginated_collection_first_model != False

        # Construct a model instance of PaginatedCollectionFirst by calling from_dict on the json representation
        paginated_collection_first_model_dict = PaginatedCollectionFirst.from_dict(paginated_collection_first_model_json).__dict__
        paginated_collection_first_model2 = PaginatedCollectionFirst(**paginated_collection_first_model_dict)

        # Verify the model instances are equivalent
        assert paginated_collection_first_model == paginated_collection_first_model2

        # Convert model instance back to dict and verify no loss of data
        paginated_collection_first_model_json2 = paginated_collection_first_model.to_dict()
        assert paginated_collection_first_model_json2 == paginated_collection_first_model_json


class TestModel_PaginatedCollectionNext:
    """
    Test Class for PaginatedCollectionNext
    """

    def test_paginated_collection_next_serialization(self):
        """
        Test serialization/deserialization for PaginatedCollectionNext
        """

        # Construct a json representation of a PaginatedCollectionNext model
        paginated_collection_next_model_json = {}
        paginated_collection_next_model_json['href'] = 'testString'
        paginated_collection_next_model_json['start'] = 'testString'

        # Construct a model instance of PaginatedCollectionNext by calling from_dict on the json representation
        paginated_collection_next_model = PaginatedCollectionNext.from_dict(paginated_collection_next_model_json)
        assert paginated_collection_next_model != False

        # Construct a model instance of PaginatedCollectionNext by calling from_dict on the json representation
        paginated_collection_next_model_dict = PaginatedCollectionNext.from_dict(paginated_collection_next_model_json).__dict__
        paginated_collection_next_model2 = PaginatedCollectionNext(**paginated_collection_next_model_dict)

        # Verify the model instances are equivalent
        assert paginated_collection_next_model == paginated_collection_next_model2

        # Convert model instance back to dict and verify no loss of data
        paginated_collection_next_model_json2 = paginated_collection_next_model.to_dict()
        assert paginated_collection_next_model_json2 == paginated_collection_next_model_json


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
        parameter_model_json['name'] = 'testString'
        parameter_model_json['display_name'] = 'testString'
        parameter_model_json['description'] = 'testString'
        parameter_model_json['type'] = 'string'

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


class TestModel_ParameterInfo:
    """
    Test Class for ParameterInfo
    """

    def test_parameter_info_serialization(self):
        """
        Test serialization/deserialization for ParameterInfo
        """

        # Construct a json representation of a ParameterInfo model
        parameter_info_model_json = {}
        parameter_info_model_json['parameter_name'] = 'location'
        parameter_info_model_json['parameter_display_name'] = 'Location'
        parameter_info_model_json['parameter_type'] = 'string'
        parameter_info_model_json['parameter_value'] = 'public'

        # Construct a model instance of ParameterInfo by calling from_dict on the json representation
        parameter_info_model = ParameterInfo.from_dict(parameter_info_model_json)
        assert parameter_info_model != False

        # Construct a model instance of ParameterInfo by calling from_dict on the json representation
        parameter_info_model_dict = ParameterInfo.from_dict(parameter_info_model_json).__dict__
        parameter_info_model2 = ParameterInfo(**parameter_info_model_dict)

        # Verify the model instances are equivalent
        assert parameter_info_model == parameter_info_model2

        # Convert model instance back to dict and verify no loss of data
        parameter_info_model_json2 = parameter_info_model.to_dict()
        assert parameter_info_model_json2 == parameter_info_model_json


class TestModel_Profile:
    """
    Test Class for Profile
    """

    def test_profile_serialization(self):
        """
        Test serialization/deserialization for Profile
        """

        # Construct dict forms of any model objects needed in order to build this model.

        control_docs_model = {}  # ControlDocs
        control_docs_model['control_docs_id'] = 'control_docs_id'
        control_docs_model['control_docs_type'] = 'control_docs_type'

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'parameter_name'
        parameter_info_model['parameter_display_name'] = 'parameter_display_name'
        parameter_info_model['parameter_type'] = 'string'
        parameter_info_model['parameter_value'] = 'public'

        implementation_model = {}  # Implementation
        implementation_model['assessment_id'] = 'assessment_id'
        implementation_model['assessment_method'] = 'assessment_method'
        implementation_model['assessment_type'] = 'assessment_type'
        implementation_model['assessment_description'] = 'assessment_description'
        implementation_model['parameter_count'] = 5
        implementation_model['parameters'] = [parameter_info_model]

        control_specifications_model = {}  # ControlSpecifications
        control_specifications_model['control_specification_id'] = 'f3517159-889e-4781-819a-89d89b747c85'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'f3517159-889e-4781-819a-89d89b747c85'
        control_specifications_model['componenet_name'] = 'componenet_name'
        control_specifications_model['environment'] = 'environment'
        control_specifications_model['control_specification_description'] = 'control_specification_description'
        control_specifications_model['assessments_count'] = 1
        control_specifications_model['assessments'] = [implementation_model]

        profile_controls_model = {}  # ProfileControls
        profile_controls_model['control_library_id'] = 'e98a56ff-dc24-41d4-9875-1e188e2da6cd'
        profile_controls_model['control_id'] = '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF'
        profile_controls_model['control_library_version'] = 'control_library_version'
        profile_controls_model['control_name'] = 'control_name'
        profile_controls_model['control_description'] = 'control_description'
        profile_controls_model['control_category'] = 'control_category'
        profile_controls_model['control_parent'] = 'control_parent'
        profile_controls_model['control_requirement'] = True
        profile_controls_model['control_docs'] = control_docs_model
        profile_controls_model['control_specifications_count'] = 5
        profile_controls_model['control_specifications'] = [control_specifications_model]

        default_parameters_prototype_model = {}  # DefaultParametersPrototype
        default_parameters_prototype_model['assessment_type'] = 'assessment_type'
        default_parameters_prototype_model['assessment_id'] = 'assessment_id'
        default_parameters_prototype_model['parameter_name'] = 'parameter_name'
        default_parameters_prototype_model['parameter_default_value'] = 'parameter_default_value'
        default_parameters_prototype_model['parameter_display_name'] = 'parameter_display_name'
        default_parameters_prototype_model['parameter_type'] = 'string'

        # Construct a json representation of a Profile model
        profile_model_json = {}
        profile_model_json['id'] = 'testString'
        profile_model_json['profile_name'] = 'testString'
        profile_model_json['profile_description'] = 'testString'
        profile_model_json['profile_type'] = 'predefined'
        profile_model_json['profile_version'] = 'testString'
        profile_model_json['version_group_label'] = 'e0923045-f00d-44de-b49b-6f1f0e8033cc'
        profile_model_json['instance_id'] = 'testString'
        profile_model_json['latest'] = True
        profile_model_json['hierarchy_enabled'] = True
        profile_model_json['created_by'] = 'testString'
        profile_model_json['created_on'] = '2019-01-01T12:00:00Z'
        profile_model_json['updated_by'] = 'testString'
        profile_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        profile_model_json['controls_count'] = 38
        profile_model_json['control_parents_count'] = 38
        profile_model_json['attachments_count'] = 38
        profile_model_json['controls'] = [profile_controls_model]
        profile_model_json['default_parameters'] = [default_parameters_prototype_model]

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


class TestModel_ProfileCollection:
    """
    Test Class for ProfileCollection
    """

    def test_profile_collection_serialization(self):
        """
        Test serialization/deserialization for ProfileCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        paginated_collection_first_model = {}  # PaginatedCollectionFirst
        paginated_collection_first_model['href'] = 'href'

        paginated_collection_next_model = {}  # PaginatedCollectionNext
        paginated_collection_next_model['href'] = 'href'
        paginated_collection_next_model['start'] = 'start'

        profile_item_model = {}  # ProfileItem
        profile_item_model['id'] = 'id'
        profile_item_model['profile_name'] = 'profile_name'
        profile_item_model['profile_description'] = 'profile_description'
        profile_item_model['profile_type'] = 'profile_type'
        profile_item_model['profile_version'] = 'profile_version'
        profile_item_model['version_group_label'] = 'version_group_label'
        profile_item_model['latest'] = True
        profile_item_model['created_by'] = 'created_by'
        profile_item_model['created_on'] = '2000-01-23T04:56:07Z'
        profile_item_model['updated_by'] = 'updated_by'
        profile_item_model['updated_on'] = '2000-01-23T04:56:07Z'
        profile_item_model['controls_count'] = 0
        profile_item_model['attachments_count'] = 6

        # Construct a json representation of a ProfileCollection model
        profile_collection_model_json = {}
        profile_collection_model_json['total_count'] = 1
        profile_collection_model_json['limit'] = 20
        profile_collection_model_json['first'] = paginated_collection_first_model
        profile_collection_model_json['next'] = paginated_collection_next_model
        profile_collection_model_json['profiles'] = [profile_item_model]

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

        control_docs_model = {}  # ControlDocs
        control_docs_model['control_docs_id'] = 'control_docs_id'
        control_docs_model['control_docs_type'] = 'control_docs_type'

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'parameter_name'
        parameter_info_model['parameter_display_name'] = 'parameter_display_name'
        parameter_info_model['parameter_type'] = 'string'
        parameter_info_model['parameter_value'] = 'public'

        implementation_model = {}  # Implementation
        implementation_model['assessment_id'] = 'assessment_id'
        implementation_model['assessment_method'] = 'assessment_method'
        implementation_model['assessment_type'] = 'assessment_type'
        implementation_model['assessment_description'] = 'assessment_description'
        implementation_model['parameter_count'] = 5
        implementation_model['parameters'] = [parameter_info_model]

        control_specifications_model = {}  # ControlSpecifications
        control_specifications_model['control_specification_id'] = 'f3517159-889e-4781-819a-89d89b747c85'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'f3517159-889e-4781-819a-89d89b747c85'
        control_specifications_model['componenet_name'] = 'componenet_name'
        control_specifications_model['environment'] = 'environment'
        control_specifications_model['control_specification_description'] = 'control_specification_description'
        control_specifications_model['assessments_count'] = 1
        control_specifications_model['assessments'] = [implementation_model]

        # Construct a json representation of a ProfileControls model
        profile_controls_model_json = {}
        profile_controls_model_json['control_library_id'] = 'e98a56ff-dc24-41d4-9875-1e188e2da6cd'
        profile_controls_model_json['control_id'] = '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF'
        profile_controls_model_json['control_library_version'] = 'testString'
        profile_controls_model_json['control_name'] = 'testString'
        profile_controls_model_json['control_description'] = 'testString'
        profile_controls_model_json['control_category'] = 'testString'
        profile_controls_model_json['control_parent'] = 'testString'
        profile_controls_model_json['control_requirement'] = True
        profile_controls_model_json['control_docs'] = control_docs_model
        profile_controls_model_json['control_specifications_count'] = 38
        profile_controls_model_json['control_specifications'] = [control_specifications_model]

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
        profile_controls_prototype_model_json['control_library_id'] = 'e98a56ff-dc24-41d4-9875-1e188e2da6cd'
        profile_controls_prototype_model_json['control_id'] = '5C453578-E9A1-421E-AD0F-C6AFCDD67CCF'

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


class TestModel_ProfileItem:
    """
    Test Class for ProfileItem
    """

    def test_profile_item_serialization(self):
        """
        Test serialization/deserialization for ProfileItem
        """

        # Construct a json representation of a ProfileItem model
        profile_item_model_json = {}
        profile_item_model_json['id'] = 'testString'
        profile_item_model_json['profile_name'] = 'testString'
        profile_item_model_json['profile_description'] = 'testString'
        profile_item_model_json['profile_type'] = 'testString'
        profile_item_model_json['profile_version'] = 'testString'
        profile_item_model_json['version_group_label'] = 'testString'
        profile_item_model_json['latest'] = True
        profile_item_model_json['created_by'] = 'testString'
        profile_item_model_json['created_on'] = '2019-01-01T12:00:00Z'
        profile_item_model_json['updated_by'] = 'testString'
        profile_item_model_json['updated_on'] = '2019-01-01T12:00:00Z'
        profile_item_model_json['controls_count'] = 38
        profile_item_model_json['attachments_count'] = 38

        # Construct a model instance of ProfileItem by calling from_dict on the json representation
        profile_item_model = ProfileItem.from_dict(profile_item_model_json)
        assert profile_item_model != False

        # Construct a model instance of ProfileItem by calling from_dict on the json representation
        profile_item_model_dict = ProfileItem.from_dict(profile_item_model_json).__dict__
        profile_item_model2 = ProfileItem(**profile_item_model_dict)

        # Verify the model instances are equivalent
        assert profile_item_model == profile_item_model2

        # Convert model instance back to dict and verify no loss of data
        profile_item_model_json2 = profile_item_model.to_dict()
        assert profile_item_model_json2 == profile_item_model_json


class TestModel_Property:
    """
    Test Class for Property
    """

    def test_property_serialization(self):
        """
        Test serialization/deserialization for Property
        """

        # Construct a json representation of a Property model
        property_model_json = {}
        property_model_json['property'] = 'allowed_network'
        property_model_json['property_description'] = 'A description for this property'
        property_model_json['operator'] = 'string_equals'
        property_model_json['expected_value'] = 'public'
        property_model_json['found_value'] = 'public'

        # Construct a model instance of Property by calling from_dict on the json representation
        property_model = Property.from_dict(property_model_json)
        assert property_model != False

        # Construct a model instance of Property by calling from_dict on the json representation
        property_model_dict = Property.from_dict(property_model_json).__dict__
        property_model2 = Property(**property_model_dict)

        # Verify the model instances are equivalent
        assert property_model == property_model2

        # Convert model instance back to dict and verify no loss of data
        property_model_json2 = property_model.to_dict()
        assert property_model_json2 == property_model_json


class TestModel_PropertyItem:
    """
    Test Class for PropertyItem
    """

    def test_property_item_serialization(self):
        """
        Test serialization/deserialization for PropertyItem
        """

        # Construct a json representation of a PropertyItem model
        property_item_model_json = {}
        property_item_model_json['name'] = 'testString'
        property_item_model_json['value'] = 'testString'

        # Construct a model instance of PropertyItem by calling from_dict on the json representation
        property_item_model = PropertyItem.from_dict(property_item_model_json)
        assert property_item_model != False

        # Construct a model instance of PropertyItem by calling from_dict on the json representation
        property_item_model_dict = PropertyItem.from_dict(property_item_model_json).__dict__
        property_item_model2 = PropertyItem(**property_item_model_dict)

        # Verify the model instances are equivalent
        assert property_item_model == property_item_model2

        # Convert model instance back to dict and verify no loss of data
        property_item_model_json2 = property_item_model.to_dict()
        assert property_item_model_json2 == property_item_model_json


class TestModel_ProviderTypeInstanceItem:
    """
    Test Class for ProviderTypeInstanceItem
    """

    def test_provider_type_instance_item_serialization(self):
        """
        Test serialization/deserialization for ProviderTypeInstanceItem
        """

        # Construct a json representation of a ProviderTypeInstanceItem model
        provider_type_instance_item_model_json = {}
        provider_type_instance_item_model_json['id'] = '7588190cce3c05ac8f7942ea597dafce'
        provider_type_instance_item_model_json['type'] = 'workload-protection'
        provider_type_instance_item_model_json['name'] = 'workload-protection-instance-1'
        provider_type_instance_item_model_json['attributes'] = {'anyKey': 'anyValue'}
        provider_type_instance_item_model_json['created_at'] = '2023-07-24T13:14:18.884000Z'
        provider_type_instance_item_model_json['updated_at'] = '2023-07-24T13:14:18.884000Z'

        # Construct a model instance of ProviderTypeInstanceItem by calling from_dict on the json representation
        provider_type_instance_item_model = ProviderTypeInstanceItem.from_dict(provider_type_instance_item_model_json)
        assert provider_type_instance_item_model != False

        # Construct a model instance of ProviderTypeInstanceItem by calling from_dict on the json representation
        provider_type_instance_item_model_dict = ProviderTypeInstanceItem.from_dict(provider_type_instance_item_model_json).__dict__
        provider_type_instance_item_model2 = ProviderTypeInstanceItem(**provider_type_instance_item_model_dict)

        # Verify the model instances are equivalent
        assert provider_type_instance_item_model == provider_type_instance_item_model2

        # Convert model instance back to dict and verify no loss of data
        provider_type_instance_item_model_json2 = provider_type_instance_item_model.to_dict()
        assert provider_type_instance_item_model_json2 == provider_type_instance_item_model_json


class TestModel_ProviderTypeInstancesResponse:
    """
    Test Class for ProviderTypeInstancesResponse
    """

    def test_provider_type_instances_response_serialization(self):
        """
        Test serialization/deserialization for ProviderTypeInstancesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_type_instance_item_model = {}  # ProviderTypeInstanceItem
        provider_type_instance_item_model['id'] = '7588190cce3c05ac8f7942ea597dafce'
        provider_type_instance_item_model['type'] = 'workload-protection'
        provider_type_instance_item_model['name'] = 'workload-protection-instance-1'
        provider_type_instance_item_model['attributes'] = {'anyKey': 'anyValue'}
        provider_type_instance_item_model['created_at'] = '2023-07-24T13:14:18.884000Z'
        provider_type_instance_item_model['updated_at'] = '2023-07-24T13:14:18.884000Z'

        # Construct a json representation of a ProviderTypeInstancesResponse model
        provider_type_instances_response_model_json = {}
        provider_type_instances_response_model_json['provider_type_instances'] = [provider_type_instance_item_model]

        # Construct a model instance of ProviderTypeInstancesResponse by calling from_dict on the json representation
        provider_type_instances_response_model = ProviderTypeInstancesResponse.from_dict(provider_type_instances_response_model_json)
        assert provider_type_instances_response_model != False

        # Construct a model instance of ProviderTypeInstancesResponse by calling from_dict on the json representation
        provider_type_instances_response_model_dict = ProviderTypeInstancesResponse.from_dict(provider_type_instances_response_model_json).__dict__
        provider_type_instances_response_model2 = ProviderTypeInstancesResponse(**provider_type_instances_response_model_dict)

        # Verify the model instances are equivalent
        assert provider_type_instances_response_model == provider_type_instances_response_model2

        # Convert model instance back to dict and verify no loss of data
        provider_type_instances_response_model_json2 = provider_type_instances_response_model.to_dict()
        assert provider_type_instances_response_model_json2 == provider_type_instances_response_model_json


class TestModel_ProviderTypeItem:
    """
    Test Class for ProviderTypeItem
    """

    def test_provider_type_item_serialization(self):
        """
        Test serialization/deserialization for ProviderTypeItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        label_type_model = {}  # LabelType
        label_type_model['text'] = '1 per instance'
        label_type_model['tip'] = 'Only 1 per instance'

        additional_property_model = {}  # AdditionalProperty
        additional_property_model['type'] = 'text'
        additional_property_model['display_name'] = 'Workload Protection Instance CRN'

        # Construct a json representation of a ProviderTypeItem model
        provider_type_item_model_json = {}
        provider_type_item_model_json['id'] = '7588190cce3c05ac8f7942ea597dafce'
        provider_type_item_model_json['type'] = 'workload-protection'
        provider_type_item_model_json['name'] = 'workload-protection'
        provider_type_item_model_json['description'] = 'Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.'
        provider_type_item_model_json['s2s_enabled'] = True
        provider_type_item_model_json['instance_limit'] = 1
        provider_type_item_model_json['mode'] = 'PULL'
        provider_type_item_model_json['data_type'] = 'com.sysdig.secure.results'
        provider_type_item_model_json['icon'] = 'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+'
        provider_type_item_model_json['label'] = label_type_model
        provider_type_item_model_json['attributes'] = {'key1': additional_property_model}
        provider_type_item_model_json['created_at'] = '2023-07-24T13:14:18.884000Z'
        provider_type_item_model_json['updated_at'] = '2023-07-24T13:14:18.884000Z'

        # Construct a model instance of ProviderTypeItem by calling from_dict on the json representation
        provider_type_item_model = ProviderTypeItem.from_dict(provider_type_item_model_json)
        assert provider_type_item_model != False

        # Construct a model instance of ProviderTypeItem by calling from_dict on the json representation
        provider_type_item_model_dict = ProviderTypeItem.from_dict(provider_type_item_model_json).__dict__
        provider_type_item_model2 = ProviderTypeItem(**provider_type_item_model_dict)

        # Verify the model instances are equivalent
        assert provider_type_item_model == provider_type_item_model2

        # Convert model instance back to dict and verify no loss of data
        provider_type_item_model_json2 = provider_type_item_model.to_dict()
        assert provider_type_item_model_json2 == provider_type_item_model_json


class TestModel_ProviderTypesCollection:
    """
    Test Class for ProviderTypesCollection
    """

    def test_provider_types_collection_serialization(self):
        """
        Test serialization/deserialization for ProviderTypesCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        label_type_model = {}  # LabelType
        label_type_model['text'] = '1 per instance'
        label_type_model['tip'] = 'Only 1 per instance'

        additional_property_model = {}  # AdditionalProperty
        additional_property_model['type'] = 'text'
        additional_property_model['display_name'] = 'Workload Protection Instance CRN'

        provider_type_item_model = {}  # ProviderTypeItem
        provider_type_item_model['id'] = '7588190cce3c05ac8f7942ea597dafce'
        provider_type_item_model['type'] = 'workload-protection'
        provider_type_item_model['name'] = 'workload-protection'
        provider_type_item_model['description'] = 'Security and Compliance Center Workload Protection helps you accelerate your Kubernetes and cloud adoption by addressing security and regulatory compliance. Easily identify vulnerabilities, check compliance, block threats and respond faster at every stage of the container and Kubernetes lifecycle.'
        provider_type_item_model['s2s_enabled'] = True
        provider_type_item_model['instance_limit'] = 1
        provider_type_item_model['mode'] = 'PULL'
        provider_type_item_model['data_type'] = 'com.sysdig.secure.results'
        provider_type_item_model['icon'] = 'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBkYXRhLW5hbWU9IkJ1aWxkIGljb24gaGVyZSIgdmlld0JveD0iMCAwIDMyIDMyIj48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSItMjgxMS4xOTgiIHgyPSItMjgxNC4xOTgiIHkxPSI1NTcuNTE3IiB5Mj0iNTU3LjUxNyIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSgyODMxLjE5OCAtNTQyLjAxNykiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLW9wYWNpdHk9IjAiLz48c3RvcCBvZmZzZXQ9Ii44Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgeGxpbms6aHJlZj0iI2EiIGlkPSJiIiB4MT0iLTgwNi4xOTgiIHgyPSItNzk5LjE5OCIgeTE9Ii0yNDE0LjQ4MSIgeTI9Ii0yNDE0LjQ4MSIgZ3JhZGllbnRUcmFuc2Zvcm09InRyYW5zbGF0ZSg4MjUuMTk4IDI0MjguOTgxKSIvPjxsaW5lYXJHcmFkaWVudCB4bGluazpocmVmPSIjYSIgaWQ9ImMiIHgxPSItODEwLjE5OCIgeDI9Ii03OTguMTk4IiB5MT0iLTI0MTkuOTgxIiB5Mj0iLTI0MTkuOTgxIiBncmFkaWVudFRyYW5zZm9ybT0idHJhbnNsYXRlKDgzMi4xOTggMjQzMi45ODEpIi8+PGxpbmVhckdyYWRpZW50IGlkPSJlIiB4MT0iLTI1MTQiIHgyPSItMjQ4MiIgeTE9Ii0yNDgyIiB5Mj0iLTI1MTQiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSAwIDAgLTEgMjUxNCAtMjQ4MikiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9Ii4xIiBzdG9wLWNvbG9yPSIjMDhiZGJhIi8+PHN0b3Agb2Zmc2V0PSIuOSIgc3RvcC1jb2xvcj0iIzBmNjJmZSIvPjwvbGluZWFyR3JhZGllbnQ+PG1hc2sgaWQ9ImQiIHdpZHRoPSIyOS4wMTciIGhlaWdodD0iMjcuOTk2IiB4PSIxLjk4MyIgeT0iMiIgZGF0YS1uYW1lPSJtYXNrIiBtYXNrVW5pdHM9InVzZXJTcGFjZU9uVXNlIj48ZyBmaWxsPSIjZmZmIj48cGF0aCBkPSJNMjkuOTc2IDE2YzAtMy43MzktMS40NTYtNy4yNTUtNC4xMDEtOS44OTlTMTkuNzE1IDIgMTUuOTc2IDIgOC43MjEgMy40NTYgNi4wNzcgNi4xMDFjLTUuNDU5IDUuNDU5LTUuNDU5IDE0LjM0IDAgMTkuNzk4QTE0LjA0NCAxNC4wNDQgMCAwIDAgMTYgMjkuOTk1di0yLjAwMWExMi4wNCAxMi4wNCAwIDAgMS04LjUwOS0zLjUxYy00LjY3OS00LjY3OS00LjY3OS0xMi4yOTIgMC0xNi45NzEgMi4yNjctMi4yNjcgNS4yOC0zLjUxNSA4LjQ4NS0zLjUxNXM2LjIxOSAxLjI0OCA4LjQ4NSAzLjUxNSAzLjUxNSA1LjI4IDMuNTE1IDguNDg1YzAgMS4zMDgtLjIxOCAyLjU4LS42MTggMy43ODZsMS44OTcuNjMyYy40NjctMS40MDguNzIyLTIuODkyLjcyMi00LjQxOFoiLz48cGF0aCBkPSJNMjQuNyAxMy42NzVhOC45NCA4Ljk0IDAgMCAwLTQuMTkzLTUuNDY1IDguOTQyIDguOTQyIDAgMCAwLTYuODMtLjg5OSA4Ljk3MSA4Ljk3MSAwIDAgMC01LjQ2MSA0LjE5NSA4Ljk4IDguOTggMCAwIDAtLjkwMyA2LjgyOGMxLjA3NyA0LjAxNiA0LjcyMiA2LjY2IDguNjk1IDYuNjYxdi0xLjk5OGMtMy4wOS0uMDAxLTUuOTI2LTIuMDU4LTYuNzYzLTUuMTgxYTcuMDEgNy4wMSAwIDAgMSA0Ljk1LTguNTc0IDYuOTU4IDYuOTU4IDAgMCAxIDUuMzEyLjY5OSA2Ljk1NCA2Ljk1NCAwIDAgMSAzLjI2MSA0LjI1Yy4zNTkgMS4zNDIuMjc1IDIuNzMyLS4xNTQgNC4wMTNsMS45MDkuNjM2YTguOTU5IDguOTU5IDAgMCAwIC4xNzYtNS4xNjdaIi8+PC9nPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0xNCAxNmMwLTEuMTAzLjg5Ny0yIDItMnMyIC44OTcgMiAyYTIgMiAwIDAgMS0uMTExLjYzbDEuODg5LjYzYy4xMzMtLjM5OC4yMjItLjgxNy4yMjItMS4yNTlhNCA0IDAgMSAwLTQgNHYtMmMtMS4xMDMgMC0yLS44OTctMi0yWiIvPjxwYXRoIGZpbGw9InVybCgjYSkiIGQ9Ik0xNyAxNGgzdjNoLTN6IiB0cmFuc2Zvcm09InJvdGF0ZSgtOTAgMTguNSAxNS41KSIvPjxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xOSAxMmg3djVoLTd6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyMi41IDE0LjUpIi8+PHBhdGggZmlsbD0idXJsKCNjKSIgZD0iTTIyIDEwaDEydjZIMjJ6IiB0cmFuc2Zvcm09InJvdGF0ZSg5MCAyOCAxMykiLz48cGF0aCBkPSJNMjUgMTloNnY0aC02ek0yMCAxOGg1djVoLTV6TTE3IDE3aDN2NmgtM3oiLz48L21hc2s+PC9kZWZzPjxwYXRoIGZpbGw9IiMwMDFkNmMiIGQ9Im0yNSAzMS4wMDEtMi4xMzktMS4wMTNBNS4wMjIgNS4wMjIgMCAwIDEgMjAgMjUuNDY4VjE5aDEwdjYuNDY4YTUuMDIzIDUuMDIzIDAgMCAxLTIuODYxIDQuNTJMMjUgMzEuMDAxWm0tMy0xMHY0LjQ2OGMwIDEuMTUzLjY3NCAyLjIxOCAxLjcxNyAyLjcxMWwxLjI4My42MDcgMS4yODMtLjYwN0EzLjAxMiAzLjAxMiAwIDAgMCAyOCAyNS40Njl2LTQuNDY4aC02WiIgZGF0YS1uYW1lPSJ1dWlkLTU1ODMwNDRiLWZmMjQtNGUyNy05MDU0LTI0MDQzYWRkZmMwNiIvPjxnIG1hc2s9InVybCgjZCkiPjxwYXRoIGZpbGw9InVybCgjZSkiIGQ9Ik0wIDBoMzJ2MzJIMHoiIHRyYW5zZm9ybT0icm90YXRlKC05MCAxNiAxNikiLz48L2c+PC9zdmc+'
        provider_type_item_model['label'] = label_type_model
        provider_type_item_model['attributes'] = {'key1': additional_property_model}
        provider_type_item_model['created_at'] = '2023-07-24T13:14:18.884000Z'
        provider_type_item_model['updated_at'] = '2023-07-24T13:14:18.884000Z'

        # Construct a json representation of a ProviderTypesCollection model
        provider_types_collection_model_json = {}
        provider_types_collection_model_json['provider_types'] = [provider_type_item_model]

        # Construct a model instance of ProviderTypesCollection by calling from_dict on the json representation
        provider_types_collection_model = ProviderTypesCollection.from_dict(provider_types_collection_model_json)
        assert provider_types_collection_model != False

        # Construct a model instance of ProviderTypesCollection by calling from_dict on the json representation
        provider_types_collection_model_dict = ProviderTypesCollection.from_dict(provider_types_collection_model_json).__dict__
        provider_types_collection_model2 = ProviderTypesCollection(**provider_types_collection_model_dict)

        # Verify the model instances are equivalent
        assert provider_types_collection_model == provider_types_collection_model2

        # Convert model instance back to dict and verify no loss of data
        provider_types_collection_model_json2 = provider_types_collection_model.to_dict()
        assert provider_types_collection_model_json2 == provider_types_collection_model_json


class TestModel_ProviderTypesInstancesResponse:
    """
    Test Class for ProviderTypesInstancesResponse
    """

    def test_provider_types_instances_response_serialization(self):
        """
        Test serialization/deserialization for ProviderTypesInstancesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_type_instance_item_model = {}  # ProviderTypeInstanceItem
        provider_type_instance_item_model['id'] = '7588190cce3c05ac8f7942ea597dafce'
        provider_type_instance_item_model['type'] = 'workload-protection'
        provider_type_instance_item_model['name'] = 'workload-protection-instance-1'
        provider_type_instance_item_model['attributes'] = {'anyKey': 'anyValue'}
        provider_type_instance_item_model['created_at'] = '2023-07-24T13:14:18.884000Z'
        provider_type_instance_item_model['updated_at'] = '2023-07-24T13:14:18.884000Z'

        # Construct a json representation of a ProviderTypesInstancesResponse model
        provider_types_instances_response_model_json = {}
        provider_types_instances_response_model_json['provider_types_instances'] = [provider_type_instance_item_model]

        # Construct a model instance of ProviderTypesInstancesResponse by calling from_dict on the json representation
        provider_types_instances_response_model = ProviderTypesInstancesResponse.from_dict(provider_types_instances_response_model_json)
        assert provider_types_instances_response_model != False

        # Construct a model instance of ProviderTypesInstancesResponse by calling from_dict on the json representation
        provider_types_instances_response_model_dict = ProviderTypesInstancesResponse.from_dict(provider_types_instances_response_model_json).__dict__
        provider_types_instances_response_model2 = ProviderTypesInstancesResponse(**provider_types_instances_response_model_dict)

        # Verify the model instances are equivalent
        assert provider_types_instances_response_model == provider_types_instances_response_model2

        # Convert model instance back to dict and verify no loss of data
        provider_types_instances_response_model_json2 = provider_types_instances_response_model.to_dict()
        assert provider_types_instances_response_model_json2 == provider_types_instances_response_model_json


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

        scope_property_model = {}  # ScopeProperty
        scope_property_model['name'] = 'scope_id'
        scope_property_model['value'] = '18d32a4430e54c81a6668952609763b2'

        attachment_scope_model = {}  # AttachmentScope
        attachment_scope_model['id'] = 'ca0941aa-b7e2-43a3-9794-1b3d322474d9'
        attachment_scope_model['environment'] = 'ibm-cloud'
        attachment_scope_model['properties'] = [scope_property_model]

        attachment_model = {}  # Attachment
        attachment_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        attachment_model['name'] = 'resource group - Default'
        attachment_model['description'] = 'Scoped to the Default resource group'
        attachment_model['schedule'] = 'daily'
        attachment_model['scope'] = [attachment_scope_model]

        # Construct a json representation of a Report model
        report_model_json = {}
        report_model_json['id'] = '44a5-a292-32114fa73558'
        report_model_json['group_id'] = '55b6-b3A4-432250b84669'
        report_model_json['created_on'] = '2022-08-15T12:30:01Z'
        report_model_json['scan_time'] = '2022-08-15T12:30:01Z'
        report_model_json['type'] = 'scheduled'
        report_model_json['cos_object'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7'
        report_model_json['instance_id'] = '84644a08-31b6-4988-b504-49a46ca69ccd'
        report_model_json['account'] = account_model
        report_model_json['profile'] = profile_info_model
        report_model_json['attachment'] = attachment_model

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


class TestModel_ReportControls:
    """
    Test Class for ReportControls
    """

    def test_report_controls_serialization(self):
        """
        Test serialization/deserialization for ReportControls
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'location'
        parameter_info_model['parameter_display_name'] = 'Location'
        parameter_info_model['parameter_type'] = 'string'
        parameter_info_model['parameter_value'] = 'public'

        assessment_model = {}  # Assessment
        assessment_model['assessment_id'] = '382c2b06-e6b2-43ee-b189-c1c7743b67ee'
        assessment_model['assessment_type'] = 'ibm-cloud-rule'
        assessment_model['assessment_method'] = 'ibm-cloud-rule'
        assessment_model['assessment_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        assessment_model['parameter_count'] = 1
        assessment_model['parameters'] = [parameter_info_model]

        control_specification_with_stats_model = {}  # ControlSpecificationWithStats
        control_specification_with_stats_model['control_specification_id'] = '18d32a4430e54c81a6668952609763b2'
        control_specification_with_stats_model['component_id'] = 'cloud-object_storage'
        control_specification_with_stats_model['control_specification_description'] = 'Check whether Cloud Object Storage is accessible only by using private endpoints'
        control_specification_with_stats_model['environment'] = 'ibm cloud'
        control_specification_with_stats_model['responsibility'] = 'user'
        control_specification_with_stats_model['assessments'] = [assessment_model]
        control_specification_with_stats_model['status'] = 'compliant'
        control_specification_with_stats_model['total_count'] = 150
        control_specification_with_stats_model['compliant_count'] = 130
        control_specification_with_stats_model['not_compliant_count'] = 5
        control_specification_with_stats_model['unable_to_perform_count'] = 5
        control_specification_with_stats_model['user_evaluation_required_count'] = 10

        control_with_stats_model = {}  # ControlWithStats
        control_with_stats_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        control_with_stats_model['control_library_id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        control_with_stats_model['control_library_version'] = 'v1.2.3'
        control_with_stats_model['control_name'] = 'Password Management'
        control_with_stats_model['control_description'] = 'Password Management'
        control_with_stats_model['control_category'] = 'Access Control'
        control_with_stats_model['control_path'] = 'AC-2(a)'
        control_with_stats_model['control_specifications'] = [control_specification_with_stats_model]
        control_with_stats_model['status'] = 'compliant'
        control_with_stats_model['total_count'] = 150
        control_with_stats_model['compliant_count'] = 130
        control_with_stats_model['not_compliant_count'] = 5
        control_with_stats_model['unable_to_perform_count'] = 5
        control_with_stats_model['user_evaluation_required_count'] = 10

        # Construct a json representation of a ReportControls model
        report_controls_model_json = {}
        report_controls_model_json['status'] = 'compliant'
        report_controls_model_json['total_count'] = 150
        report_controls_model_json['compliant_count'] = 130
        report_controls_model_json['not_compliant_count'] = 5
        report_controls_model_json['unable_to_perform_count'] = 5
        report_controls_model_json['user_evaluation_required_count'] = 10
        report_controls_model_json['home_account_id'] = 'testString'
        report_controls_model_json['report_id'] = 'testString'
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

        eval_stats_model = {}  # EvalStats
        eval_stats_model['status'] = 'compliant'
        eval_stats_model['total_count'] = 140
        eval_stats_model['pass_count'] = 123
        eval_stats_model['failure_count'] = 12
        eval_stats_model['error_count'] = 5
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

        scope_property_model = {}  # ScopeProperty
        scope_property_model['name'] = 'scope_id'
        scope_property_model['value'] = '18d32a4430e54c81a6668952609763b2'

        attachment_scope_model = {}  # AttachmentScope
        attachment_scope_model['id'] = 'ca0941aa-b7e2-43a3-9794-1b3d322474d9'
        attachment_scope_model['environment'] = 'ibm-cloud'
        attachment_scope_model['properties'] = [scope_property_model]

        attachment_model = {}  # Attachment
        attachment_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        attachment_model['name'] = 'resource group - Default'
        attachment_model['description'] = 'Scoped to the Default resource group'
        attachment_model['schedule'] = 'daily'
        attachment_model['scope'] = [attachment_scope_model]

        report_model = {}  # Report
        report_model['id'] = '44a5-a292-32114fa73558'
        report_model['group_id'] = '55b6-b3A4-432250b84669'
        report_model['created_on'] = '2022-08-15T12:30:01Z'
        report_model['scan_time'] = '2022-08-15T12:30:01Z'
        report_model['type'] = 'scheduled'
        report_model['cos_object'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7'
        report_model['instance_id'] = '84644a08-31b6-4988-b504-49a46ca69ccd'
        report_model['account'] = account_model
        report_model['profile'] = profile_info_model
        report_model['attachment'] = attachment_model

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


class TestModel_ReportPage:
    """
    Test Class for ReportPage
    """

    def test_report_page_serialization(self):
        """
        Test serialization/deserialization for ReportPage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_model = {}  # PageHRef
        page_h_ref_model['href'] = 'testString'

        account_model = {}  # Account
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        profile_info_model = {}  # ProfileInfo
        profile_info_model['id'] = '44a5-a292-32114fa73558'
        profile_info_model['name'] = 'IBM FS Cloud'
        profile_info_model['version'] = '0.1'

        scope_property_model = {}  # ScopeProperty
        scope_property_model['name'] = 'scope_id'
        scope_property_model['value'] = '18d32a4430e54c81a6668952609763b2'

        attachment_scope_model = {}  # AttachmentScope
        attachment_scope_model['id'] = 'ca0941aa-b7e2-43a3-9794-1b3d322474d9'
        attachment_scope_model['environment'] = 'ibm-cloud'
        attachment_scope_model['properties'] = [scope_property_model]

        attachment_model = {}  # Attachment
        attachment_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        attachment_model['name'] = 'resource group - Default'
        attachment_model['description'] = 'Scoped to the Default resource group'
        attachment_model['schedule'] = 'daily'
        attachment_model['scope'] = [attachment_scope_model]

        report_model = {}  # Report
        report_model['id'] = '44a5-a292-32114fa73558'
        report_model['group_id'] = '55b6-b3A4-432250b84669'
        report_model['created_on'] = '2022-08-15T12:30:01Z'
        report_model['scan_time'] = '2022-08-15T12:30:01Z'
        report_model['type'] = 'scheduled'
        report_model['cos_object'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/531fc3e28bfc43c5a2cea07786d93f5c:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:b1a8f3da-49d2-4966-ae83-a8d02bc2aac7'
        report_model['instance_id'] = '84644a08-31b6-4988-b504-49a46ca69ccd'
        report_model['account'] = account_model
        report_model['profile'] = profile_info_model
        report_model['attachment'] = attachment_model

        # Construct a json representation of a ReportPage model
        report_page_model_json = {}
        report_page_model_json['total_count'] = 230
        report_page_model_json['limit'] = 50
        report_page_model_json['start'] = 'testString'
        report_page_model_json['first'] = page_h_ref_model
        report_page_model_json['next'] = page_h_ref_model
        report_page_model_json['home_account_id'] = 'testString'
        report_page_model_json['reports'] = [report_model]

        # Construct a model instance of ReportPage by calling from_dict on the json representation
        report_page_model = ReportPage.from_dict(report_page_model_json)
        assert report_page_model != False

        # Construct a model instance of ReportPage by calling from_dict on the json representation
        report_page_model_dict = ReportPage.from_dict(report_page_model_json).__dict__
        report_page_model2 = ReportPage(**report_page_model_dict)

        # Verify the model instances are equivalent
        assert report_page_model == report_page_model2

        # Convert model instance back to dict and verify no loss of data
        report_page_model_json2 = report_page_model.to_dict()
        assert report_page_model_json2 == report_page_model_json


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

        compliance_stats_model = {}  # ComplianceStats
        compliance_stats_model['status'] = 'compliant'
        compliance_stats_model['total_count'] = 150
        compliance_stats_model['compliant_count'] = 130
        compliance_stats_model['not_compliant_count'] = 5
        compliance_stats_model['unable_to_perform_count'] = 5
        compliance_stats_model['user_evaluation_required_count'] = 10

        eval_stats_model = {}  # EvalStats
        eval_stats_model['status'] = 'compliant'
        eval_stats_model['total_count'] = 140
        eval_stats_model['pass_count'] = 123
        eval_stats_model['failure_count'] = 12
        eval_stats_model['error_count'] = 5
        eval_stats_model['completed_count'] = 135

        tags_model = {}  # Tags
        tags_model['user'] = ['testString']
        tags_model['access'] = ['testString']
        tags_model['service'] = ['testString']

        resource_summary_item_model = {}  # ResourceSummaryItem
        resource_summary_item_model['name'] = 'my-bucket'
        resource_summary_item_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        resource_summary_item_model['service'] = 'cloud-object-storage'
        resource_summary_item_model['tags'] = tags_model
        resource_summary_item_model['account'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        resource_summary_item_model['status'] = 'compliant'
        resource_summary_item_model['total_count'] = 140
        resource_summary_item_model['pass_count'] = 123
        resource_summary_item_model['failure_count'] = 12
        resource_summary_item_model['error_count'] = 5
        resource_summary_item_model['completed_count'] = 135

        resource_summary_model = {}  # ResourceSummary
        resource_summary_model['status'] = 'compliant'
        resource_summary_model['total_count'] = 150
        resource_summary_model['compliant_count'] = 130
        resource_summary_model['not_compliant_count'] = 5
        resource_summary_model['unable_to_perform_count'] = 5
        resource_summary_model['user_evaluation_required_count'] = 10
        resource_summary_model['top_failed'] = [resource_summary_item_model]

        # Construct a json representation of a ReportSummary model
        report_summary_model_json = {}
        report_summary_model_json['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        report_summary_model_json['isntance_id'] = '84644a08-31b6-4988-b504-49a46ca69ccd'
        report_summary_model_json['account'] = account_model
        report_summary_model_json['score'] = compliance_score_model
        report_summary_model_json['controls'] = compliance_stats_model
        report_summary_model_json['evaluations'] = eval_stats_model
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
        tags_model['user'] = ['user', 'user', 'user', 'user', 'user']
        tags_model['access'] = ['access', 'access', 'access', 'access', 'access']
        tags_model['service'] = ['service', 'service', 'service', 'service', 'service']

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

        # Construct a json representation of a ReportViolationDataPoint model
        report_violation_data_point_model_json = {}
        report_violation_data_point_model_json['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        report_violation_data_point_model_json['report_group_id'] = '55b6-b3A4-432250b84669'
        report_violation_data_point_model_json['scan_time'] = '2022-08-15T12:30:01Z'
        report_violation_data_point_model_json['controls'] = compliance_stats_model

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

        report_violation_data_point_model = {}  # ReportViolationDataPoint
        report_violation_data_point_model['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        report_violation_data_point_model['report_group_id'] = '55b6-b3A4-432250b84669'
        report_violation_data_point_model['scan_time'] = '2022-08-15T12:30:01Z'
        report_violation_data_point_model['controls'] = compliance_stats_model

        # Construct a json representation of a ReportViolationsDrift model
        report_violations_drift_model_json = {}
        report_violations_drift_model_json['home_account_id'] = 'testString'
        report_violations_drift_model_json['report_id'] = 'testString'
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

        # Construct a json representation of a Resource model
        resource_model_json = {}
        resource_model_json['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        resource_model_json['id'] = 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::'
        resource_model_json['resource_name'] = 'jeff\'s key'
        resource_model_json['component_id'] = 'cloud-object_storage'
        resource_model_json['environment'] = 'ibm cloud'
        resource_model_json['account'] = account_model
        resource_model_json['status'] = 'compliant'
        resource_model_json['total_count'] = 140
        resource_model_json['pass_count'] = 123
        resource_model_json['failure_count'] = 12
        resource_model_json['error_count'] = 5
        resource_model_json['completed_count'] = 135

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

        page_h_ref_model = {}  # PageHRef
        page_h_ref_model['href'] = 'testString'

        account_model = {}  # Account
        account_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        account_model['name'] = 'NIST'
        account_model['type'] = 'account_type'

        resource_model = {}  # Resource
        resource_model['report_id'] = '30b434b3-cb08-4845-af10-7a8fc682b6a8'
        resource_model['id'] = 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::'
        resource_model['resource_name'] = 'jeff\'s key'
        resource_model['component_id'] = 'cloud-object_storage'
        resource_model['environment'] = 'ibm cloud'
        resource_model['account'] = account_model
        resource_model['status'] = 'compliant'
        resource_model['total_count'] = 140
        resource_model['pass_count'] = 123
        resource_model['failure_count'] = 12
        resource_model['error_count'] = 5
        resource_model['completed_count'] = 135

        # Construct a json representation of a ResourcePage model
        resource_page_model_json = {}
        resource_page_model_json['total_count'] = 230
        resource_page_model_json['limit'] = 50
        resource_page_model_json['start'] = 'testString'
        resource_page_model_json['first'] = page_h_ref_model
        resource_page_model_json['next'] = page_h_ref_model
        resource_page_model_json['home_account_id'] = 'testString'
        resource_page_model_json['report_id'] = 'testString'
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
        resource_summary_item_model['name'] = 'my-bucket'
        resource_summary_item_model['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        resource_summary_item_model['service'] = 'cloud-object-storage'
        resource_summary_item_model['tags'] = tags_model
        resource_summary_item_model['account'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        resource_summary_item_model['status'] = 'compliant'
        resource_summary_item_model['total_count'] = 140
        resource_summary_item_model['pass_count'] = 123
        resource_summary_item_model['failure_count'] = 12
        resource_summary_item_model['error_count'] = 5
        resource_summary_item_model['completed_count'] = 135

        # Construct a json representation of a ResourceSummary model
        resource_summary_model_json = {}
        resource_summary_model_json['status'] = 'compliant'
        resource_summary_model_json['total_count'] = 150
        resource_summary_model_json['compliant_count'] = 130
        resource_summary_model_json['not_compliant_count'] = 5
        resource_summary_model_json['unable_to_perform_count'] = 5
        resource_summary_model_json['user_evaluation_required_count'] = 10
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
        resource_summary_item_model_json['name'] = 'my-bucket'
        resource_summary_item_model_json['id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        resource_summary_item_model_json['service'] = 'cloud-object-storage'
        resource_summary_item_model_json['tags'] = tags_model
        resource_summary_item_model_json['account'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        resource_summary_item_model_json['status'] = 'compliant'
        resource_summary_item_model_json['total_count'] = 140
        resource_summary_item_model_json['pass_count'] = 123
        resource_summary_item_model_json['failure_count'] = 12
        resource_summary_item_model_json['error_count'] = 5
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

        parameter_model = {}  # Parameter
        parameter_model['name'] = 'name'
        parameter_model['display_name'] = 'display_name'
        parameter_model['description'] = 'description'
        parameter_model['type'] = 'string'

        import_model = {}  # Import
        import_model['parameters'] = [parameter_model]

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'name'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'value'

        target_model = {}  # Target
        target_model['service_name'] = 'service_name'
        target_model['service_display_name'] = 'service_display_name'
        target_model['resource_kind'] = 'resource_kind'
        target_model['additional_target_attributes'] = [additional_target_attribute_model]

        required_config_items_model = {}  # RequiredConfigItemsRequiredConfigOr
        required_config_items_model['description'] = 'testString'

        required_config_model = {}  # RequiredConfigRequiredConfigAnd
        required_config_model['description'] = 'testString'
        required_config_model['and'] = [required_config_items_model]

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
        rule_model_json['target'] = target_model
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


class TestModel_RulesPageBase:
    """
    Test Class for RulesPageBase
    """

    def test_rules_page_base_serialization(self):
        """
        Test serialization/deserialization for RulesPageBase
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_h_ref_first_model = {}  # PageHRefFirst
        page_h_ref_first_model['href'] = 'href'

        page_h_ref_next_model = {}  # PageHRefNext
        page_h_ref_next_model['href'] = 'href'
        page_h_ref_next_model['start'] = 'start'

        parameter_model = {}  # Parameter
        parameter_model['name'] = 'name'
        parameter_model['display_name'] = 'display_name'
        parameter_model['description'] = 'description'
        parameter_model['type'] = 'string'

        import_model = {}  # Import
        import_model['parameters'] = [parameter_model]

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'name'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'value'

        target_model = {}  # Target
        target_model['service_name'] = 'service_name'
        target_model['service_display_name'] = 'service_display_name'
        target_model['resource_kind'] = 'resource_kind'
        target_model['additional_target_attributes'] = [additional_target_attribute_model]

        required_config_items_model = {}  # RequiredConfigItemsRequiredConfigOr
        required_config_items_model['description'] = 'testString'

        required_config_model = {}  # RequiredConfigRequiredConfigAnd
        required_config_model['description'] = 'testString'
        required_config_model['and'] = [required_config_items_model]

        rule_model = {}  # Rule
        rule_model['created_on'] = '2000-01-23T04:56:07Z'
        rule_model['created_by'] = 'created_by'
        rule_model['updated_on'] = '2000-01-23T04:56:07Z'
        rule_model['updated_by'] = 'updated_by'
        rule_model['id'] = 'id'
        rule_model['account_id'] = 'account_id'
        rule_model['description'] = 'description'
        rule_model['type'] = 'user_defined'
        rule_model['version'] = 'version'
        rule_model['import'] = import_model
        rule_model['target'] = target_model
        rule_model['required_config'] = required_config_model
        rule_model['labels'] = ['labels', 'labels', 'labels', 'labels', 'labels']

        # Construct a json representation of a RulesPageBase model
        rules_page_base_model_json = {}
        rules_page_base_model_json['limit'] = 50
        rules_page_base_model_json['total_count'] = 230
        rules_page_base_model_json['first'] = page_h_ref_first_model
        rules_page_base_model_json['next'] = page_h_ref_next_model
        rules_page_base_model_json['rules'] = [rule_model]

        # Construct a model instance of RulesPageBase by calling from_dict on the json representation
        rules_page_base_model = RulesPageBase.from_dict(rules_page_base_model_json)
        assert rules_page_base_model != False

        # Construct a model instance of RulesPageBase by calling from_dict on the json representation
        rules_page_base_model_dict = RulesPageBase.from_dict(rules_page_base_model_json).__dict__
        rules_page_base_model2 = RulesPageBase(**rules_page_base_model_dict)

        # Verify the model instances are equivalent
        assert rules_page_base_model == rules_page_base_model2

        # Convert model instance back to dict and verify no loss of data
        rules_page_base_model_json2 = rules_page_base_model.to_dict()
        assert rules_page_base_model_json2 == rules_page_base_model_json


class TestModel_Scan:
    """
    Test Class for Scan
    """

    def test_scan_serialization(self):
        """
        Test serialization/deserialization for Scan
        """

        # Construct a json representation of a Scan model
        scan_model_json = {}
        scan_model_json['id'] = 'testString'
        scan_model_json['account_id'] = 'testString'
        scan_model_json['attachment_id'] = 'testString'
        scan_model_json['report_id'] = 'testString'
        scan_model_json['status'] = 'completed'
        scan_model_json['last_scan_time'] = 'testString'
        scan_model_json['next_scan_time'] = 'testString'
        scan_model_json['scan_type'] = 'ondemand'
        scan_model_json['occurence'] = 38

        # Construct a model instance of Scan by calling from_dict on the json representation
        scan_model = Scan.from_dict(scan_model_json)
        assert scan_model != False

        # Construct a model instance of Scan by calling from_dict on the json representation
        scan_model_dict = Scan.from_dict(scan_model_json).__dict__
        scan_model2 = Scan(**scan_model_dict)

        # Verify the model instances are equivalent
        assert scan_model == scan_model2

        # Convert model instance back to dict and verify no loss of data
        scan_model_json2 = scan_model.to_dict()
        assert scan_model_json2 == scan_model_json


class TestModel_ScopeProperty:
    """
    Test Class for ScopeProperty
    """

    def test_scope_property_serialization(self):
        """
        Test serialization/deserialization for ScopeProperty
        """

        # Construct a json representation of a ScopeProperty model
        scope_property_model_json = {}
        scope_property_model_json['name'] = 'scope_id'
        scope_property_model_json['value'] = '18d32a4430e54c81a6668952609763b2'

        # Construct a model instance of ScopeProperty by calling from_dict on the json representation
        scope_property_model = ScopeProperty.from_dict(scope_property_model_json)
        assert scope_property_model != False

        # Construct a model instance of ScopeProperty by calling from_dict on the json representation
        scope_property_model_dict = ScopeProperty.from_dict(scope_property_model_json).__dict__
        scope_property_model2 = ScopeProperty(**scope_property_model_dict)

        # Verify the model instances are equivalent
        assert scope_property_model == scope_property_model2

        # Convert model instance back to dict and verify no loss of data
        scope_property_model_json2 = scope_property_model.to_dict()
        assert scope_property_model_json2 == scope_property_model_json


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
        event_notifications_model['instance_crn'] = 'crn:v1:staging:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::'
        event_notifications_model['updated_on'] = '2000-01-23T04:56:07Z'
        event_notifications_model['source_id'] = 'crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::'
        event_notifications_model['source_description'] = 'This source is used for integration with IBM Cloud Security and Compliance Center.'
        event_notifications_model['source_name'] = 'compliance'

        object_storage_model = {}  # ObjectStorage
        object_storage_model['instance_crn'] = 'instance_crn'
        object_storage_model['bucket'] = 'bucket'
        object_storage_model['bucket_location'] = 'bucket_location'
        object_storage_model['bucket_endpoint'] = 'bucket_endpoint'
        object_storage_model['updated_on'] = '2000-01-23T04:56:07Z'

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

        additional_target_attribute_model = {}  # AdditionalTargetAttribute
        additional_target_attribute_model['name'] = 'name'
        additional_target_attribute_model['operator'] = 'string_equals'
        additional_target_attribute_model['value'] = 'value'

        # Construct a json representation of a Target model
        target_model_json = {}
        target_model_json['service_name'] = 'testString'
        target_model_json['service_display_name'] = 'testString'
        target_model_json['resource_kind'] = 'testString'
        target_model_json['additional_target_attributes'] = [additional_target_attribute_model]

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


class TestModel_TargetInfo:
    """
    Test Class for TargetInfo
    """

    def test_target_info_serialization(self):
        """
        Test serialization/deserialization for TargetInfo
        """

        # Construct a json representation of a TargetInfo model
        target_info_model_json = {}
        target_info_model_json['id'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket'
        target_info_model_json['account_id'] = '59bcbfa6ea2f006b4ed7094c1a08dcdd'
        target_info_model_json['resource_crn'] = 'crn:v1:bluemix:public:cloud-object-storage:global:a/59bcbfa6ea2f006b4ed7094c1a08dcdd:1a0ec336-f391-4091-a6fb-5e084a4c56f4:bucket:mybucket'
        target_info_model_json['resource_name'] = 'mybucket'
        target_info_model_json['service_name'] = 'cloud-object-storage'

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


class TestModel_RequiredConfigItemsRequiredConfigAnd:
    """
    Test Class for RequiredConfigItemsRequiredConfigAnd
    """

    def test_required_config_items_required_config_and_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigItemsRequiredConfigAnd
        """

        # Construct a json representation of a RequiredConfigItemsRequiredConfigAnd model
        required_config_items_required_config_and_model_json = {}
        required_config_items_required_config_and_model_json['description'] = 'testString'

        # Construct a model instance of RequiredConfigItemsRequiredConfigAnd by calling from_dict on the json representation
        required_config_items_required_config_and_model = RequiredConfigItemsRequiredConfigAnd.from_dict(required_config_items_required_config_and_model_json)
        assert required_config_items_required_config_and_model != False

        # Construct a model instance of RequiredConfigItemsRequiredConfigAnd by calling from_dict on the json representation
        required_config_items_required_config_and_model_dict = RequiredConfigItemsRequiredConfigAnd.from_dict(required_config_items_required_config_and_model_json).__dict__
        required_config_items_required_config_and_model2 = RequiredConfigItemsRequiredConfigAnd(**required_config_items_required_config_and_model_dict)

        # Verify the model instances are equivalent
        assert required_config_items_required_config_and_model == required_config_items_required_config_and_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_items_required_config_and_model_json2 = required_config_items_required_config_and_model.to_dict()
        assert required_config_items_required_config_and_model_json2 == required_config_items_required_config_and_model_json


class TestModel_RequiredConfigItemsRequiredConfigBase:
    """
    Test Class for RequiredConfigItemsRequiredConfigBase
    """

    def test_required_config_items_required_config_base_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigItemsRequiredConfigBase
        """

        # Construct a json representation of a RequiredConfigItemsRequiredConfigBase model
        required_config_items_required_config_base_model_json = {}
        required_config_items_required_config_base_model_json['description'] = 'testString'
        required_config_items_required_config_base_model_json['property'] = 'testString'
        required_config_items_required_config_base_model_json['operator'] = 'string_equals'
        required_config_items_required_config_base_model_json['value'] = 'testString'

        # Construct a model instance of RequiredConfigItemsRequiredConfigBase by calling from_dict on the json representation
        required_config_items_required_config_base_model = RequiredConfigItemsRequiredConfigBase.from_dict(required_config_items_required_config_base_model_json)
        assert required_config_items_required_config_base_model != False

        # Construct a model instance of RequiredConfigItemsRequiredConfigBase by calling from_dict on the json representation
        required_config_items_required_config_base_model_dict = RequiredConfigItemsRequiredConfigBase.from_dict(required_config_items_required_config_base_model_json).__dict__
        required_config_items_required_config_base_model2 = RequiredConfigItemsRequiredConfigBase(**required_config_items_required_config_base_model_dict)

        # Verify the model instances are equivalent
        assert required_config_items_required_config_base_model == required_config_items_required_config_base_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_items_required_config_base_model_json2 = required_config_items_required_config_base_model.to_dict()
        assert required_config_items_required_config_base_model_json2 == required_config_items_required_config_base_model_json


class TestModel_RequiredConfigItemsRequiredConfigOr:
    """
    Test Class for RequiredConfigItemsRequiredConfigOr
    """

    def test_required_config_items_required_config_or_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigItemsRequiredConfigOr
        """

        # Construct a json representation of a RequiredConfigItemsRequiredConfigOr model
        required_config_items_required_config_or_model_json = {}
        required_config_items_required_config_or_model_json['description'] = 'testString'

        # Construct a model instance of RequiredConfigItemsRequiredConfigOr by calling from_dict on the json representation
        required_config_items_required_config_or_model = RequiredConfigItemsRequiredConfigOr.from_dict(required_config_items_required_config_or_model_json)
        assert required_config_items_required_config_or_model != False

        # Construct a model instance of RequiredConfigItemsRequiredConfigOr by calling from_dict on the json representation
        required_config_items_required_config_or_model_dict = RequiredConfigItemsRequiredConfigOr.from_dict(required_config_items_required_config_or_model_json).__dict__
        required_config_items_required_config_or_model2 = RequiredConfigItemsRequiredConfigOr(**required_config_items_required_config_or_model_dict)

        # Verify the model instances are equivalent
        assert required_config_items_required_config_or_model == required_config_items_required_config_or_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_items_required_config_or_model_json2 = required_config_items_required_config_or_model.to_dict()
        assert required_config_items_required_config_or_model_json2 == required_config_items_required_config_or_model_json


class TestModel_RequiredConfigRequiredConfigAnd:
    """
    Test Class for RequiredConfigRequiredConfigAnd
    """

    def test_required_config_required_config_and_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigRequiredConfigAnd
        """

        # Construct dict forms of any model objects needed in order to build this model.

        required_config_items_model = {}  # RequiredConfigItemsRequiredConfigOr
        required_config_items_model['description'] = 'testString'

        # Construct a json representation of a RequiredConfigRequiredConfigAnd model
        required_config_required_config_and_model_json = {}
        required_config_required_config_and_model_json['description'] = 'testString'
        required_config_required_config_and_model_json['and'] = [required_config_items_model]

        # Construct a model instance of RequiredConfigRequiredConfigAnd by calling from_dict on the json representation
        required_config_required_config_and_model = RequiredConfigRequiredConfigAnd.from_dict(required_config_required_config_and_model_json)
        assert required_config_required_config_and_model != False

        # Construct a model instance of RequiredConfigRequiredConfigAnd by calling from_dict on the json representation
        required_config_required_config_and_model_dict = RequiredConfigRequiredConfigAnd.from_dict(required_config_required_config_and_model_json).__dict__
        required_config_required_config_and_model2 = RequiredConfigRequiredConfigAnd(**required_config_required_config_and_model_dict)

        # Verify the model instances are equivalent
        assert required_config_required_config_and_model == required_config_required_config_and_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_required_config_and_model_json2 = required_config_required_config_and_model.to_dict()
        assert required_config_required_config_and_model_json2 == required_config_required_config_and_model_json


class TestModel_RequiredConfigRequiredConfigBase:
    """
    Test Class for RequiredConfigRequiredConfigBase
    """

    def test_required_config_required_config_base_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigRequiredConfigBase
        """

        # Construct a json representation of a RequiredConfigRequiredConfigBase model
        required_config_required_config_base_model_json = {}
        required_config_required_config_base_model_json['description'] = 'testString'
        required_config_required_config_base_model_json['property'] = 'testString'
        required_config_required_config_base_model_json['operator'] = 'string_equals'
        required_config_required_config_base_model_json['value'] = 'testString'

        # Construct a model instance of RequiredConfigRequiredConfigBase by calling from_dict on the json representation
        required_config_required_config_base_model = RequiredConfigRequiredConfigBase.from_dict(required_config_required_config_base_model_json)
        assert required_config_required_config_base_model != False

        # Construct a model instance of RequiredConfigRequiredConfigBase by calling from_dict on the json representation
        required_config_required_config_base_model_dict = RequiredConfigRequiredConfigBase.from_dict(required_config_required_config_base_model_json).__dict__
        required_config_required_config_base_model2 = RequiredConfigRequiredConfigBase(**required_config_required_config_base_model_dict)

        # Verify the model instances are equivalent
        assert required_config_required_config_base_model == required_config_required_config_base_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_required_config_base_model_json2 = required_config_required_config_base_model.to_dict()
        assert required_config_required_config_base_model_json2 == required_config_required_config_base_model_json


class TestModel_RequiredConfigRequiredConfigOr:
    """
    Test Class for RequiredConfigRequiredConfigOr
    """

    def test_required_config_required_config_or_serialization(self):
        """
        Test serialization/deserialization for RequiredConfigRequiredConfigOr
        """

        # Construct dict forms of any model objects needed in order to build this model.

        required_config_items_model = {}  # RequiredConfigItemsRequiredConfigOr
        required_config_items_model['description'] = 'testString'

        # Construct a json representation of a RequiredConfigRequiredConfigOr model
        required_config_required_config_or_model_json = {}
        required_config_required_config_or_model_json['description'] = 'testString'
        required_config_required_config_or_model_json['or'] = [required_config_items_model]

        # Construct a model instance of RequiredConfigRequiredConfigOr by calling from_dict on the json representation
        required_config_required_config_or_model = RequiredConfigRequiredConfigOr.from_dict(required_config_required_config_or_model_json)
        assert required_config_required_config_or_model != False

        # Construct a model instance of RequiredConfigRequiredConfigOr by calling from_dict on the json representation
        required_config_required_config_or_model_dict = RequiredConfigRequiredConfigOr.from_dict(required_config_required_config_or_model_json).__dict__
        required_config_required_config_or_model2 = RequiredConfigRequiredConfigOr(**required_config_required_config_or_model_dict)

        # Verify the model instances are equivalent
        assert required_config_required_config_or_model == required_config_required_config_or_model2

        # Convert model instance back to dict and verify no loss of data
        required_config_required_config_or_model_json2 = required_config_required_config_or_model.to_dict()
        assert required_config_required_config_or_model_json2 == required_config_required_config_or_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
